from bs4 import BeautifulSoup
import codecs
import re
import pandas as pd
import csv
import os
with open('Harvey_files.csv', mode = 'w', newline = '') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['num_people_enrolled', 'total_class_size', 'class_number','term', 'professor'])
    writer.writeheader()

    seasons = ['FALL', 'SPRING']
    for season in seasons:
        for j in range(4,6):
            if season is 'SPRING' or season is 'FALL':
                loc = 'HARVEY HTML\\' + season + ' ' + str(j) +'.htm'
                loc = 'HARVEY HTML\\'
                print(os.listdir(loc))
                url = codecs.open(loc,'r', 'utf-8')


                document = BeautifulSoup(url.text, 'html.parser')
                body = document.find('div', {'class': 'pContent CS'})
                panel_body = body.find('tbody', {'class': 'gbody'})
                each_class = panel_body.find_all('tr')

                for i in each_class:
                    each_body = i.find_all('td', {'valign': 'top'})
                    class_name = each_body[2].text
                    #lec_or_lab = each_body.find('div', {'class': 'col-xs-6 col-sm-6'}).text.split(' ')[1]
                    #enrollment_size = enrollment[2].text
                    #enrolled = enrollment_size.split(' ')

                    #class_name = i.a.text;
                    #class_name_num = class_name.split(' ')[1]
                    if(lec_or_lab != 'LAB:'):
                        class_info = {
                        'num_people_enrolled' : enrolled[1],
                        'total_class_size' : enrolled[3],
                        'class_number' : class_name,
                        'term' : season + ' 20' +  str(j)
						}
                        writer.writerow(class_info)
