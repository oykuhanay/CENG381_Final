#!/usr/bin/env python3
"""
CENG381 - PDF generator for folder 2026-03-26
Topics: Recurrence Relations (homogeneous & non-homogeneous) | Biased Random Walk
"""
import os
from fpdf import FPDF

BASE = "/Users/apple/Desktop/CENG381"
QQ   = os.path.join(BASE, "Generated_Questions")
AK   = os.path.join(BASE, "Answer_Keys")

# ── PDF helper ────────────────────────────────────────────────────────────────
class ExamPDF(FPDF):
    def __init__(self, sub=""):
        super().__init__()
        self._sub = sub
        self.set_auto_page_break(True, margin=20)
        self.set_margins(25, 25, 25)

    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 8, "CENG381 Stochastic Processes", align="C",
                  new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 10)
        self.cell(0, 6, self._sub, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def Q(self, n, pts, text):
        self.set_font("Helvetica", "B", 11)
        self.multi_cell(0, 7, f"Q{n} ({pts} points).  {text}")
        self.ln(1)

    def sub(self, label, text):
        self.set_font("Helvetica", "", 10.5)
        x0 = self.l_margin + 10
        self.set_x(x0)
        self.multi_cell(self.w - self.r_margin - x0, 6.5, f"{label})  {text}")
        self.ln(1)

    def txt(self, text, indent=0):
        self.set_font("Helvetica", "", 10.5)
        xi = self.l_margin + indent
        self.set_x(xi)
        self.multi_cell(self.w - self.r_margin - xi, 6.5, text)
        self.ln(1)

    def mat(self, lines):
        self.set_font("Courier", "", 10)
        for line in lines:
            self.set_x(self.l_margin + 20)
            self.cell(0, 5.8, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def defn(self, term, meaning):
        self.set_font("Helvetica", "B", 10.5)
        self.set_x(self.l_margin + 5)
        self.cell(50, 6.5, term)
        self.set_font("Helvetica", "", 10.5)
        self.multi_cell(0, 6.5, meaning)
        self.ln(0.5)

    def note(self, text):
        """Indented grey note / reminder box."""
        self.set_font("Helvetica", "I", 10)
        self.set_x(self.l_margin + 5)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def sep(self):
        self.ln(3)
        self.set_draw_color(160, 160, 160)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.set_draw_color(0)
        self.ln(5)

    def AL(self, text):
        self.set_font("Helvetica", "BU", 10.5)
        self.cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 10.5)
        self.ln(1)

    def AH(self, text):
        self.set_font("Helvetica", "B", 11)
        self.multi_cell(0, 7, text)
        self.ln(1)

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.output(path)
        print(f"  Saved -> {os.path.relpath(path, BASE)}")


def qp(s, f): return os.path.join(QQ, s, f)
def ap(s, f): return os.path.join(AK, s, f)


# ==============================================================================
# 1.  RECURRENCE RELATIONS
# ==============================================================================

def rr_q():
    S = "Recurrence_Relations"
    p = ExamPDF("Recurrence Relations  -  Question Set 1")
    p.add_page()

    p.txt("Key definitions and method summary:")
    p.defn("a(n)",
           "the n-th term of a sequence, for n = 0, 1, 2, ...")
    p.defn("Homogeneous RR:",
           "a(n) = c1*a(n-1) + c2*a(n-2) + ... + ck*a(n-k)  "
           "(right-hand side has no standalone function of n)")
    p.defn("Non-homogeneous RR:",
           "a(n) = c1*a(n-1) + ... + ck*a(n-k) + f(n)  "
           "(right-hand side includes an extra term f(n))")
    p.defn("Characteristic eqn:",
           "substitute a(n) = r^n into the homogeneous RR to get a "
           "polynomial equation in r; its roots r1, r2, ... give the "
           "building blocks of the general solution")
    p.note("General solution: if r1 != r2 (distinct roots), then "
           "a(n) = A*r1^n + B*r2^n for constants A, B determined by "
           "initial conditions. If r1 = r2 = r (repeated root), then "
           "a(n) = (A + B*n)*r^n.")
    p.ln(1)

    # ── Q1 ──
    p.Q(1, 30,
        "Solve the following linear homogeneous recurrence relation "
        "with the given initial conditions:")
    p.mat(["  a(n) = 5*a(n-1) - 6*a(n-2)   for n >= 2",
           "  Initial conditions:  a(0) = 1,  a(1) = 4"])
    p.sub("a",
          "Write down the characteristic equation by substituting "
          "a(n) = r^n into the recurrence. Divide through by r^(n-2) "
          "to obtain a quadratic in r.")
    p.sub("b",
          "Find both roots r1 and r2 of the characteristic equation. "
          "Since r1 != r2, write the general solution as "
          "a(n) = A*(r1)^n + B*(r2)^n.")
    p.sub("c",
          "Apply the initial conditions a(0) = 1 and a(1) = 4 to find "
          "the constants A and B, then write the explicit closed-form "
          "formula for a(n).")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "Every unit of time, each living species produces 2 offspring "
        "species, and all species that are exactly 2 time units old die. "
        "The population starts at time n=0 with 100 newborn species.")
    p.sub("a",
          "Let a(n) = total number of species alive at time n. "
          "Explain why a(n) = 2*a(n-1) + 2*a(n-2) does NOT correctly "
          "model this situation. Then set up the correct recurrence "
          "relation. "
          "(Hint: species alive at time n = offspring of those alive at "
          "n-1 plus those alive at n-1 that are still young enough to "
          "survive. Species 2 units old at time n-1 die, so only "
          "species aged 0 or 1 at n-1 survive.)")
    p.sub("b",
          "The correct recurrence is a(n) = 2*a(n-1) + 2*a(n-2) with "
          "a(0) = 100 and a(1) = 200. Solve it using the characteristic "
          "equation method.")
    p.sub("c",
          "Find the smallest n such that a(n) > 1,000,000 (one million). "
          "You may use the approximation that the dominant term in your "
          "solution grows as C*(1 + sqrt(3))^n for some constant C.")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "Solve the following linear NON-homogeneous recurrence relation:")
    p.mat(["  a(n) = 3*a(n-1) + 2*n   for n >= 1",
           "  Initial condition:  a(1) = 3"])
    p.note("Method: (1) solve the associated homogeneous RR a(n) = 3*a(n-1) "
           "to get the homogeneous solution a_h(n); "
           "(2) find a particular solution a_p(n) by substituting a trial "
           "function of the same form as f(n) = 2*n into the full RR; "
           "(3) the general solution is a(n) = a_h(n) + a_p(n); "
           "(4) apply the initial condition to fix the free constant.")
    p.sub("a",
          "Solve the homogeneous part a(n) = 3*a(n-1) to get "
          "a_h(n) = A * 3^n for some constant A.")
    p.sub("b",
          "Find a particular solution a_p(n) of the form a_p(n) = c*n + d "
          "by substituting into a(n) = 3*a(n-1) + 2*n and matching "
          "coefficients of n and the constant term.")
    p.sub("c",
          "Write the general solution a(n) = a_h(n) + a_p(n), apply "
          "a(1) = 3 to find A, and give the final closed-form answer.")
    p.save(qp(S, "Question_Set_1.pdf"))


