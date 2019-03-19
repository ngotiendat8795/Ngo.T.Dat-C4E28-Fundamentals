#1. Create connection

from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel


url ="https://dantri.com.vn"
conn = urlopen(url)

#2 Content download

raw_data = conn.read()
html_content = raw_data.decode("utf-8")

with open("dantri.html", "wb") as  f:
    f.write(raw_data)  # tao file dantri.html, save noi dung cua html_content

3. Find ROI (Range of Interest)

soup = BeautifulSoup(html_content,"html.parser")
ul = soup.find("ul","ul1 ulnew")

li_list = ul.find_all("li")  #ket qua tra ra dang list

# for li in li_list:
#     print(li)
#     print("--------------------------------------------------------")

excel_dict = []

for li in li_list:

    h4=li.h4
    a = h4.a
    title = a.string

    link = url + a['href']
   
    matrix= OrderedDict({
        "Title":title,
        "Link":link
    })

    excel_dict.append(matrix)



pyexcel.save_as(records=excel_dict, dest_file_name="your_file.xlsx")








# attribute la class thi chi can viet gia tri, atribute la cai khac vd ID thi phai viet ro Id="ul1 ulnew"

