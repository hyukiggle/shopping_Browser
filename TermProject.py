#!/usr/bin/env python
# coding: utf-8

# ### 라이브러리 목록

# In[3]:


import urllib.request 
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import selenium

from selenium import webdriver as wb
import time
import re


# ### CatchesFashion으로부터 인기브랜드 목록 가져오기

# In[4]:



options = wb.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = wb.Chrome('C:/Users/kion9/Desktop/2020-2학기/웹파이썬프로그래밍/term_project/chromedriver',chrome_options=options)
driver.implicitly_wait(3)

driver.get('https://www.catchfashion.com/men/brands')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
pop_brand = []
elems = soup.find_all('img', class_='logo')
for brands in elems:
    pop_brand.append(brands['alt'])
    if(len(pop_brand)==24):
        break
'''
brands = soup.find('div', class_='sc-oUmCr bMisCU')
#for b in brands:
 #   brandPre = b.find('div',class_='sc-fzoCUK kBjMiw font_secondaryRegular__2O8hV Typography_UntitledSansR14__1rNws')
  #  brand = brandPre.text
   # pop_brand.append(brand)
'''
print()

pop_brand = sorted(pop_brand)
pop_brand


# ## 각 사이트 별로 브랜드 목록 가져오기

# ### 1. Matchesfashion

# In[5]:


#Matchesfashion | https://www.matchesfashion.com/kr/mens/bags?noattraqt=set
matches_brand = []
'''
options = wb.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
'''
driver = wb.Chrome('C:/Users/kion9/Desktop/2020-2학기/웹파이썬프로그래밍/term_project/chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.matchesfashion.com/kr/mens/designers')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


elems = soup.find_all('a', class_='designeraz__list__item tooltipstered')
for brands in elems:
    brand = brands.get_text()
    matches_brand.append(brand)
    
matches_brand = sorted(matches_brand)
matches_brand


# ### 2. Farfetch

# In[6]:


#Farfetch | https://www.farfetch.com/kr/shopping/men/items.aspx
farfetch_brand = []
options = wb.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = wb.Chrome('C:/Users/kion9/Desktop/2020-2학기/웹파이썬프로그래밍/term_project/chromedriver',chrome_options=options)
driver.implicitly_wait(3)
driver.get('https://www.farfetch.com/kr/designers/men')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
brandsFar = soup.find_all('li', class_='_3d4abb _a99adf')
for b in brandsFar:
    farfetch_brand.append(b.get_text())

farfetch_brand


# ### 3. SSENSE

# In[7]:


#ssense | https://www.ssense.com/en-us/men
ssense_brand = []
driver = wb.Chrome('C:/Users/kion9/Desktop/2020-2학기/웹파이썬프로그래밍/term_project/chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.ssense.com/en-us/men')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

brands = soup.find_all('span', class_='s-text s-text--font-family-inter')
for b in brands:
    ssense_brand.append(b.get_text())
for i in range(4):
    ssense_brand.pop()
ssense_brand


# ### 4. MyTheresa

# In[8]:


#Mytheresa | https://www.mytheresa.com/ko-kr/men.html
mytheresa_brand = []

options = wb.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = wb.Chrome('C:/Users/kion9/Desktop/2020-2학기/웹파이썬프로그래밍/term_project/chromedriver',chrome_options=options)
driver.implicitly_wait(3)
driver.get("https://www.mytheresa.com/ko-kr/men/designers.html")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

brands = soup.find_all('p')
for b in brands:
    brand = b.get_text().strip().replace('\xa0new','')
    brand = brand.replace('\xa0coming soon','')
    mytheresa_brand.append(brand)

start_index = mytheresa_brand.index('1017 ALYX 9SM')

for i in range(start_index):
    del mytheresa_brand[0]
    
for j in range(4):
    del mytheresa_brand[-1]
