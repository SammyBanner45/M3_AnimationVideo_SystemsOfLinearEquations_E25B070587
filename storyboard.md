# Storyboard — Understanding $Ax=b$

Target: about 4:30–5:00 at 30 FPS, 1920×1080. Each section is an independent Manim scene so it can be previewed and revised on its own. Durations are approximate; pauses are intentional teaching beats.

| Scene | Approx. | Visual and teaching beat |
|---|---:|---|
| 1. Opening and hook | 0:32 | Title and student details; introduce the two equations as clues. Test the tempting guess $(1,3)$: it satisfies the first equation but fails the second. Pose the shared-solution question. |
| 2. Matrix form | 0:45 | Transform the equations into $Ax=b$. Reveal the coefficient matrix, unknown vector, and constants separately. Track each row back to its equation and identify the role of each entry. |
| 3. Visual intuition | 0:56 | Left: plot both lines and mark their intersection $(2,1)$. Right: show $b=2a_1+a_2$ as a scaled-column sum in the output plane. |
| 4. Gaussian elimination | 1:08 | Present the augmented matrix. Show and explain all four row operations with intermediate matrices. Read off $(x,y)=(2,1)$ and substitute into both equations. |
| 5. Solution cases | 0:44 | Three small coordinate plots show intersecting, parallel, and coincident lines. Connect determinant to the unique-solution case for square systems; distinguish inconsistent from consistent singular systems. Show $\det(A)=-3$. |
| 6. Summary and credits | 0:25 | Three takeaways, student name and ID, references, AI disclosure, and the supplied music track credit. |

## Mathematical examples

- Unique: $y=5-2x$ and $y=x-1$; intersection $(2,1)$.
- No solution: $y=2x+1$ and $y=2x-2$ (parallel, distinct).
- Infinitely many: $y=2x+1$ and $2y=4x+2$ (same line).

For the original coefficient matrix, $\det(A)=2(-1)-1(1)=-3$. A nonzero determinant guarantees one solution for a square system. A zero determinant means the coefficient matrix is singular; the augmented system is either inconsistent or has infinitely many solutions.
