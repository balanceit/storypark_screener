# Storypark screener

## Question 1
### What’s your proudest achievement?

During my time with Loyalty NZ we ran into a problem when handling backdated transactions (someone buying something, not the db kind).  The problem was how to correctly calculate the amount of loyalty points (AirNZ dollars, New world dollars, FlyBy points, etc.) when the current point to dollar exchange rate may have changed since the point of time of these backdated transactions. At times the calculations were run weeks after the actual transaction had taken place.

In order to overcome this problem I introduced the concept of 'Effective dating' resources in our API. By using a combination of database (PostgreSQL) triggers and ActiveRecord mixins this issue was solved with minimal rewrite to the existing API implementation.

I wrote database migration generators to create the triggers and additional tables and assisted in the design and review of the ActiveRecord mixins.

I am quite proud of this work because I was able to implement a solution which could be generically applied, prevented the necessity for a rewrite of a substantial portion of the points calculation and transaction code base and was done in a way which resulted in minimal computational overhead.

* rest API framework GEM: https://loyaltynz.github.io/hoodoo/
* documentation of how used: https://github.com/LoyaltyNZ/hoodoo/tree/master/docs/api_specification#http_x_dated_at
* the generators: https://github.com/LoyaltyNZ/service_shell/blob/master/bin/generators/classes/effective_date_class.rb
* the ActiveRecord mixin: https://github.com/LoyaltyNZ/hoodoo/blob/master/lib/hoodoo/active/active_record/dated.rb


## Question 2
### What's the most interesting technical article you've read recently? What did you like about it and why should we take a look at it?

While working on implementing a content based recommendation system for MBIE recently I came across an article (see below) written by Alyona Medelyan, a graduate of the University of Waikato, about automatic keyword extraction.  I liked this article because it was written in a clear and approachable way, it contains all the source code, and helped me better understand the problem with which I was tackling.  In the end I didn't end up implementing the RAKE algorithm to assist in the recommendation system but it was helpful and interesting nonetheless.

After watching the demo video of the Storypark application I noticed how each story can be associated with one or more "Learning Tags". This made me think of a way in which as a story is being written suggestions can be made about which Learning Tags to apply to this story.  A text's keywords can be part of the input to a recommendation system.  The RAKE algorithm is a straightforward way to get these keywords.

https://www.airpair.com/nlp/keyword-extraction-tutorial


## Question 3
### Write some code, that will flatten an array of arbitrarily nested arrays of integers into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].

I liked this one, thought about doing just something simple by calling ruby's `[].flatten` method but thought that would be a bit cheeky.  So keeping with python (2.7.11) (I actually started working on Q4 first) I solved this with a recursive function `flatten`.

To run the tests

`python ./Question3/flatten_test.py`

To show the method flattening a couple of nested arrays run:

`python ./Question3/main.py`

## Question 4
### Display all staff, ordered by name, who live within 2km of our office.

I really liked this one, was fun to work through and reverse engineer the equation. Bringing back all my trigonometry maths from school.  Was a little amazed that it was still in there somewhere (kind of ;]).

I decided to do this in python (2.7.11) because I had never done any unit testing in python and took this as an opportunity to learn a bit of something.

To run the tests

`python ./Question4/greatcircle_test.py`

To show the staff members who are within 2 km of the office

`python ./Question4/main.py`
