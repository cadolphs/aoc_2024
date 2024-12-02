# Day 02

## Part 1

This is a classic "easy" Leetcode problem: Check if a list is either only ascending or only descending. Here we throw in the extra twist of a "maximum" difference.

Some things of note:

A list that has only one element does not _violate_ anything, so it should be classified as safe.

If we're into hardcore functional programming we could probably write that with the `fold` function.

## Part 2

There's a _brute force_ solution where, for each list that was identified as unsafe, we try again with each version of the list missing one level. If there are N lists and their max length is k, this algorithm will require time O(N*k^2) because we'd have a double-loop over the list.

We should be able to improve on that complexity by being smarter about what we check. There are two variations of violation. The "directional" violation and the "magnitudinal" violation.

We also need to act differently depending on whether we're at the beginning or the middle. Instead of talking about elements, let's primarily talk about pairs.

The first pair sets the sign that the following pairs need to follow. If the second pair already violates that, we can try deleting any of the three:

4 5 4 3 2 1 -> Fix by deleting first.
4 5 4 6 7 8 -> Fix by deleting second.
4 5 3 6 7 8 -> Fix by deleting third.

Basically can I just look at a _window_ of the last _3_ items?

If a pair later than the second pair violates the sign, deleting the first item of the first pair won't help, and deleting anything else doesn't help either. But does it make sense trying to delete the 2nd instead of 3rd?

a > b < c and we're in the middle, we can try deleting either b or c:
  If we delete b, we _need_ a > c, and then we continue with [a, c, ...]
  If we delete c, we _have_ a > b so we can just continue [a, b, ...]

Next, let's check the step size. Here it's purely in the pairs and no "established" order. So, assuming a triplet
a < b < c of increasing numbers, what's going on?

If the step from b to c is too large, we can't delete b, because that makes the step even larger. So we have to delete c.
