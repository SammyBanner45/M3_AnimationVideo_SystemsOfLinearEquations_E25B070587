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
        self.wait(1.5)

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
        self.play(FadeOut(student), FadeIn(question, shift=0.15 * UP))
        self.wait(18)  # Hold the central question for the spoken hook.


class MatrixForm(Scene):
    """Map equation coefficients and constants into A, x, and b."""

    def construct(self):
        title = heading("From equations to matrix form").to_edge(UP, buff=0.42)
        eqs = equation_pair(0.78).move_to(LEFT * 4.2 + UP * 0.35)
        self.play(FadeIn(title), Write(eqs))
        self.wait(1)

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
            MathTex(r"x", color=GOLD, font_size=40),
            MathTex(r"b", color=GREEN, font_size=40),
        )
        labels[0].next_to(matrix[0], DOWN, buff=0.18)
        labels[1].next_to(matrix[1], DOWN, buff=0.18)
        labels[2].next_to(matrix[3], DOWN, buff=0.18)
        self.play(Write(matrix), FadeIn(labels))
        self.wait(1.5)

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
        self.wait(38)  # Leave room to explain A, x, b, and the row-to-equation mapping.


class VisualIntuition(Scene):
    """Connect the system to intersecting lines and column combinations."""

    def construct(self):
        title = heading("Two pictures of the same solution").to_edge(UP, buff=0.38)
        self.play(FadeIn(title))

        # Row picture: each equation is a line; their common point solves both.
        left_title = Text("Row picture: intersecting lines", font=FONT,
                          font_size=24, color=WHITE)
        left_title.move_to(LEFT * 3.55 + UP * 2.35)
        axes = system_axes(width=5.2, height=3.2).move_to(LEFT * 3.5 + DOWN * 0.55)
        line1 = axes.plot(lambda x: 5 - 2*x, x_range=(-0.3, 3.25), color=BLUE, stroke_width=4)
        line2 = axes.plot(lambda x: x - 1, x_range=(-0.2, 4.0), color=GOLD, stroke_width=4)
        l1 = MathTex(r"2x+y=5", color=BLUE, font_size=26)
        l2 = MathTex(r"x-y=1", color=GOLD, font_size=26)
        row_legend = VGroup(l1, l2).arrange(RIGHT, buff=0.6)
        row_legend.move_to(LEFT * 3.5 + UP * 1.65)
        dot = Dot(axes.c2p(2, 1), radius=0.09, color=CYAN)
        sol = MathTex(r"(2,1)", color=CYAN, font_size=34).next_to(dot, UR, buff=0.12)
        self.play(FadeIn(left_title), Create(axes), Create(line1), Create(line2), FadeIn(row_legend))
        self.play(FadeIn(dot, scale=0.4), Write(sol), Indicate(dot, color=CYAN))

        # Column picture: a1 is doubled, then a2 is added head-to-tail to reach b.
        right_title = Text("Column picture: build b from columns", font=FONT,
                           font_size=24, color=WHITE).move_to(RIGHT * 3.45 + UP * 2.35)
        c_axes = Axes(
            x_range=(0, 6, 1), y_range=(-2, 4, 1), x_length=4.8, y_length=3.2,
            axis_config={"color": MUTED, "include_numbers": True, "font_size": 20,
                         "stroke_width": 2}, tips=True,
        ).move_to(RIGHT * 3.35 + DOWN * 0.55)
        col_legend = VGroup(
            MathTex(r"a_1=(2,1)", color=BLUE, font_size=22),
            MathTex(r"a_2=(1,-1)", color=GOLD, font_size=22),
            MathTex(r"b=(5,1)", color=GREEN, font_size=22),
        ).arrange(RIGHT, buff=0.18).move_to(RIGHT * 3.35 + UP * 1.65)
        self.play(FadeIn(right_title), FadeIn(col_legend), Create(c_axes))

        start = c_axes.c2p(0, 0)
        doubled_end = c_axes.c2p(4, 2)
        b_end = c_axes.c2p(5, 1)
        vec_a1 = Arrow(start, doubled_end, buff=0, color=BLUE, stroke_width=6, max_tip_length_to_length_ratio=0.12)
        vec_a2 = Arrow(doubled_end, b_end, buff=0, color=GOLD, stroke_width=6, max_tip_length_to_length_ratio=0.3)
        vec_b = Arrow(start, b_end, buff=0, color=GREEN, stroke_width=4, max_tip_length_to_length_ratio=0.12)
        a1_label = MathTex(r"2a_1=(4,2)", color=BLUE, font_size=24).move_to(c_axes.c2p(2.8, 2.6))
        a2_label = MathTex(r"a_2=(1,-1)", color=GOLD, font_size=24).move_to(c_axes.c2p(5.4, 2.1))
        b_label = MathTex(r"b=(5,1)", color=GREEN, font_size=24).move_to(c_axes.c2p(4.6, 0.35))
        self.play(GrowArrow(vec_a1), FadeIn(a1_label))
        self.play(GrowArrow(vec_a2), FadeIn(a2_label))
        self.play(GrowArrow(vec_b), FadeIn(b_label))
        equation = MathTex(r"2a_1", "+", r"a_2", "=", "b", font_size=38).to_edge(DOWN, buff=0.28)
        equation[0].set_color(BLUE)
        equation[2].set_color(GOLD)
        equation[4].set_color(GREEN)
        self.play(Write(equation))
        self.wait(48)  # Narration covers the row picture and column construction.


