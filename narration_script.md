# Narration Script

Approximate runtime: about five minutes at a calm pace, including pauses. The spoken text is about 580 words. Bracketed cues are not spoken.

## Scene 1 — Opening and hook

Together, these two equations ask for one pair of numbers that makes both statements true.

Here are our clues: two x plus y equals five, and x minus y equals one. Before we solve them, consider the guess x equals one, y equals three. In the first equation, two times one plus three is five. That clue checks out. [Pause.] But in the second equation, one minus three is negative two, not one. The guess fails.

We need one pair that satisfies both. We will explore the system with matrices, pictures, and row operations.

## Scene 2 — Understanding Ax equals b

Collect the coefficients into matrix A: two and one from the first equation, one and negative one from the second.

Put the unknowns in vector x and the constants in vector b. Each row of A forms a dot product with x: the first gives two x plus y, and the second gives x minus y. Together, this is A x equals b.

Each entry tells how an unknown contributes to an equation; b gives the target values. This notation also scales to larger systems: a row for every equation, and a column for each unknown.

## Scene 3 — Visual intuition

Picture each equation as a line. The first slopes downward, while the second slopes upward. A solution must lie on both. Their crossing point is two, one. [Pause.] Both equations are true there. The graph makes the shared-solution idea visible at a glance.

The columns of A are vectors: a one is two, one; a two is one, negative one. The solution weights them: twice a one plus a two gives five, one, which is b. The animation first doubles the first vector, then adds the second head-to-tail. Solving means building b from A's columns, with x and y as the weights.

## Scene 4 — Gaussian elimination

Now solve systematically. The augmented matrix collects coefficients and constants. Row operations preserve the solution.

Swap rows to put a one in the first pivot position. Replace row two by itself minus twice row one. The second row becomes zero, three, three. [Pause.] Divide it by three to get zero, one, one. Finally, add row two to row one. This removes the remaining negative one above the pivot. The identity matrix remains on the left, with answers two and one on the right.

Thus x is two and y is one. Check: four plus one is five, and two minus one is one. Both equations hold.

## Scene 5 — Three solution cases

Two lines can meet once, never meet, or coincide: one solution, none, or infinitely many.

For a square system, a nonzero determinant means exactly one solution. Here it is two times negative one, minus one: negative three. So our system has a unique solution.

When it is zero, the constants decide: parallel distinct lines are inconsistent; coincident lines have infinitely many solutions. This determinant shortcut applies to square coefficient matrices; consistency is still the key question in the singular cases.

## Scene 6 — Summary and credits

Remember: write a system as A x equals b; interpret its solution as a line intersection and a column combination; use Gaussian elimination to solve it systematically.

Prepared by Sambuddha Banerjee, E25B070587. References: Gilbert Strang, *Introduction to Linear Algebra*, and Manim Community documentation. AI helped draft the code and narration; calculations were checked during authoring. The background track is “Snowfall” by Asher Fulero from the YouTube Audio Library; the supplied license says attribution is not required.
