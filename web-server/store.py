import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    return r.json()