class GaussianElimination(Scene):
    """Show each elementary row operation and preserve every intermediate."""

    def construct(self):
        title = heading("Solve it with Gaussian elimination").to_edge(UP, buff=0.38)
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
            r"R_1 \leftrightarrow R_2  \quad\text{(swap rows)}",
            r"R_2 \to R_2-2R_1  \quad\text{(eliminate }x\text{ below pivot)}",
            r"R_2 \to \frac{1}{3}R_2  \quad\text{(make pivot one)}",
            r"R_1 \to R_1+R_2  \quad\text{(eliminate }y\text{ above pivot)}",
        ]
        op_text = MathTex(operations[0], font_size=34, color=CYAN).move_to(UP * 1.2)
        current = matrices[0].move_to(ORIGIN + DOWN * 0.15)
        self.play(FadeIn(op_text), Write(current))
        self.wait(1.2)

        for index in range(1, len(matrices)):
            new_op = MathTex(operations[index], font_size=32, color=CYAN).move_to(op_text)
            new_matrix = matrices[index].move_to(current)
            # ReplacementTransform avoids ambiguous token matching for repeated
            # entries such as the zeros and ones in adjacent matrices.
            self.play(Transform(op_text, new_op), ReplacementTransform(current, new_matrix))
            current = new_matrix
            self.play(Indicate(current, color=GOLD, scale_factor=1.04))
            self.wait(1.15)

        answer = MathTex(r"x=2,\qquad y=1", font_size=48, color=CYAN).to_edge(DOWN, buff=0.4)
        self.play(Write(answer))
        self.wait(1)
        check_head = Text("Check in the original equations", font=FONT,
                          font_size=27, color=WHITE).move_to(DOWN * 1.25)
        check = MathTex(r"2(2)+1=5\qquad\checkmark\qquad 2-1=1\qquad\checkmark",
                        font_size=36, color=GREEN).move_to(DOWN * 2.0)
        self.play(FadeIn(check_head), Write(check))
        self.wait(48)  # Pause for the narrated verification of both equations.


class SolutionCases(Scene):
    """Compare the three geometric outcomes and the determinant test."""

    def construct(self):
        title = heading("Three possible solution cases").to_edge(UP, buff=0.35)
        self.play(FadeIn(title))
        specs = [
            ("One solution", "Intersecting", lambda x: 0.7*x+1, lambda x: -0.8*x+2.5, CYAN),
            ("No solution", "Parallel", lambda x: 0.65*x+1.4, lambda x: 0.65*x-0.3, RED),
            ("Infinitely many", "Coincident", lambda x: 0.55*x+1, lambda x: 0.55*x+1, GREEN),
        ]
        centers = [LEFT * 4.15, ORIGIN, RIGHT * 4.15]
        for i, (caption, sub, f1, f2, color) in enumerate(specs):
            mini = Axes(
                x_range=(-2, 2.5, 1), y_range=(-1, 4, 1), x_length=3.55, y_length=2.65,
                axis_config={"color": MUTED, "stroke_width": 1.6, "include_numbers": False},
                tips=True,
            ).move_to(centers[i] + DOWN * 0.2)
            a = mini.plot(f1, x_range=(-1.8, 2.2), color=BLUE, stroke_width=4)
            b = mini.plot(f2, x_range=(-1.8, 2.2), color=GOLD, stroke_width=4)
            cap = Text(caption, font=FONT, font_size=24, color=color, weight=MEDIUM)
            cap.move_to(centers[i] + UP * 1.85)
            subcap = Text(sub, font=FONT, font_size=20, color=MUTED).next_to(cap, DOWN, buff=0.12)
            self.play(Create(mini), Create(a), Create(b), FadeIn(cap), FadeIn(subcap), run_time=0.8)

        determinant = MathTex(r"\det(A)=2(-1)-1(1)=-3\ne0", font_size=42, color=CYAN)
        determinant.move_to(DOWN * 2.25)
        note = Text("For a square system: nonzero determinant → unique solution.",
                    font=FONT, font_size=23, color=WHITE).next_to(determinant, DOWN, buff=0.22)
        note2 = Text("Zero determinant → inconsistent or infinitely many solutions.",
                     font=FONT, font_size=22, color=MUTED).next_to(note, DOWN, buff=0.15)
        self.play(Write(determinant), FadeIn(note), FadeIn(note2))
        self.wait(39)  # Let the three cases and determinant distinction register.


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
