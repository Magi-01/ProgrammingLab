k = int(input("how many numbers do you want to insert: "))
my_list = []


for i in range (0,k):
  my = int(input("Insert your numbers: "))
  my_list.append(my)



m = 0

for i in range(len(my_list)):
  m = my_list[i] + m
print ("Your sum is %d" %m)