'''  
for index in range(len(mytheresa_brand)):
    if('\xa0new' in mytheresa_brand[index]):
        mytheresa_brand[index].replace('xa0new','')
        '''
mytheresa_brand = list(filter(None, mytheresa_brand)) # 빈 분자열 제거

print(mytheresa_brand)


# ### 5. END clothing

# In[9]:


#END | https://www.endclothing.com/kr
end_brand =[]

options = wb.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = wb.Chrome('C:/Users/kion9/Desktop/2020-2학기/웹파이썬프로그래밍/term_project/chromedriver',chrome_options=options)
driver.implicitly_wait(3)
driver.get("https://www.endclothing.com/kr/brands")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

brands = soup.find_all('a', class_ = 'Link__InnerLink-e4qf6g-0 fyNuGQ LetterBrandsSection__BrandLinkSC-sc-1hk2oim-4 koSxWv')
for brand in brands:
    b = brand.get_text()
    end_brand.append(b)
    
print(end_brand)


# ### 6. Mr.Porter

# In[10]:


#MrPorter | https://www.mrporter.com/en-kr/
mrporter_brand = []
'''
options = wb.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
'''
driver = wb.Chrome('C:/Users/kion9/Desktop/2020-2학기/웹파이썬프로그래밍/term_project/chromedriver')
driver.implicitly_wait(3)
driver.get("https://www.mrporter.com/en-kr/mens/azdesigners")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

brandAll = soup.find_all('ul', class_= 'DesignerList5__group')

for brands in brandAll:
    for brand in brands.select('li > a'):
        b = brand.get_text()
        mrporter_brand.append(b)    

print(mrporter_brand)
print(len(mrporter_brand))


# In[11]:


matches_brand
farfetch_brand
ssense_brand
mytheresa_brand
end_brand
mrporter_brand
brand_common = list(set(matches_brand) & set(farfetch_brand) & set(ssense_brand) & set(mytheresa_brand) & set(end_brand) & set(mrporter_brand))

brand_common = sorted(brand_common)
brand_set = set(brand_common)
print(brand_common)


# 이제 브랜드를 모두 정리했으니 카테고리를 만들 차례이다.

# ## 카테고리 선택 만들기

# https://www.matchesfashion.com/kr/mens/designers/  
# https://www.farfetch.com/kr/shopping/men/  
# https://www.ssense.com/en-us/men/designers/  
# https://www.mytheresa.com/en-kr/men/designers/  
# https://www.endclothing.com/kr/  
# https://www.mrporter.com/en-kr/mens/designer/  
# 

# ## GUI 생성

# In[14]:


import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from tkinter import *
from tkinter import ttk

