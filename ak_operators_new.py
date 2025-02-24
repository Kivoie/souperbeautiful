from bs4 import BeautifulSoup
import requests, re
from tabulate import tabulate


def get_data():
    web_url = 'https://arknights.wiki.gg/wiki/Headhunting/Banners/Upcoming'	#hard coded the URL
    #tempfile = '/home/ubuntu/Documents/souperbeautiful/ak_new.txt'
    #tempfile2 = '/home/ubuntu/Documents/souperbeautiful/ak-simple-new.txt'
    
    try:
        print(f"Connecting to {web_url}...")
        response = requests.get(web_url)	#attempt to connect to the web page
    
    except Exception as e:
        print(f"Could not open the webpage\n{e}")	#quit if not successful
        return str(e)
    else:
        print(f"Connection to {web_url} successful")

    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')	#parse the web page

    banner_names = []
    operator_names = []
    temp_operator_names = []
    release_date_cn = []
    combined_array = []
    
    table = soup.find("table", {"class":"mrfz-wtable"})		#find the "table" tag with the class 'mrfz-wtable'

    for row in table.findAll('tr'):                         #search through each row in the table
        div_banner = row.find('div', {"class":"banner"})    #find the banner names
        if div_banner:
            spans = div_banner.findAll('span')
            for span in spans:
                if not 'Kernel' in str(span.get_text()):
                    banner_names.append(str(span.get_text()))

    for row in table.findAll('tr'):                         #search through each row in the table
        div_date = row.find('div', {"style":"margin:5px; text-align:center;"})  #find the release dates
        if div_date:
            divs = div_date.findAll('div')
            for div in divs:
                if div.get_text():
                    release_date_cn.append(re.sub("\\u2013", '-', (str(div.get_text()))))       #This is a really weird hyphen character

    for row in table.findAll('tr'):                         #search through each row in the table
        div_operators = row.findAll('div', {"class":"character-tooltip"})       #find all character icons and extract the names from each

        for data_name_attribute in div_operators:
            data_name = data_name_attribute.get('data-name')
            if data_name:
                temp_operator_names.append(str(data_name))

        if div_operators:
            operator_names.append(temp_operator_names)
            temp_operator_names = []

    #for i in range(len(banner_names)):
        #combined_array.append((banner_names[i], release_date_cn[i], operator_names[i]))
    combined_output = ''
    for i in range(len(banner_names)):
        combined_output += f"**{banner_names[i]}**\n{release_date_cn[i]}\n"
        for j in range(len(operator_names[i])):
            combined_output += f"{operator_names[i][j]}\n"
        combined_output += "\n"

    #print(combined_output)
    return str(combined_output)


    #json_string = json.dumps(combined_array, indent=4)
    #print(re.sub("\[", '', str(json_string)))

    #new_table = tabulate(combined_array, headers=["Banner", "Operators", "Event Duration"], tablefmt="html")
    #print(new_table)
    #return str(new_table)

get_data()

