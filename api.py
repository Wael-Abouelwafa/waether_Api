
import requests
import json
access_key="28ed04f9d3016ca0bd20c74d6b5d50cd"
url = "http://api.weatherstack.com/current"

while True:
        city = input("enter city name: ")
        if city == 'q':
                break
        params = {
        "access_key" : access_key,
        "query":city
        }
            
        api_result = requests.get(url, params=params)
        api_response = api_result.json()
        res = json.loads(api_result.text)
        print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))