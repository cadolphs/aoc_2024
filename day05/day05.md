# Day 5

## Part 1

At first glance these types of ordering problems make me thinkg about directed acyclic graphs (DAG). BUT: There's no guarantee that the input actually describes an acyclic graph. It might be that only the _induced subgraphs_ of a given input are acyclic.

Instead, for  the first part, we can try the following: As we go through the list, create a _must not see_ set. For example, the rule 42 | 55 says that 42 needs to come before 55. When parsing an input from left to right and we come across a 55, at that point we can add 42 to the "must not see" set.

## Part 2

We don't actually have to _sort_ the update. We just have to find the _median_ (according to the special ordering rules).

A page number is the median number if there are exactly as many pages before it than after it in the right order.

Let's say I grab the _must not see_ pages for a given page and _intersect_ that with the actual pages in the update. Wouldn't the size of the remaining set tell me exactly that? Let's try. To simplify, we just assume that the rules are exactly those of odering the natural numbers. So consider the update

5,4,3,2,1. The middle page number would be 3 in the correct order 1,2,3,4,5. The must-not-see set for page 3 is {1, 2}. Intersecting that with all the pages yields {1, 2}, which is exactlt len//2. In contrast, the must-not-see-set for page 4 is 3,2,1 with size 3 and that for page 2 is just {1}.

So all we have to do is iterate over the pages and return the first page for which the intersection of those sets is the right size.

We could speed things up a bit more; in the current version we re-compute whether a set is valid for part 2, and of course we only have to do that once. There might even be an itertool that returns two lists based on a condition. I know Rust has that. This is left as an exercise for the reader. ;)
