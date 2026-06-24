#!/usr/bin/env python3
"""
CENG381 - V2 Generator  |  Folder 2026-03-26
Topics : Recurrence Relations  |  Biased Random Walk
Outputs: Generated_Questions_V2/   and   Answer_Keys_V2/
"""
import os
from fpdf import FPDF

BASE = "/Users/apple/Desktop/CENG381"
QQ   = os.path.join(BASE, "Generated_Questions_V2")
AK   = os.path.join(BASE, "Answer_Keys_V2")
SFNS = "/System/Library/Fonts/SFNS.ttf"
MONO = "/System/Library/Fonts/SFNSMono.ttf"

_MONO_SUB = str.maketrans(
    "₀₁₂₃₄₅₆₇₈₉ᵗᵀ⁰¹²³⁴⁵⁶⁷⁸⁹ⁿₙ",
    "0123456789tT0123456789nn"
)


class ExamPDF(FPDF):
    def __init__(self, subtitle=""):
        super().__init__()
        self._sub = subtitle
        self.set_auto_page_break(True, margin=22)
        self.set_margins(25, 28, 25)
        self.add_font("SFNS", "", SFNS)
        self.add_font("Mono", "", MONO)

    def header(self):
        self.set_font("SFNS", size=13)
        self.set_text_color(20, 20, 20)
        self.cell(0, 9, "CENG381  Stochastic Processes",
                  align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("SFNS", size=10)
        self.set_text_color(90, 90, 90)
        self.cell(0, 6, self._sub,
                  align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self.set_draw_color(160, 160, 160)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(),
                  self.w - self.r_margin, self.get_y())
        self.set_draw_color(0)
        self.set_line_width(0.2)
        self.ln(6)
        self.set_text_color(0)

    def footer(self):
        self.set_y(-15)
        self.set_font("SFNS", size=8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")
        self.set_text_color(0)

    def Q(self, n, pts, text):
        self.set_font("SFNS", size=11.5)
        self.set_text_color(0)
        self.multi_cell(0, 7.5,
                        f"Q{n}  ({pts} points).  {text}",
                        new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def sub(self, label, text):
        self.set_font("SFNS", size=10.5)
        x0 = self.l_margin + 10
        self.set_x(x0)
        self.multi_cell(self.w - self.r_margin - x0, 6.5,
                        f"{label})  {text}",
                        new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def txt(self, text, indent=0):
        self.set_font("SFNS", size=10.5)
        xi = self.l_margin + indent
        self.set_x(xi)
        self.multi_cell(self.w - self.r_margin - xi, 6.5,
                        text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def mat(self, lines):
        self.set_fill_color(246, 246, 246)
        self.set_font("Mono", size=10)
        for line in lines:
            xi = self.l_margin + 20
            self.set_x(xi)
            self.multi_cell(self.w - self.r_margin - xi, 5.8,
                            line.translate(_MONO_SUB), fill=True,
                            new_x="LMARGIN", new_y="NEXT")
        self.set_fill_color(255, 255, 255)
        self.ln(3)

    def eqn(self, *lines):
        self.set_fill_color(242, 242, 242)
        self.set_font("Mono", size=10.5)
        xi = self.l_margin + 12
        avail = self.w - self.r_margin - xi
        for line in lines:
            self.set_x(xi)
            self.multi_cell(avail, 6.5,
                            line.translate(_MONO_SUB), fill=True,
                            new_x="LMARGIN", new_y="NEXT")
        self.set_fill_color(255, 255, 255)
        self.ln(3)

    def sep(self):
        self.ln(5)
        self.set_draw_color(190, 190, 190)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(),
                  self.w - self.r_margin, self.get_y())
        self.set_draw_color(0)
        self.ln(7)

    def AL(self, text):
        self.set_font("SFNS", size=10.5)
        self.set_text_color(0, 70, 150)
        self.multi_cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0)
        self.ln(0.5)

    def AH(self, text):
        self.set_font("SFNS", size=12)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0)
        self.ln(1)

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.output(path)
        print(f"  Saved  →  {os.path.relpath(path, BASE)}")


def qp(subj, f): return os.path.join(QQ, subj, f)
def ap(subj, f): return os.path.join(AK, subj, f)


# ══════════════════════════════════════════════════════════════════════════════
# 1.  RECURRENCE RELATIONS
# ══════════════════════════════════════════════════════════════════════════════

def rr_q():
    S = "Recurrence_Relations"
    p = ExamPDF("Recurrence Relations  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Solve the linear homogeneous recurrence relation with distinct roots:")
    p.mat([
        "  a_n = 5·a_(n-1)  −  6·a_(n-2),    n >= 2",
        "  a_0 = 2,   a_1 = 5",
    ])
    p.sub("a",
          "Write the characteristic equation.  Find its two roots r₁ and r₂.")
    p.sub("b",
          "Write the general solution  aₙ = α₁·r₁ⁿ + α₂·r₂ⁿ.  "
          "Apply the initial conditions to find α₁ and α₂.")
    p.sub("c",
          "Write the closed-form solution.  Compute a₄.  "
          "As n → ∞, which root dominates?  What does this imply about "
          "the growth rate of aₙ?")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "Solve the linear homogeneous recurrence relation with a repeated root:")
    p.mat([
        "  a_n = 6·a_(n-1)  −  9·a_(n-2),    n >= 2",
        "  a_0 = 1,   a_1 = 6",
    ])
    p.sub("a",
          "Write the characteristic equation.  "
          "Show it has a repeated root r = 3.")
    p.sub("b",
          "For a repeated root r, the general solution is "
          "aₙ = (α₁ + α₂·n)·rⁿ.  "
          "Apply the initial conditions to find α₁ and α₂.")
    p.sub("c",
          "Write the closed-form solution.  Compute a₃.  "
          "How does the growth rate compare to the distinct-root case in Q1?")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "Solve the linear non-homogeneous recurrence relation:")
    p.mat([
        "  a_n = 4·a_(n-1)  +  3n,    n >= 2",
        "  a_1 = 2",
    ])
    p.sub("a",
          "Ignore the non-homogeneous term for now.  "
          "Solve the homogeneous part  aₙ = 4·aₙ₋₁  "
          "to get the homogeneous solution aₙ^(h).")
    p.sub("b",
          "Find a particular solution by substituting  "
          "aₙ^(p) = cn + d  into the original recurrence.  "
          "Determine the constants c and d.")
    p.sub("c",
          "The general solution is  aₙ = α₁·4ⁿ + cn + d.  "
          "Apply the initial condition a₁ = 2 to find α₁.  "
          "Verify by computing a₂ directly from the recurrence.")

    p.save(qp(S, "Practice_1.pdf"))


