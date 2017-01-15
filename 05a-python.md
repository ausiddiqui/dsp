# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and Tuples in Python are both data structures that can store a list of values. They both use indexing in the same way, i.e. starting from zero, they both can be named and initiated with a comma separated list of values and can contain a mixture of different data types. The main difference though is that tuples are immutable, i.e. once a tuple is declared its contents cannot be modified. Tuples would work as keys in dictionaries as the key needs to be a value that does not change in a dictionary, the immutable nature of tuples make them relevant to use as keys.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets can contain a collection of objects like lists and supports some of the functions of lists like iterating and checking length. Sets can be both mutable and immutable (frozenset). Unlike lists, sets cannot be indexed as the collection in unordered. Additionally, Python sets are like sets from set theory in mathematics, as a result they cannot contain duplicates.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> 'Lambda' functions are a simplified syntax functions that are not reused as they cannot be referenced by a name and reused again. The notation is similar to that of functional program, and it is possible to use a 'lambda' function without assigning it to a variable. They are used in cases where an inline function is a better option than writing a full function as the syntax is compact and the function won't be reused for any purpose again. When used with the 'sorted' function, they can be used to define a custom function that is used to sort the values of an iterable object. For example:

```
sorted([4, 5, -3, 6, 1, 8, -2], key=lambda x: x**2 - 10*x + 3)
# output: [5, 4, 6, 8, 1, -2, -3]
# In this example each element of the input list goes through the quadratic function and its evaluation is the basis for sorting the input list values.
```

```
sorted([('tom', 'A', 9.0), ('jane', 'A+', 9.5), ('brent', 'C', 5.5)], key=lambda student_grades: student_grades[2])
# output: [('brent', 'C', 5.5), ('tom', 'A', 9.0), ('jane', 'A+', 9.5)]
# In this example a list of tuples is passed in, and then sorted on the third tuple variable.
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are another functional programming concept that allow certain types of for loops to be simplified and written in a more functional and compact way. One of the design patterns that are relevant for using list comprehensions is a for loop that reads through an existing list to check for a condition and if the condition holds appends values to a result list after manipulating the value from the existing list for which the condition holds. But the simpler unconditional loops can also be handled by list comprehensions. For example:
```
# For loop through a list that will look for even numbers then output them as squared numbers in a new list.

old_list = [1, 2, 3, 4, 5]
new_list = []

for v in old_list:
    if v % 2 == 0:
        new_list.append(v**2)
print new_list

# [4, 16]

# Same results using a list comprehension.
old_list = [1, 2, 3, 4, 5]
new_list = [v**2 for v in old_list if v % 2 == 0]
print new_list
# [4, 16]
```

The 'map' function is capable of doing the same in terms of converting a for loop that carries out a particular transformation on the values into a more compact syntax. The transformation fucntion can be applied using a named / defined function or by using a lambda function inline. For example, we can convert the unconditional version (i.e. square all values, not just even numbers) of function above into a map function syntax:

```
old_list = [1, 2, 3, 4, 5]
new_list = map(lambda v: v**2, old_list)
print new_list
# [1, 4, 9, 16, 25]
```

Using the 'filter' function takes a sequence and applies a condition on it to return true for those items for which the condition holds true.

```
old_list = [1, 2, 3, 4, 5]
new_list = filter(lambda v: v % 2 == 0, old_list)
print new_list
# [2, 4]
```
These two functions can be combined to carry out the same type of task as a list comprehension with a condition. The data from the original list is passed through the filter (i.e. the condition), then the results of that conditional list is passed to the map function which carries out the transformation of the filtered values. For example:

```
old_list = [1, 2, 3, 4, 5]
new_list = map(lambda v: v**2, filter(lambda v: v % 2 == 0, old_list))
print new_list
# [4, 16]
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
