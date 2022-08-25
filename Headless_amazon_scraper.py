import Headless_amazon_scraper
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from datetime import datetime



################################################################################################################################################################################
                                                            #create a header for the requests library, a browser request is needed to receive
                                                            #JSON and html files as a response, the user agent can be found the local machine

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}
################################################################################################################################################################################
        
                                                            #requests can't have space between them so it replaces them with "+"
                                                            #the URL query is created with the user input

def amazon(search_keyword, maxvalue, minvalue, dt):

    user_input = search_keyword.replace(' ', '+')
    base_url = 'https://www.amazon.co.uk/s?k={0}'.format(user_input)
################################################################################################################################################################################
   
                                                            #create new arrays to store information that are needed to be printed on files 


    graphing = []
    amazon_items = []
    for i in range(1, 5):                                                                                               #create a requests for 5 pages
        print('Processing {0}...'.format(base_url + '&page={0}'.format(i)))
        response = requests.get(base_url + '&page={0}'.format(i), headers=headers)                                      #create a request and receive data in html to be read
        browser = BeautifulSoup(response.content, 'html.parser')                                                        #use beautiful soup to read the data 
        listed_items = browser.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})    #listing are stored in array


################################################################################################################################################################################


                                                             #go trough the response to find and parse all the required data into two arrays

        for items in listed_items:
            product_name = items.h2.text
            try:
                item_info = {}
                item_info['To be alerted'] = False                                                                                                #assigning data to the attributes of the item info object
                item_info['Listed name'] = items.h2.text
                item_price1 = items.find('span', {'class': 'a-price-whole'}).text.replace(",","")
                item_price2 = (items.find('span', {'class': 'a-price-fraction'}).text)
                item_info['Listing price'] = (item_price1+item_price2).replace(" ",".")
                item_info['Link to the item'] = ('https://www.amazon.co.uk/'+items.a['href'].replace(" ","-"))
                
                graph_info = {}                                                                                                                    #assigning data to the attributes of the graph info object

                graph_info['Listing price'] = item_info['Listing price']
                graph_info['Timestamp'] =  dt


                if float(item_info.get('Listing price')) < maxvalue and float(item_info.get('Listing price')) > minvalue :                           #check to see if any item meets the max price requirement
                    item_info['To be alerted'] = True
                        

                if item_info.get('To be alerted') == True:                                                                                           #adds the filtered items onto the list of items
                    amazon_items.append(item_info)  

                graphing.append(graph_info)

            except AttributeError:
                continue

        sleep(1.5)

################################################################################################################################################################################
    


    df = pd.DataFrame(graphing, columns=['Listing price','Timestamp'])                               #create dataframes to add to csv file and export it 
    df.to_csv(f'amazon_prices_{user_input}.csv', index=False)
    print('printed csv for Amazon!!!')


################################################################################################################################################################################
    
                                                                 #create dataframes to add to an excell file and export it 


    file_to_check = pd.DataFrame(amazon_items).drop(columns='To be alerted')        
    writer = pd.ExcelWriter(f'{user_input}_Amazon_items_To_Look_At.xlsx') 
    file_to_check.sort_values('Listing price').to_excel(writer, sheet_name='item_found_to_check', index=False, na_rep='NaN')



                                                                #set up a the column on excell and the rows filled with data

    for column in file_to_check:
        column_width = max(file_to_check[column].astype(str).map(len).max(), len(column))
        col_idx = file_to_check.columns.get_loc(column)
        writer.sheets['item_found_to_check'].set_column(col_idx, col_idx, column_width)
    writer.save()
    print('printed excell file for Amazon!!!')

    return 
