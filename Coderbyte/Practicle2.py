import pandas as pd
import requests
from bs4 import BeautifulSoup


# https://www.google.com/search?q=scraping+data+and+save+in+excel+file+in+python&sxsrf=ALiCzsYTXerFrEdhmYWO5jdL5sNOoTsOJw%3A1651679904272&ei=oKJyYuahEMqZr7wPg5W7kAo&ved=0ahUKEwjm8eePm8b3AhXKzIsBHYPKDqIQ4dUDCA4&uact=5&oq=scraping+data+and+save+in+excel+file+in+python&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BwgjELACECc6BQgAEKIEOgQIIxAnOgUIIRCgAToICCEQFhAdEB46BwghEAoQoAFKBQg8EgE0SgQIQRgASgQIRhgAUI0NWM1fYO5haARwAXgAgAH9AYgB3B6SAQYwLjIzLjKYAQCgAQHIAQjAAQE&sclient=gws-wiz#kpvalbx=_taJyYqnuNIONmAXCk6CIBQ16
def get_data(brand_name,pcount):
# try:
 url = 'https://www.flipkart.com/search?q=' + brand_name + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
 responce = requests.get(url)
 soup = BeautifulSoup(responce.content, 'html.parser')
 print(responce)
 print(responce.url)
 data = []
 bunch = soup.find_all("div", class_="_4ddWXP")
 counter = 0
 for link in range(len(bunch)):
        item = {}
        Total_product_count=""
        # Scraping feilds

        Total_product_count = bunch[link].find("span", class_="_10Ermr").get_text()
        item["URL"] = 'https://www.flipkart.com' + bunch[link].find("a", class_="s1Q9rs")['href']
        item["Title"] = bunch[link].find("a", class_="s1Q9rs").get_text()
        item["Price"] = bunch[link].find("div", class_="_30jeq3").get_text()
        Total_product_count = bunch[link].find("span", class_="_10Ermr").get_text()
        print("count of product is:" ,Total_product_count)
        # Total_product_count=Total_product_count.split("of")
        # Total_product_count=Total_product_count[]
        counter = counter + 1
        if counter<=10:
            print("less then 10 Product found on website itself")
        else:
            print("")

        # for sorting products
        if pcount==counter:
            break
        else pcount=0:
          if counter == 10:
              break

        # print("Total count of data scraped from first page is: ", counter)
        # print(title)
        # print(Product_url)
        # print(price)
        data.append(item)
 return data

def create_file(data):
    df = pd.DataFrame(data)
    df.to_excel("Flipkart_Links.xlsx")

    # filename = "Flipkart_Links.txt"
    # with open(filename, 'w', newline='', encoding='utf-8') as file:
    #  file.write(title)
    #  file.flush()
    #  file.close()

if __name__ == '__main__':
    search = input("Enter brand name from FlipKart e.g: Lorial: ")
    Product_count = input("Enter the count of product to scrape: ")
    data = get_data(search,Product_count)
    create_file(data)
    print("Scraping Done for first Page...")
