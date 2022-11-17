def sum_csv(file_name):
  values = []
  my_file = open(file_name,'r')
  for line in my_file:
    elements = line.split(',')
      
    if elements[0] != 'Date':
        value = elements[1]
          
        values.append(value)
      
  risultato = 0
  #print (values)
  for item in values:
      risultato += float(item)
  if risultato == 0:
    return None
  return risultato