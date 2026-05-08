# Introduction: The requests module simplifies making HTTP requests, allowing Python scripts to interact with web services and APIs effortlessly.

https://jsonplaceholder.typicode.com/ - is a free online REST APIю

r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(r)
Output: <Response [200]>

print(r.status_code)
Output: 200

print(r.url)
Output: https://jsonplaceholder.typicode.com/todos/1

print(r.content)
Output: b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'

print(str(r.content))
Output: b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'

print(r.text)
Output: 
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}

------------------------------------
# GET request parameters. The most common HTTP method is GET, used to retrieve information from a specified resource.
my_params = { "userID": 1 }
r = requests.get("https://jsonplaceholder.typicode.com/todos/1", params = my_params)
print(r.url)
Output: https://jsonplaceholder.typicode.com/todos/1?userID=1

my_paramss = { "userID": 1, "ID": 2 }
r = requests.get("https://jsonplaceholder.typicode.com/todos/1", params = my_params)
print(r.url)
https://jsonplaceholder.typicode.com/todos/1?userID=1&ID=2

-----------------------------------------------------------------------
# POST request parameters. POST requests are used to submit data to be processed to a specified resource.

my_data = {'username': 'john_doe', 'password': 'secure_password'}
response = requests.post('https://api.example.com/login', data = my_data)
print(response.json())

-----------------------------------------------------------------------
# Handling Responses: Responses from HTTP requests contain useful information like status codes, headers, and response content.
# Here, we check if the status code is 200 (OK) and print the content if the request was successful.
import requests

response = requests.get('https://api.example.com/data')

# Check if the request was successful (status code 200)
import requests
response = requests.get("https://example.com")
if response.status_code == 200:
    print('Request successful!')
    print(response.text)
else:
    print(f'Request failed with status code {response.status_code}')

-----------------------------------------------------------------------




























