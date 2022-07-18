#program to determine the direction of monotonic sequence numbers
def monotonic(l):
    if l == sorted(l):
       if len(set(l))==len(l):
          print('strictly increasing')
       else:
          print('increasing')
    else:
      if len(set(l))==len(l):
          print('strictly decreasing')
      else:
          print('decreasing')
l=[7,6,5,1]
monotonic(l)
