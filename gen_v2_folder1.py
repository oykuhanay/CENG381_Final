#!/usr/bin/env python3
"""
CENG381 - V2 Generator  |  Folder 2026-02-26
Topics : Finite Markov Chains  |  Stationary Distribution  |  Rate of Convergence
Outputs: Generated_Questions_V2/   and   Answer_Keys_V2/
"""
import os
from fpdf import FPDF

BASE = "/Users/apple/Desktop/CENG381"
QQ   = os.path.join(BASE, "Generated_Questions_V2")
AK   = os.path.join(BASE, "Answer_Keys_V2")
SFNS = "/System/Library/Fonts/SFNS.ttf"
MONO = "/System/Library/Fonts/SFNSMono.ttf"

# ── PDF helper ────────────────────────────────────────────────────────────────
# Characters unsupported by SFNSMono — translate before mono rendering
_MONO_SUB = str.maketrans(
    "₀₁₂₃₄₅₆₇₈₉ᵗᵀ⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ",
    "0123456789tT0123456789n"
)

class ExamPDF(FPDF):
    def __init__(self, subtitle=""):
        super().__init__()
        self._sub = subtitle
        self.set_auto_page_break(True, margin=22)
        self.set_margins(25, 28, 25)
        self.add_font("SFNS",     "", SFNS)
        self.add_font("SFNSItal", "", "/System/Library/Fonts/SFNSItalic.ttf")
        self.add_font("Mono",     "", MONO)

    # ── header / footer ──────────────────────────────────────────────────────
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

    # ── content helpers ───────────────────────────────────────────────────────
    def Q(self, n, pts, text):
        """Question heading: bold-style via size bump."""
        self.set_font("SFNS", size=11.5)
        self.set_text_color(0, 0, 0)
        label = f"Q{n}  ({pts} points).  "
        # print label in one cell, then rest in multi_cell
        self.multi_cell(0, 7.5,
                        label + text,
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
                        text,
                        new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def mat(self, lines):
        """Monospace matrix block on a light-gray background."""
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
        """Equation block: monospace, slightly indented, gray fill."""
        self.set_fill_color(242, 242, 242)
        self.set_font("Mono", size=10.5)
        xi = self.l_margin + 12
        avail = self.w - self.r_margin - xi
        for line in lines:
            self.set_x(xi)
            self.multi_cell(avail, 6.5, line.translate(_MONO_SUB), fill=True,
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
        """Answer label — blue, slightly larger."""
        self.set_font("SFNS", size=10.5)
        self.set_text_color(0, 70, 150)
        self.multi_cell(0, 7, text,
                        new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0)
        self.ln(0.5)

    def AH(self, text):
        """Answer section heading."""
        self.set_font("SFNS", size=12)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 8, text,
                        new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0)
        self.ln(1)

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.output(path)
        print(f"  Saved  →  {os.path.relpath(path, BASE)}")


def qp(subj, f): return os.path.join(QQ, subj, f)
def ap(subj, f): return os.path.join(AK, subj, f)


# ══════════════════════════════════════════════════════════════════════════════
# 1.  FINITE MARKOV CHAINS
# ══════════════════════════════════════════════════════════════════════════════

def finite_mc_q():
    S = "Finite_Markov_Chains"
    p = ExamPDF("Finite Markov Chains  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "A meteorologist models daily weather with states: Sunny (S), "
        "Cloudy (C), Rainy (R).  The one-step transition matrix is:")
    p.mat([
        "        S      C      R",
        "  S  [  ?     0.3    0.2  ]",
        "  C  [ 0.4     ?     0.3  ]",
        "  R  [ 0.1    0.5     ?   ]",
    ])
    p.sub("a",
          "Determine each missing entry so that P is a valid stochastic "
          "matrix (every row sums to 1).")
    p.sub("b",
          "Compute the two-step transition matrix P⁽²⁾ = P · P.")
    p.sub("c",
          "Using the Chapman-Kolmogorov equation, find the three-step "
          "transition probability p_{SR}⁽³⁾ — the probability of going "
          "from Sunny to Rainy in exactly three days.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "Consider the Markov chain on states {1, 2, 3, 4, 5} with "
        "transition matrix:")
    p.mat([
        "        1      2      3      4      5",
        "  1  [ 1/2   1/2     0      0      0  ]",
        "  2  [ 1/2   1/2     0      0      0  ]",
        "  3  [  0    1/3    1/3    1/3     0  ]",
        "  4  [  0     0      0    1/3    2/3  ]",
        "  5  [  0     0      0    2/3    1/3  ]",
    ])
    p.sub("a", "Draw the transition diagram.")
    p.sub("b",
          "Identify all communicating classes.  State whether each class "
          "is positive recurrent, null recurrent, or transient.")
    p.sub("c",
          "Find the limiting state probabilities.  "
          "(If there are multiple recurrent classes, give the limiting "
          "distribution restricted to each class, and state the absorption "
          "probabilities for the transient state.)")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A student's daily mood follows a Markov chain on "
        "{Good (G), Neutral (N), Bad (B)}:")
    p.mat([
        "  From G :  stay G  0.6,  go N  0.3,  go B  0.1",
        "  From N :  go G   0.4,  stay N  0.3,  go B  0.3",
        "  From B :  go G   0.2,  go N   0.5,  stay B  0.3",
    ])
    p.sub("a",
          "Write the 3×3 transition matrix P with rows and columns "
          "ordered (G, N, B).")
    p.sub("b",
          "The student is Neutral on Monday.  Find the probability "
          "distribution over {G, N, B} on Wednesday by computing "
          "μ₁ = (0, 1, 0)·P  and  μ₂ = μ₁·P.")
    p.sub("c",
          "Use the Chapman-Kolmogorov equation to find p_{GB}⁽³⁾ — "
          "the probability of going from Good to Bad in exactly three days.  "
          "First compute row G of P⁽²⁾, then apply "
          "p_{GB}⁽³⁾ = Σₖ p_{Gk}⁽²⁾ · P_{kB}.")

    p.save(qp(S, "Practice_1.pdf"))


