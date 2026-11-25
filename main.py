"""Six-scene explainer: Systems of Linear Equations — Understanding Ax=b.

Render an individual scene with `manim -ql main.py OpeningHook`. Shared helpers
keep the palette, matrix typography, and labels consistent across the video.
"""

from manim import *


# Keep the 16:9 frame while allowing `-ql` previews to use Manim's smaller size.
# Use `-qh` for the 1920×1080 master; frame rate remains fixed at 30 FPS.
config.frame_rate = 30
config.background_color = "#03021c"

NAVY = "#03021c"
WHITE = "#F5F7FF"
BLUE = "#66A8FF"       # coefficient matrix A
GOLD = "#FFD166"       # unknown vector x
GREEN = "#53D6A0"      # constant vector b
CYAN = "#62E8F2"       # solution and pivots
MUTED = "#A9B5D0"
RED = "#FF7885"
FONT = "Avenir Next"


def heading(text, size=40, color=WHITE):
    """A consistent top-aligned scene heading."""
    return Text(text, font=FONT, font_size=size, color=color, weight=MEDIUM)


def math_label(tex, size=42, color=WHITE):
    return MathTex(tex, font_size=size, color=color)


def equation_pair(scale=1.0):
    return VGroup(
        MathTex(r"2x+y=5", font_size=48, color=WHITE),
        MathTex(r"x-y=1", font_size=48, color=WHITE),
    ).arrange(DOWN, buff=0.42).scale(scale)


def aug_matrix(rows, font_size=46, color=WHITE):
    """Build an augmented matrix with a clear visual separator."""
    return MathTex(
        r"\left[\begin{array}{cc|c}"
        + rows
        + r"\end{array}\right]",
        font_size=font_size,
        color=color,
    )


def system_axes(x_range=(-0.6, 4.4, 1), y_range=(-1.5, 6.5, 1), width=5.6, height=4.4):
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=width,
        y_length=height,
        axis_config={"color": MUTED, "stroke_width": 2, "include_numbers": True,
                     "font_size": 22, "include_tip": True},
        tips=True,
    )
    return axes


class OpeningHook(Scene):
    """Set the problem and show why one equation is not enough."""

    def construct(self):
        title = Text("Systems of Linear Equations", font=FONT, font_size=50,
                     color=WHITE, weight=BOLD).to_edge(UP, buff=0.48)
        subtitle = MathTex(r"\text{Understanding } Ax=b", font_size=38,
                          color=CYAN).next_to(title, DOWN, buff=0.15)
        student = Text("Sambuddha Banerjee  •  E25B070587", font=FONT,
                       font_size=23, color=MUTED).to_edge(DOWN, buff=0.32)
        self.play(FadeIn(title, shift=0.2 * UP), Write(subtitle), FadeIn(student))
        self.wait(2)

        clues_title = Text("Two clues. One pair must satisfy both.", font=FONT,
                           font_size=30, color=WHITE).move_to(UP * 1.55)
        clues = equation_pair().move_to(LEFT * 3.55 + DOWN * 0.25)
        self.play(Write(clues_title), Write(clues))
        self.wait(1.0)  # Place the row-to-row matching animation at 0:23 overall.

        guess_label = Text("Try a guess", font=FONT, font_size=25, color=MUTED)
        guess = MathTex(r"(x,y)=(1,3)", font_size=38, color=GOLD)
        guess_group = VGroup(guess_label, guess).arrange(DOWN, buff=0.22)
        guess_group.move_to(RIGHT * 3.4 + UP * 0.55)
        check1 = MathTex(r"2(1)+3=5", font_size=35, color=GREEN)
        check2 = MathTex(r"1-3=-2\ne 1", font_size=35, color=RED)
        checks = VGroup(check1, check2).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        checks.next_to(guess_group, DOWN, buff=0.55)
        self.play(FadeIn(guess_group, shift=0.2 * RIGHT))
        self.play(Indicate(clues[0], color=GREEN), Write(check1))
        self.wait(1)
        self.play(Indicate(clues[1], color=RED), Write(check2))
        self.wait(1.3)

        question = Text("How do we find a pair that satisfies both?", font=FONT,
                        font_size=34, color=CYAN, weight=MEDIUM)
        question.to_edge(DOWN, buff=0.85)
        self.wait(2.2)  # Hold the failed-guess beat until the question at 0:16.
        self.play(FadeOut(student), FadeIn(question, shift=0.15 * UP))
        self.wait(3)  # Let the closing question land before the next scene.


