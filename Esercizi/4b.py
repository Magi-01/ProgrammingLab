file_name = 'shampoo_sales.csv'

class CSVFile():
  def __init__(self,file_name):
    self.name = file_name
    
  def get_data(self):
    values = []
    name = open(self.name,'r')
    for line in name:
      elements = line.strip('\n').split(',')
      if elements[0] != 'Date':
        value = elements
        values.append(value)
    return values

get_data_set = CSVFile(file_name)
data_set = get_data_set.get_data()

for item in data_set:
  print(item)