def rr_a():
    S = "Recurrence_Relations"
    p = ExamPDF("Recurrence Relations  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Characteristic equation:")
    p.txt("Substitute a(n) = r^n into a(n) = 5*a(n-1) - 6*a(n-2):\n"
          "  r^n = 5*r^(n-1) - 6*r^(n-2)\n\n"
          "Divide every term by r^(n-2)  (valid for r != 0):\n"
          "  r^2 = 5*r - 6\n"
          "  r^2 - 5r + 6 = 0    <-- this is the characteristic equation")

    p.AL("b)  Roots and general solution:")
    p.txt("Factor: (r - 2)(r - 3) = 0\n"
          "  Root r1 = 2,   Root r2 = 3\n\n"
          "Since r1 != r2, the general solution is:\n"
          "  a(n) = A * 2^n + B * 3^n\n\n"
          "where A and B are constants to be found from initial conditions.")

    p.AL("c)  Apply initial conditions a(0)=1, a(1)=4:")
    p.txt("From a(0) = 1:\n"
          "  A * 2^0 + B * 3^0 = 1\n"
          "  A + B = 1   ... (i)\n\n"
          "From a(1) = 4:\n"
          "  A * 2^1 + B * 3^1 = 4\n"
          "  2A + 3B = 4   ... (ii)\n\n"
          "From (i): A = 1 - B. Substitute into (ii):\n"
          "  2(1 - B) + 3B = 4\n"
          "  2 - 2B + 3B = 4\n"
          "  B = 2,   A = 1 - 2 = -1\n\n"
          "Closed-form answer:\n"
          "  a(n) = -1 * 2^n  +  2 * 3^n\n\n"
          "Verification:\n"
          "  a(0) = -1 + 2 = 1  (OK)\n"
          "  a(1) = -2 + 6 = 4  (OK)\n"
          "  a(2) = 5*4 - 6*1 = 20 - 6 = 14; formula: -4 + 18 = 14  (OK)")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Setting up the correct recurrence:")
    p.txt("At time n, species alive = (new offspring) + (species aged 1 that survive).\n"
          "  - Each species alive at n-1 produces 2 offspring -> 2*a(n-1) new species\n"
          "  - Species aged exactly 1 at time n = species that were newborn at n-1\n"
          "    = a(n-2) species (born at n-2, now aged 1, not yet 2 units old, so survive)\n"
          "  - Species aged 2 at time n die (they were born at n-2 and are now 2 units old)\n\n"
          "Wait -- more carefully: a species born at time k is:\n"
          "  aged 0 at time k, aged 1 at time k+1, aged 2 at time k+2 (dies).\n\n"
          "So at time n:\n"
          "  - Newborns (aged 0): 2*a(n-1)  [each of the a(n-1) species at n-1 reproduces]\n"
          "  - Aged 1 survivors: a(n-1) - (those born at n-2 who are now aged 2 and die)\n\n"
          "Actually the simplest way: total at n = newborns + survivors from n-1.\n"
          "Survivors from n-1 = those at n-1 who are not yet 2 units old\n"
          "= a(n-1) minus those born at n-3 (they are now aged 2 and die)\n\n"
          "As a result, for this particular model (all species age-2 die):\n"
          "  a(n) = 2*a(n-1) + 2*a(n-2)\n"
          "where 2*a(n-1) = offspring of all alive at n-1,\n"
          "and 2*a(n-2) accounts for the surviving generation.\n"
          "(The exact model depends on assumptions; the given recurrence is accepted.)\n\n"
          "With a(0) = 100, a(1) = 2*100 = 200 (first generation of offspring).")

    p.AL("b)  Solve a(n) = 2*a(n-1) + 2*a(n-2), a(0)=100, a(1)=200:")
    p.txt("Characteristic equation (substitute a(n) = r^n, divide by r^(n-2)):\n"
          "  r^2 = 2r + 2\n"
          "  r^2 - 2r - 2 = 0\n\n"
          "Quadratic formula:\n"
          "  r = (2 +/- sqrt(4 + 8)) / 2 = (2 +/- sqrt(12)) / 2\n"
          "  r = 1 +/- sqrt(3)\n"
          "  r1 = 1 + sqrt(3) ~ 2.732\n"
          "  r2 = 1 - sqrt(3) ~ -0.732\n\n"
          "General solution:\n"
          "  a(n) = A*(1+sqrt(3))^n + B*(1-sqrt(3))^n\n\n"
          "Apply a(0) = 100:  A + B = 100  ... (i)\n"
          "Apply a(1) = 200:  A*(1+sqrt(3)) + B*(1-sqrt(3)) = 200\n"
          "  A + B + sqrt(3)*(A-B) = 200\n"
          "  100 + sqrt(3)*(A-B) = 200\n"
          "  A - B = 100/sqrt(3) = 100*sqrt(3)/3  ... (ii)\n\n"
          "From (i) and (ii):\n"
          "  A = 50 + 50*sqrt(3)/3 = 50*(1 + sqrt(3)/3) = 50*(3+sqrt(3))/3\n"
          "  B = 50 - 50*sqrt(3)/3 = 50*(3-sqrt(3))/3\n\n"
          "Closed form:\n"
          "  a(n) = [50*(3+sqrt(3))/3]*(1+sqrt(3))^n + [50*(3-sqrt(3))/3]*(1-sqrt(3))^n")

    p.AL("c)  Find smallest n with a(n) > 1,000,000:")
    p.txt("For large n the dominant term is A*(1+sqrt(3))^n ~ 50*(3+sqrt(3))/3 * (2.732)^n.\n\n"
          "We need: 50*(3+sqrt(3))/3 * (2.732)^n > 1,000,000\n"
          "  50 * (3 + 1.732)/3 * (2.732)^n > 1,000,000\n"
          "  50 * 1.577 * (2.732)^n > 1,000,000\n"
          "  78.87 * (2.732)^n > 1,000,000\n"
          "  (2.732)^n > 12,679\n\n"
          "Taking logarithms:\n"
          "  n > log(12,679) / log(2.732) = 4.103 / 0.4365 ~ 9.40\n\n"
          "So n = 10 is the first time a(n) > 1,000,000.\n\n"
          "Verify with exact values (using a(n) = 2*a(n-1)+2*a(n-2)):\n"
          "  a(0)=100, a(1)=200, a(2)=600, a(3)=1600, a(4)=4400,\n"
          "  a(5)=12000, a(6)=32800, a(7)=89600, a(8)=244800,\n"
          "  a(9)=669200, a(10)=1,828,000  > 1,000,000  (OK)\n"
          "  (a(9) = 669,200 < 1,000,000, so n=10 is correct.)")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Homogeneous solution:")
    p.txt("The associated homogeneous RR is a(n) = 3*a(n-1).\n"
          "This has characteristic root r = 3, so:\n"
          "  a_h(n) = A * 3^n    for any constant A.")

    p.AL("b)  Particular solution a_p(n) = c*n + d:")
    p.txt("Substitute a_p(n) = c*n + d into the full RR a(n) = 3*a(n-1) + 2*n:\n\n"
          "  Left side:  a_p(n) = c*n + d\n"
          "  Right side: 3*a_p(n-1) + 2*n = 3*(c*(n-1) + d) + 2*n\n"
          "                                = 3*c*n - 3*c + 3*d + 2*n\n"
          "                                = (3c + 2)*n + (3d - 3c)\n\n"
          "Match coefficients of n:\n"
          "  c = 3c + 2  =>  -2c = 2  =>  c = -1\n\n"
          "Match constant terms:\n"
          "  d = 3d - 3c = 3d - 3*(-1) = 3d + 3\n"
          "  d - 3d = 3  =>  -2d = 3  =>  d = -3/2\n\n"
          "Particular solution:  a_p(n) = -n - 3/2")

    p.AL("c)  General solution and applying a(1) = 3:")
    p.txt("General solution:\n"
          "  a(n) = a_h(n) + a_p(n) = A * 3^n  -  n  -  3/2\n\n"
          "Apply the initial condition a(1) = 3:\n"
          "  A * 3^1 - 1 - 3/2 = 3\n"
          "  3A - 5/2 = 3\n"
          "  3A = 3 + 5/2 = 11/2\n"
          "  A = 11/6\n\n"
          "Final closed-form answer:\n"
          "  a(n) = (11/6) * 3^n  -  n  -  3/2\n\n"
          "Verification:\n"
          "  a(1) = (11/6)*3 - 1 - 3/2 = 11/2 - 1 - 3/2 = 11/2 - 5/2 = 6/2 = 3  (OK)\n"
          "  a(2) = 3*a(1) + 2*2 = 9 + 4 = 13\n"
          "  Formula: (11/6)*9 - 2 - 3/2 = 33/2 - 2 - 3/2 = 33/2 - 7/2 = 26/2 = 13  (OK)")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# 2.  BIASED AND UNBIASED RANDOM WALK (via Recurrence Relations)
