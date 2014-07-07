'''
Created on Jul 2, 2014

@author: viejoemer

Are there other ways to insert data into a dictionary in Python?

¿Hay otras formas de insertar datos en un diccionario en Python?

Python has a __setitem__ special method to add items in a dictionary, 
and others not so commons
'''

#Definition of a dictionary
d = {'three': 3, 'two': 2, 'one': 1}
print(d)

#Using a special method __setitem__
d.__setitem__("Four", 4)
print(d)

d = {}

#Inserting/Updating value
d['a']=1  # updates if 'a' exists, else adds 'a'
print(d)

#or
d.update({'a':2})
print(d)

#or
d.update(dict(a=3))
print(d)

#or
d.update(a=4)
print(d)

#or
d.update([("a",5)])
print(d)