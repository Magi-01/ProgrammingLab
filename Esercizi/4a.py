file_name = 'shampoo_sales.csv'

class file_name_op():
  def pars_file(self):
    values = []
    for line in self.f:
      elements = line.split(',')
      if elements[0] != 'Date':
        value = elements[1] 
        values.append(value)
    return values
  
  def __init__(self,file_name):
    file = open(file_name,'r')
    self.f = file

def sum_csv(file_name):
  my_file_sum = file_name_op(file_name)
  risultato = 0
  for item in my_file_sum.pars_file():
    try:
      risultato += float(item)
    except ValueError:
      risultato = risultato
  if risultato == 0:
    return None
  return risultato

get_sum = sum_csv(file_name)
print(get_sum)