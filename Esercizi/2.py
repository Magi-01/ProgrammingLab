my_list = []

def sum_list(my_list):
  for i in range(len(my_list)):
    risultato = sum(my_list)
    return risultato

risultato = sum_list(my_list)
if risultato == None:
  print ("You sum is None")
if risultato != None:
  print ("You sum is %d" %risultato)