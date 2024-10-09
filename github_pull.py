import requests

owner = "kubernetes"
repo = "kubernetes"


url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

response = requests.get(url)

complete_detail = response.json()


for element in range(len(complete_detail)):

    print(complete_detail[element]['user']['login'])
