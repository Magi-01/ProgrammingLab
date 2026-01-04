def maxArea(height) -> list:
  n = len(height)

  if n <= 2:
    return []

  arr = []

  for i in range(n):
    for j in range(i+1, n):
      for k in range(j+1, n):
        if height[i] + height[j] + height[k] == 0:
          arr.append([height[i], height[j], height[k]])
  
  return arr

height = [-1,0,1,2,-1,-4]
print(maxArea(height))