class MatrixForm(Scene):
    """Map equation coefficients and constants into A, x, and b."""

    def construct(self):
        title = heading("From equations to matrix form").to_edge(UP, buff=0.42)
        eqs = equation_pair(0.78).move_to(LEFT * 4.2 + UP * 0.35)
        eq_heading = Text("Equation form", font=FONT, font_size=27, color=CYAN)
        eq_heading.move_to(LEFT * 4.2 + UP * 1.65)
        self.play(FadeIn(title), FadeIn(eq_heading), Write(eqs))

        matrix = MathTex(
            r"\begin{bmatrix}2&1\\1&-1\end{bmatrix}", r"\begin{bmatrix}x\\y\end{bmatrix}",
            r"=", r"\begin{bmatrix}5\\1\end{bmatrix}",
            font_size=52,
        ).move_to(RIGHT * 2.1 + UP * 0.55)
        matrix[0].set_color(BLUE)
        matrix[1].set_color(GOLD)
        matrix[3].set_color(GREEN)
        labels = VGroup(
            MathTex(r"A", color=BLUE, font_size=40),
            MathTex(r"\mathbf{x}", color=GOLD, font_size=40),
            MathTex(r"b", color=GREEN, font_size=40),
        )
        labels[0].next_to(matrix[0], DOWN, buff=0.18)
        labels[1].next_to(matrix[1], DOWN, buff=0.18)
        labels[2].next_to(matrix[3], DOWN, buff=0.18)
        mat_heading = Text("Matrix form", font=FONT, font_size=27, color=CYAN)
        mat_heading.move_to(RIGHT * 2.1 + UP * 1.65)
        self.play(Write(matrix), FadeIn(labels), FadeIn(mat_heading))
        self.wait(0.5)

        # Pair each equation with the corresponding row of A.
        a_matrix = matrix[0]
        for row_index, (equation, color, y_offset) in enumerate([
            (eqs[0], BLUE, 1), (eqs[1], GOLD, -1),
        ]):
            eq_box = SurroundingRectangle(equation, color=color, buff=0.08)
            row_box = Rectangle(
                width=a_matrix.width + 0.16,
                height=a_matrix.height * 0.42,
                color=color,
                stroke_width=2.5,
            ).move_to(a_matrix.get_center() + UP * (a_matrix.height * 0.24 * y_offset))
            connector = Arrow(
                eq_box.get_right(), row_box.get_left(),
                buff=0.08, color=color, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.12,
            )
            self.play(Create(eq_box), Create(row_box), GrowArrow(connector))
            self.wait(0.45)
            self.play(FadeOut(eq_box), FadeOut(row_box), FadeOut(connector))

        self.wait(2)  # Preserve the expanded-product start time after moving the row match earlier.

        expanded = MathTex(
            r"\begin{bmatrix}2&1\\1&-1\end{bmatrix}", r"\begin{bmatrix}x\\y\end{bmatrix}",
            r"=", r"\begin{bmatrix}2x+y\\x-y\end{bmatrix}", r"=", r"\begin{bmatrix}5\\1\end{bmatrix}",
            font_size=42,
        ).move_to(DOWN * 1.25)
        expanded[0].set_color(BLUE)
        expanded[1].set_color(GOLD)
        expanded[3].set_color(CYAN)
        expanded[5].set_color(GREEN)
        note = Text("Each row forms one equation; each entry is a coefficient.",
                    font=FONT, font_size=24, color=MUTED).next_to(expanded, DOWN, buff=0.55)
        self.play(TransformMatchingTex(matrix.copy(), expanded), FadeIn(note))
        self.wait(24.3)  # Preserve the scene duration after moving the matching beat to 0:23.


class VisualIntuition(Scene):
    """Connect the system to intersecting lines and column combinations."""

    def construct(self):
        # Row picture, algebra first: both equations must hold at once.
        row_alg_title = heading("Row picture — equations").to_edge(UP, buff=0.4)
        row_equations = equation_pair(1.0).move_to(UP * 0.65)
        row_solution = MathTex(r"\text{Solution: }(x,y)=(2,1)", color=CYAN, font_size=40)
        row_solution.next_to(row_equations, DOWN, buff=0.8)
        row_note = Text("A solution satisfies both equations simultaneously.",
                        font=FONT, font_size=27, color=MUTED).next_to(row_solution, DOWN, buff=0.35)
        self.play(FadeIn(row_alg_title), Write(row_equations), run_time=0.4)
        self.play(Write(row_solution), FadeIn(row_note), run_time=0.4)
        self.wait(4.5)
        self.play(FadeOut(row_alg_title), FadeOut(row_equations), FadeOut(row_solution), FadeOut(row_note), run_time=0.4)

        # Full-screen row graph. Equal ranges and lengths give equal unit scale.
        row_title = heading("Row picture — graph").to_edge(UP, buff=0.4)
        axes = Axes(
            x_range=(-1, 5, 1), y_range=(-1, 5, 1), x_length=5.0, y_length=5.0,
            axis_config={"color": MUTED, "stroke_width": 2.2, "include_numbers": True,
                         "font_size": 22, "include_tip": True}, tips=True,
        ).move_to(DOWN * 0.8)
        row_legend = VGroup(
            MathTex(r"2x+y=5", color=BLUE, font_size=31),
            MathTex(r"x-y=1", color=GOLD, font_size=31),
        ).arrange(RIGHT, buff=1.0).move_to(UP * 2.5)
        line1 = axes.plot(lambda x: 5 - 2*x, x_range=(0.15, 3.0), color=BLUE, stroke_width=5)
        line2 = axes.plot(lambda x: x - 1, x_range=(0.15, 5.0), color=GOLD, stroke_width=5)
        point = Dot(axes.c2p(2, 1), radius=0.1, color=CYAN)
        solution_label = MathTex(r"(2,1)", color=CYAN, font_size=34).next_to(point, UR, buff=0.15)
        row_caption = Text("The shared point is the solution.", font=FONT,
                           font_size=25, color=MUTED).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(row_title), FadeIn(row_legend), Create(axes), Create(line1), Create(line2))
        self.play(FadeIn(point, scale=0.4), Write(solution_label), Indicate(point, color=CYAN))
        self.play(FadeIn(row_caption))
        self.wait(13)  # Hold the row graph so column algebra begins 18 seconds after it.
        self.play(FadeOut(row_title), FadeOut(row_legend), FadeOut(axes), FadeOut(line1),
                  FadeOut(line2), FadeOut(point), FadeOut(solution_label), FadeOut(row_caption))

        # Column picture, algebra first: distinguish vector x from scalar weights.
        col_alg_title = heading("Column picture — algebra").to_edge(UP, buff=0.4)
        product = MathTex(r"A", r"\mathbf{x}", "=", "x", r"a_1", "+", "y", r"a_2", "=", "b",
                          font_size=54).move_to(UP * 0.8)
        for part, color in [(0, BLUE), (1, GOLD), (4, BLUE), (7, GOLD), (9, GREEN)]:
            product[part].set_color(color)
        product_note = VGroup(
            MathTex(r"a_1=\begin{bmatrix}2\\1\end{bmatrix}", color=BLUE, font_size=34),
            MathTex(r"a_2=\begin{bmatrix}1\\-1\end{bmatrix}", color=GOLD, font_size=34),
            Text("For this solution, x = 2 and y = 1 are the weights.",
                 font=FONT, font_size=25, color=MUTED),
        ).arrange(DOWN, buff=0.3).next_to(product, DOWN, buff=0.55)
        weights = MathTex("2a_1", "+", "a_2", "=", "b", font_size=48).next_to(product_note, DOWN, buff=0.45)
        weights[0].set_color(BLUE)
        weights[2].set_color(GOLD)
        weights[4].set_color(GREEN)
        self.play(FadeIn(col_alg_title), Write(product))
        self.play(Write(product_note), Write(weights))
        self.wait(9)
        self.play(FadeOut(col_alg_title), FadeOut(product), FadeOut(product_note), FadeOut(weights))

        # Full-screen vector construction: 2a1 followed head-to-tail by a2.
        col_title = heading("Column picture — vector sum").to_edge(UP, buff=0.4)
        c_axes = Axes(
            x_range=(0, 6, 1), y_range=(-2, 4, 1), x_length=5.0, y_length=5.0,
            axis_config={"color": MUTED, "include_numbers": True, "font_size": 21,
                         "stroke_width": 2}, tips=True,
        ).move_to(DOWN * 0.45)
        col_legend = VGroup(
            MathTex(r"a_1=(2,1)", color=BLUE, font_size=26),
            MathTex(r"a_2=(1,-1)", color=GOLD, font_size=26),
            MathTex(r"b=(5,1)", color=GREEN, font_size=26),
        ).arrange(RIGHT, buff=0.6).move_to(UP * 2.5)
        start, doubled_end, b_end = c_axes.c2p(0, 0), c_axes.c2p(4, 2), c_axes.c2p(5, 1)
        vec_a1 = Arrow(start, doubled_end, buff=0, color=BLUE, stroke_width=7)
        vec_a2 = Arrow(doubled_end, b_end, buff=0, color=GOLD, stroke_width=7)
        vec_b = Arrow(start, b_end, buff=0, color=GREEN, stroke_width=5)
        scale_label = MathTex(r"2a_1=(4,2)", color=BLUE, font_size=27).move_to(c_axes.c2p(2.4, 2.8))
        a2_label = MathTex(r"a_2=(1,-1)", color=GOLD, font_size=26).move_to(c_axes.c2p(5.1, 2.0))
        b_label = MathTex(r"b=(5,1)", color=GREEN, font_size=26).move_to(c_axes.c2p(4.5, 0.2))
        sum_eq = MathTex(r"2a_1", "+", r"a_2", "=", "b", font_size=38).to_edge(DOWN, buff=0.2)
        sum_eq[0].set_color(BLUE)
        sum_eq[2].set_color(GOLD)
        sum_eq[4].set_color(GREEN)
        self.play(FadeIn(col_title), FadeIn(col_legend), Create(c_axes))
        self.play(GrowArrow(vec_a1), FadeIn(scale_label))
        self.play(GrowArrow(vec_a2), FadeIn(a2_label))
        self.play(GrowArrow(vec_b), FadeIn(b_label), Write(sum_eq))
        self.wait(9.9)  # Shift Scene 4 and its narration one second later.


class GaussianElimination(Scene):
    """Show each elementary row operation and preserve every intermediate."""

    def construct(self):
        title = heading("Solve it with Gauss–Jordan elimination").to_edge(UP, buff=0.38)
        self.play(FadeIn(title))

        matrices = [
            aug_matrix(r"2&1&5\\1&-1&1"),
            aug_matrix(r"1&-1&1\\2&1&5"),
            aug_matrix(r"1&-1&1\\0&3&3"),
            aug_matrix(r"1&-1&1\\0&1&1"),
            aug_matrix(r"1&0&2\\0&1&1"),
        ]
        operations = [
            r"\text{Starting augmented matrix}",
            r"R_1 \leftrightarrow R_2  \quad\text{(put 1 in the first pivot)}",
            r"R_2 \to R_2-2R_1  \quad\text{(eliminate }x\text{ below pivot)}",
            r"R_2 \to \frac{1}{3}R_2  \quad\text{(make pivot one)}",
            r"R_1 \to R_1+R_2  \quad\text{(eliminate }y\text{ above pivot)}",
        ]
        op_text = MathTex(operations[0], font_size=34, color=CYAN).move_to(UP * 1.2)
        current = matrices[0].move_to(ORIGIN + DOWN * 0.15)
        self.play(FadeIn(op_text), Write(current))
        self.wait(5.9)  # Keep the starting augmented matrix visible until 1:51 overall.

        for index in range(1, len(matrices)):
            new_op = MathTex(operations[index], font_size=32, color=CYAN).move_to(op_text)
            new_matrix = matrices[index].move_to(current)
            # ReplacementTransform avoids ambiguous token matching for repeated
            # entries such as the zeros and ones in adjacent matrices.
            self.play(Transform(op_text, new_op), ReplacementTransform(current, new_matrix))
            current = new_matrix
            self.play(Indicate(current, color=GOLD, scale_factor=1.04))
            if index == 1:
                self.wait(8.0)  # Hold the row swap through 2:01 overall.
            elif index == 2:
                self.wait(8.0)  # Hold R2 - 2R1 through 2:11 overall.
            elif index == 3:
                self.wait(2.0)  # Hold the scaled row through 2:15 overall.
            else:
                self.wait(12.2)  # Leave the remaining elimination timing unchanged for now.

        answer = MathTex(r"x=2,\qquad y=1", font_size=48, color=CYAN).to_edge(DOWN, buff=0.4)
        self.play(Write(answer))
        self.wait(1)
        check_head = Text("Check in the original equations", font=FONT,
                          font_size=27, color=WHITE).move_to(DOWN * 1.25)
        check = MathTex(r"2(2)+1=5\qquad\checkmark\qquad 2-1=1\qquad\checkmark",
                        font_size=36, color=GREEN).move_to(DOWN * 2.0)
        self.play(FadeIn(check_head), Write(check))
        self.wait(5.6)  # Keep Scene 5's outcomes page anchored at 2:40.


class SolutionCases(Scene):
    """Use one coefficient matrix to compare consistency and rank."""

    def construct(self):
        title = heading("Three solution outcomes").to_edge(UP, buff=0.38)
        self.play(FadeIn(title), run_time=0.5)
        self.wait(1.0)  # Outcomes title is visible for exactly 1.5 seconds.
        self.play(FadeOut(title), run_time=0.5)
        self.wait(1.0)  # Leave the requested 1.5-second gap before the unique case.

        cases = [
            {
                "name": "Unique solution", "color": CYAN,
                "system": r"2x+y=5\quad x-y=1",
                "row": r"\det(A)=-3\ne0",
                "rank": r"\operatorname{rank}(A)=\operatorname{rank}([A|b])=2=n",
                "meaning": "The lines meet once: (2,1).",
                "lines": (lambda x: 5-2*x, lambda x: x-1, (2, 1)),
            },
            {
                "name": "Infinitely many solutions", "color": GREEN,
                "system": r"2x+y=5\quad 4x+2y=10",
                "row": r"R_2-2R_1:\ [0\quad0\mid0]",
                "rank": r"\operatorname{rank}(A)=\operatorname{rank}([A|b])=1<2",
                "meaning": "The equations are the same line; det(A)=0.",
                "lines": (lambda x: 5-2*x, lambda x: 5-2*x, None),
            },
            {
                "name": "No solution", "color": RED,
                "system": r"2x+y=5\quad 4x+2y=7",
                "row": r"R_2-2R_1:\ [0\quad0\mid-3]\quad(0=-3)",
                "rank": r"\operatorname{rank}(A)=1<\operatorname{rank}([A|b])=2",
                "meaning": "Parallel distinct lines; det(A)=0 again.",
                "lines": (lambda x: 5-2*x, lambda x: 7/2-2*x, None),
            },
        ]

        for index, case in enumerate(cases):
            if index > 0:
                self.play(FadeOut(*self.mobjects), run_time=0.5)
                if index == 1:
                    self.wait(0.5)  # Infinite-solutions page begins at 2:58.
            title = heading(case["name"], size=39, color=case["color"]).to_edge(UP, buff=0.38)
            eq = MathTex(case["system"], font_size=39, color=WHITE).move_to(UP * 1.65)
            axes = Axes(
                x_range=(-1, 4, 1), y_range=(-2, 6, 1), x_length=3.4, y_length=5.44,
                axis_config={"color": MUTED, "stroke_width": 1.7, "include_numbers": True,
                             "font_size": 17}, tips=True,
            ).move_to(LEFT * 3.25 + DOWN * 0.65)
            f1, f2, solution = case["lines"]
            line_x_range = (-0.5, 2.7) if case["name"] == "No solution" else (-0.5, 3.3)
            l1 = axes.plot(f1, x_range=line_x_range, color=BLUE, stroke_width=5)
            l2 = axes.plot(f2, x_range=line_x_range, color=GOLD, stroke_width=4)
            if case["name"] == "Infinitely many solutions":
                l2 = DashedVMobject(l2, num_dashes=25)
            math_rows = VGroup(
                MathTex(case["row"], font_size=29, color=case["color"]),
                MathTex(case["rank"], font_size=27, color=WHITE),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.48).move_to(RIGHT * 2.55 + UP * 0.4)
            note = Text(case["meaning"], font=FONT, font_size=24, color=MUTED)
            note.move_to(RIGHT * 2.55 + DOWN * 1.2)
            det_note = Text("det(A)=0 in both cases; it cannot distinguish them.",
                            font=FONT, font_size=18, color=CYAN).move_to(RIGHT * 3.2 + DOWN * 2.55)
            self.play(FadeIn(title), Write(eq), Create(axes), Create(l1), Create(l2), run_time=0.5)
            if solution:
                dot = Dot(axes.c2p(*solution), color=CYAN, radius=0.08)
                self.play(FadeIn(dot, scale=0.5), run_time=0.5)
            self.play(Write(math_rows), FadeIn(note), run_time=0.5)
            if case["name"] == "No solution":
                self.play(FadeIn(det_note), run_time=0.5)
            if case["name"] == "Unique solution":
                self.wait(12.5)  # Unique case remains through 2:57.
            elif case["name"] == "Infinitely many solutions":
                self.wait(18.5)  # Infinite case remains through 3:17.5.
            else:
                self.wait(17.5)  # End the no-solution case at 3:37.
        self.play(FadeOut(*self.mobjects))
        conclusion_title = heading("Why determinant zero is not enough", size=38, color=CYAN).to_edge(UP, buff=0.45)
        conclusion = VGroup(
            MathTex(r"\det(A)=0\quad\text{in both singular examples}", font_size=39, color=WHITE),
            MathTex(r"[0\quad0\mid0]\Rightarrow\text{ infinitely many solutions}", font_size=35, color=GREEN),
            MathTex(r"[0\quad0\mid-3]\Rightarrow\text{ no solution}", font_size=35, color=RED),
            Text("The row result or rank comparison distinguishes them.",
                 font=FONT, font_size=27, color=MUTED),
        ).arrange(DOWN, buff=0.48).move_to(DOWN * 0.2)
        self.play(FadeIn(conclusion_title), LaggedStart(*[Write(item) for item in conclusion], lag_ratio=0.3), run_time=2)
        self.wait(12)  # Keep Scene 6 anchored at 3:52 after the earlier handoff.


class SummaryCredits(Scene):
    """Close with the learning goals, authorship, and attribution."""

    def construct(self):
        title = heading("Three ideas to take with you").to_edge(UP, buff=0.4)
        points = VGroup(
            MathTex(r"1.\quad\text{A system can be written as }Ax=b.", font_size=34, color=WHITE),
            MathTex(r"2.\quad\text{Solutions are line intersections and column combinations.}", font_size=31, color=WHITE),
            MathTex(r"3.\quad\text{Gaussian elimination gives a systematic solution.}", font_size=32, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.48)
        points.move_to(UP * 0.75)
        for point in points:
            point.set_color(CYAN)
        self.play(FadeIn(title), LaggedStart(*[Write(p) for p in points], lag_ratio=0.35))
        self.wait(1.5)

        credit = Text("Sambuddha Banerjee  •  E25B070587", font=FONT,
                      font_size=27, color=GOLD).move_to(DOWN * 1.45)
        refs = Text("References: Strang, Introduction to Linear Algebra; Manim Community documentation",
                    font=FONT, font_size=18, color=MUTED).move_to(DOWN * 2.05)
        disclosure = Text("AI assistance: code and narration drafted with AI; calculations checked.",
                          font=FONT, font_size=18, color=MUTED).next_to(refs, DOWN, buff=0.14)
        music = Text("Music: Snowfall — Asher Fulero (YouTube Audio Library; no attribution required).",
                     font=FONT, font_size=18, color=MUTED).next_to(disclosure, DOWN, buff=0.14)
        self.play(FadeIn(credit), FadeIn(refs), FadeIn(disclosure), FadeIn(music))
        self.wait(19)  # Readable end card and credits.