def finite_mc_a():
    S = "Finite_Markov_Chains"
    p = ExamPDF("Finite Markov Chains  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Each row must sum to 1:")
    p.eqn(
        "Row S:  ? = 1 − 0.3 − 0.2 = 0.5",
        "Row C:  ? = 1 − 0.4 − 0.3 = 0.3",
        "Row R:  ? = 1 − 0.1 − 0.5 = 0.4",
    )
    p.mat([
        "        S      C      R",
        "  S  [ 0.5    0.3    0.2 ]",
        "  C  [ 0.4    0.3    0.3 ]",
        "  R  [ 0.1    0.5    0.4 ]",
    ])

    p.AL("b)  P⁽²⁾ = P · P  (entry p_{ij}⁽²⁾ = Σₖ P_{ik} · P_{kj}):")
    p.txt(
        "Row S of P⁽²⁾:\n"
        "  p_{SS}⁽²⁾ = 0.5×0.5 + 0.3×0.4 + 0.2×0.1 = 0.25+0.12+0.02 = 0.39\n"
        "  p_{SC}⁽²⁾ = 0.5×0.3 + 0.3×0.3 + 0.2×0.5 = 0.15+0.09+0.10 = 0.34\n"
        "  p_{SR}⁽²⁾ = 0.5×0.2 + 0.3×0.3 + 0.2×0.4 = 0.10+0.09+0.08 = 0.27\n\n"
        "Row C of P⁽²⁾:\n"
        "  p_{CS}⁽²⁾ = 0.4×0.5 + 0.3×0.4 + 0.3×0.1 = 0.20+0.12+0.03 = 0.35\n"
        "  p_{CC}⁽²⁾ = 0.4×0.3 + 0.3×0.3 + 0.3×0.5 = 0.12+0.09+0.15 = 0.36\n"
        "  p_{CR}⁽²⁾ = 0.4×0.2 + 0.3×0.3 + 0.3×0.4 = 0.08+0.09+0.12 = 0.29\n\n"
        "Row R of P⁽²⁾:\n"
        "  p_{RS}⁽²⁾ = 0.1×0.5 + 0.5×0.4 + 0.4×0.1 = 0.05+0.20+0.04 = 0.29\n"
        "  p_{RC}⁽²⁾ = 0.1×0.3 + 0.5×0.3 + 0.4×0.5 = 0.03+0.15+0.20 = 0.38\n"
        "  p_{RR}⁽²⁾ = 0.1×0.2 + 0.5×0.3 + 0.4×0.4 = 0.02+0.15+0.16 = 0.33",
        indent=0)
    p.mat([
        "P⁽²⁾  =",
        "  [ 0.39   0.34   0.27 ]   (row sums: 1.00 ✓)",
        "  [ 0.35   0.36   0.29 ]   (row sums: 1.00 ✓)",
        "  [ 0.29   0.38   0.33 ]   (row sums: 1.00 ✓)",
    ])

    p.AL("c)  p_{SR}⁽³⁾ via Chapman-Kolmogorov (n=2, m=1):")
    p.eqn(
        "p_{SR}⁽³⁾ = p_{SS}⁽²⁾·P_{SR} + p_{SC}⁽²⁾·P_{CR} + p_{SR}⁽²⁾·P_{RR}",
        "         = 0.39×0.2  +  0.34×0.3  +  0.27×0.4",
        "         = 0.078 + 0.102 + 0.108",
        "         = 0.288",
    )

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Transition diagram (description):")
    p.txt(
        "States 1 and 2 each have self-loops (prob ½) and arrows to each "
        "other (prob ½).  State 3 has arrows to states 2, 3, 4 (each prob ⅓).  "
        "States 4 and 5 communicate with each other: 4→5 (prob ⅔), 5→4 (prob ⅔), "
        "4→4 (prob ⅓), 5→5 (prob ⅓).  There are no arrows from {1,2} to {3,4,5} "
        "or from {4,5} back to {1,2,3}.")

    p.AL("b)  Communicating classes:")
    p.txt(
        "Class {1, 2}:  P(1,2)=½>0 and P(2,1)=½>0, so 1↔2.  "
        "No transitions leave this class (P(1,3)=P(2,3)=…=0).  "
        "→  CLOSED  →  Positive Recurrent.\n\n"
        "Class {3}:  From 3 we can reach 2 (prob ⅓) or 4 (prob ⅓).  "
        "Neither 2 nor 4 can return to 3.  State 3 can never return to "
        "itself with prob 1.  →  Transient.\n\n"
        "Class {4, 5}:  P(4,5)=⅔>0 and P(5,4)=⅔>0, so 4↔5.  "
        "No transitions leave this class.  "
        "→  CLOSED  →  Positive Recurrent.")

    p.AL("c)  Limiting distributions:")
    p.txt(
        "Within class {1, 2} (restricted matrix, solve π·P = π):\n"
        "  π₁ = ½π₁ + ½π₂  and  π₁+π₂=1  →  π₁=π₂  →  π₁=π₂=½\n\n"
        "Within class {4, 5}:\n"
        "  π₄ = ⅓π₄ + ⅔π₅  →  ⅔π₄=⅔π₅  →  π₄=π₅=½\n\n"
        "Absorption from state 3 (let h = P(absorbed by {1,2} | start 3)):\n"
        "  h = ⅓·1 + ⅓·h + ⅓·0   →   ⅔h = ⅓   →   h = ½\n"
        "  So from state 3: absorbed into {1,2} with prob ½, into {4,5} with prob ½.\n\n"
        "Long-run probabilities starting from state 3:\n"
        "  π₁=π₂=¼,  π₃=0,  π₄=π₅=¼  (weighted average of the two class limits).")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Transition matrix P (order G, N, B):")
    p.mat([
        "        G      N      B",
        "  G  [ 0.6    0.3    0.1 ]",
        "  N  [ 0.4    0.3    0.3 ]",
        "  B  [ 0.2    0.5    0.3 ]",
    ])

    p.AL("b)  Two-step distribution from N (Monday → Wednesday):")
    p.txt(
        "μ₀ = (0, 1, 0)  (start in N on Monday)\n\n"
        "μ₁ = μ₀·P = (0·0.6+1·0.4+0·0.2,  0·0.3+1·0.3+0·0.5,  0·0.1+1·0.3+0·0.3)\n"
        "   = (0.4,  0.3,  0.3)   [Tuesday distribution]")
    p.eqn(
        "μ₂[G] = 0.4×0.6 + 0.3×0.4 + 0.3×0.2 = 0.24+0.12+0.06 = 0.42",
        "μ₂[N] = 0.4×0.3 + 0.3×0.3 + 0.3×0.5 = 0.12+0.09+0.15 = 0.36",
        "μ₂[B] = 0.4×0.1 + 0.3×0.3 + 0.3×0.3 = 0.04+0.09+0.09 = 0.22",
        "Check: 0.42+0.36+0.22 = 1.00  ✓",
    )
    p.txt("Wednesday distribution:  P(G)=0.42,  P(N)=0.36,  P(B)=0.22.")

    p.AL("c)  p_{GB}⁽³⁾ via Chapman-Kolmogorov:")
    p.txt("First, compute row G of P⁽²⁾:")
    p.eqn(
        "p_{GG}⁽²⁾ = 0.6×0.6+0.3×0.4+0.1×0.2 = 0.36+0.12+0.02 = 0.50",
        "p_{GN}⁽²⁾ = 0.6×0.3+0.3×0.3+0.1×0.5 = 0.18+0.09+0.05 = 0.32",
        "p_{GB}⁽²⁾ = 0.6×0.1+0.3×0.3+0.1×0.3 = 0.06+0.09+0.03 = 0.18",
        "Check: 0.50+0.32+0.18 = 1.00  ✓",
    )
    p.eqn(
        "p_{GB}⁽³⁾ = p_{GG}⁽²⁾×P_{GB} + p_{GN}⁽²⁾×P_{NB} + p_{GB}⁽²⁾×P_{BB}",
        "         = 0.50×0.1 + 0.32×0.3 + 0.18×0.3",
        "         = 0.050 + 0.096 + 0.054",
        "         = 0.200",
    )

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 2.  STATIONARY DISTRIBUTION
# ══════════════════════════════════════════════════════════════════════════════

