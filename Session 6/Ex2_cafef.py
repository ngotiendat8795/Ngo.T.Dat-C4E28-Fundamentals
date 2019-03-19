from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

data = urlopen(url)
raw_data= data.read()
clean_data = raw_data.decode()

soup = BeautifulSoup(clean_data,"html.parser")

header = soup.find("table",id={"tblGridData"})
list_raw_headers = header.find_all("td")


list_headers = []

for td in list_raw_headers:
    list_headers.append(td.string)


Table_Data = []

content = soup.find("table",id={"tableContent"})

row_list = content.find_all("tr",class="r_item")


for row in row_list:
    cells = row.find_all("td","b_r_c")
    cell_data = []
    for td in cells:
        cell_data.append(td.string)
        Data_List = dict(zip(list_headers,cell_data))

    Table_Data.append(Data_List)





pyexcel.save_as(records=Table_Data,dest_file_name="cafef.xlsx")





