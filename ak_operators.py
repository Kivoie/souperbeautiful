from bs4 import BeautifulSoup
import requests, re
from tabulate import tabulate
from datetime import datetime
from time import sleep


def get_data():
    web_url = 'https://gamepress.gg/arknights/database/operator-release-dates-and-how-obtain'	#hard coded the URL
    tempfile = '/home/ubuntu/Documents/souperbeautiful/ak.txt'
    
    try:
        response = requests.get(web_url)	#attempt to connect to the web page
    
    except Exception as e:
    
        print(f"Could not open the webpage\n{e}")	#quit if not successful
        quit()
    
        
    html_content = response.content
    
    soup = BeautifulSoup(html_content, 'html.parser')	#parse the web page
    
    
    table = soup.find("table", id="sort-table")		#find the "table" tag with the id "sort-table"
    
    operator_names = table.findAll("td", {"class":"views-field views-field-title"})					#all operator names
    operator_obtain = table.findAll("td", {"class":"views-field views-field-field-obtain-approach"})		#all operation acquisition methods
    operator_times_cn = table.findAll("td", {"class":"views-field views-field-field-operator-release-date-cn"})	#all operator release dates (CN)
    operator_times_na = table.findAll("td", {"class":"views-field views-field-field-operator-release-date-na"})	#all operator release dates (NA), aka Global
    
    
    ##### Parse for all the unreleased operators in NA #####
    
    count = 0						#counter for counting the number entries
    output_table_tbd = []					#initialize an array to store all the results later
    for i in range (0, len(operator_times_na)):		#iterate through all the operators listed in the table
    
        if str(operator_times_na[i].text).strip() == "":		#there is a trailing character (space or CRLF, I can't tell). strip it to make it easier to parse
            if str(operator_names[i].text).strip() == 'Tulip' or str(operator_names[i].text).strip() == 'Reserve Operator - Defender' or str(operator_names[i].text).strip() == 'Vector - APRIL FOOLS!' or str(operator_names[i].text).strip() == 'Ashlock':
                continue	#just skip these 4 operators because there is some missing information from the editor
            else:
    
                #add the new entries to the table
                new_entry = [(count + 1 + 5), operator_names[i].text, str(re.sub(r'\b(\w+)\b(?=.*\b\1\b)', '', operator_obtain[i].text.replace("\n", " "))).strip(), operator_times_cn[i].text.strip(), operator_times_na[i].text.strip()]
                output_table_tbd.append(new_entry)
                
                count += 1
    
    
    ##### Parse for all the released operators in NA #####
    
    release_context = 5					#integer to count how many RELEASED operators to include for context
    count = 0						#counter for counting the number of entries
    output_table_released = []				#initialize an array to store all the results later
    for i in range (0, 40):
        if operator_times_na[-i].text.strip():
            
            #add the new entries to a different table
            new_entry = [(release_context - count), operator_names[-i].text, str(re.sub(r'\b(\w+)\b(?=.*\b\1\b)', '', operator_obtain[-i].text.replace("\n", " "))).strip(), operator_times_cn[-i].text.strip(), operator_times_na[-i].text.strip()]
            output_table_released.append(new_entry)
            
            count += 1
        
        if count >= release_context:
            output_table_released = output_table_released[::-1]
            break
    
                
    #combine both arrays in order
    combined_array = []
    combined_array.extend(output_table_released)
    combined_array.extend(output_table_tbd)
    
    #print statements to output everything from above
    timestamp = str(datetime.now().strftime("%Y%m%d-%H:%M:%S"))
    #print(f"Dan's script: 'ak-operators.py' executed on {}")
    #print(tabulate(combined_array, headers=['#', 'Operator', 'Acquisition', 'CN Release', 'NA Release']))

    with open(tempfile, "w+") as output_file:

        output_file.write(f"Dan's script: 'ak_operators.py' executed on {timestamp}\n")
        output_file.write(tabulate(combined_array, headers=['#', 'Operator', 'Acquisition', 'CN Release', 'NA Release']))
    
    sleep(2)


