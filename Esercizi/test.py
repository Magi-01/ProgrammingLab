import timeit

def combinationSum(candidates, target): 
        results = []
        def rec(i, current, remaining):
          # base cases
          if remaining == 0:
              results.append(current[:])
              return
          if remaining < 0 or i == len(candidates):
              return

          # TAKE candidates[i]
          rec(i, current + [candidates[i]], remaining - candidates[i])

          # LEAVE candidates[i]
          rec(i + 1, current, remaining)

        rec(0, [], target)
        return results


nums = [3,6,7,2]
k = 7
print(combinationSum(nums, k))
print(timeit.timeit("combinationSum(nums, k)", number=10,globals=globals()))