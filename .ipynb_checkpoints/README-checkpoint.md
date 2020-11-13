This was a pilot project I wrote as part of a longer 
term project to write a pythonic implementation of the 
Prolog unification algorithm. The idea behind unfication
is to take a list of propositions and a logical query 
and try to prove the query using the propositions.

In this version, I adopted the slightly different goal
of accepting a list of equality constraints from the
user and finding a variable assignment to make
them all true.

##### In this pilot
I was mostly playing with the API in this version. The
idea was to see how close I could get to a symbolic
interface in Python using just magic methods. I thought
it was reasonably successful, at this level of complexity,
but we'll see how well it scales to more operators.

This version of the algorithm doesn't support 
backtracking. So, higher order operators like implication
and disjunction are not supported. In fact, it really just 
does equality.

There are some demos in ```main.ipynb```.

##### Scripts
To install dependencies, run ```pip install -r 
requirements.txt``` in the root directory.

To run all tests, run ```pytest``` in the root 
directory.