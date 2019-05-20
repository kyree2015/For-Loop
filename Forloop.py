def basic():
    for x in range(0,151,1):
        print(x)

def multiples_of_five():
    for x in range(5,1001,5):
        print(x)

def the_dojo_way():
    for i in range(0,101):
      if i % 10 == 0:
        print("Coding Dojo")
      elif i % 5 == 0: 
        print("Coding")
    else:
        print(i)
the_dojo_way()

def that_suckers_huge():
    final_sum = 0
    for i in range(0,500000,2):
        final_sum += i
    print(final_sum)
that_suckers_huge()

def countdown_by_fours():
    for i in range(2018,0,-4):
        print(i)
countdown_by_fours()        
