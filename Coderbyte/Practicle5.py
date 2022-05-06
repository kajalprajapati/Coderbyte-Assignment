import requests
from bs4 import BeautifulSoup
import random
import lxml

def get_data(url):

 proxies = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080',
    }
 user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    ]
 user_agent = user_agent_list[random.randint(0, len(user_agent_list) - 1)]
 headers = {
        'User-Agent': user_agent,
        'authority': 'www.amazon.in',
        'content-type': 'text/html;charset=UTF-8',
    }
 responce = requests.get(url,proxies,headers=headers)
 soup = BeautifulSoup(responce.content, 'lxml')
 print(responce)
 strhtml=responce.text
 if strhtml.__contains__('catpcha"'):
      print("Bloking page found")

 return responce


get_data("https://www.amazon.in/Lino-Perros-Womens-Tote-Pink/dp/B07JN9G66H")