values = []

file_name_open = open('C:/Users/User_name/Documents/Python_CVS_TXT/shampoo_sales.txt','rw')

file_name = file_name_open.open()
#file_name = ("file_name and location", "type of operation ('r'=read,'w'=write,'rw'=read and write)")

#print(file_name.readline()) prints one line one after the other and if there is no other line prints NONE vantaggio e se hai 12GB di file, opera su un pezzo alla volta invece di caricare tutta la ram

#.split() non toglie i spazi, lo dovete fare manualmente

#float() and int() are functions that convert string into float or integer repectevely. unlike c/c++ it does not convert char caracters into ascii

#.append() appends the value to the array



def sum_cvs(file_name):
  #row_x = sum(1 for line in file_name)
  #from itertools import islice
  for line in file_name:
      elements = line.split(',')

      if elements[0] != 'Date':
        value = elements[1]
        values.append(value)

  values_Space = values.strip('\n')
  risultato = sum(float(values_Space))
     
  return risultato



risultato = sum_cvs(file_name)
if risultato == None:
  print ("You sum is None")
if risultato != None:
  print ("You sum is %d" %risultato)

file_name_open.close()