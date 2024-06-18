import requests

url = "https://truecaller4.p.rapidapi.com/api/v1/getDetails"

querystring = {"phone":"505271606","countryCode":"AE"}

headers = {
	"X-RapidAPI-Key": "cecd24cf5amsh0457b3c7fb4fe7bp1972c9jsndf435613763b",
	"X-RapidAPI-Host": "truecaller4.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

if response.status_code == 200:
    data = response.json()
    if 'name' in data:
       data.get(data['data'][0]['name']),
    else:
        print(f"{data['data'][0]['name']}")
else:
    print(f"Error: {response.status_code}, {response.text}")