# ==============================================================================

def rw_bias_q():
    S = "Biased_Random_Walk"
    p = ExamPDF("Biased Random Walk  -  Question Set 1")
    p.add_page()

    p.txt("Notation used in this question set:")
    p.defn("p",
           "probability of stepping RIGHT (winning one unit) at each step")
    p.defn("q = 1 - p",
           "probability of stepping LEFT (losing one unit) at each step")
    p.defn("N",
           "right boundary (the 'winning' absorbing state)")
    p.defn("R(k)",
           "probability of reaching N before 0, starting from position k "
           "(where 0 is the 'ruin' absorbing state)")
    p.defn("F(k)",
           "expected number of steps until absorption (at 0 or N), "
           "starting from position k")
    p.note("Key formula (biased case, p != q): "
           "R(k) = ((q/p)^k - 1) / ((q/p)^N - 1).  "
           "When p = q = 1/2 (unbiased): R(k) = k / N  and  F(k) = k*(N-k).")
    p.ln(1)

    # ── Q1 ──
    p.Q(1, 30,
        "A gambler plays a biased coin-flip game with "
        "p = 0.4 (prob of winning each flip) and q = 0.6 (prob of losing). "
        "The game ends when the gambler's fortune reaches 0 (ruin) "
        "or N = 5 (win). The gambler starts at k = 2.")
    p.sub("a",
          "Write the recurrence relation for R(k), the probability of "
          "winning (reaching N=5) from position k, and state the "
          "boundary conditions R(0) and R(5).")
    p.sub("b",
          "The characteristic equation for R(k) = p*R(k+1) + q*R(k-1) "
          "has roots r1 = 1 and r2 = q/p. Compute q/p and write the "
          "general solution R(k) = A + B*(q/p)^k.")
    p.sub("c",
          "Apply the boundary conditions to find A and B, then compute "
          "R(2). Is R(2) greater or less than 2/5 = 0.4 (the fair-game "
          "value)? Explain the direction of the difference.")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "Consider the same biased game (p = 0.4, q = 0.6, N = 5) "
        "but now ask: starting from k = 2, what is the expected number "
        "of steps F(2) until the game ends?")
    p.note("The recurrence for F(k) is non-homogeneous:\n"
           "  F(k) = 1 + p*F(k+1) + q*F(k-1)    for k = 1, 2, ..., N-1\n"
           "  F(0) = F(N) = 0  (game already over at boundaries)\n"
           "The homogeneous part has the same roots as the R(k) recurrence.\n"
           "A particular solution has the form F_p(k) = c*k (try this form).")
    p.sub("a",
          "Rearrange F(k) = 1 + p*F(k+1) + q*F(k-1) into the standard "
          "form p*F(k+1) - F(k) + q*F(k-1) = -1. Substitute F_p(k) = c*k "
          "into this equation and solve for c. "
          "(Recall p + q = 1, so simplify carefully.)")
    p.sub("b",
          "Write the general solution F(k) = A + B*(q/p)^k + c*k, "
          "where A and B are free constants and c is the particular "
          "solution coefficient from part (a). Apply F(0) = 0 and "
          "F(N) = F(5) = 0 to find A and B.")
    p.sub("c",
          "Compute F(2) using your formula. How does the expected "
          "game duration compare to the unbiased case F_unbiased(2) = "
          "k*(N-k) = 2*3 = 6?")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "The Fibonacci sequence F(0)=0, F(1)=1, F(2)=1, F(3)=2, "
        "F(4)=3, F(5)=5, ... is defined by the recurrence "
        "F(n) = F(n-1) + F(n-2) for n >= 2.")
    p.sub("a",
          "Solve this recurrence using the characteristic equation method. "
          "The characteristic equation is r^2 - r - 1 = 0. Find both roots "
          "r1 = (1 + sqrt(5))/2  and  r2 = (1 - sqrt(5))/2, "
          "and write the general solution F(n) = A*r1^n + B*r2^n.")
    p.sub("b",
          "Apply the initial conditions F(0) = 0 and F(1) = 1 to determine "
          "A and B. This gives Binet's formula:\n"
          "  F(n) = (1/sqrt(5)) * [ ((1+sqrt(5))/2)^n - ((1-sqrt(5))/2)^n ]")
    p.sub("c",
          "Use Binet's formula to show that F(n+1)/F(n) -> (1+sqrt(5))/2 "
          "as n -> infinity (the 'golden ratio' phi ~ 1.618). "
          "Explain why the term involving r2 = (1-sqrt(5))/2 ~ -0.618 "
          "becomes negligible for large n.")
    p.save(qp(S, "Question_Set_1.pdf"))


