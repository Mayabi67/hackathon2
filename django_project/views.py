import requests
from django.shortcuts import render


def home(request):
  #USING APIs => Example 1
  response = requests.get('https://api.github.com/events')
  data = response.json()
  results = data[0]["repo"]

  #Example 2
  response2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = response2.json()
  results2 = data2["message"]

  #Example 3
  response3 = requests.get('https://api.github.com/users/octocat/repos')
  data3 = response3.json()
  results3 = data3[0]["name"]

  return render(request, 'templates/index.html', {
      'results': results,
      'results2': results2,
      'results3': results3
  })
