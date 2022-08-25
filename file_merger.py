import pandas as pd
from os.path import exists as file_exists




#################################################################################################################### 
	
						#adds the averaged data into the final csv that is needed for graphing (or creates a new one if it doesnt exist)


def file_merger(ebay,amazon,user_input):

	data = pd.read_csv(ebay)												#reads the data from the file

	if file_exists(f'Ebay_graphing_list_{user_input}.csv') == True:											#adds data to the final file if it exist
		data.to_csv(f'Ebay_graphing_list_{user_input}.csv', mode='a', index=False, header =False)
	else:																									#creates a new file with headers if it doesnt exist
		data.to_csv(f'Ebay_graphing_list_{user_input}.csv', mode='a', index=False, header =True)
		


	data = pd.read_csv(amazon)												#reads the data from the file

	if file_exists(f'Amazon_graphing_list_{user_input}.csv') == True:										#adds data to the final file if it exist
		data.to_csv(f'Amazon_graphing_list_{user_input}.csv', mode='a', index=False, header =False)
	else:																									#creates a new file with headers if it doesnt exist
		data.to_csv(f'Amazon_graphing_list_{user_input}.csv', mode='a', index=False, header =True)			
		
	return True


#################################################################################################################### 

