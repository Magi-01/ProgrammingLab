file_name = 'shampoo_sales.csv'

def sum_csv(file_name):  
  my_file_sum = pars_file(file_name)
  risultato = 0
  for item in my_file_sum:
    try:
      risultato += float(item)
    except ValueError:
      risultato = risultato
  if risultato == 0:
    return None
  return risultato


def pars_file(file_name):
  values = []
  my_file_parse = opn_file(file_name)
  for line in my_file_parse:
    elements = line.split(',')
    if elements[0] != 'Date':
        value = elements[1] 
        values.append(value)
  return values

  
def opn_file(file_name):
  my_file = open(file_name,'r')
  return my_file

print(sum_csv(file_name))