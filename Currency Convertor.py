import requests,json,sys
from pprint import pprint
def fun():


    head={
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
     'Accept-Encoding':'gzip, deflate, br',
     'HostType':"www.nrb.org.np",
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
}
    
    #MadeBySijan
    print("Simple Currency Convertor From SIJAN")
    print("                                                        Exchange Rate Display+Currency Converter                                       ")
    print("                                                                      ---|Api|---                              ")

    print("                                                                        BASE:EUR                                                    "  )

  
  

    api=('https://api.exchangerate.host/latest')                   #IncaseApi dead Just Change
    req=requests.get(api)

    data = req.json()
    
  
    for x in data :
         AED=data['rates'] [str('AED')]
         AFN=data['rates'] [str('AFN')]
         #print(AED)
         #print(AFN)
         NPR=data['rates'] [str('NPR')]
         #print(NPR)
         ALL=data['rates'] [str('ALL')]
         AMD=data['rates'] [str('AMD')]
         ANG=data['rates'] [str('ANG')]
         AOA=data['rates'] [str('AOA')]
         ARS=data['rates'] [str('ARS')]
         AUD=data['rates'] [str('AUD')]
         AWG=data['rates'] [str('AWG')]
         AZN=data['rates'] [str('AZN')]
         BAM=data['rates'] [str('BAM')]
         BDT=data['rates'] [str('BDT')]
         BGN=data['rates'] [str('BGN')]
         BHD=data['rates'] [str('BHD')]
         BOB=data['rates'] [str('BOB')]
         BRL=data['rates'] [str('BRL')]
         BTC=data['rates'] [str('BTC')]
         BBD=data['rates'] [str('BBD')]
         BSD=data['rates'] [str('BSD')]
         BTN=data['rates'] [str('BTN')]
         BWP=data['rates'] [str('BWP')]
         BYN=data['rates'] [str('BYN')]
         CAD=data['rates'] [str('CAD')]
         GBP=data['rates'] [str('GBP')]
         EUR=data['rates'] [str('EUR')]
         JPY=data['rates'] [str('JPY')]
         RUB=data['rates'] [str('RUB')]
         SGD=data['rates'] [str('SGD')]
         INR=data['rates'] [str('INR')]
         HRK=data['rates'] [str('HRK')]
         LRD=data['rates'] [str('LRD')]


    print("                                                                :Grabbing exchange rate:                                                              ")
    def switch(argument):
 
     switcher ={
         0:AED,
         1:AFN,
         3:NPR,
         4:ALL,
         5:AMD,
         6:ANG,
         7:AOA,
         8:ARS,
         9:AUD,
         10:AWG,
         11:AZN,
         12:BAM,
         13:BDT,
         14:BGN,
         15:BHD,
         16:BOB,
         17:BRL,
         18:BTC,
         19:BBD,
         20:BSD,
         21:BTN,
         22:BWP,
         23:BYN,
         24:CAD,
         25:GBP,
         26:EUR,
         27:JPY,
         28:RUB,
         29:SGD,
         30:INR,
         31:HRK,
         32:LRD,
                            
         
         
      }
     #print(switcher)
     return switcher.get(argument)
    print("0:AED  1:AFN  3:NPR  4:ALL  5:AMD  6:ANG  7:AOA  8:ARS  9:AUD  10:AWG  11:AZN  12:BAM  13:BDT  14:BGN  15:BHD  16:BOB  17:BRL")
    print("18:BTC  19:BBD  20:BSD  21:BTN  22:BWP  23:BYN  24:CAD  25:GBP  26:EUR  27:JPY  28:RUB  29:SGD  30:INR  31:HRK  32:LRD ")
    argument = float(input())


    
  
    #print(argument)
    print (           "                             Selected Curremcy's Rate (Unit:1) Euro Equivalent :                      " ,      switch(argument))
    switch(argument)
    value = float(input())
    convert=value*(switch(argument))
   
  
    print(convert)
    print(" To Convert 'n' number of Npr in euro:   -------    Press:y / n")
    operator = input()
    if operator == "y":
      finalValue=convert/NPR
      print(finalValue)
      #print("In NPR           :         " +finalValue)
    else:

        print("    For Another  Converting      ")


    return fun()
fun()


 # Made by SijanDC
 # return fun()




