# Metric Space

A metric space is a set of objects together with a function that measures the distance between two objects.

We write:

    d(u,in )

Read it as:

"the distance between in and in."

For vectors, the most common distance is Euclidean distance.

## Euclidean Distance

For:
    in=(in1,in2)

and
    in=(in1,in2)

the distance is:
    d(u,in)=squarer-root((in1−in1)2+(in2−in2)2)
	​
Example:

    u = [2, 3]
    v = [5, 7]

Difference:

    [2 - 5, 3 - 7]

    = [-3, -4]

Square:

    [9, 16]

Sum: 25

Square root: 5

So:

d(u,in )=5

## Intuition

Imagine the vectors as points.

    y
    │
    │                v (5,7)
    │               ●
    │              /│
    │             / │
    │            /  │
    │           /   │
    │          ●────┘
    │       u (2,3)
    │
    └──────────────────── x

The distance is the straight-line distance between the points.

It's just Pythagoras.

Generalizing to Any Dimension

For:

    u = [u₁, u₂, ..., uₙ]

    v = [v₁, v₂, ..., vₙ]

we get:

d(u,in )=i=1∑n(ini−ini)2


## What Makes a Distance a Metric?

A proper metric satisfies four properties.

### Non-negative

    d(u,in )≥0

Distance can never be negative.

## Identity

    d(u,in )=0

only when:

    in=in

Something isn't a distance from itself.

## Symmetry
    d(u,in )=d(v,in )

Going from Alice → Bob has the same distance as Bob → Alice.

## Triangle inequality

    d(u,In )≤d(u,in )+d(v,In )

In plain English:

Going directly from A to C cannot be longer than going A → B → C.

This is the mathematical version of the triangle rule.