def rr_a():
    S = "Recurrence_Relations"
    p = ExamPDF("Recurrence Relations  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Characteristic equation and roots:")
    p.eqn(
        "Substitute a_n = r^n:",
        "  r^2 = 5r - 6",
        "  r^2 - 5r + 6 = 0",
        "  (r - 2)(r - 3) = 0",
        "  r1 = 2,   r2 = 3  (distinct roots)",
    )

    p.AL("b)  General solution and constants:")
    p.eqn(
        "a_n = alpha1 * 2^n  +  alpha2 * 3^n",
        "",
        "a_0 = 2:  alpha1 + alpha2 = 2             ... (I)",
        "a_1 = 5:  2*alpha1 + 3*alpha2 = 5         ... (II)",
        "",
        "(II) - 2*(I):  alpha2 = 5 - 4 = 1",
        "(I):           alpha1 = 2 - 1 = 1",
    )

    p.AL("c)  Closed form, a₄, and growth rate:")
    p.eqn(
        "a_n = 2^n + 3^n",
        "",
        "a_4 = 2^4 + 3^4 = 16 + 81 = 97",
        "",
        "As n -> inf:  3^n dominates (since 3 > 2).",
        "a_n ~ 3^n,  i.e. the sequence grows exponentially at rate 3.",
    )

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Characteristic equation and repeated root:")
    p.eqn(
        "r^2 - 6r + 9 = 0",
        "(r - 3)^2 = 0",
        "r = 3  (double root)",
    )

    p.AL("b)  General solution for repeated root:")
    p.eqn(
        "a_n = (alpha1 + alpha2*n) * 3^n",
        "",
        "a_0 = 1:  alpha1 * 1 = 1  =>  alpha1 = 1",
        "a_1 = 6:  (1 + alpha2) * 3 = 6  =>  1 + alpha2 = 2  =>  alpha2 = 1",
    )

    p.AL("c)  Closed form and comparison:")
    p.eqn(
        "a_n = (1 + n) * 3^n",
        "",
        "a_3 = (1 + 3) * 3^3 = 4 * 27 = 108",
        "",
        "Growth rate: both Q1 and Q2 grow at rate 3^n.",
        "The extra factor n makes the repeated-root solution grow slightly",
        "faster (n*3^n vs 3^n), but the exponential base is the same.",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Homogeneous part:")
    p.eqn(
        "a_n = 4 * a_(n-1)  =>  r - 4 = 0  =>  r = 4",
        "a_n^(h) = alpha1 * 4^n",
    )

    p.AL("b)  Particular solution via cn + d:")
    p.txt("Substitute aₙ = cn + d into the full recurrence:")
    p.eqn(
        "cn + d = 4*[c(n-1) + d]  +  3n",
        "cn + d = 4cn - 4c + 4d + 3n",
        "",
        "Collect coefficient of n:  c = 4c + 3  =>  -3c = 3  =>  c = -1",
        "Collect constants:         d = -4c + 4d  =>  -3d = -4c = 4  =>  d = -4/3",
        "",
        "Particular solution:  a_n^(p) = -n - 4/3",
    )

    p.AL("c)  Full solution and verification:")
    p.eqn(
        "a_n = alpha1 * 4^n  -  n  -  4/3",
        "",
        "Apply a_1 = 2:",
        "  4*alpha1 - 1 - 4/3 = 2",
        "  4*alpha1 = 2 + 1 + 4/3 = 3 + 4/3 = 13/3",
        "  alpha1 = 13/12",
        "",
        "Closed form:  a_n = (13/12)*4^n - n - 4/3",
    )
    p.txt("Verify a₂ from the recurrence:")
    p.eqn(
        "a_2 = 4*a_1 + 3*2 = 4*2 + 6 = 14",
        "",
        "From formula:  a_2 = (13/12)*16 - 2 - 4/3",
        "             = 208/12 - 24/12 - 16/12 = 168/12 = 14  ✓",
    )

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 2.  BIASED RANDOM WALK
# ══════════════════════════════════════════════════════════════════════════════

def biased_q():
    S = "Biased_Random_Walk"
    p = ExamPDF("Biased Random Walk  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "A particle starts at position k = 2 on the integer path "
        "{0, 1, 2, 3, 4}.  "
        "State 0 is a 'Pit of Disaster' (absorbing) and state 4 is 'Home' "
        "(absorbing).  "
        "At each step the particle moves right with probability p = 2/3 "
        "and left with probability q = 1/3.")
    p.sub("a",
          "Let Rₙ = P(reach Home | start at n).  "
          "Write the recurrence relation for Rₙ (1 ≤ n ≤ 3) "
          "and state boundary conditions R₀ and R₄.")
    p.sub("b",
          "The characteristic equation of the homogeneous part is "
          "pr² − r + q = 0.  "
          "Factor it as (pr − q)(r − 1) = 0 to find both roots.  "
          "Compute q/p and write the general solution Rₙ = α₁·(q/p)ⁿ + α₂.")
    p.sub("c",
          "Apply R₀ = 0 and R₄ = 1 to find α₁ and α₂.  "
          "Compute R₂.  "
          "Compare with the unbiased result R₂ = 2/4 = 1/2 and explain "
          "the direction of the change.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "Using the same biased walk (p = 2/3, q = 1/3) on {0, 1, 2, 3, 4}, "
        "let Xₙ = E[absorption time | start at n].  "
        "Both barriers 0 and 4 are absorbing, so X₀ = X₄ = 0.")
    p.sub("a",
          "Write the recurrence for Xₙ (1 ≤ n ≤ 3).  "
          "Note this is a linear non-homogeneous recurrence.")
    p.sub("b",
          "The homogeneous solution is α₁·(1/2)ⁿ + α₂.  "
          "Find a particular solution of the form cn + d by substituting "
          "into the recurrence.  Show that c = −1/(p−q) = −3 and d = 0.")
    p.sub("c",
          "Write the general solution Xₙ = α₁·(1/2)ⁿ + α₂ − 3n.  "
          "Apply X₀ = 0 and X₄ = 0 to find α₁ and α₂.  "
          "Compute X₂.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A stencil starts at position k = 3 on the path {0, 1, 2, 3, 4, 5, 6} "
        "(w = 6).  "
        "State 0 = 'Pit of Disaster' and state 6 = 'Cliff of Doom', "
        "both absorbing.  "
        "The walk is biased: p = 2/3 (right) and q = 1/3 (left).")
    p.sub("a",
          "Find Rₙ = P(reach Cliff of Doom | start n) using the formula:"
          "\n\n"
          "           [(q/p)ⁿ − 1]\n"
          "  Rₙ  =  ————————————————\n"
          "           [(q/p)^w − 1]\n\n"
          "Compute R₃.  Does the particle more likely end up in the Pit or "
          "at the Cliff?")
    p.sub("b",
          "For the 'Cliff of Doom' boundary conditions (R₀ = 1, R_w = 0), "
          "the formula becomes:\n\n"
          "           (q/p)ⁿ − (q/p)^w\n"
          "  Rₙ  =  ————————————————————\n"
          "              1 − (q/p)^w\n\n"
          "Compute R₃ under these conditions.  "
          "Verify that the two probabilities from (a) and (b) sum to 1.")
    p.sub("c",
          "The expected absorption time follows "
          "Xₙ = α₁·(1/2)ⁿ + α₂ − 3n with X₀ = X₆ = 0.  "
          "Find X₃.  Compare with the unbiased expected time "
          "Xₙ^(unbiased) = n(w − n), which gives X₃^(unbiased) = 9.")

    p.save(qp(S, "Practice_1.pdf"))


def biased_a():
    S = "Biased_Random_Walk"
    p = ExamPDF("Biased Random Walk  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Recurrence and boundary conditions:")
    p.eqn(
        "Rn = q*R(n-1) + p*R(n+1)  for 1 <= n <= 3",
        "   = (1/3)*R(n-1) + (2/3)*R(n+1)",
        "",
        "R0 = 0  (Pit of Disaster is the losing state)",
        "R4 = 1  (Home is the winning state)",
    )

    p.AL("b)  Characteristic equation and roots:")
    p.eqn(
        "p*r^2 - r + q = 0",
        "(2/3)*r^2 - r + (1/3) = 0  =>  multiply by 3:",
        "2r^2 - 3r + 1 = 0  =>  (2r-1)(r-1) = 0",
        "r1 = 1/2 = q/p,   r2 = 1",
        "",
        "General solution:  Rn = alpha1*(1/2)^n + alpha2",
    )

    p.AL("c)  Applying boundary conditions and computing R₂:")
    p.eqn(
        "R0 = 0:  alpha1 + alpha2 = 0  =>  alpha2 = -alpha1",
        "R4 = 1:  alpha1*(1/16) - alpha1 = 1",
        "         alpha1*(1/16 - 1) = 1",
        "         alpha1*(-15/16)  = 1",
        "         alpha1 = -16/15,   alpha2 = 16/15",
        "",
        "Rn = (16/15)*[1 - (1/2)^n]",
        "",
        "R2 = (16/15)*(1 - 1/4) = (16/15)*(3/4) = 48/60 = 4/5 = 0.80",
        "",
        "Unbiased:  R2 = 1/2 = 0.50",
    )
    p.txt(
        "The rightward drift (p=2/3) raises the win probability from "
        "50% to 80%.  Since p > q, the walk tends to drift towards "
        "the winning boundary, so R₂ increases above the unbiased value.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Recurrence for Xₙ:")
    p.eqn(
        "Xn = 1 + q*X(n-1) + p*X(n+1)",
        "   = 1 + (1/3)*X(n-1) + (2/3)*X(n+1)  for 1 <= n <= 3",
        "X0 = 0,  X4 = 0",
    )

    p.AL("b)  Particular solution cn + d:")
    p.txt("Substitute Xₙ = cn + d into the recurrence:")
    p.eqn(
        "cn+d = 1 + (1/3)*[c(n-1)+d] + (2/3)*[c(n+1)+d]",
        "cn+d = 1 + cn/3 - c/3 + d/3 + 2cn/3 + 2c/3 + 2d/3",
        "cn+d = 1 + cn*(1/3+2/3) + c*(-1/3+2/3) + d*(1/3+2/3)",
        "cn+d = 1 + cn + c/3 + d",
        "",
        "Coefficient of n:  0 = 1 + c/3  =>  c = -3",
        "Constant:          0 = 1  =>  contradiction if d is free;",
        "                   set d = 0 (absorbed into alpha2).",
        "",
        "Particular solution:  Xn^(p) = -3n",
        "(Equivalently: c = -1/(p-q) = -1/(2/3-1/3) = -1/(1/3) = -3  ✓)",
    )

    p.AL("c)  Full solution and X₂:")
    p.eqn(
        "Xn = alpha1*(1/2)^n + alpha2 - 3n",
        "",
        "X0=0:  alpha1 + alpha2 = 0  =>  alpha2 = -alpha1",
        "X4=0:  alpha1*(1/16) - alpha1 - 12 = 0",
        "       alpha1*(1/16 - 1) = 12",
        "       alpha1*(-15/16) = 12",
        "       alpha1 = -12*(16/15) = -64/5",
        "       alpha2 = 64/5",
        "",
        "Xn = (64/5)*[1 - (1/2)^n] - 3n",
        "",
        "X2 = (64/5)*(1 - 1/4) - 6",
        "   = (64/5)*(3/4) - 6",
        "   = 48/5 - 30/5 = 18/5 = 3.6 steps",
    )
    p.txt(
        "Compare with the unbiased expected time X₂ = 2·(4−2) = 4 steps.  "
        "The biased walk reaches absorption faster (3.6 < 4) because the "
        "rightward drift moves the particle efficiently toward state 4.")

    p.sep()

    # ── Q3 ─────────────────────════════════════════════════════════════════
    p.AH("Q3  Solution")

    p.AL("a)  Probability of reaching Cliff of Doom (state 6), R₀=0, R₆=1:")
    p.eqn(
        "q/p = (1/3)/(2/3) = 1/2,   w = 6",
        "",
        "Rn = [(1/2)^n - 1] / [(1/2)^6 - 1]",
        "   = [(1/2)^n - 1] / (1/64 - 1)",
        "   = [(1/2)^n - 1] / (-63/64)",
        "   = (64/63)*[1 - (1/2)^n]",
        "",
        "R3 = (64/63)*(1 - 1/8) = (64/63)*(7/8) = 448/504 = 8/9",
    )
    p.txt(
        "R₃ = 8/9 ≈ 89%.  The particle is much more likely to reach the "
        "Cliff of Doom (state 6) than the Pit of Disaster (state 0), "
        "because p=2/3 creates a strong rightward bias.")

    p.AL("b)  Probability of reaching Pit of Disaster (state 0), R₀=1, R₆=0:")
    p.eqn(
        "Rn = [(1/2)^n - (1/2)^6] / [1 - (1/2)^6]",
        "   = [(1/2)^n - 1/64] / [1 - 1/64]",
        "   = [(1/2)^n - 1/64] / (63/64)",
        "",
        "R3 = [(1/8) - (1/64)] / (63/64)",
        "   = [(8/64) - (1/64)] * (64/63)",
        "   = (7/64) * (64/63) = 7/63 = 1/9",
        "",
        "Check:  R3(Cliff) + R3(Pit) = 8/9 + 1/9 = 1  ✓",
    )

    p.AL("c)  Expected absorption time X₃ and comparison:")
    p.eqn(
        "Xn = alpha1*(1/2)^n + alpha2 - 3n  [same particular solution]",
        "",
        "X0=0:  alpha1 + alpha2 = 0  =>  alpha2 = -alpha1",
        "X6=0:  alpha1*(1/64) - alpha1 - 18 = 0",
        "       alpha1*(1/64 - 1) = 18",
        "       alpha1*(-63/64) = 18",
        "       alpha1 = -18*(64/63) = -1152/63 = -128/7",
        "       alpha2 = 128/7",
        "",
        "Xn = (128/7)*[1 - (1/2)^n] - 3n",
        "",
        "X3 = (128/7)*(1 - 1/8) - 9",
        "   = (128/7)*(7/8) - 9",
        "   = 128/8 - 9 = 16 - 9 = 7 steps",
    )
    p.txt(
        "Biased: X₃ = 7 steps.  Unbiased: X₃ = n(w−n) = 3·3 = 9 steps.  "
        "The biased walk (p=2/3) is absorbed 2 steps faster on average.  "
        "This makes sense: the drift toward the right boundary shortens "
        "the time to reach either absorbing state.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== V2  |  Folder 2026-03-26 ===")
    print("Topics: Recurrence Relations | Biased Random Walk\n")

    print("Generating question PDFs …")
    rr_q()
    biased_q()

    print("\nGenerating answer-key PDFs …")
    rr_a()
    biased_a()

    print("\nDone.  4 PDFs written to:")
    print(f"  {os.path.relpath(QQ, BASE)}/")
    print(f"  {os.path.relpath(AK, BASE)}/")
