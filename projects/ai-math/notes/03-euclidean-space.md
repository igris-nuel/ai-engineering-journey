# Euclidean space / inner product space
## inner product space
Step 1 — Start from the right question

Do not start with the definition. Start with the problem the definition is solving.

You have a vector space. You can add vectors and scale them. You proved that polynomials, functions, and matrices all live in vector spaces. Good. But now ask yourself a very concrete question:

Given two vectors, how do you measure the angle between them?

For arrows in 2D, you have a geometric picture. You can draw the two arrows, use a protractor, and read off the angle. But what does it even mean to ask: "what is the angle between the polynomial 3 + 2x − x² and the polynomial 1 + 5x²?" Or: "what is the angle between the function sin(x) and the function x²?"

Those questions sound absurd at first. Polynomials and functions don't look like arrows. They don't live in physical space where you can draw them and measure with a protractor.

And yet — these questions have precise, computable answers. The machinery that makes them answerable is the inner product.

So the inner product is not just a generalisation of the dot product. It is the answer to the question: how do you build a complete geometry — lengths, distances, and angles — on any vector space at all, including abstract ones like function spaces?


## Step 2 — What geometry actually needs

Let's be precise about what "geometry" requires. Classical Euclidean geometry rests on three primitive measurements:

    Length — how long is this object?
    Distance — how far apart are these two objects?
    Angle — how much do these two directions diverge?

In the previous parts you saw that a metric gives you distance. But a metric — even a good one — does not automatically give you lengths of individual vectors or angles between vectors. It only gives pairwise distances between points.

What you want is a single operation that:

    Takes two vectors as inputs
    Returns a single real number
    From which you can extract length (apply it to a vector with itself)
    From which you can extract angle (divide by the product of lengths)
    And which is tightly coupled to the linear structure (so you can compute it by breaking vectors into components)

The inner product is precisely and exactly that operation. It is the minimal structure you need to add to a vector space in order to have complete Euclidean-style geometry.

## Step 3 — The definition, written out fully

An inner product on a real vector space V is a function:

⟨ · , · ⟩ : V × V → ℝ

The notation V × V means the inputs are ordered pairs (u, v) of vectors from V. The output is always a real number. You feed in two vectors, you get out one number.

⟨u, v⟩ = ‖u‖·‖v‖·cos θ

Now read this formula carefully from right to left. ‖u‖ is the length of u. ‖v‖ is the length of v. cos θ captures the angular relationship — how much their directions overlap. The inner product ⟨u, v⟩ is the product of both lengths times the cosine of the angle between them. It is a single number that encodes the combined effect of the magnitudes of both vectors and the alignment of their directions.

This is the geometric soul of the inner product.


## Step 4 — The four cases of the angle, fully understood

Case 1: 
    θ = 0° (u and v point in the same direction)
    cos 0° = 1, so ⟨u, v⟩ = ‖u‖·‖v‖. 

This is the maximum possible value of the inner product (by Cauchy-Schwarz). The vectors are perfectly aligned — every bit of u's length contributes fully to the overlap with v.

Case 2: 
    θ = 180° (u and v point in opposite directions)
    cos 180° = −1, so ⟨u, v⟩ = −‖u‖·‖v‖. 

This is the minimum (most negative) value. The vectors are perfectly anti-aligned.

Case 3: 
    θ = 90° (u and v are perpendicular)
    cos 90° = 0, so ⟨u, v⟩ = 0. 

The inner product vanishes. Perpendicular vectors have zero inner product. This is the definition of orthogonality: u and v are orthogonal when ⟨u, v⟩ = 0.

Case 4: 
    0° < θ < 90°
    cos θ > 0, so ⟨u, v⟩ > 0. 

The vectors have a component pointing in the same general direction. The inner product is positive.

Case 5: 

    90° < θ < 180°
    cos θ < 0, so ⟨u, v⟩ < 0. 

The vectors have a component pointing in opposite general directions. The inner product is negative.

The sign of the inner product tells you whether two vectors are "on the same side" (positive), "perpendicular" (zero), or "on opposite sides" (negative).

## Step 5 Orthogonality: 

Two vectors u and v are orthogonal if ⟨u, v⟩ = 0.

Why orthogonality is the central concept

Orthogonality is the generalisation of "perpendicular" to any inner product space — including function spaces, polynomial spaces, and everything else. Once you have an inner product, you can ask about orthogonality in any vector space.

## Step 12 — Projection: what the inner product is really computing

This is the geometric heart of the whole theory.

Given vectors u and v, the projection of u onto v is the vector in the direction of v that is "as close as possible" to u. It is the "shadow" that u casts onto the line containing v when light falls perpendicularly.

The formula is:

proj_v(u) = (⟨u, v⟩ / ‖v‖²) · v = (⟨u, v⟩ / ⟨v, v⟩) · v

Derivation: We want to find a scalar t such that tv (a vector along v) is as close as possible to u. "As close as possible" means minimising ‖u − tv‖². Expand:

‖u − tv‖² = ⟨u − tv, u − tv⟩ = ‖u‖² − 2t⟨u,v⟩ + t²‖v‖²

This is a quadratic in t (the same one from the Cauchy-Schwarz proof). Minimise by taking the derivative with respect to t and setting it to zero:

d/dt [‖u‖² − 2t⟨u,v⟩ + t²‖v‖²] = −2⟨u,v⟩ + 2t‖v‖² = 0
t = ⟨u,v⟩ / ‖v‖²

So the projection is t·v = (⟨u,v⟩/‖v‖²)·v.

What this means for the inner product: The scalar t = ⟨u,v⟩/‖v‖² measures "how much of u lies in the direction of v." It is the signed length of u's shadow on v, divided by the length of v. Rearranging: ⟨u,v⟩ = t·‖v‖² = (signed shadow length of u on v) · ‖v‖.

Or equivalently: ⟨u,v⟩ = (signed shadow length of u on v) · ‖v‖ = ‖u‖cos θ · ‖v‖.

The inner product is: (signed length of u's projection onto v) times (length of v). That is the complete geometric meaning. It measures how much of u's length goes in the direction of v, scaled by v's length.

This projection picture is the reason the inner product appears everywhere: in physics (work = force · displacement = F · d = ‖F‖‖d‖cos θ, where cos θ captures how much force is in the direction of motion), in signal processing (how much of signal u is in the "direction" of frequency component v), in machine learning (how similar two data vectors are).


## Euclidean space