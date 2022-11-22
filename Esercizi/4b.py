class CSVFile():
  def __iter__(self):
    return iter(self.pars_file())
  
  def get_data(self):
    values = []
    for line in self.f:
      elements = line.split(',')
      if elements[0] != 'Date':
        value = elements
        values.append(value)
    return values
  
  def __init__(self,name):
    file = open(name,'r')
    self.f = file