def stationary_q():
    S = "Stationary_Distribution"
    p = ExamPDF("Stationary Distribution  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "A marine biologist tags fish that move between two coastal areas, "
        "A and B.  Each day, 2 out of every 3 fish in area A swim to area B, "
        "while only 1 out of every 5 fish in area B return to area A.")
    p.sub("a",
          "Model this as a two-state Markov chain and write the transition "
          "matrix P (states ordered A, B).")
    p.sub("b",
          "Find the stationary distribution π = (π_A, π_B) by solving "
          "π·P = π  together with  π_A + π_B = 1.  "
          "Set up the balance equations explicitly.")
    p.sub("c",
          "Interpret π_A: in the long run, what fraction of days does a "
          "tagged fish spend in area A?")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "A factory machine cycles through three states each day: "
        "Working (W), Under Maintenance (M), and Failed (F).  "
        "The transition matrix is:")
    p.mat([
        "        W      M      F",
        "  W  [ 1/2    1/3    1/6 ]",
        "  M  [ 1/2     0     1/2 ]",
        "  F  [  1      0      0  ]",
    ])
    p.sub("a",
          "Find the stationary distribution π = (π_W, π_M, π_F) by "
          "solving the balance equations π·P = π with π_W+π_M+π_F = 1.")
    p.sub("b",
          "Verify your answer by computing π·P directly and confirming "
          "each component equals the corresponding π value.")
    p.sub("c",
          "Test whether the chain is time-reversible by checking the "
          "detailed balance condition  π_i · P_{ij} = π_j · P_{ji}  "
          "for the pair (W, M) and the pair (W, F).  "
          "What do you conclude?")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "An ATM machine is classified at the start of each business day as: "
        "Full (F) — cash above 80%, Normal (N) — cash between 20–80%, "
        "or Low (L) — cash below 20%.  The transition probabilities are:\n"
        "  • From F: stays Full with prob 1/2, drops to Normal with prob 1/2.\n"
        "  • From N: refilled to Full with prob 1/4, stays Normal with prob 1/2, "
        "drops to Low with prob 1/4.\n"
        "  • From L: always refilled to Normal overnight.")
    p.sub("a",
          "Write the 3×3 transition matrix P (rows and columns ordered F, N, L).")
    p.sub("b",
          "Find the stationary distribution π = (π_F, π_N, π_L).")
    p.sub("c",
          "What fraction of days is the ATM in the Low state?  "
          "Compare π_F and π_L.  "
          "Which state is most frequently visited in the long run?")

    p.save(qp(S, "Practice_1.pdf"))


