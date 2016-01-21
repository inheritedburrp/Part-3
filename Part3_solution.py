import random

#Method makes a random list of given size with values between(-5,5)
def makeRandomList(size):
  f = lambda x:random.randrange(-5,6)
  return [f(x) for x in range(int(size))]


#Method selects n number of elements from list and sorts them with abs
def selectAndSort(n, list_to_sort):
  list_to_sort = customer_ratings_list[:int(n)]
  list_to_sort.sort(key = abs, reverse=True)
  return list_to_sort


array_size = raw_input('How many customer ratings are there? : ')
customer_ratings_list = makeRandomList(array_size)
print "customer ratings list: ", customer_ratings_list
n = raw_input("Please enter the number of elements to pick from the total customer ratings. : ")

#To make sure that selected number to sort are less than the array size
while(n>array_size):	
  print "This Number should be less than the array size which is ", array_size
  n = raw_input("Please enter the number of elements to pick from the total customer ratings. : ")

sorted_list = selectAndSort(n, customer_ratings_list)
print 'sorted customer ratings are: ', sorted_list
