import requests
from django.shortcuts import render


def fetch_data(url):
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {url}: {e}")
    return None


def home(request):
  #USING APIs => Example 1
  response = requests.get(
      'https://restcountries.com/v3.1/all?fields=name,flags`')
  data = response.json()
  results = data[0:1]

  #Example 2
  response2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = response2.json()
  results2 = data2["message"]

  #Example 3
  response3 = requests.get('http://randomfox.ca/floof/')
  data3 = response3.json()
  results3 = data3["image"]
                           

  #Example 4
  response4 = requests.get(
      'https://uselessfacts.jsph.pl/random.json?language=en')
  data4 = response4.json()
  results4 = data4["text"]

  #Example 5
  response5 = requests.get('https://api.chucknorris.io/jokes/random')
  data5 = response5.json()
  results5 = data5["value"]

  return render(
      request, 'templates/index.html', {
          'results': results,
          'results2': results2,
          'results3': results3,
          'results4': results4,
          'results5': results5
      })