def stationary_a():
    S = "Stationary_Distribution"
    p = ExamPDF("Stationary Distribution  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Transition matrix:")
    p.txt(
        "From A: P(A→A) = 1 − 2/3 = 1/3,  P(A→B) = 2/3\n"
        "From B: P(B→A) = 1/5,              P(B→B) = 4/5")
    p.mat([
        "         A      B",
        "  A  [ 1/3    2/3 ]",
        "  B  [ 1/5    4/5 ]",
    ])

    p.AL("b)  Stationary distribution (balance equations):")
    p.eqn(
        "π_A = π_A·(1/3) + π_B·(1/5)   ... (I)",
        "π_B = π_A·(2/3) + π_B·(4/5)   ... (II)",
        "π_A + π_B = 1                  ... (III)",
    )
    p.txt(
        "From (I):  π_A − (1/3)π_A = (1/5)π_B\n"
        "           (2/3)π_A = (1/5)π_B\n"
        "           π_B = (10/3)π_A\n\n"
        "Substitute into (III):\n"
        "  π_A + (10/3)π_A = 1   →   (13/3)π_A = 1")
    p.eqn(
        "π_A = 3/13 ≈ 0.231,   π_B = 10/13 ≈ 0.769",
    )

    p.AL("c)  Interpretation:")
    p.txt(
        "π_A = 3/13 ≈ 23.1%.  In the long run, a tagged fish spends about "
        "23% of its days in area A and 77% in area B.  This asymmetry "
        "arises because the rate of leaving A (2/3) is much higher than "
        "the rate of leaving B (1/5).")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Balance equations π·P = π:")
    p.eqn(
        "π_W = π_W·(1/2) + π_M·(1/2) + π_F·1   ... (I)",
        "π_M = π_W·(1/3) + π_M·0     + π_F·0   ... (II)",
        "π_F = π_W·(1/6) + π_M·(1/2) + π_F·0   ... (III)",
        "π_W + π_M + π_F = 1                    ... (IV)",
    )
    p.txt(
        "From (II):  π_M = (1/3)π_W\n\n"
        "From (III): π_F = (1/6)π_W + (1/2)·(1/3)π_W\n"
        "                = (1/6)π_W + (1/6)π_W = (1/3)π_W\n\n"
        "Substitute into (IV):\n"
        "  π_W + (1/3)π_W + (1/3)π_W = 1   →   (5/3)π_W = 1")
    p.eqn(
        "π_W = 3/5 = 0.6,   π_M = 1/5 = 0.2,   π_F = 1/5 = 0.2",
    )

    p.AL("b)  Verification  π·P = π:")
    p.eqn(
        "(π·P)[W] = 0.6·(1/2)+0.2·(1/2)+0.2·1 = 0.30+0.10+0.20 = 0.60 = π_W  ✓",
        "(π·P)[M] = 0.6·(1/3)+0.2·0    +0.2·0 = 0.20             = 0.20 = π_M  ✓",
        "(π·P)[F] = 0.6·(1/6)+0.2·(1/2)+0.2·0 = 0.10+0.10       = 0.20 = π_F  ✓",
    )

    p.AL("c)  Detailed balance test:")
    p.eqn(
        "Pair (W, M):  π_W·P_{WM} = 0.6·(1/3) = 0.20",
        "              π_M·P_{MW} = 0.2·(1/2) = 0.10",
        "  0.20 ≠ 0.10  →  detailed balance FAILS for (W,M).",
        "",
        "Pair (W, F):  π_W·P_{WF} = 0.6·(1/6) = 0.10",
        "              π_F·P_{FW} = 0.2·1      = 0.20",
        "  0.10 ≠ 0.20  →  detailed balance FAILS for (W,F).",
    )
    p.txt(
        "Conclusion: the chain is NOT time-reversible.  "
        "There is a net directional flow W → M → F → W, "
        "which is characteristic of a non-reversible process.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Transition matrix P (order F, N, L):")
    p.mat([
        "         F      N      L",
        "  F  [ 1/2    1/2     0  ]",
        "  N  [ 1/4    1/2    1/4 ]",
        "  L  [  0      1      0  ]",
    ])

    p.AL("b)  Balance equations π·P = π:")
    p.eqn(
        "π_F = (1/2)π_F + (1/4)π_N            ... (I)",
        "π_N = (1/2)π_F + (1/2)π_N + π_L     ... (II)",
        "π_L = (1/4)π_N                        ... (III)",
        "π_F + π_N + π_L = 1                  ... (IV)",
    )
    p.txt(
        "From (I):  (1/2)π_F = (1/4)π_N   →   π_N = 2π_F\n\n"
        "From (III): π_L = (1/4)·2π_F = (1/2)π_F\n\n"
        "Substitute into (IV):\n"
        "  π_F + 2π_F + (1/2)π_F = 1   →   (7/2)π_F = 1")
    p.eqn(
        "π_F = 2/7 ≈ 0.286,   π_N = 4/7 ≈ 0.571,   π_L = 1/7 ≈ 0.143",
    )
    p.txt("Verification of (II): (1/2)·(2/7)+(1/2)·(4/7)+(1)·(1/7) = 1/7+2/7+1/7 = 4/7 = π_N ✓")

    p.AL("c)  Interpretation:")
    p.txt(
        "The ATM is in the Low state on about 1/7 ≈ 14.3% of days.\n"
        "π_F = 2/7 ≈ 28.6%  (Full),  π_L = 1/7 ≈ 14.3%  (Low).\n"
        "So the ATM is Full about twice as often as Low.\n"
        "The Normal state (π_N = 4/7 ≈ 57.1%) is the most frequently visited.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 3.  RATE OF CONVERGENCE
# ══════════════════════════════════════════════════════════════════════════════

def convergence_q():
    S = "Rate_of_Convergence"
    p = ExamPDF("Rate of Convergence  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "A user is either Online (O) or Offline (I) at the start of each "
        "hour.  The transition matrix is:")
    p.mat([
        "         O       I",
        "  O  [  0.6     0.4  ]",
        "  I  [  0.5     0.5  ]",
    ])
    p.sub("a",
          "Find the stationary distribution π = (π_O, π_I) using the "
          "formula  π_O = q/(p+q),  π_I = p/(p+q),  "
          "where p = P(O→I) and q = P(I→O).")
    p.sub("b",
          "Define Δ_t = μ_t(O) − π_O, where μ_t(O) is the probability "
          "of being Online at time t.  Show that Δ_{t+1} = λ₂ · Δ_t, "
          "and identify λ₂ = 1 − p − q.")
    p.sub("c",
          "Starting from Offline (μ₀(O) = 0), how many steps until "
          "|Δ_t| < 0.01?  Use |Δ_t| = |λ₂|^t · |Δ₀| and solve for t.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "For the same chain as Q1, derive an explicit formula for the "
        "n-step transition probability p_{OO}⁽ⁿ⁾ using diagonalization.")
    p.sub("a",
          "State both eigenvalues of P.  Recall that for a 2×2 "
          "stochastic matrix, λ₁ = 1 always and λ₂ = 1 − p − q.")
    p.sub("b",
          "Using the spectral decomposition, the n-step entry is:\n"
          "  p_{OO}⁽ⁿ⁾ = π_O  +  λ₂ⁿ · π_I\n"
          "Derive this formula from first principles by writing "
          "P = π·1^T + λ₂ · (correction matrix)  and taking the nth power.")
    p.sub("c",
          "Compute p_{OO}⁽⁵⁾ exactly.  What is lim_{n→∞} p_{OO}⁽ⁿ⁾?  "
          "Verify it equals π_O from Q1.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "Two web servers are modeled as 2-state Markov chains on "
        "{Up (0), Down (1)}:")
    p.mat([
        "  Server A:   P_A = [ 0.8   0.2 ]   (p=0.2, q=0.3)",
        "                    [ 0.3   0.7 ]",
        "",
        "  Server B:   P_B = [ 0.9   0.1 ]   (p=0.1, q=0.05)",
        "                    [ 0.05  0.95]",
    ])
    p.sub("a",
          "Find the second eigenvalue λ₂ for each server.  "
          "Which server's chain converges faster to stationarity?  "
          "Why?")
    p.sub("b",
          "Find the stationary distribution for each server.  "
          "Which server has higher long-run availability (fraction of time Up)?")
    p.sub("c",
          "For each server, starting from state 0 (Up), find the minimum "
          "number of steps n such that  |p_{00}⁽ⁿ⁾ − π₀| < 0.001.  "
          "Use the formula  |p_{00}⁽ⁿ⁾ − π₀| = |λ₂|ⁿ · π₁  "
          "and compare the two servers.")

    p.save(qp(S, "Practice_1.pdf"))


def convergence_a():
    S = "Rate_of_Convergence"
    p = ExamPDF("Rate of Convergence  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Stationary distribution (p=0.4, q=0.5):")
    p.eqn(
        "π_O = q/(p+q) = 0.5/(0.4+0.5) = 0.5/0.9 = 5/9 ≈ 0.556",
        "π_I = p/(p+q) = 0.4/0.9        = 4/9 ≈ 0.444",
    )

    p.AL("b)  Convergence derivation:")
    p.txt(
        "μ_{t+1}(O) = μ_t(O)·(1−p) + μ_t(I)·q\n"
        "           = μ_t(O)·(1−p) + (1−μ_t(O))·q\n"
        "           = μ_t(O)·(1−p−q) + q\n\n"
        "Subtract π_O = q/(p+q) from both sides:")
    p.eqn(
        "Δ_{t+1} = μ_{t+1}(O) − π_O",
        "        = μ_t(O)·(1−p−q) + q − q/(p+q)",
        "        = (1−p−q)·(μ_t(O) − q/(p+q))",
        "        = (1−p−q)·Δ_t",
        "λ₂ = 1 − p − q = 1 − 0.4 − 0.5 = 0.1",
    )

    p.AL("c)  Steps needed for |Δ_t| < 0.01:")
    p.eqn(
        "Δ₀ = μ₀(O) − π_O = 0 − 5/9 = −5/9 ≈ −0.556",
        "|Δ_t| = |λ₂|^t · |Δ₀| = (0.1)^t · (5/9)",
    )
    p.txt(
        "Solve  (0.1)^t · (5/9) < 0.01:\n"
        "  (0.1)^t < 0.01 × 9/5 = 0.018\n"
        "  t · ln(0.1) < ln(0.018)\n"
        "  t > ln(0.018)/ln(0.1) = (−4.017)/(−2.303) ≈ 1.74")
    p.eqn(
        "Minimum t = 2 steps.",
        "Check: (0.1)² · (5/9) = 0.01 · 0.556 ≈ 0.0056 < 0.01  ✓",
    )
    p.txt(
        "The chain converges extremely fast because λ₂ = 0.1 is very "
        "close to 0.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Eigenvalues of P:")
    p.eqn(
        "λ₁ = 1   (every stochastic matrix has 1 as an eigenvalue)",
        "λ₂ = 1 − p − q = 1 − 0.4 − 0.5 = 0.1",
    )

    p.AL("b)  Derivation of p_{OO}⁽ⁿ⁾:")
    p.txt(
        "Decompose P into the rank-1 part (projection onto stationary dist) "
        "plus a residual:\n\n"
        "  P = Π + λ₂·(P − Π)\n\n"
        "where Π has all rows equal to π = (5/9, 4/9).  "
        "The rank-1 matrix Π satisfies Π² = Π (idempotent), and "
        "(P−Π)² = λ₂·(P−Π), so:")
    p.eqn(
        "Pⁿ = Π + λ₂ⁿ·(P − Π)",
        "",
        "Entry (O,O):  p_{OO}⁽ⁿ⁾ = π_O + λ₂ⁿ·(P_{OO} − π_O)",
        "             = 5/9 + (0.1)ⁿ·(0.6 − 5/9)",
        "             = 5/9 + (0.1)ⁿ·(0.6 − 0.556)",
        "             = 5/9 + (0.1)ⁿ·(4/9·... )",
    )
    p.txt(
        "More directly, using the standard formula for 2-state chains:\n"
        "  p_{OO}⁽ⁿ⁾ = π_O + λ₂ⁿ · π_I = 5/9 + (0.1)ⁿ · (4/9)")

    p.AL("c)  Compute p_{OO}⁽⁵⁾ and the limit:")
    p.eqn(
        "p_{OO}⁽⁵⁾ = 5/9 + (0.1)⁵ · (4/9)",
        "           = 5/9 + 0.00001 · (4/9)",
        "           ≈ 0.5556 + 0.0000044",
        "           ≈ 0.5556   (chain has essentially converged!)",
        "",
        "lim_{n→∞} p_{OO}⁽ⁿ⁾ = 5/9 = π_O  ✓",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Second eigenvalue and convergence speed:")
    p.eqn(
        "Server A:  λ₂(A) = 1 − 0.2 − 0.3 = 0.5",
        "Server B:  λ₂(B) = 1 − 0.1 − 0.05 = 0.85",
    )
    p.txt(
        "Server A converges FASTER because |λ₂(A)| = 0.5 < 0.85 = |λ₂(B)|.  "
        "A smaller |λ₂| means the deviation from stationarity shrinks more "
        "rapidly each step.  Server B has very sticky states (high self-loop "
        "probabilities 0.9 and 0.95), so it mixes slowly.")

    p.AL("b)  Stationary distributions:")
    p.eqn(
        "Server A:  π₀(A) = q/(p+q) = 0.3/0.5 = 0.6,   π₁(A) = 0.4",
        "Server B:  π₀(B) = q/(p+q) = 0.05/0.15 = 1/3 ≈ 0.333,  π₁(B) = 2/3",
    )
    p.txt(
        "Server A has higher long-run availability: 60% vs. 33.3% for Server B.  "
        "Server B fails more often relative to its repair rate.")

    p.AL("c)  Steps for |p_{00}⁽ⁿ⁾ − π₀| < 0.001:")
    p.txt("Using |p_{00}⁽ⁿ⁾ − π₀| = |λ₂|ⁿ · π₁:")
    p.eqn(
        "Server A:  (0.5)ⁿ · 0.4 < 0.001",
        "           (0.5)ⁿ < 0.0025",
        "           n > log(0.0025)/log(0.5) = 8.64   →   n ≥ 9 steps",
        "",
        "Server B:  (0.85)ⁿ · (2/3) < 0.001",
        "           (0.85)ⁿ < 0.0015",
        "           n > log(0.0015)/log(0.85) = 39.9  →   n ≥ 40 steps",
    )
    p.txt(
        "Server A converges in 9 steps; Server B needs 40 steps — over 4× longer.  "
        "This illustrates that even a modest increase in λ₂ (from 0.5 to 0.85) "
        "can dramatically slow down the mixing of the chain.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== V2  |  Folder 2026-02-26 ===")
    print("Topics: Finite Markov Chains | Stationary Distribution | "
          "Rate of Convergence\n")

    print("Generating question PDFs …")
    finite_mc_q()
    stationary_q()
    convergence_q()

    print("\nGenerating answer-key PDFs …")
    finite_mc_a()
    stationary_a()
    convergence_a()

    print("\nDone.  6 PDFs written to:")
    print(f"  {os.path.relpath(QQ, BASE)}/")
    print(f"  {os.path.relpath(AK, BASE)}/")
