
def add_evens_up_to(upper_range):
  sum_of_all_evens = 0
  for number in range(2, upper_range + 1, 2):
    sum_of_all_evens += number
  #sum_of_all_evens is a local variable.
  #So it's only avilable within the function.
  print(sum_of_all_evens)

add_evens_up_to(100)  