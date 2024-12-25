# module9.py 
 
import requests 
 
def fetch_data(url): 
Пример функции для выполнения сетевого запроса. 
    print(f"Fetching data from {url}...") 
    response = requests.get(url) 
    response.raise_for_statuse() 
    return response.json() 