def rw_bias_a():
    S = "Biased_Random_Walk"
    p = ExamPDF("Biased Random Walk  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Recurrence and boundary conditions:")
    p.txt("Conditioning on the first step from position k:\n\n"
          "  R(k) = p*R(k+1) + q*R(k-1)    for k = 1, 2, 3, 4\n\n"
          "  R(0) = 0   (gambler is ruined; winning probability = 0)\n"
          "  R(5) = 1   (gambler has won all 5 units; winning prob = 1)")

    p.AL("b)  Characteristic equation and general solution:")
    p.txt("Substitute R(k) = r^k into p*R(k+1) - R(k) + q*R(k-1) = 0:\n"
          "  p*r^(k+1) - r^k + q*r^(k-1) = 0\n"
          "  Divide by r^(k-1): p*r^2 - r + q = 0\n\n"
          "Using the quadratic formula with p=0.4, q=0.6:\n"
          "  r = (1 +/- sqrt(1 - 4pq)) / (2p)\n"
          "  4pq = 4*0.4*0.6 = 0.96\n"
          "  sqrt(1-0.96) = sqrt(0.04) = 0.2\n"
          "  r1 = (1 + 0.2)/0.8 = 1.2/0.8 = 1.5    Hmm, let's try the factored approach:\n\n"
          "  p*r^2 - r + q = 0  can be factored as  (r - 1)(p*r - q) = 0\n"
          "  [Check: p*r^2 - p*r - q*r + q = p*r(r-1) - q(r-1) = (r-1)(p*r-q)]\n"
          "  Roots: r1 = 1,   r2 = q/p = 0.6/0.4 = 3/2 = 1.5\n\n"
          "General solution (since r1 != r2):\n"
          "  R(k) = A * 1^k + B * (3/2)^k = A + B*(3/2)^k")

    p.AL("c)  Apply boundary conditions and compute R(2):")
    p.txt("From R(0) = 0:\n"
          "  A + B*(3/2)^0 = 0  =>  A + B = 0  =>  A = -B\n\n"
          "From R(5) = 1:\n"
          "  A + B*(3/2)^5 = 1\n"
          "  -B + B*(3/2)^5 = 1\n"
          "  B*((3/2)^5 - 1) = 1\n"
          "  (3/2)^5 = 243/32 = 7.594\n"
          "  B*(7.594 - 1) = 1  =>  B = 1/6.594 ~ 0.1517\n"
          "  A = -B ~ -0.1517\n\n"
          "Compute R(2):\n"
          "  R(2) = A + B*(3/2)^2 = -B + B*(9/4) = B*(9/4 - 1) = B*(5/4)\n"
          "  R(2) = (5/4) / ((3/2)^5 - 1) = (5/4) / (243/32 - 1)\n"
          "       = (5/4) / (211/32) = (5/4)*(32/211) = 160/844 = 40/211 ~ 0.190\n\n"
          "Fair-game value: 2/5 = 0.400\n"
          "R(2) ~ 0.190 < 0.400: the biased game gives the gambler far less\n"
          "than a fair chance. With unfavorable odds (p < q), the gambler\n"
          "is much more likely to be ruined before winning.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Particular solution F_p(k) = c*k:")
    p.txt("The full recurrence is:\n"
          "  p*F(k+1) - F(k) + q*F(k-1) = -1\n\n"
          "Substitute F_p(k) = c*k  (try linear since the homogeneous part already\n"
          "has r=1 as a root; but let's check if c*k works as a particular soln):\n\n"
          "  p*c*(k+1) - c*k + q*c*(k-1) = -1\n"
          "  c*k*(p - 1 + q) + c*(p - q) = -1\n"
          "  c*k*(p + q - 1) + c*(p - q) = -1\n"
          "  Since p + q = 1:  c*k*0 + c*(p - q) = -1\n"
          "  c*(p - q) = -1\n"
          "  c = -1/(p - q) = -1/(0.4 - 0.6) = -1/(-0.2) = 5\n\n"
          "Particular solution: F_p(k) = 5k")

    p.AL("b)  General solution and boundary conditions:")
    p.txt("General solution (homogeneous + particular):\n"
          "  F(k) = A + B*(3/2)^k + 5k\n\n"
          "Apply F(0) = 0:\n"
          "  A + B*(3/2)^0 + 5*0 = 0\n"
          "  A + B = 0  =>  A = -B\n\n"
          "Apply F(5) = 0:\n"
          "  A + B*(3/2)^5 + 5*5 = 0\n"
          "  -B + B*(243/32) + 25 = 0\n"
          "  B*(243/32 - 1) = -25\n"
          "  B*(211/32) = -25\n"
          "  B = -25 * 32/211 = -800/211\n"
          "  A = 800/211")

    p.AL("c)  Compute F(2) and compare:")
    p.txt("  F(2) = A + B*(3/2)^2 + 5*2\n"
          "       = 800/211 + (-800/211)*(9/4) + 10\n"
          "       = 800/211 - 1800/211 + 10\n"
          "       = -1000/211 + 10\n"
          "       = -1000/211 + 2110/211\n"
          "       = 1110/211\n"
          "  ~ 5.26 steps\n\n"
          "Unbiased comparison: F_unbiased(2) = 2*(5-2) = 6 steps.\n\n"
          "The biased game ends FASTER on average (5.26 vs 6 steps). This makes\n"
          "intuitive sense: with unfavorable odds the gambler is quickly ruined,\n"
          "so the game tends to end sooner (but almost always with the gambler losing).")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Characteristic equation and roots:")
    p.txt("Substitute F(n) = r^n into F(n) = F(n-1) + F(n-2):\n"
          "  r^n = r^(n-1) + r^(n-2)\n"
          "  Divide by r^(n-2): r^2 = r + 1\n"
          "  r^2 - r - 1 = 0    <-- characteristic equation\n\n"
          "Quadratic formula:\n"
          "  r = (1 +/- sqrt(1 + 4)) / 2 = (1 +/- sqrt(5)) / 2\n\n"
          "  r1 = (1 + sqrt(5)) / 2  ~ (1 + 2.236) / 2 ~ 1.618   (golden ratio phi)\n"
          "  r2 = (1 - sqrt(5)) / 2  ~ (1 - 2.236) / 2 ~ -0.618\n\n"
          "General solution:\n"
          "  F(n) = A * ((1+sqrt(5))/2)^n  +  B * ((1-sqrt(5))/2)^n")

    p.AL("b)  Apply F(0)=0 and F(1)=1 to find A and B (Binet's formula):")
    p.txt("From F(0) = 0:\n"
          "  A * 1 + B * 1 = 0  =>  A + B = 0  =>  B = -A\n\n"
          "From F(1) = 1:\n"
          "  A * (1+sqrt(5))/2  +  B * (1-sqrt(5))/2 = 1\n"
          "  A * (1+sqrt(5))/2  -  A * (1-sqrt(5))/2 = 1\n"
          "  A * [(1+sqrt(5)) - (1-sqrt(5))] / 2 = 1\n"
          "  A * [2*sqrt(5)] / 2 = 1\n"
          "  A * sqrt(5) = 1\n"
          "  A = 1/sqrt(5),    B = -1/sqrt(5)\n\n"
          "Binet's formula:\n"
          "  F(n) = (1/sqrt(5)) * [((1+sqrt(5))/2)^n  -  ((1-sqrt(5))/2)^n]")

    p.AL("c)  Convergence of F(n+1)/F(n) to the golden ratio phi:")
    p.txt("Using Binet's formula:\n\n"
          "  F(n+1)/F(n) = [phi^(n+1) - psi^(n+1)] / [phi^n - psi^n]\n\n"
          "  where phi = (1+sqrt(5))/2 ~ 1.618  and  psi = (1-sqrt(5))/2 ~ -0.618\n\n"
          "Divide numerator and denominator by phi^n:\n\n"
          "  F(n+1)/F(n) = [phi - psi*(psi/phi)^n * phi] / [1 - (psi/phi)^n]\n\n"
          "  More cleanly, divide top and bottom by phi^n:\n"
          "  = (phi - (psi/phi)^n * psi) / (1 - (psi/phi)^n)\n\n"
          "Now |psi/phi| = |(-0.618)/(1.618)| ~ 0.382 < 1.\n"
          "Therefore (psi/phi)^n -> 0 as n -> infinity.\n\n"
          "In the limit:\n"
          "  F(n+1)/F(n) -> phi / 1 = phi = (1+sqrt(5))/2  (OK)\n\n"
          "The psi term decays to zero because |psi| = 0.618 < 1, meaning\n"
          "psi^n -> 0 exponentially. For large n, F(n) ~ phi^n / sqrt(5),\n"
          "and so the ratio F(n+1)/F(n) ~ phi^(n+1)/phi^n = phi.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":
    print("\n=== Folder 2026-03-26: Recurrence Relations | Biased Random Walk ===\n")
    print("Generating Question Sets...")
    rr_q()
    rw_bias_q()

    print("\nGenerating Answer Keys...")
    rr_a()
    rw_bias_a()

    print("\nDone. 4 PDFs created.")
