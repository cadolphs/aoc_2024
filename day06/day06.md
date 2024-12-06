# Day 6

## Part 1

Map stuff! All about having data structures that facilitate what we're trying to do.

On a high level, the loop would look like this:

```pseudocode
WHILE inside map area
  add position to visited position set
  IF obstacle in front
    turn 90 degrees
  ELSE
    take step forward
  END IF
END WHILE
```

What's the simplest story we can write for this? Probably something like "We can read in a map and query if a given position in inside the map"

Okay, that gives us a simple data structure and class for the Map.

Next, there's the position and state of the guard. We just move our way up the functionality stack that we need: Read the guard's position and direction. Identify whether there's an obstacle _in front of_ the guard, and functions to turn right, step forward, and "execute a move".

Then we basically have all we need to write in Python what we explained above in the pseudocode.

## Part 2

Technically there could be _lots_ of positions to check for obstacles, but we only need to check those positions that were actually visited by the guard (except the starting position).

Then, we need to identify loops. We have entered a loop when the guard repeats both their position _and_ their direction, so we'll just keep track of that.

In pseudocode:

```pseudocode
FOR EACH position IN visited position set EXCEPT start position:
  create map with obstacle in position
  initialize set of visited positions and guard directions
  WHILE guard is inside area and guard position/direction not in visited set:
    add position/direction to visited set
    execute step
  END WHILE
  IF guard is inbounds
    add obstacle position to list of successful loop obstacles
  END
```

Note: This is _relatively_ slow in Python since it's just using loops; I'm also not using any smart method to compute the path faster, taking advantage of the geometry. Basically, if we scale up the map, keeping the number of obstacles the same but addings lots of empty space between them, my method will run slower because I'm visiting every position individually, whereas a better algorithm would just check, for the given position and direction, where the next hit obstacle would be. Then, we know we're in a loop if we hit the same obstacle twice. For this sort of check, we can even come up with sophisticated data structures: Based on our direction, the relevant obstacle will be in the same row or in the same column as us, and it will be the one with the next larger or next smaller coordinate in the other dimension.

But, I'm running out of time and this is good enough :p
