import os
import csv 

bank_path = os.path.join("Resources","pybank.csv") 



with open(bank_path) as bankcsv: 
 csvreader= csv.reader(bankcsv, delimiter=',')
 next(csvreader, None) 
 netprofit=0
 dates = 0
 change = 0
 greatestincrease = []
 greatestdecrease = []
 
 for x in csvreader:
     dates=dates+(len(list(csvreader)))
     for i in x: 
         netprofit += int(i[1])
         change -=int(i[1])
         avg_change=int(change/dates)
         greatestincrease.append(i[1])
         greatestdecrease.append(i[1])
     

     print(min(greatestdecrease))
     print(max(greatestincrease)) 
     print(avg_change) 
     print(netprofit)
     print(dates)
     
   # for z in csvreader: 
    #    change -=int(x[1])
     #   avg_change=int(change/int(len(list(csvreader)))
      #      print(avg_change) 




