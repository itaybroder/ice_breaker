import requests

gist_response = requests.get(
    "https://gist.githubusercontent.com/itaybroder/9b85e4e1d5ab5ec05af3e28a2e5bcf8a/raw/e0ac325dc7f939ea56c0a547fd2eca86b06d5a8b/roy_ohana.json"
)
print(gist_response.json()["full_name"])
