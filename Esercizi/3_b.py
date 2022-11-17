def sum_cvs(file_name):
  values = []
  my_file = open(file_name,'r')
    for line in my_file:
      elements = line.split(',')
      
      if elements[0] != 'Date':
        value = elements[1]
          
        values.append(value)

    risultato = 0.0

    for item in values:
      risultato += float(item)
     
    return risultato
