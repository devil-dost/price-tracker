
import requests
from bs4 import BeautifulSoup
import smtplib
import time



URL = "https://www.amazon.in/Rockerz-255-Pro-Technology-Resistance/dp/B082VS5H3Y/ref=sr_1_16?crid=6YV5W3Q3TW8F&dchild=1&keywords=bluthoothearphone&qid=1612370071&sprefix=blu%2Caps%2C298&sr=8-16"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', 
'Connection' : 'close'
}

set_price = 1000

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    product_title = str(title)
    product_title = product_title.strip()
    print(product_title)
    try:
        price = soup.find(class_='a-price a-text-price a-size-medium apexPriceToPay').get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
    except:
        AttributeError
        price = soup.find(class_='a-price a-text-price a-size-medium apexPriceToPay').get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
    
    product_price = float(price[0:5])
    print(product_price)
    
    if product_price<=set_price:
        
       send_mail()
    else:
        print("abhi nhi hua dropp")
        
        

def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('{YOUR ID HERE}@gmail.com', '{HERE COMES PASSWORD}')

  subject = 'Price Fell Down'
  body = ("Check the amazon link "+URL)

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    '{YOUR ID}@gmail.com',
    '{RECEIVER'S ID}@gmail.com',
    msg
  )
  
  print('mei huhi genius!!!!!!!')
  
  server.quit()

while(True):
  check_price()
  time.sleep(60 * 60)
    
    
    
    
