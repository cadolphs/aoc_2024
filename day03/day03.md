# Day 03

## Part 1

Classic pattern matching. We can just use the regex module from Python. To maker sure we get the regex right, we'll write a few tests. This helps with getting the indexing into the match groups just right. For example, there are quirky differences between `findall` and `finditer`.

Once we have an iterator over all multiplication pairs, we can just use general iterator fun to multiply and sum everything.

## Part 2

Now we're adding expressions. Makes the parsing a tad trickier. Conceptually, we'll want one part that generates the stream of commands, and one part that processes them.

In Rust, we'd be using an enum type...

Let's first refactor our code from part 1 so it returns a MultExpr.

Next, learning a cool trick about using dataclasses and type aliases to simulate the enum variant behaviour of rust.

Now, for the actual computation, we don't do anything fancy just yet because we don't know if subsequent days will build on the "computer" of this day. So right now, we just have a simple loop over the expressions and don't bother making a `Computer` class.
