# Storyboard — Understanding $Ax=b$

Target: about 4:30–5:00 at 30 FPS, 1920×1080. Each section is an independent Manim scene so it can be previewed and revised on its own. Durations are approximate; pauses are intentional teaching beats.

| Scene | Approx. | Visual and teaching beat |
|---|---:|---|
| 1. Opening and hook | 0:32 | Title and student details; introduce the two equations as clues. Test the tempting guess $(1,3)$: it satisfies the first equation but fails the second. Pose the shared-solution question. |
| 2. Matrix form | 0:45 | Headings distinguish equation form and matrix form. Use bold $\mathbf{x}$ for the unknown vector. Match each row of $A$ to its equation, then expand the product to show how the rows produce the left-hand sides. |
| 3. Row and column pictures | 1:10 | Present row algebra, then a full-screen row graph with equal unit scales and the intersection $(2,1)$. Present $A\mathbf{x}=x a_1+y a_2=b$ algebraically, identify the columns and scalar weights, then animate the full-screen head-to-tail vector sum. |
| 4. Gauss–Jordan elimination | 1:08 | Present the augmented matrix. Explain why swapping rows puts a one in the first pivot position; show all four operations. Name the method Gauss–Jordan because entries above and below pivots are cleared. Verify the answer in both equations. |
| 5. Solution structure | 1:15 | Use one coefficient matrix to show unique, infinite, and no-solution cases. Pair each example with a graph, row reduction, determinant, and rank comparison. Explain why determinant zero cannot distinguish the two singular outcomes. |
| 6. Summary and credits | 0:25 | Three takeaways, student name and ID, references, AI disclosure, and the supplied music track credit. |

## Mathematical examples

- Unique: $2x+y=5$ and $x-y=1$; intersection $(2,1)$; $\det(A)=-3$; both ranks are $2=n$.
- Infinitely many: $2x+y=5$ and $4x+2y=10$; $R_2-2R_1$ gives $[0\ 0\mid0]$; both ranks are one.
- No solution: $2x+y=5$ and $4x+2y=7$; $R_2-2R_1$ gives $[0\ 0\mid-3]$; coefficient rank one, augmented rank two.

For the original coefficient matrix, $\det(A)=2(-1)-1(1)=-3$. A nonzero determinant guarantees one solution for a square system. A zero determinant means the coefficient matrix is singular; the augmented system is either inconsistent or has infinitely many solutions.
