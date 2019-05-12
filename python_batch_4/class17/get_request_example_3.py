import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')


 requests.post('https://httpbin.org/post', data={'key':'value'})
#>>> requests.put('https://httpbin.org/put', data={'key':'value'})
#>>> requests.delete('https://httpbin.org/delete')
#>>> requests.head('https://httpbin.org/get')
#>>> requests.patch('https://httpbin.org/patch', data={'key':'value'})
#>>> requests.options('https://httpbin.org/get')

