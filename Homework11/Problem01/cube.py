"""
This program will print out the cube result given by a function
if the value is not even. Otherwise it will just print the value itself.
Example Innvocation: python3 ./cube.py
"""

def cb(x):
  print(x*x*x)


for x in range(20):
  if(x%2 == 0):
    print(x)
  else:
    cb(x)
