from bs4 import BeautifulSoup
import codecs
import re
import pandas as pd
import csv
with open('UCSC files.csv', mode = 'w', newline = '') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['num_people_enrolled', 'total_class_size', 'class_number','term', 'professor'])
    writer.writeheader()

    seasons = ['FALL', 'SPRING', 'WINTER']
    for season in seasons:
        for j in range(4,20):
            if j >= 5 or seasons is 'FALL':
                folder = 'UCSC HTML\\' + season + ' ' + str(j) +'.html'

                url = codecs.open(folder,'r', 'utf-8')
                document = BeautifulSoup(url, 'html.parser')

                body = document.find('div', {'class': 'panel panel-info center-block'})
                panel_body = body.find('div', {'class': 'panel-body'})
                each_class = panel_body.find_all('div', {'class': 'panel panel-default row'})

                for i in each_class:
                    each_body = i.find('div', {'class': 'panel-body'})
                    enrollment = each_body.find_all('div', {'class': 'col-xs-6 col-sm-3'})
                    lec_or_lab = each_body.find('div', {'class': 'col-xs-6 col-sm-6'}).text.split(' ')[1]
                    enrollment_size = enrollment[2].text
                    enrolled = enrollment_size.split(' ')
                    prof = enrollment[1].text.split(' ')[1]

                    class_name = i.a.text;
                    class_name_num = class_name.split(' ')[1]
                    if(lec_or_lab != 'LAB:'):
                        class_info = {
                        'num_people_enrolled' : enrolled[1],
                        'total_class_size' : enrolled[3],
                        'class_number' : class_name_num,
                        'term' : season + ' 20' +  str(j),
                        'professor': prof
						}
                        writer.writerow(class_info)
