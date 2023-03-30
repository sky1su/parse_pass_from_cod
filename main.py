from requests_html import HTMLSession
import csv

file_in = 'urls.txt'
file_out = 'out.csv'
with open (file_out, 'w') as pass_file:
    fieldnames = ['host',
                  'login',
                  'password'
                  ]
    writer = csv.DictWriter(pass_file, fieldnames, delimiter=';')
    writer.writeheader()
    with open(file_in, 'r') as urls_list:
        while True:
            line = urls_list.readline()
            if not line:
                break
            line1 = line.split()
            # print (line1)
            try:
                session = HTMLSession()
                r = session.get(line1[2])
                result = (r.html.find('center', first=True).text.split())
                data = [{
                    'host': line1[0]+" "+line1[1],
                    'login': result[1],
                    'password': result[3]
                }]
            except:
                break
            for field in data:
                writer.writerow(field)



