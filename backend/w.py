import requests
from bs4 import BeautifulSoup
import pyautogui


# url = 'https://torob.com/p/4b0c3d72-defc-456f-97f4-813a5ebbcf6d/%DA%AF%D9%88%D8%B4%DB%8C-%D8%A7%D9%BE%D9%84-iphone-13-pro-max-not-active-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/'

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# price = soup.find('div', {'class': 'price'}).text
# name = soup.find('h1', {'class' : 'jsx-63b317fab2efbae'}).text

# n = name.split('|')[0]
# p = ''.join([i for i in price if i.isdigit()])


# pyautogui.alert(p)
# pyautogui.alert(n)


links = [
    'https://torob.com/p/b768a136-d151-4abd-9072-7724158b21cc/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a73-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/78548a2d-f5f2-4e3c-ab58-166df48a50e2/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-s23-ultra-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-12-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/76ffa3ee-b6e8-4147-8d9f-7a452bd0a128/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a14-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-64-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/0c2d0e0a-55cc-4fc6-b660-cd865c45d11b/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C-redmi-note-11s-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/1d271685-1c53-48f8-a419-ebc9f33cfe00/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-s21-fe-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/3e7e8907-cd2a-4668-b8ea-8017eeed6f64/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a53-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/c248e83f-2af8-4957-8a91-5e72a0f3acef/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a13-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-64-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/3f85efce-55a0-41e0-b1fc-e8b3266ff394/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a23-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/54b035ab-6415-404a-9308-f0c28c09cb64/%DA%AF%D9%88%D8%B4%DB%8C-%D8%A7%D9%BE%D9%84-iphone-13-not-active-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/f25e0f3e-cb35-4ad1-a8cb-54b620b41c11/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a14-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/4b6389b3-0674-43aa-8657-65ad48113eea/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a34-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/',
    'https://torob.com/p/07a238be-e4cf-4256-b6f3-9497584fe94b/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C-poco-x5-pro-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/'
]
prices =[]
names = []
for i in links :
    response = requests.get(i)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('div', {'class': 'price'}).text
    name = soup.find('h1', {'class' : 'jsx-63b317fab2efbae'}).text
    n = name.split('|')[0]
    p = ''.join([i for i in price if i.isdigit()])
    prices.append(p)
    names.append(n)

pyautogui.alert(prices)
pyautogui.alert(names)