class windows_tkinter:
    def __init__(self, broswer):
        self.browser = browser
        self.browser.title("Your Shopping Host")
        self.browser.geometry("450x200")

        self.var1 = StringVar()
        self.var2 = StringVar()

        self.welc = Label(self.browser, text="Welcome back shopping!\n", font = "BerlinSansFB 20")
        self.welc.grid(row=0, column = 1)

        self.brnd = Label(self.browser, text="Brand", font = "BerlinSansFB 10")
        self.brnd.grid(row=1, column =0)

        self.Combo1 = ttk.Combobox(textvariable = self.var1, width=20,state='readonly')
        self.Combo1['value'] = ('1017 ALYX 9SM', 'Acne Studios', 'Alexander McQueen', 'Balenciaga', 'Balmain', 'Burberry', 'Canada Goose', 'Casablanca', 'Common Projects', 'Craig Green', 'Givenchy', 'Gucci', 'JW Anderson', 'Mackintosh', 'Maison Margiela', 'Moncler', 'Moncler Grenoble', 'Polo Ralph Lauren', 'Raf Simons', 'Rick Owens', 'Satisfy', 'Sunspel', 'Thom Browne', 'Tom Wood', 'Undercover', 'Valentino', 'Versace')
        self.Combo1.current(0)
        self.Combo1.grid(row=1, column=1)
        self.selectedBrand = self.Combo1.get()

        self.ctgry =  Label(self.browser, text="Category", font = "BerlinSansFB 10")
        self.ctgry.grid(row=3, column =0)

        self.Combo2 = ttk.Combobox(textvariable = self.var2, width=20,state='readonly')
        self.Combo2['value'] = ('clothing', 'shoes', 'bags', 'accessories')
        self.Combo2.current(0)
        self.Combo2.grid(row=3, column=1)
        self.selectedCategory = self.Combo2.get()
        self.mAddress_list = ["https://www.matchesfashion.com/kr/mens/designers/","https://www.farfetch.com/kr/shopping/men/","https://www.ssense.com/en-us/men/designers/","https://www.mytheresa.com/en-kr/men/designers/","https://www.mrporter.com/en-kr/mens/designer/"]
        self.__main__()

    def genAddress_and_exe(self):
        self.selectedBrand = self.Combo1.get()
        self.selectedCategory = self.Combo2.get()
        brand = self.selectedBrand.replace(' ', '-')

        for mAddress in self.mAddress_list:
            if(mAddress == "https://www.farfetch.com/kr/shopping/men/"):
                if(self.selectedCategory == 'clothing'):
                    category = "/items.aspx?view=90&category=136330"
                elif(self.selectedCategory == 'bags'):
                    category = "bags-purses-2/items.aspx"
                elif(self.selectedCategory =='shoes'):
                    category = "shoes-2/items.aspx"
                elif(self.selectedCategory =='accessories'):
                    category = "accessories-all-2/items.aspx"
                self.address1 = mAddress + brand + '/'+ category
            elif(mAddress == "https://www.ssense.com/en-us/men/designers/"):
                if(brand == "1017-ALYX-9SM"):
                    brandSsense = "alyx"
                else:
                    brandSsense = str.lower(brand)
                self.address2 = mAddress + brandSsense + '/'+self.selectedCategory    
            elif(mAddress == "https://www.mytheresa.com/en-kr/men/designers/"):
                if(brand == "1017-ALYX-9SM"):
                    brandTheresa = str.lower(brand)
                else:
                    brandTheresa = str.lower(brand)
                self.address3 = mAddress + brandTheresa + '/'+self.selectedCategory + ".html"   
            elif(mAddress == "https://www.mrporter.com/en-kr/mens/designer/"):
                if(self.selectedCategory == "bags"):
                    category = "accessories/bags"
                else:
                    category = self.selectedCategory
                self.address4 = mAddress + brand + '/'+ category
            else:
                self.address5 = mAddress + brand + '/'+ self.selectedCategory
   
        CHROMEDRIVER_PATH = './chromedriver.exe'
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument("--disable-infobars")

        #브라우저 실행 및 탭 추가
        driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
        driver.execute_script('window.open("about:blank", "_blank");')
        driver.execute_script('window.open("about:blank", "_blank");')
        driver.execute_script('window.open("about:blank", "_blank");')
        driver.execute_script('window.open("about:blank", "_blank");')

        tabs = driver.window_handles

        # TAB_1
        driver.switch_to_window(tabs[0])
        driver.get(self.address1)

        # TAB_2
        driver.switch_to_window(tabs[1])
        driver.get(self.address2)

        # TAB_3
        driver.switch_to_window(tabs[2])
        driver.get(self.address3)

        # TAB_4
        driver.switch_to_window(tabs[3])
        driver.get(self.address4)

        # TAB_5
        driver.switch_to_window(tabs[4])
        driver.get(self.address5)


    def __main__(self):
        bttn = Button(self.browser, text = "Browse!",command=lambda:self.genAddress_and_exe())
        bttn.grid(row=4, column = 1)

if __name__ == '__main__':    
    browser = Tk()
    windows_tkinter(browser)
    browser.mainloop()


# In[ ]:




