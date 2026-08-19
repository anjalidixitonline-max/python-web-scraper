import requests
from bs4 import BeautifulSoup
import csv
page_to_scrape = 1
print("Here's the list of all books:")
count = 0
total = 0
with open("all_books.csv","w",newline = "", encoding ="utf8") as f:
    writer = csv.writer(f)
    writer.writerow(['Number',"Name","Price","Availability"])
    while True:
        url = f"https://books.toscrape.com/catalogue/page-{page_to_scrape}.html"
        page = requests.get(url)
        if page.status_code != 200:
            if page_to_scrape <50:
                print("Page not found!")
            elif page_to_scrape >= 50:
                print('------------------')
                print('All the pages of website have been scrapped!!')
            break 
        soup = BeautifulSoup(page.content,"html.parser")
        Big_box = soup.find_all('article' ,class_="product_pod")
        for Small_box in Big_box :
            htag = Small_box.find('h3')
            atag = htag.find('a')
            Title = atag['title']
            Price = Small_box.find('p',class_="price_color")
            stock = Small_box.find("p" ,class_="instock availability")
            status = stock.text
            cost = Price.text
            value = cost[1:]
            count += 1
            total = total + float(value)
            print(f'{count:>4} Name: {Title}')
            print(f"     Price: {cost}")
            print(f"     Availability: {status.strip("\n ")}\n")
            writer.writerow([count,Title,cost,status.strip("\n ")])
        page_to_scrape += 1        
print("Total pages:",page_to_scrape - 1)
print('Total books:',count)
print('Total price of all books:','£',total)
print('\nSUCCESS! Check your folder for all_books.csv')