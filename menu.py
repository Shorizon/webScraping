import Headless_amazon_scraper
import Headless_ebay_scraper
import average
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from datetime import datetime
import file_merger
import plottercsv
import PySimpleGUI as sg 
import os
from os.path import exists as file_exists
import webbrowser


                                    #define data for timestamps that are needed for the graphs
dt = datetime.now().date()

                                                        #set a theme for the UI
sg.theme("DarkAmber")

###########################################################################################################################

                                #set the visual layout the GUI, in order (Top to bottom)


column_lay = [


]

layout = [

    [
        sg.Text("enter the item to scan:   "),
        sg.InputText(),                                      # pysimpleGUI's input detection
    ],
    [
        sg.Text("budget you have:            "),
        sg.InputText()                                       
    ],
    [
        sg.Text("ignore items lower than:"),
        sg.InputText()
    ],
    [
        sg.Button("Run"),
        sg.Button("Open excel"),
        sg.Button("Open cheapest"),
        sg.Button("Exit", key="Exit")
     
    ],
    [
       sg.Text("Please fill up all the fields and run once before attempting to open the excell"),

    ],
    [

        sg.Output(size=(75,15), key='-OUTPUT-'),

    ],                                             
]


###########################################################################################################################

                                            #set the windows' options 

window = sg.Window("Quick_Searcher_Multitool", layout, finalize= True, element_justification= "Justified")


###########################################################################################################################

                                            #event loop needed to run the GUI (awaits for events to trigger)
while True:
    event,values = window.read()
                                                                                    #reads values that the window sends(eg. on clicks, button presses etc.)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break 
    if event == "Run" and values[0] != '' and values[1] != '' and values[2] != '' and values[0] != '':              #check for empty input boxes
        search_keyword = values[0]
        maxvalue = float(values[1])
        minvalue = float(values[2])
        user_input = search_keyword.replace(' ', '+')    
        Headless_amazon_scraper.amazon(search_keyword, maxvalue, minvalue,dt)                                        #runs the modules' methods 
        sent = Headless_ebay_scraper.ebay(search_keyword, maxvalue, minvalue,dt)
        print(sent)
        average.meaning(f'Ebay_prices_{user_input}.csv',f'Amazon_prices_{user_input}.csv',user_input)
        file_merger.file_merger(f'Ebay_averaged_{user_input}.csv',f'Amazon_averaged_{user_input}.csv',user_input)
        plottercsv.graph_plotter(f'Ebay_graphing_list_{user_input}.csv',f'Amazon_graphing_list_{user_input}.csv')                                                            #prompts the user to fill all the boxes
    if event == "Open excel":
        try:
            if file_exists(f'{user_input}_Ebay_items_To_Look_At.xlsx') == True and file_exists(f'{user_input}_Amazon_items_To_Look_At.xlsx') == True:
                os.system(f'start excel.exe {user_input}_Ebay_items_To_Look_At.xlsx')
                os.system(f'start excel.exe {user_input}_Amazon_items_To_Look_At.xlsx')
            else:
                 sg.Popup("the files don't seem to exist, please run the program once")
        except NameError:
         sg.Popup("Please enter the item you are looking for")
         continue   
    if event == "Open cheapest":
        try:
            webbrowser.open(sent)
        except Exception as e:
            sg.Popup("no file found, please run the program once")
            continue

window.close()
