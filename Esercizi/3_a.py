values = []

file_name = open('C:/Users/User_name/Documents/Python_CVS_TXT/shampoo_sales.txt')



def sum_cvs(file_name):
    from itertools import islice
    for line in islice(file_name,1,39):
        elements = line.split(',')

        value = float(elements[1])

        values.append(value)


    risultato = sum(values)
     
    return risultato



risultato = sum_cvs(file_name)
if risultato == None:
  print ("You sum is None")
if risultato != None:
  print ("You sum is %d" %risultato)