import requests

api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
api_key = "kD0gOr6PGzQOJ5-hK5t8hw"
header_dic = {"Authorization": "Bearer " + api_key}
params = {
    "url": "https://www.linkedin.com/in/roy-ohana/",
}
response = requests.get(api_endpoint, params=params, headers=header_dic)

print(response.json())
