values = []

file_name = open('C:/Users/mutua/Documents/Python_CVS_TXT/shampoo_sales.csv')

def sum_cvs(file_name):
    for line in file_name:
        elements = line.split(',')
      
        if line != 'Date' and 'Sales':
            value = elements[1]
            print (value)
          
            if value != 'Sales\n':
                values.append(float(value))


    print (values)
    values_digit = values
    risultato = sum(values_digit)

    print (risultato)
     
    return risultato



risultato = sum_cvs(file_name)
if risultato == None:
  print ("You sum is None")
if risultato != None:
  print ("You sum is %f" %risultato)
