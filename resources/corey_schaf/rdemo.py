import requests

#r = requests.get('https://xkcd.com/comics/python.png')

#dir shows attributes and methods that we can access
#can also run through help()
#text content of response in unicode
#print(dir(r))
#html parser
##beautifulsoup4
##requests_html
#print(r.content)
# 'wb' write byte
##saving a png
# with open('comic.png', 'wb') as f:
#     f.write(r.content)

##checking if we gett a good response
#200 success
#300 redirect
#400 client error
#500 server errors site crashes and can't access
#print(r.status_code)

#anything less than a 400 response
#print(r.ok)

#get all headers that come with response
#print(r.headers)

#httpbin.org allow us to test different queries
#will responsd with json information

### Part 2
#can put in dictionary to have arguements

#https://httpbin.org/get?page=2&count=25
# payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)
#
# print(r.url)

#if we want to post- data that was posted
#pass in form data
# payload = {'username': 'corey', 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data = payload)
#
# #print(r.text)
# #json method instead
# r_dict = r.json() #creates python dictionary from json response
#
# print(r_dict['form'])

### Part 3
r = requests.get('http://httpbin.org/delay/6', timeout = 3)

print(r)

#401 unauthorized reponse code
#response is good [200]

#set a timeout for a request

#exception is ReadTimeout 
