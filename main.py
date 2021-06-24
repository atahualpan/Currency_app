from kivy.app import App
#for graphs
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from kmplot.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
#for google ad banner
from kivmob import KivMob
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen,WipeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle, Color,Line
from kivy.utils import platform
import os
from kivy.uix.label import Label
#to write csv file inside app folder
import csv    
import datetime
#regex library
import re
#for request and webscrape data from BNR website
import urllib3
import certifi
import os
import chardet
import idna
#to get current date
import time
#for google play store link
import webbrowser
# cancell back button to close application
Config.set('kivy', 'exit_on_escape', '0')

# Here's all the magic for web request to work!
os.environ['SSL_CERT_FILE'] = certifi.where()

#Spinner Class
class SpinnerOptionsBlue(SpinnerOption):
    def __init__(self, **kwargs):
        super(SpinnerOptionsBlue, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = "0488D8"   # white colour
        self.color = [1, 1, 1, 1]
        with self.canvas:
            Color(0,0,0,1)
            for x in range(0,int(self.height)*40,int(self.height)):
                Line(width= 1,rectangle= ([-20, x, Window.size[0]*3, self.height]))
                ''' Line(width= 2,rectangle= ([self.x, 96, Window.size[0]*0.999, self.height]))
                Line(width= 2,rectangle= ([self.x, 144, Window.size[0]*0.999, self.height]))
                Line(width= 2,rectangle= ([self.x, 192, Window.size[0]*0.999, self.height]))
                Line(width= 2,rectangle= ([self.x, self.y, Window.size[0]*0.999, self.height]))'''

class CSpinnerBlue(Spinner):
    
    def __init__(self, **kwargs):
        super(CSpinnerBlue, self).__init__(**kwargs)
        self.dropdown_cls = SpinnerDropdown
        self.option_cls = SpinnerOptionsBlue
        self.color= [0, 0, 0, 1]
        self.background_normal= ""
        self.background_color = 1,1,1,1
       

        
class SpinnerOptions(SpinnerOption):

    def __init__(self, **kwargs):
        super(SpinnerOptions, self).__init__(**kwargs)
        self.listasteag = ['aed.png', 'aud.png', 'bgn.png', 'brl.png', 'cad.png', 'chf.png', 'cny.png', 'czk.png', 'dkk.png', 'egp.png', 'eur.png', 'gbp.png', 'hrk.png', 'huf.png', 'inr.png', 'jpy.png', 'krw.png', 'mdl.png', 'mxn.png', 'nok.png', 'nzd.png', 'pln.png',
 'rsd.png', 'rub.png', 'sek.png', 'thb.png', 'try.png', 'uah.png', 'usd.png', 'xau.png', 'xdr.png', 'zar.png','zron.png']
       
        self.background_normal = ''
        self.background_color = 1,1,1,1    # white colour
        self.color = [0, 0, 0, 1]
        with self.canvas:
            Color(0,0,0,1)
            for x in range(0,int(self.height)*40,int(self.height)):
                Line(width= 1,rectangle= ([-20, x, Window.size[0]*3, self.height]))
            
class SpinnerDropdown(DropDown):

    def __init__(self, **kwargs):
        super(SpinnerDropdown, self).__init__(**kwargs)
        self.max_height= 1000
        self.bar_width= 15
        self.bar_color= 0,0,0,1   # black
        self.bar_inactive_color= 0,0,0,1  # black        
        self.effect_cls= 'ScrollEffect'
        self.scroll_type= ['bars', 'content']
        
class CSpinner(Spinner):
    
    def __init__(self, **kwargs):
        super(CSpinner, self).__init__(**kwargs)
        self.dropdown_cls = SpinnerDropdown
        self.option_cls = SpinnerOptions
        self.color= [0, 0, 0, 1]
        self.background_normal= ""
        self.background_color = 1,1,1,1

        

#TextInput class
class TextInput1(TextInput):
    def on_focus(self, *args):
        #for solving textinput unfocus bug(bug that disable android backbutton)
         if platform == "android":
            from kvdroid import activity
            from android.runnable import run_on_ui_thread

            @run_on_ui_thread
            def fix():
                activity.onWindowFocusChanged(False)
                activity.onWindowFocusChanged(True)
            if not args[1]:
                fix()

#class for store dictionaries,list and functions that will be used for other classes
class Monedev():
    def __init__(self,**kwargs):
        super(Monedev, self).__init__(**kwargs)
        self.listasteag = ['aed.png', 'aud.png', 'bgn.png', 'brl.png', 'cad.png', 'chf.png', 'cny.png', 'czk.png', 'dkk.png', 'egp.png', 'eur.png', 'gbp.png', 'hrk.png', 'huf.png', 'inr.png', 'jpy.png', 'krw.png', 'mdl.png', 'mxn.png', 'nok.png', 'nzd.png', 'pln.png',
 'rsd.png', 'rub.png', 'sek.png', 'thb.png', 'try.png', 'uah.png', 'usd.png', 'xau.png', 'xdr.png', 'zar.png']
        self.simboluri = ['AED', 'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EGP', 'EUR', 'GBP', 'HRK', 'HUF', 'INR', 'JPY', 'KRW', 'MDL', 'MXN', 'NOK', 'NZD', 'PLN', 'RSD', 'RUB', 'SEK', 'THB', 'TRY', 'UAH', 'USD', 'XAU', 'XDR', 'ZAR','RON']
        self.dictluni= {"Ianuarie":"01","Februarie":"02","Martie":"03","Aprilie":"04","Mai":"05","Iunie":"06","Iulie":"07","August":"08","Septembrie":"09","Octombrie":"10","Noiembrie":"11","Decembrie":"12"}
        self.listaluni = list(key for key in self.dictluni)
        self.listalunaircc = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        self.dictlunaircc = dict(zip(self.listaluni,self.listalunaircc))
        self.dictlunairccinv = dict(zip(self.listalunaircc,self.listaluni))
        self.listadenumire = ["Dirhamul Emiratelor","Dolarul australian","Leva bulgarească","Realul brazilian","Dolarul canadian","Francul elveţian",
                              "Renminbi-ul chinezesc","Coroana cehă","Coroana daneză","Lira egipteană","Euro","Lira sterlină","Kuna croată","Forint maghiar",
                              "Rupia indiană","Yen japonez","Won sud-corean","Leul moldovenesc","Peso-ul mexican","Coroana norvegiană",
                              "Dolarul neo-zeelandez","Zlotul polonez","Dinarul sârbesc","Rubla rusească","Coroana suedeză","Bahtul thailandez","Noua lira turcească",
                              "Hryvna ucraineană","Dolarul american","Gramul de aur","DST","Randul sud-african","Leu românesc"]
        self.listazile = ["01","02","03","04","05","06","07","08","09",'10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21','22', '23', '24', '25', '26', '27','28', '29', '30', '31']      
        self.arhivaluni= {"Ianuarie":".Jan","Februarie":".Feb","Martie":".Mar","Aprilie":".Apr","Mai":".May","Iunie":".Jun","Iulie":".Jul","August":".Aug","Septembrie":".Sep","Octombrie":".Oct","Noiembrie":".Nov","Decembrie":".Dec"}
        self.valori = self.vtoday()
        self.lunabnr = [".Dec"".Jan",".Feb",".Mar",".Apr",".May",".Jun",".Jul",".Aug",".Sep",".Oct",".Nov",".Dec"]
        self.lunadit = dict(zip(self.lunabnr,list(str(x) for x in range(0,13))))
        self.lunaditinv = dict(zip(list(str(x) for x in range(0,13)),self.lunabnr))
        self.valori[13] = str(round(float(self.valori[13])/100,6))
        self.valori[15] = str(round(float(self.valori[15])/100,6))
        self.valori[16] = str(round(float(self.valori[16])/100,6))
        self.cursbnrcurs = dict(zip(self.listadenumire,self.valori))
        self.dictmonth = dict(zip(self.listazile[0:12],self.listaluni))
        self.valori.append("1")
        self.valoricurs = list(str(round(1/float(v),200)) for v in self.valori)

        self.cursbnr = dict(zip(self.listadenumire,self.valoricurs)) 
        self.year = str(datetime.date.today().year)
        self.month = str(datetime.date.today().month)
        
        self.day = str(datetime.date.today().day)
        if int(self.month) in range(1,10):
            self.month = "0"+str(self.month)
        else:
            self.month = str(self.month)

        if int(self.day) in range(1,10):
            self.day = "0"+str(self.day)
        else:
            self.day = str(self.day)
        self.steag = dict(zip(self.listadenumire,self.listasteag))
        self.lunaazi = str(int(self.month)+1)
    #func to scrape and get daily currency values
    def getvaloricurs(self):
      try:
        valori = re.findall(r'\d.\d\d\d\d|\d\d\d.\d\d\d\d',str(urllib3.PoolManager().request("GET","https://www.bnr.ro/nbrfxrates.xml").data))
        return valori
      except:
        pass
    #func to write daily values to csv file 
    def vtoday(self):

        if type(self.getvaloricurs()) == list:
            with open('values.csv', mode='w') as valte_file:
              employee_writer = csv.writer(valte_file, delimiter=',')
              employee_writer.writerow(self.getvaloricurs())

        val = []
        with open('values.csv') as valute_file:
          valute_reader = csv.reader(valute_file, delimiter=',')
          for row in valute_reader:
            for r in row:
              val.append(r)
        return val
    #func to go to main screen
    def backtomenu(self):       
        mainApp.sm.current = 'menu'

#main screen class        
class MainMenu(Screen,Monedev):
    
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.inflatie = ""
        self.robor3m = ""
        self.ircc = ""
        self.ids.rvsc.data = [{'text': f"     [color=#000FC1]{self.listadenumire[x]}[/color]  [color=#DE2711]{self.valori[x]}[/color]",'image':f"{self.listasteag[x]}"} for x in [10,28,11,5,17,13,26,2,1,3,4,6,7,8,9,12,14,15,16,18,19,20,21,22,0,23,24,25,27,29,30,31]]
        self.dictarhcurs = {"Euro":"5462","Dolarul american":"5471","Lira sterlină":"5463","Francul elveţian":"5458","Leul moldovenesc":"5466","100 Forinți maghiari":"5464"}
        self.labelmenux()
        self.width = Window.size[0]
        Window.bind(on_keyboard=self.Android_back_click_menu)
        Window.softinput_mode = 'below_target'
        self.butonda = Button(text="DA",background_normal="",background_color=[0,0,1,1])
        self.butonnu = Button(text="NU",background_normal="",background_color=[0,0,1,1])
        self.gridpop = GridLayout(cols=2,spacing=10,padding=10)
        self.gridpop.add_widget(self.butonda)
        self.gridpop.add_widget(self.butonnu)
        
        self.popup = Popup(title='Dorești să închizi aplicația?',title_size=60,content=self.gridpop,size_hint=(None, None), size=(Window.size[0]/1.2, Window.size[1]/5),background ="",title_color=[0,0,0,1])
        self.butonnu.bind(on_press=self.popup.dismiss)
        self.butonda.bind(on_press=self.close_application)
        
    def close_application(self,*args):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()
    def Android_back_click_menu(self,window,key,*largs):
            if key == 27 and mainApp.sm.current_screen.name == "menu":
                self.popup.open()
                
    #func for creating recycleview and scrape daily data
    def labelmenux(self,*args):
        
        if self.inflatie == None :
            self.inflatie = "Conexiune Internet inexistentă"
            self.robor3m = "Conexiune Internet inexistentă"
            self.ircc = "Conexiune Internet inexistentă"
        else:
            try:
                self.ircc = str(list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',str(urllib3.PoolManager().request("GET","https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=1831&column=26031").data))) if i%2==1)[0])      
                self.inflatie = str(re.findall(r'\d,\d\d',str(urllib3.PoolManager().request("GET","https://www.bnr.ro/Home.aspx").data))[1].replace(",","."))
                self.robor3m = str(list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',str(urllib3.PoolManager().request("GET","https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=642&column=3573").data))) if i%2==1)[1])
            except:
                self.ircc = "Conexiune Internet inexistentă"     
                self.inflatie = "Conexiune Internet inexistentă"
                self.robor3m = "Conexiune Internet inexistentă"
        butonmenu = Button(text="Actualizare date",background_normal= '' ,background_color= "019FFF",)
        labelmenu = Label(text= "[color=#000FC1]IRCC 3 LUNI - "+f"[color=#DE2711]{self.ircc}%[/color]  "
                          +"[color=#000FC1]ROBOR3M - "+f"[color=#DE2711]{self.robor3m}% "+"\n[color=#000FC1]RATA INFLAŢIEI - "+f"[color=#DE2711]{self.inflatie}% ",markup= True)
                
        self.ids.gridmenu.add_widget(labelmenu)
        butonmenu.bind(on_press=self.actualizare)
        self.ids.gridmenu.add_widget(butonmenu)
        self.ids.rvsc.data = [{'text': f"     [color=#000FC1]{self.listadenumire[x]}[/color]  [color=#DE2711]{self.valori[x]}[/color]",'image':f"{self.listasteag[x]}"} for x in [10,28,11,5,17,13,26,2,1,3,4,6,7,8,9,12,14,15,16,18,19,20,21,22,0,23,24,25,27,29,30,31]]

    #func for main screen converter(converting user input to desire currency)
    def valuta(self,fromunit,value):
        try:
            self.ids.input34.text = str(round(float(value) * float(self.cursbnr[self.ids.spiner2.text])/float(self.cursbnr[fromunit]),2))            
        except:
            pass
        
    #button func for switching type of currency      
    def switchunit(self):
        unit1 = self.ids.spiner1.text
        unit2 = self.ids.spiner2.text
        self.ids.spiner1.text = unit2
        self.ids.spiner2.text = unit1

    #to go to desired screen, and navigate google play store link   
    def gotocursarhiva(self):
        Config.set('kivy', 'exit_on_escape', '0')
        
        if self.ids.spinermenu.text == "Curs Valutar arhivă - Grafice":
            if self.b == 0:
                mainApp.sm.add_widget(Cursarhiva(name='cursarhiva')) 
                self.b += 1
            mainApp.sm.current = 'cursarhiva'
            self.ids.spinermenu.text = "Meniu"
            
        elif self.ids.spinermenu.text == "Info":
            if self.a == 0:
                mainApp.sm.add_widget(Info(name='info')) 
                self.a += 1
            mainApp.sm.current = 'info'
            self.ids.spinermenu.text = "Meniu"
            
        elif self.ids.spinermenu.text == "Date IRCC - ROBOR":
            if self.c == 0:
                mainApp.sm.add_widget(IRCCROBOR(name='irccrobor'))
                self.c += 1
            mainApp.sm.current = 'irccrobor'
            self.ids.spinermenu.text = "Meniu"
            
        #navigate google play store link 
        elif self.ids.spinermenu.text == "Evaluează aplicația":
            webbrowser.open("https://play.google.com/store/apps/details?id=org.fmzkapps.cursrobor.fmzkapps")
            self.ids.spinermenu.text = "Meniu"       

    #update daily values button in case internet down   
    def actualizare(self,*args):
        self.valori = self.vtoday()
        self.ids.rvsc.data = [{'text': f"     [color=#000FC1]{self.listadenumire[x]}[/color]  [color=#DE2711]{self.valori[x]}[/color]",'image':f"{self.listasteag[x]}"} for x in [10,28,11,5,17,13,26,2,1,3,4,6,7,8,9,12,14,15,16,18,19,20,21,22,0,23,24,25,27,29,30,31]]
        try:
            self.ircc = str(list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',str(urllib3.PoolManager().request("GET","https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=1831&column=26031").data))) if i%2==1)[0])      

            self.inflatie = str(re.findall(r'\d,\d\d',str(urllib3.PoolManager().request("GET","https://www.bnr.ro/Home.aspx").data))[1].replace(",","."))
            self.robor3m = str(list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',str(urllib3.PoolManager().request("GET","https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=642&column=3573").data))) if i%2==1)[1])
        except:
            self.ircc = "Conexiune Internet inexistentă"
            self.inflatie = "Conexiune Internet inexistentă"
            self.robor3m = "Conexiune Internet inexistentă"
       
        self.ids.gridmenu.children[-1].text = "[color=#000FC1]IRCC 3 LUNI - "+f"[color=#DE2711]{self.ircc}%[/color] \n" +"[color=#000FC1]ROBOR3M - "+f"[color=#DE2711]{self.robor3m}% "+"\n[color=#000FC1]RATA INFLAŢIEI - "+f"[color=#DE2711]{self.inflatie}% "
                  
#class for currency archive data and graphs       
class Cursarhiva(Screen,Monedev):
 
    def __init__(self, **kwargs):
        super(Cursarhiva, self).__init__(**kwargs)
        self.dictarhcurs = {"Euro":"5462","Dolarul american":"5471","Lira sterlină":"5463","Francul elveţian":"5458",
                            "Leul moldovenesc":"5466","Forint maghiar":"5464","Leva bulgarească":"5476","Dolarul australian":"5456",
                            "Dolarul canadian":"5457","Coroana cehă":"5459","Coroana daneză":"5460","Lira egipteană":"5461",
                            "Coroana norvegiană":"5467","Zlotul polonez":"5468","Coroana suedeză":"5469","Noua lira turcească":"5470",
                            "Gramul de aur":"5472","DST":"5473","Rubla rusească":"5474","Yen japonez":"5465","Randul sud-african":"5477",
                            "Realul brazilian":"5478","Renminbi-ul chinezesc":"5479","Rupia indiană":"5480","100 Woni sud-coreeni":"5481",
                            "Peso-ul mexican":"5482", "Dolarul neo-zeelandez":"5483","Dinarul sârbesc":"5484","Hryvna ucraineană":"5485",
                            "Bahtul thailandez":"24691","Dirhamul Emiratelor":"5486","Kuna croată":"20251"}

        self.listaarhcu = [self.valori[10],"1"]

        Window.softinput_mode = 'below_target'
        
        Window.bind(on_keyboard=self.Android_back_click)
        self.butoninchide = Button(text="Închide",background_normal="",background_color=[0,0,1,1],size_hint=(1, 0.1),pos_hint={'x': 0, 'y':0})
        self.figura = FigureCanvasKivyAgg(plt.gcf(),size_hint=(1, 0.8),pos_hint={'x': 0, 'y':0.2})
        self.gridpop = BoxLayout(orientation = "vertical")
        self.eticheta = Button(text="",color = [0,0,0,1],background_normal="",background_color=[0,0,0,0],size_hint=(1, 0.1),pos_hint={'x': 0, 'y':0.1})
        self.popup = Popup(title=f'Grafic {self.ids.spinerarhiva.text}',content=self.gridpop,background ="",
                           title_color=[0,0,0,1],separator_height = 2,size_hint=(1, 0.88),pos_hint={'x': 0, 'y':0})

    #back to main screen   
    def Android_back_click(self,window,key,*largs):
            if key == 27:
                Clock.schedule_once(self.menucurrent,0.1)
    def menucurrent(self,*args):
        mainApp.sm.current = 'menu'
    #webscrape for currency archive data
    def getarhivacurs(self,zi,luna,an,val):
        self.ids.spinergrafluna.text = "Perioadă Grafic "+f"{self.ids.spinerarhiva.text}"
        if int(self.dictluni[self.ids.spinerluna.text]) > int(self.month) and int(self.ids.spineran.text) == int(self.year):
            self.ids.labeleroare.text = "Eroare"
        elif int(self.dictluni[self.ids.spinerluna.text]) == int(self.month) and int(self.ids.spineran.text) == int(self.year) and int(self.ids.spinerzi.text) > int(self.day):
            self.ids.labeleroare.text = "Eroare"
            
            
            
        else:
            self.ids.labeleroare.text = ""
            try:
                valoare = str(re.findall(f'{zi}{luna}{an}.......................................',str(urllib3.PoolManager().request("GET",
                     f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={val}").data)))[-8:-2]
                self.ids.labelarh.text = valoare
                self.ids.labeleroare.text = ""
                ziua = self.ids.spinerzi.text
                zizi = 0
                lulu = 0
                anan = 0
                if valoare == "-</td>" :
                    self.ids.labelarh.text = ""
                    self.ids.labeleroare.text = "Randul,Realul,Renminbi-ul,Rupia,Won-ul,Peso-ul,Dolarul neo-zeelandez,Dinarul,Hryvna,Dirhamul-începand cu [color=#000FC1]02 Mar 2009[/color]\nLeva-începand cu [color=#000FC1]03 Dec 2007[/color]\nRubla-începand cu [color=#000FC1]12 Nov 2007[/color]\nBahtul-începand cu [color=#000FC1]19 Iun 2017[/color]\nKuna-începand cu [color=#000FC1]21 Aug 2015[/color]\n"
                        
                    
                while valoare == '':
                    
                    #self.ids.spinerzi.text
                    zi = str(int(ziua)-1-zizi)
                    zizi += 1
                    valoare = str(re.findall(f'{zi}{luna}{an}.......................................',str(urllib3.PoolManager().request("GET",
                     f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={val}").data)))[-8:-2]
                    self.ids.labelarh.text = valoare
                    if zi== "0":
                        if luna ==".Jan":
                            luna = ".Dec"
                            zi = "31"
                            an = str(int(self.ids.spineran.text)-1)
                            valoare = str(re.findall(f'{zi}{luna}{an}.......................................',str(urllib3.PoolManager().request("GET",
                             f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={val}").data)))[-8:-2]
                            self.ids.labelarh.text = valoare
                            zizi = 0
                            ziua = "31"
                        else:     
                            zi = "31"                   
                            lunacifra = str(int(self.lunadit[luna])-1)
                            luna = self.lunaditinv[lunacifra]
                            valoare = str(re.findall(f'{zi}{luna}{an}.......................................',str(urllib3.PoolManager().request("GET",
                             f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={val}").data)))[-8:-2]
                            self.ids.labelarh.text = valoare
                            zizi = 0
                            ziua = "31"
                        

                else:
                    if valoare == "-</td>" :
                        self.ids.labelarh.text = ""
                        self.ids.labeleroare.text = "Randul,Realul,Renminbi-ul,Rupia,Won-ul,Peso-ul,Dolarul neo-zeelandez,Dinarul,Hryvna,Dirhamul-începand cu [color=#000FC1]02 Mar 2009[/color]\nLeva-începand cu [color=#000FC1]03 Dec 2007[/color]\nRubla-începand cu [color=#000FC1]12 Nov 2007[/color]\nBahtul-începand cu [color=#000FC1]19 Iun 2017[/color]\nKuna-începand cu [color=#000FC1]21 Aug 2015[/color]\n"

                    else:
                        pass
                    
                    
                if self.ids.spinerconv1.text == "Leu românesc" and self.ids.spinerconv2.text != "Leu românesc":
                    valoare1 = "1"
                    valoare2 = str(re.findall(f'{zi}{luna}{an}.......................................',str(urllib3.PoolManager().request("GET",
                                f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={self.dictarhcurs[self.ids.spinerconv2.text]}").data)))[-8:-2]
                    
                elif self.ids.spinerconv2.text == "Leu românesc" and self.ids.spinerconv1.text != "Leu românesc":
                    valoare1 = str(re.findall(f'{zi}{luna}{an}.......................................',str(urllib3.PoolManager().request("GET",
                        f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={self.dictarhcurs[self.ids.spinerconv1.text]}").data)))[-8:-2]                
                    valoare2 = "1"

                elif self.ids.spinerconv2.text == "Leu românesc" and self.ids.spinerconv1.text == "Leu românesc":
                    valoare1 = "1"
                    valoare2 = "1"
                else:
                    valoare1 = str(re.findall(f'{zi}{luna}{an}.......................................',str(urllib3.PoolManager().request("GET",
                                                                f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={self.dictarhcurs[self.ids.spinerconv1.text]}").data)))[-8:-2]
                    valoare2 = str(re.findall(f'{zi}{luna}{an}.......................................',str(urllib3.PoolManager().request("GET",
                                                                f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={self.dictarhcurs[self.ids.spinerconv2.text]}").data)))[-8:-2]

                self.listaarhcu = []
                self.listaarhcu.append(valoare1)
                self.listaarhcu.append(valoare2)
                self.ids.inputconv34.text = str(round(float(self.ids.inputconv33.text) * float(self.listaarhcu[-2])/float(self.listaarhcu[-1]),2))
            except:
                self.ids.labelarh.text = ""
                self.ids.labeleroare.text = "Conexiune internet inexistentă"
    #func to show today date on spinners      
    def cursazi(self):        
        self.ids.spinerzi.text = self.day
        self.ids.spinerluna.text = self.dictmonth[self.month]
        self.ids.spineran.text = self.year
        self.text = self.cursbnrcurs[self.ids.spinerarhiva.text]
    #func to close graph    
    def popfunc(self,*args):
        self.popup.dismiss()
        self.ids.spinergrafluna.text = "Perioadă Grafic "+f"{self.ids.spinerarhiva.text}"

    #converter func     
    def valutar(self):
        try:
            self.ids.inputconv34.text = str(round(float(self.ids.inputconv33.text) * float(self.listaarhcu[-2])/float(self.listaarhcu[-1]),2))         
        except:
            pass
    #button func to switch currency     
    def switchunit(self):
        unit1 = self.ids.spinerconv1.text
        unit2 = self.ids.spinerconv2.text
        self.ids.spinerconv1.text = unit2
        self.ids.spinerconv2.text = unit1
    #func to webscrape data and plot desired graph
    def plotgraf(self):
        self.popup.title = f'Grafic {self.ids.spinerarhiva.text}'
        
        try:
            if self.ids.spinerarhiva.text == "Bahtul thailandez":
                self.v = re.findall(r'\d+.\d+|\d\d.\D\D\D\d\d\d\d',str(urllib3.PoolManager().request("GET",
                                f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={self.dictarhcurs[self.ids.spinerarhiva.text]}").data))[8:-3035]
            elif self.ids.spinerarhiva.text in ["Kuna croată"]:
                self.v = re.findall(r'\d+.\d+|\d\d.\D\D\D\d\d\d\d',str(urllib3.PoolManager().request("GET",
                                f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={self.dictarhcurs[self.ids.spinerarhiva.text]}").data))[8:-2575]
                
            elif self.ids.spinerarhiva.text in ["Leva bulgarească"]:
                 self.v = re.findall(r'\d+.\d+|\d\d.\D\D\D\d\d\d\d',str(urllib3.PoolManager().request("GET",
                    f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={self.dictarhcurs[self.ids.spinerarhiva.text]}").data))[8:-618]
            elif self.ids.spinerarhiva.text in ["Rubla rusească"]:
                 self.v = re.findall(r'\d+.\d+|\d\d.\D\D\D\d\d\d\d',str(urllib3.PoolManager().request("GET",
                    f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={self.dictarhcurs[self.ids.spinerarhiva.text]}").data))[8:-603]
                 print(len(self.v))


                 
            elif self.ids.spinerarhiva.text in ["Randul sud-african","Realul brazilian","Renminbi-ul chinezesc",
                "Rupia indiană","Won sud-corean","Peso-ul mexican","Dolarul neo-zeelandez","Dinarul sârbesc","Hryvna ucraineană","Dirhamul Emiratelor"]:
                 self.v = re.findall(r'\d+.\d+|\d\d.\D\D\D\d\d\d\d',str(urllib3.PoolManager().request("GET",
                    f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={self.dictarhcurs[self.ids.spinerarhiva.text]}").data))[8:-931]
            else:
                
                self.v = re.findall(r'\d+.\d+|\d\d.\D\D\D\d\d\d\d',str(urllib3.PoolManager().request("GET",
                                f"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=668&column={self.dictarhcurs[self.ids.spinerarhiva.text]}").data))[8:]
            
            self.listadate = list(str(x) for i,x in enumerate(self.v) if i%2==0)
            self.listavvalori = list(float(x) for i,x in enumerate(self.v) if i%2==1)
            self.listval = self.listavvalori[::-1]
            self.listadat = self.listadate[::-1]
            self.gridpop.remove_widget(self.figura)
            self.gridpop.remove_widget(self.eticheta)
            self.gridpop.remove_widget(self.butoninchide)
            if self.ids.spinergrafluna.text == "1 luna":
                global line1
                global x100
                global y100
                x100 = self.listadat[-22:]
                y100 = self.listval[-22:]
                fig, ax = plt.subplots(sharex=True)  # Create a figure containing a single axes.
                
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval[-22:])/4)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - lei')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)              
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()

            elif self.ids.spinergrafluna.text == "3 luni":
                
                x100 = self.listadat[-63:]
                y100 = self.listval[-63:]
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval[-63:-1])/5)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - lei')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)              
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()
            elif self.ids.spinergrafluna.text == "6 luni":
                self.tc =  int(len(self.listval[-126:])/5)
                x100 = self.listadat[-126:]
                y100 = self.listval[-126:]
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval[-126:])/5)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - lei')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()
                
            elif self.ids.spinergrafluna.text == "1 an":
                x100 = self.listadat[-252:]
                y100 = self.listval[-252:]
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval[-252:])/5)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - lei')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()                
            elif self.ids.spinergrafluna.text == "5 ani":     
                x100 = self.listadat[-1260:]
                y100 = self.listval[-1260:]
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval[-1260:])/5)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - lei')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()                
            elif self.ids.spinergrafluna.text == "Total":
                x100 = self.listadat
                y100 = self.listval
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval)/5)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - lei')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()  
        except:
            popup = Popup(title='Conexiune internet inexistentă',background ="",title_color=[0,0,0,1],separator_height = 2,size_hint=(1,0.2),pos_hint={'x': 0, 'y':0.4})
            popup.open()
            
    # func to get data when you hover over graph
    def mouse_hover(self, event):
        # mouse hover event to track position of mouse on matplotlib chart 
        # and trigger show/hide popup label tasks

        xd, yd = event.xdata, event.ydata
        active, ind = line1.contains(event) # check to see if the mouse is 
        # hovering over any of the points on the line..
        if event.xdata == None:
                pass
        else:
            valoare = round(event.ydata,4)
        
        if active: # if the mouse is hovering over a point on the line 
        # then..
            pos = str([ind["ind"][0]]) # fetch the array position of the 
            # point..
            pos = pos.replace("[", "")
            pos = pos.replace("]", "")
            found_x = x100[int(pos)] # use the array position to figure out its 
            # x and y cordinates that we stored in the x and y lists above..
            found_y = y100[int(pos)]
            text = "(" + str(found_x) + ", " + str(found_y) + ")"
            self.eticheta.text = str(found_x) + " " + str(found_y)+" lei"
            #self.show_popup_label() 
        else: # if the mouse is NOT hovering over a point on the line then..
            #self.hide_popup_label()
            if event.xdata == None:
                pass
            else:
                m = int(event.xdata)
                if m in list(x for x in range(1,len(x100))):
                    found_x= x100[m]
                    found_y= y100[m]
                    self.eticheta.text =  str(found_x) + " " + str(found_y)+" lei"
                elif m >= len(x100):
                    self.eticheta.text = ""

#class for IRCC and ROBOR screen data                    
class IRCCROBOR(Screen,Monedev):
    def __init__(self, **kwargs):
        super(IRCCROBOR, self).__init__(**kwargs)
        
        self.width = Window.size[0]
        self.dictirccrobor = {"IRCC 3 LUNI": "https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=1831&column=26031",
                              "ROBOR 3 LUNI": "https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=642&column=3573",
                              "ROBOR 1 SĂPTĂMÂNĂ":"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=642&column=3571",
                              "ROBOR 1 LUNĂ": "https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=642&column=3572",
                              "ROBOR 6 LUNI":"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=642&column=3574",
                              "ROBOR 12 LUNI":"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=642&column=3576",
                              "ROBOR OVERNIGHT":"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=642&column=3569",
                              "ROBOR TOMORROW NEXT":"https://www.bnr.ro/StatisticsReportHTML.aspx?icid=800&table=642&column=3570"}
        self.listaluna =[]
        self.listaval = []
        try: 
            self.valoriircc = list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',
                                                                     str(urllib3.PoolManager().request("GET",self.dictirccrobor[self.ids.spinerircc.text]).data))) if i%2==1)
            self.listadataircc = list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',
                                                                        str(urllib3.PoolManager().request("GET",self.dictirccrobor[self.ids.spinerircc.text]).data))) if i%2==0)
            for i,x in enumerate(self.listadataircc): 
                xx= re.findall(f"\d\d.{self.dictlunaircc[self.ids.spinerlunaircc.text]}{self.ids.spineranircc.text}",x)
                if xx!= []:
                    xxx = re.sub(f".{self.dictlunaircc[self.ids.spinerlunaircc.text]}",f" {self.dictlunairccinv[self.dictlunaircc[self.ids.spinerlunaircc.text]]} ",xx[0])
                    self.listaluna.append(xxx)
                    self.listaval.append(self.valoriircc[i])
            self.ids.rvirccrobor.data = [{'text': f"[color=#000FC1]{self.listaluna[x]}[/color] [color=#DE2711]{self.listaval[x]}%[/color]"} for x in range(0,len(self.listaluna))]
        except:
            pass
        Window.bind(on_keyboard=self.Android_back_click)
        self.butoninchide = Button(text="Închide",background_normal="",background_color=[0,0,1,1],size_hint=(1, 0.1),pos_hint={'x': 0, 'y':0})
        self.figura = FigureCanvasKivyAgg(plt.gcf(),size_hint_x = 1.2)
        self.gridpop = BoxLayout(orientation = "vertical")
        self.eticheta = Button(text="",color = [0,0,0,1],background_normal="",background_color=[0,0,0,0],size_hint=(1, 0.1),pos_hint={'x': 0, 'y':0.1})
        self.popup = Popup(title=f'Grafic {self.ids.spinerircc.text}',content=self.gridpop,background ="",title_color=[0,0,0,1],separator_height = 2,size_hint=(1, 0.88),pos_hint={'x': 0, 'y':0})

    #back to main screen    
    def Android_back_click(self,window,key,*largs):
            if key == 27:
                Clock.schedule_once(self.menucurrent,0.1)
    def menucurrent(self,*args):
        mainApp.sm.current = 'menu'

    #close graph
    def popfunc(self,*args):
        self.popup.dismiss()                      
        self.ids.spinerirccluna.text = "Perioadă Grafic"

    #func to webscrape ircc or robor data and show inside a recycleview (monthly view)       
    def gotodateirccrobor(self):
        self.ids.spinerirccluna.text = "Perioadă Grafic"
        try:
            if self.ids.spinerircc.text == "IRCC ZILNIC":
                mml= re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d|\d\d[.]\d\d[.]\d\d\d\d|\d,\d\d',str(urllib3.PoolManager().request("GET","https://www.bnr.ro/Indicele-de-referin%c8%9ba-pentru-creditele-consumatorilor--19492.aspx#peloc").data))
                mm = mml[::-1]
                for x in mm[::-1]:
                    ll =  re.findall(r'\d\d[.]\d\d[.]\d\d\d\d',x)
                    if ll == [] :
                        mm.pop()
                    else:
                        mm = mm[::-1]
                        break
                self.valoriircc = list(re.sub(",",".",x) for i,x in enumerate(mm) if i%2==1)[10:] 
                self.listadataircc = list(x for i,x in enumerate(mm) if i%2==0)[10:] 
                self.listaluna = []
                self.listaval = []
                
                for i,x in enumerate(self.listadataircc): 
                    xx= re.findall(f"\d\d.{self.dictluni[self.ids.spinerlunaircc.text]}.{self.ids.spineranircc.text}",x)
                    if xx!= []:
                        xxx = re.sub(f".{self.dictluni[self.ids.spinerlunaircc.text]}.",f" {self.dictmonth[self.dictluni[self.ids.spinerlunaircc.text]]} ",xx[0])
                        self.listaluna.append(xxx)
                        self.listaval.append(self.valoriircc[i])
                self.ids.rvirccrobor.data = [{'text': f"[color=#000FC1]{self.listaluna[x]}[/color] [color=#DE2711]{self.listaval[x]}%[/color]"} for x in range(0,len(self.listaluna))]
                self.ids.labelscrir.text = ""
            elif self.ids.spinerircc.text == "IRCC 3 LUNI":
                self.valoriircc = list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',str(urllib3.PoolManager().request("GET",self.dictirccrobor[self.ids.spinerircc.text]).data))) if i%2==1)
                self.listadataircc = list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',
                                                                            str(urllib3.PoolManager().request("GET",self.dictirccrobor[self.ids.spinerircc.text]).data))) if i%2==0)

                self.ids.rvirccrobor.data = [{'text': f"[color=#000FC1]{self.listadataircc[x]}[/color] [color=#DE2711]{self.valoriircc[x]}%[/color]"} for x in range(0,len(self.listadataircc))]                
            else:
                self.valoriircc = list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',
                                                                         str(urllib3.PoolManager().request("GET",self.dictirccrobor[self.ids.spinerircc.text]).data))) if i%2==1)
                self.listadataircc = list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',
                                                                            str(urllib3.PoolManager().request("GET",self.dictirccrobor[self.ids.spinerircc.text]).data))) if i%2==0)
                self.listaluna = []
                self.listaval = []
                for i,x in enumerate(self.listadataircc): 
                    xx= re.findall(f"\d\d.{self.dictlunaircc[self.ids.spinerlunaircc.text]}{self.ids.spineranircc.text}",x)
                    if xx!= []:
                        xxx = re.sub(f".{self.dictlunaircc[self.ids.spinerlunaircc.text]}",f" {self.dictlunairccinv[self.dictlunaircc[self.ids.spinerlunaircc.text]]} ",xx[0])
                        self.listaluna.append(xxx)
                        self.listaval.append(self.valoriircc[i])
                self.ids.rvirccrobor.data = [{'text': f"[color=#000FC1]{self.listaluna[x]}[/color] [color=#DE2711]{self.listaval[x]}%[/color]"} for x in range(0,len(self.listaluna))]
                self.ids.labelscrir.text = ""
        except:
            #internet down popup
            popup = Popup(title='Conexiune internet inexistentă',background ="",title_color=[0,0,0,1],separator_height = 2,size_hint=(1,0.2),pos_hint={'x': 0, 'y':0.4})
            popup.open()
            
    #func to webscrape data and plot desired graph     
    def plotgraf(self):
        self.popup.title=f'Grafic {self.ids.spinerircc.text}'
        try: 
            self.valoriircc = list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',
                                                                     str(urllib3.PoolManager().request("GET",self.dictirccrobor[self.ids.spinerircc.text]).data))) if i%2==1)
            self.listadataircc = list(x for i,x in enumerate(re.findall(r'\d[.]\d\d|\d\d.\D\D\D\d\d\d\d|[A-Z][a-z][a-z]\d\d\d\d',
                                                                        str(urllib3.PoolManager().request("GET",self.dictirccrobor[self.ids.spinerircc.text]).data))) if i%2==0)
            for i,x in enumerate(self.listadataircc): 
                xx= re.findall(f"\d\d.{self.dictlunaircc[self.ids.spinerlunaircc.text]}{self.ids.spineranircc.text}",x)
                if xx!= []:
                    xxx = re.sub(f".{self.dictlunaircc[self.ids.spinerlunaircc.text]}",f" {self.dictlunairccinv[self.dictlunaircc[self.ids.spinerlunaircc.text]]} ",xx[0])
                    self.listaluna.append(xxx)
                    self.listaval.append(self.valoriircc[i])
            self.ids.rvirccrobor.data = [{'text': f"[color=#000FC1]{self.listaluna[x]}[/color] [color=#DE2711]{self.listaval[x]}%[/color]"} for x in range(0,len(self.listaluna))]
        except:
            pass
        try:
            self.listval = self.valoriircc[::-1]
            self.listadat = self.listadataircc[::-1]
            self.listval = list(float(x) for x in self.listval)

            self.gridpop.remove_widget(self.figura)
            self.gridpop.remove_widget(self.eticheta)
            self.gridpop.remove_widget(self.butoninchide)
            if self.ids.spinerirccluna.text == "1 luna":
                global line1
                global x100
                global y100
                x100 = self.listadat[-22:]
                y100 = self.listval[-22:]
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval[-22:])/4)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - %')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)              
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()
            elif self.ids.spinerirccluna.text == "3 luni":
                x100 = self.listadat[-63:]
                y100 = self.listval[-63:]
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval[-63:])/4)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - %')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)              
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()
            elif self.ids.spinerirccluna.text == "6 luni":
                x100 = self.listadat[-126:]
                y100 = self.listval[-126:]
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval[-126:])/4)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - %')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)              
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()
            elif self.ids.spinerirccluna.text == "1 an":
                x100 = self.listadat[-252:]
                y100 = self.listval[-252:]
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval[-252:])/4)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                
                ax.set_ylabel('Valoare - %')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)              
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()
            elif self.ids.spinerirccluna.text == "5 ani":
                x100 = self.listadat[-1260:]
                y100 = self.listval[-1260:]
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval[-1260:])/4)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - %')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)              
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()
            elif self.ids.spinerirccluna.text == "Total":
                x100 = self.listadat
                y100 = self.listval
                fig, ax = plt.subplots()  # Create a figure containing a single axes.
                line1, = ax.plot(x100,y100)  # Plot some data on the axes.
                ax.fill_between(x100,y100,min(y100)-0.001)
                self.tc =  int(len(self.listval)/4)
                ax.xaxis.set_major_locator(ticker.MultipleLocator(self.tc ))
                ax.set_ylabel('Valoare - %')
                self.figura = FigureCanvasKivyAgg(plt.gcf())
                self.gridpop.add_widget(self.figura)
                self.gridpop.add_widget(self.eticheta)
                self.gridpop.add_widget(self.butoninchide)
                self.butoninchide.bind(on_press=self.popfunc)              
                self.figura.mpl_connect("motion_notify_event", self.mouse_hover)
                self.popup.open()
        except:
            pass
        
    # func to get data when you hover over graph
    def mouse_hover(self, event):
        # mouse hover event to track position of mouse on matplotlib chart 
        # and trigger show/hide popup label tasks

        xd, yd = event.xdata, event.ydata
        active, ind = line1.contains(event) # check to see if the mouse is 
        # hovering over any of the points on the line..
        if event.xdata == None:
                pass
        else:
            valoare = round(event.ydata,4)
        
        if active: # if the mouse is hovering over a point on the line 
        # then..
            pos = str([ind["ind"][0]]) # fetch the array position of the 
            # point..
            pos = pos.replace("[", "")
            pos = pos.replace("]", "")
            found_x = x100[int(pos)] # use the array position to figure out its 
            # x and y cordinates that we stored in the x and y lists above..
            found_y = y100[int(pos)]
            text = "(" + str(found_x) + ", " + str(found_y) + ")"
            self.eticheta.text = str(found_x) + " " + str(found_y)+" %"
            #self.show_popup_label() 
        else: # if the mouse is NOT hovering over a point on the line then..
            #self.hide_popup_label()
            if event.xdata == None:
                pass
            else:
                m = int(event.xdata)
                if m in list(x for x in range(1,len(x100))):
                    found_x= x100[m]
                    found_y= y100[m]
                    self.eticheta.text =  str(found_x) + " " + str(found_y)+" %"
                elif m >= len(x100):
                    self.eticheta.text = ""


#Information screen about application            
class Info(Screen,Monedev):
    def __init__(self, **kwargs):
        super(Info, self).__init__(**kwargs)             
        Window.bind(on_keyboard=self.Android_back_click)

    #func to get to main screen on backbutton    
    def Android_back_click(self,window,key,*largs):
            if key == 27:
                Clock.schedule_once(self.menucurrent,0.1)
    def menucurrent(self,*args):
        mainApp.sm.current = 'menu'
    
        
#app class   
class mainApp(App):
    #Create the screen manager
    sm = ScreenManager(transition=WipeTransition())

    def build(self):
        #google ad banner setting
        self.ads = KivMob("ca-app-pub-5269931013353517~8160976063")
        self.ads.new_banner("ca-app-pub-5269931013353517/2637186648", top_pos=True)
        self.ads.request_banner()
        self.ads.show_banner()        
        
        #window background color
        Window.clearcolor =(0.9,0.9,0.9,1)
        #adding main screen 
        mainApp.sm.add_widget(MainMenu(name='menu'))
        mainApp.sm.current = 'menu'         
        return mainApp.sm


        
if __name__ == '__main__':   
    mainApp().run()
