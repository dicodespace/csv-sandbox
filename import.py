import csv
with open('C:/Users/lenovo/Desktop/vs code/demo.csv','r') as file:
    csv_reader=csv.reader(file)
    for row in csv_reader:
        print(row)
    
