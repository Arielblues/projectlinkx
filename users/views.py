from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import scrapy
from urllib.parse import urlencode
from urllib.parse import urlparse
import json
from datetime import datetime
API_KEY = 'YOUR_KEY'



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been createed {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})








def get_url(url):
   payload = {'api_key': API_KEY, 'url': url, 'autoparse': 'true', 'country_code': 'us'}
   proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
   return proxy_url

def create_google_url(query, site=''):
   google_dict = {'q': query, 'num': 100, }
   if site:
       web = urlparse(site).netloc
       google_dict['as_sitesearch'] = web
       return 'http://www.google.com/search?' + urlencode(google_dict)
   return 'http://www.google.com/search?' + urlencode(google_dict)

class GoogleSpider(scrapy.Spider):
   name = 'google'
   allowed_domains = ['api.scraperapi.com']
   custom_settings = {'ROBOTSTXT_OBEY': False, 'LOG_LEVEL': 'INFO',
                  'CONCURRENT_REQUESTS_PER_DOMAIN': 10}

   def start_requests(self):
       queries = ['scrapy', 'beautifulsoup'] 
       for query in queries:
           url = create_google_url(query)
           yield scrapy.Request(get_url(url), callback=self.parse, meta={'pos': 0})

   def parse(self, response):
       di = json.loads(response.text)
       pos = response.meta['pos']
       dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       for result in di['organic_results']:
           title = result['title']
           snippet = result['snippet']
           link = result['link']
           item = {'title': title, 'snippet': snippet, 'link': link, 'position': pos, 'date': dt}
           pos += 1
           yield item
       next_page = di['pagination']['nextPageUrl']
       if next_page:
           yield scrapy.Request(get_url(next_page), callback=self.parse, meta={'pos': pos})








@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)