# Narration Script with Video Cues

Target pace: calm and conversational, roughly 135–145 words per minute. Read the spoken lines in the matching section; bracketed cues are visual timing guides and are not spoken. Timestamps are approximate for the current 4:45 video and may shift slightly during transitions. Leave the marked pauses; do not rush to fill silence.

## Scene 1 — Opening and hook | 0:00–0:17

**0:00–0:03 — Title**  
“In this video, we’ll understand systems of linear equations through matrices, graphs, and vectors.”

**0:03–0:07 — Equations appear**  
“Here are our two equations: two x plus y equals five, and x minus y equals one.”

**0:07–0:13 — Test the guess**  
“Try x equals one and y equals three. The first equation works: two times one plus three is five. But in the second, one minus three is negative two, not one. So this guess fails.”

**0:13–0:17 — Closing question**  
“How do we find a pair that satisfies both?”

## Scene 2 — From equations to matrix form | 0:17–1:06

**0:17–0:28 — Equation and matrix headings**  
“Collect the coefficients into matrix A: two and one in the first row, one and negative one in the second. The unknown vector, x, contains x and y. Vector b contains the right-hand sides, five and one.”

**0:28–0:43 — Match rows to equations**  
“Multiply each row of A by the unknown vector. The first row gives 2x+y. The second gives x - y. Those results match the entries of b, so the system is A x equals b.”

**0:43–1:06 — Expanded product and explanation**  
“Each row encodes one equation, and each column records the coefficients of one unknown. This same structure works for larger systems: one row for each equation and one column for each unknown.”

## Scene 3 — Row and column pictures | 1:06–1:53

**1:06–1:16 — Row picture, algebra**  
“A solution must make both equations true at once.”

**1:16–1:29 — Row picture, graph**  
“Each equation becomes a line. Both axes use the same unit scale, so the slopes are shown faithfully. The lines cross at (2,1). That shared point satisfies both equations.”

**1:29–1:39 — Column picture, algebra**  
“The columns of A are a1, which is two, one, and a1, which is one, negative one.”

**1:39–1:53 — Vector sum**  
“In A  x, x and y are weights on those columns. Here the weights are two and one. Double a1, then add a2 head-to-tail. The result is b, five, one.”

## Scene 4 — Gauss–Jordan elimination | 1:53–3:11

**1:53–2:02 — Starting augmented matrix**  
“The augmented matrix records the coefficients and constants together. Elementary row operations keep the solution set unchanged.”

**2:02–2:12 — Swap rows**  
“Swap the rows to put a1 in the first pivot position. Swapping equations does not change which values satisfy both.”

**2:12–2:30 — Eliminate x**  
“Replace row 2 by row 2 - twice row 1. The new second row is zero, three, three.”

**2:30–2:48 — Scale the pivot row**  
“Divide the second row by three to make its pivot one.”

**2:48–3:06 — Clear above the pivot and read the answer**  
“Add row two to row one to clear the entry above that pivot. Because we clear above as well as below, this is Gauss–Jordan elimination. The identity matrix is on the left, and the solution is x equals two, y equals one.”

**3:06–3:11 — Check**  
“Check: four plus one is five, and two minus one is one.”

## Scene 5 — Three solution outcomes | 3:11–4:21

**3:11–3:29 — Unique solution**  
“In our first system, the lines meet once, at (2,1). The determinant is -3, so this square system has one solution. Both ranks are two, the number of unknowns.”

**3:29–3:48 — Infinitely many solutions**  
“Now make the second equation twice the first. Subtract twice row one from row two, and the new row is all zeros. The equations are the same line, so there are infinitely many solutions. Both ranks are one.”

**3:48–4:07 — No solution**  
“Change the second right-hand side to seven. The row operation gives zero, zero, negative three: the contradiction zero equals negative three. There is no solution. The coefficient rank is one, while the augmented rank is two.”

**4:07–4:21 — Determinant comparison**  
“Both singular examples have determinant zero. The determinant alone cannot distinguish infinitely many solutions from no solution. The row result or rank comparison does.”

## Scene 6 — Summary and credits | 4:21–4:45

**4:21–4:27 — Three takeaways**  
“Remember: a system can be written as A bold x equals b; solutions are line intersections and column combinations; and Gauss–Jordan elimination solves the system systematically.”

**4:27–4:45 — Credits**  
“Prepared by Sambuddha Banerjee. References include Gilbert Strang’s *Introduction to Linear Algebra* and Manim Community documentation. The music is ‘Snowfall’ by Asher Fulero from the YouTube Audio Library.”

