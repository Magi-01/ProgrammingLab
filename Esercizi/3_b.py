values = []

file_name = open('shampoo_sales.csv','r')

def sum_cvs(file_name):
    for line in file_name:
      elements = line.split(',')
      
      if elements[0] != 'Date':
        value = elements[1]
          
        values.append(value)

    risultato = 0.0

    for item in values:
      risultato += float(item)
     
    return risultato



risultato = sum_cvs(file_name)
if risultato == None:
  print ("You sum is None")
if risultato != None:
  print ("You sum is %f" %risultato)
