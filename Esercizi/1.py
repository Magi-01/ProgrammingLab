def sum(n):
  if (n==1):
    return 1
  return n + sum(n-1)

def main():
  n = int(input("Insert the maximum: "))
  m = sum(n)
  print("Your sum is %d" %m)
  #ladiladila

main()