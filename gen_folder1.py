#!/usr/bin/env python3
"""
CENG381 — PDF generator for folder 2026-02-26
Topics: Finite Markov Chains | Stationary Distribution | Rate of Convergence
"""
import os
from fpdf import FPDF

BASE   = "/Users/apple/Desktop/CENG381"
QQ     = os.path.join(BASE, "Generated_Questions")
AK     = os.path.join(BASE, "Answer_Keys")

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
        for ln in lines:
            self.set_x(self.l_margin + 20)
            self.cell(0, 5.5, ln, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def sep(self):
        self.ln(3)
        self.set_draw_color(160, 160, 160)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.set_draw_color(0)
        self.ln(5)

    def AL(self, text):                       # answer label (bold+underline)
        self.set_font("Helvetica", "BU", 10.5)
        self.cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 10.5)
        self.ln(1)

    def AH(self, text):                       # answer section heading
        self.set_font("Helvetica", "B", 11)
        self.multi_cell(0, 7, text)
        self.ln(1)

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.output(path)
        print(f"  Saved -> {os.path.relpath(path, BASE)}")


def qp(subj, f): return os.path.join(QQ, subj, f)
def ap(subj, f): return os.path.join(AK, subj, f)

# ══════════════════════════════════════════════════════════════════════════════
# 1.  FINITE MARKOV CHAINS
# ══════════════════════════════════════════════════════════════════════════════

def finite_mc_q():
    S = "Finite_Markov_Chains"
    p = ExamPDF("Finite Markov Chains  -  Question Set 1")
    p.add_page()

    # ── Q1 ──
    p.Q(1, 30,
        "Consider the Markov chain on states {0, 1, 2} with transition matrix:")
    p.mat(["           0      1      2",
           "  State 0 [  ?     0.4    0.2 ]",
           "  State 1 [  0.3    ?     0.3 ]",
           "  State 2 [  0.1   0.3     ?  ]"])
    p.sub("a", "Replace each '?' with the correct value so that P is a valid "
               "stochastic matrix.")
    p.sub("b", "Compute the two-step transition matrix P^(2).")
    p.sub("c", "Find p_{02}^(3), the probability of moving from state 0 to "
               "state 2 in exactly three steps.")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "A frog lives on two lily pads: East (E) and West (W). Each day it "
        "jumps to the other pad with probability p (from E) or probability q "
        "(from W), and stays with the complementary probability.")
    p.sub("a", "Write the 2x2 transition matrix P in the order (E, W).")
    p.sub("b", "Starting from E, what is the probability of being at E after "
               "exactly 2 jumps? Express your answer in terms of p and q.")
    p.sub("c", "Compute P^(2) symbolically and identify the pattern in terms "
               "of p and q. What does this suggest about the long-run behaviour?")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "A small company tracks employee satisfaction each week as one of three "
        "states: Satisfied (S), Neutral (N), or Dissatisfied (D). The weekly "
        "transition probabilities are:")
    p.mat(["  From S: stay S with prob 0.7, go to N with prob 0.2, go to D with prob 0.1",
           "  From N: go to S with prob 0.3, stay N with prob 0.5, go to D with prob 0.2",
           "  From D: go to S with prob 0.1, go to N with prob 0.4, stay D with prob 0.5"])
    p.sub("a", "Write the 3x3 transition matrix P (rows and columns in order S, N, D).")
    p.sub("b", "Starting from state N, compute the probability distribution over "
               "{S, N, D} after 2 weeks by evaluating mu_1 = (0,1,0) * P and "
               "mu_2 = mu_1 * P.")
    p.sub("c", "Apply the Chapman-Kolmogorov equation "
               "p_{ij}^(n+m) = sum_k p_{ik}^(n) * p_{kj}^(m) "
               "to find p_{SD}^(3) using your P^(2) from part (b) and the original P.")
    p.save(qp(S, "Question_Set_1.pdf"))


def finite_mc_a():
    S = "Finite_Markov_Chains"
    p = ExamPDF("Finite Markov Chains  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Each row must sum to 1.")
    p.txt("Row 0: ? = 1 - 0.4 - 0.2 = 0.4\n"
          "Row 1: ? = 1 - 0.3 - 0.3 = 0.4\n"
          "Row 2: ? = 1 - 0.1 - 0.3 = 0.6")
    p.mat(["       0      1      2",
           "  0 [  0.4   0.4   0.2 ]",
           "  1 [  0.3   0.4   0.3 ]",
           "  2 [  0.1   0.3   0.6 ]"])

    p.AL("b)  P^(2) = P * P  (p_{ij}^(2) = sum_k P_{ik} * P_{kj})")
    p.txt("p00^2 = 0.4*0.4 + 0.4*0.3 + 0.2*0.1 = 0.16+0.12+0.02 = 0.30\n"
          "p01^2 = 0.4*0.4 + 0.4*0.4 + 0.2*0.3 = 0.16+0.16+0.06 = 0.38\n"
          "p02^2 = 0.4*0.2 + 0.4*0.3 + 0.2*0.6 = 0.08+0.12+0.12 = 0.32\n"
          "p10^2 = 0.3*0.4 + 0.4*0.3 + 0.3*0.1 = 0.12+0.12+0.03 = 0.27\n"
          "p11^2 = 0.3*0.4 + 0.4*0.4 + 0.3*0.3 = 0.12+0.16+0.09 = 0.37\n"
          "p12^2 = 0.3*0.2 + 0.4*0.3 + 0.3*0.6 = 0.06+0.12+0.18 = 0.36\n"
          "p20^2 = 0.1*0.4 + 0.3*0.3 + 0.6*0.1 = 0.04+0.09+0.06 = 0.19\n"
          "p21^2 = 0.1*0.4 + 0.3*0.4 + 0.6*0.3 = 0.04+0.12+0.18 = 0.34\n"
          "p22^2 = 0.1*0.2 + 0.3*0.3 + 0.6*0.6 = 0.02+0.09+0.36 = 0.47")
    p.mat(["P^(2) =",
           "[ 0.30   0.38   0.32 ]",
           "[ 0.27   0.37   0.36 ]",
           "[ 0.19   0.34   0.47 ]"])

    p.AL("c)  p_{02}^(3) = sum_k  p_{0k}^(2) * P_{k2}")
    p.txt("= 0.30*0.2  +  0.38*0.3  +  0.32*0.6\n"
          "= 0.060 + 0.114 + 0.192\n"
          "= 0.366")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Transition matrix (E=east, W=west):")
    p.mat(["       E       W",
           "  E [  1-p     p  ]",
           "  W [   q     1-q ]"])

    p.AL("b)  p_{EE}^(2) = probability of returning to E after 2 steps starting from E:")
    p.txt("p_{EE}^(2) = P[E][E]*P[E][E] + P[E][W]*P[W][E]\n"
          "           = (1-p)^2 + p*q")

    p.AL("c)  Full P^(2):")
    p.txt("p_{EE}^(2) = (1-p)^2 + pq\n"
          "p_{EW}^(2) = (1-p)*p + p*(1-q) = p(2-p-q) = p(1 - (p+q-1))\n"
          "p_{WE}^(2) = q*(1-p) + (1-q)*q = q(2-p-q)\n"
          "p_{WW}^(2) = q*p + (1-q)^2\n\n"
          "In general P^(n) converges to the stationary distribution as n -> inf,\n"
          "meaning all rows approach the same limiting vector [pi_E, pi_W].\n"
          "This suggests that regardless of the starting state, long-run\n"
          "probabilities settle to the stationary distribution.")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Transition matrix P (order S, N, D):")
    p.mat(["       S     N     D",
           "  S [  0.7   0.2   0.1 ]",
           "  N [  0.3   0.5   0.2 ]",
           "  D [  0.1   0.4   0.5 ]"])

    p.AL("b)  Starting from N: mu_0 = (0, 1, 0)")
    p.txt("mu_1 = (0,1,0) * P = (0.3, 0.5, 0.2)\n\n"
          "mu_2 = (0.3, 0.5, 0.2) * P:\n"
          "  mu_2[S] = 0.3*0.7 + 0.5*0.3 + 0.2*0.1 = 0.21+0.15+0.02 = 0.38\n"
          "  mu_2[N] = 0.3*0.2 + 0.5*0.5 + 0.2*0.4 = 0.06+0.25+0.08 = 0.39\n"
          "  mu_2[D] = 0.3*0.1 + 0.5*0.2 + 0.2*0.5 = 0.03+0.10+0.10 = 0.23\n\n"
          "Distribution after 2 weeks: (S=0.38, N=0.39, D=0.23)")

    p.AL("c)  p_{SD}^(3) using C-K with n=2, m=1:")
    p.txt("p_{SD}^(3) = sum_k  p_{Sk}^(2) * P_{kD}\n\n"
          "First compute row S of P^(2):\n"
          "  p_{SS}^(2) = 0.7*0.7 + 0.2*0.3 + 0.1*0.1 = 0.49+0.06+0.01 = 0.56\n"
          "  p_{SN}^(2) = 0.7*0.2 + 0.2*0.5 + 0.1*0.4 = 0.14+0.10+0.04 = 0.28\n"
          "  p_{SD}^(2) = 0.7*0.1 + 0.2*0.2 + 0.1*0.5 = 0.07+0.04+0.05 = 0.16\n\n"
          "p_{SD}^(3) = p_{SS}^(2)*P[S][D] + p_{SN}^(2)*P[N][D] + p_{SD}^(2)*P[D][D]\n"
          "           = 0.56*0.1  +  0.28*0.2  +  0.16*0.5\n"
          "           = 0.056 + 0.056 + 0.080\n"
          "           = 0.192")

    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 2.  STATIONARY DISTRIBUTION
# ══════════════════════════════════════════════════════════════════════════════

def stationary_q():
    S = "Stationary_Distribution"
    p = ExamPDF("Stationary Distribution  -  Question Set 1")
    p.add_page()

    # ── Q1 ──
    p.Q(1, 30,
        "Three out of every five buses on a route are followed by a car, while "
        "only one out of every four cars is followed by a bus. Assume vehicles "
        "on the road form a Markov chain with states {Bus, Car}.")
    p.sub("a", "Set up the transition matrix P for this Markov chain.")
    p.sub("b", "Find the stationary distribution pi = (pi_B, pi_C) by solving "
               "pi * P = pi and pi_B + pi_C = 1.")
    p.sub("c", "Interpret pi_B: what fraction of vehicles on the road are buses?")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "A frog sits on two lily pads labelled E (east) and W (west). The "
        "transition matrix is:")
    p.mat(["        E      W",
           "   E [  1-p    p  ]",
           "   W [   q    1-q ]"])
    p.txt("where p, q > 0 and p + q < 1.", indent=0)
    p.sub("a", "Verify that pi(E) = q/(p+q) and pi(W) = p/(p+q) is a "
               "stationary distribution, i.e. show pi * P = pi.")
    p.sub("b", "Let M_t be the distribution at time t and M_0 = (1, 0) "
               "(starting at E). Write a recurrence for M_t and confirm that "
               "M_t -> pi as t -> infinity.")
    p.sub("c", "For p = 0.3 and q = 0.4, compute pi and find the exact value "
               "of P^(2) using the formula P^(2) = S^(-1) D^2 S where "
               "lambda_1=1 and lambda_2=1-p-q are the eigenvalues of P.")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "Consider the Markov chain with 3 states {0, 1, 2} and transition matrix:")
    p.mat(["        0      1      2",
           "   0 [  1/2   1/3   1/6 ]",
           "   1 [  1/4   1/2   1/4 ]",
           "   2 [  1/6   1/3   1/2 ]"])
    p.sub("a", "Find the stationary distribution pi = (pi_0, pi_1, pi_2) by "
               "solving pi * P = pi with pi_0 + pi_1 + pi_2 = 1.")
    p.sub("b", "Verify your answer by checking pi * P = pi directly.")
    p.sub("c", "Is this chain time-reversible? Check the detailed balance "
               "condition pi_i * P_{ij} = pi_j * P_{ji} for all pairs (i,j). "
               "What does this tell you about the long-run flow between states?")
    p.save(qp(S, "Question_Set_1.pdf"))


def stationary_a():
    S = "Stationary_Distribution"
    p = ExamPDF("Stationary Distribution  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Transition matrix:")
    p.txt("From Bus: P(Bus follows Bus) = 1 - 3/5 = 2/5,  P(Car follows Bus) = 3/5\n"
          "From Car: P(Bus follows Car) = 1/4,            P(Car follows Car) = 3/4")
    p.mat(["           Bus    Car",
           "  Bus  [  2/5    3/5  ]",
           "  Car  [  1/4    3/4  ]"])

    p.AL("b)  Solve pi * P = pi:")
    p.txt("pi_B = pi_B*(2/5) + pi_C*(1/4)\n"
          "pi_C = pi_B*(3/5) + pi_C*(3/4)\n"
          "pi_B + pi_C = 1\n\n"
          "From the first equation:\n"
          "  pi_B - (2/5)*pi_B = (1/4)*pi_C\n"
          "  (3/5)*pi_B = (1/4)*pi_C\n"
          "  pi_C = (12/5)*pi_B\n\n"
          "Substituting into pi_B + pi_C = 1:\n"
          "  pi_B + (12/5)*pi_B = 1\n"
          "  (17/5)*pi_B = 1\n"
          "  pi_B = 5/17 ~ 0.294\n"
          "  pi_C = 12/17 ~ 0.706")

    p.AL("c)  Interpretation:")
    p.txt("pi_B = 5/17 ~ 29.4% of vehicles on the road are buses in the long run.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Verify pi * P = pi:")
    p.txt("(pi*P)[E] = pi(E)*(1-p) + pi(W)*q\n"
          "          = [q/(p+q)]*(1-p) + [p/(p+q)]*q\n"
          "          = [q(1-p) + pq] / (p+q)\n"
          "          = [q - qp + pq] / (p+q)\n"
          "          = q/(p+q)  =  pi(E)  (OK)\n\n"
          "(pi*P)[W] = pi(E)*p + pi(W)*(1-q)\n"
          "          = [q/(p+q)]*p + [p/(p+q)]*(1-q)\n"
          "          = [qp + p(1-q)] / (p+q)\n"
          "          = [qp + p - pq] / (p+q)\n"
          "          = p/(p+q)  =  pi(W)  (OK)")

    p.AL("b)  Recurrence and convergence:")
    p.txt("M_t = M_{t-1} * P, so M_t = M_0 * P^t.\n"
          "Define Delta_t = mu_t(E) - q/(p+q). Then:\n"
          "  Delta_{t+1} = (1-p-q) * Delta_t\n"
          "So Delta_t = (1-p-q)^t * Delta_0.\n"
          "Since 0 < p+q < 1 (given p,q>0 and p+q<1), we have |1-p-q| < 1,\n"
          "so Delta_t -> 0, meaning M_t -> pi as t -> infinity.")

    p.AL("c)  For p=0.3, q=0.4:")
    p.txt("pi(E) = 0.4/0.7 = 4/7 ~ 0.571\n"
          "pi(W) = 0.3/0.7 = 3/7 ~ 0.429\n"
          "lambda_2 = 1 - 0.3 - 0.4 = 0.3\n\n"
          "Eigendecomposition: P = S^(-1) D S where D = diag(1, 0.3)\n"
          "P^(2) entries:\n"
          "  P^(2)_{EE} = q/(p+q) + lambda_2^2 * p/(p+q)\n"
          "             = 4/7 + (0.09)*(3/7)\n"
          "             = 4/7 + 0.27/7\n"
          "             = (4 + 0.27)/7 ~ 0.610\n"
          "  P^(2)_{EW} = p/(p+q) - lambda_2^2 * p/(p+q)\n"
          "             = 3/7 - 0.09*(3/7) ~ 0.390\n"
          "  P^(2)_{WE} ~ 4/7 - 0.09*(4/7) ~ 0.571 - 0.051 = 0.520  [check: 0.7*0.4+0.3*0.4=0.28+0.12=0.40... ]\n\n"
          "Direct computation: P^(2)_{EE} = (0.7)^2 + (0.3)(0.4) = 0.49+0.12 = 0.61\n"
          "                    P^(2)_{EW} = 0.7*0.3 + 0.3*0.6 = 0.21+0.18 = 0.39\n"
          "                    P^(2)_{WE} = 0.4*0.7 + 0.6*0.4 = 0.28+0.24 = 0.52\n"
          "                    P^(2)_{WW} = 0.4*0.3 + 0.6*0.6 = 0.12+0.36 = 0.48")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Solve pi * P = pi:")
    p.txt("pi_0*(1/2) + pi_1*(1/4) + pi_2*(1/6) = pi_0  ... (i)\n"
          "pi_0*(1/3) + pi_1*(1/2) + pi_2*(1/3) = pi_1  ... (ii)\n"
          "pi_0*(1/6) + pi_1*(1/4) + pi_2*(1/2) = pi_2  ... (iii)\n"
          "pi_0 + pi_1 + pi_2 = 1                         ... (iv)\n\n"
          "From (i): -pi_0/2 + pi_1/4 + pi_2/6 = 0  =>  -6*pi_0 + 3*pi_1 + 2*pi_2 = 0\n"
          "From (iii): pi_0/6 + pi_1/4 - pi_2/2 = 0  =>  2*pi_0 + 3*pi_1 - 6*pi_2 = 0\n\n"
          "Notice the matrix is symmetric: P_{ij} = P_{ji}, so by detailed balance\n"
          "pi_i * P_{ij} = pi_j * P_{ji} is satisfied when pi is uniform!\n\n"
          "Check: if pi_0 = pi_1 = pi_2 = 1/3, then rows of P each sum to 1\n"
          "and all columns of P each also sum to 1 (doubly stochastic).\n"
          "=> pi = (1/3, 1/3, 1/3)")

    p.AL("b)  Verification:")
    p.txt("(pi*P)[0] = (1/3)*(1/2) + (1/3)*(1/4) + (1/3)*(1/6)\n"
          "          = (1/3)*(1/2 + 1/4 + 1/6)\n"
          "          = (1/3)*(6/12 + 3/12 + 2/12)\n"
          "          = (1/3)*(11/12)  -- wait, let's recheck column sum:\n"
          "Column 0 sum: 1/2 + 1/4 + 1/6 = 6/12+3/12+2/12 = 11/12 != 1\n\n"
          "So P is NOT doubly stochastic. Solve properly:\n"
          "From equations: pi_0 = pi_2 (by symmetry of equations (i) and (iii)).\n"
          "Let pi_0 = pi_2 = x, pi_1 = y. Then 2x + y = 1.\n"
          "From (i): x/2 + y/4 + x/6 = x  =>  (3x+6y/4+2x)/6 is wrong; redo:\n"
          "  -x/2 + y/4 + x/6 = 0  => multiply by 12: -6x + 3y + 2x = 0\n"
          "  => 3y = 4x => y = 4x/3\n"
          "  2x + 4x/3 = 1 => 10x/3 = 1 => x = 3/10\n"
          "  y = 4/10 = 2/5\n\n"
          "pi = (3/10, 2/5, 3/10) = (0.30, 0.40, 0.30)")

    p.AL("c)  Detailed balance check:")
    p.txt("pi_0 * P_{01} = 0.30 * (1/3) = 0.10\n"
          "pi_1 * P_{10} = 0.40 * (1/4) = 0.10  (OK)\n\n"
          "pi_0 * P_{02} = 0.30 * (1/6) = 0.05\n"
          "pi_2 * P_{20} = 0.30 * (1/6) = 0.05  (OK)\n\n"
          "pi_1 * P_{12} = 0.40 * (1/4) = 0.10\n"
          "pi_2 * P_{21} = 0.30 * (1/3) = 0.10  (OK)\n\n"
          "Detailed balance holds => the chain is time-reversible.\n"
          "This means the long-run rate of flow from i to j equals the rate\n"
          "from j to i: the process looks the same forwards and backwards.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 3.  RATE OF CONVERGENCE
# ══════════════════════════════════════════════════════════════════════════════

def convergence_q():
    S = "Rate_of_Convergence"
    p = ExamPDF("Rate of Convergence  -  Question Set 1")
    p.add_page()

    # ── Q1 ──
    p.Q(1, 30,
        "Consider the 2-state Markov chain on {E, W} with transition matrix:")
    p.mat(["        E      W",
           "   E [  0.7    0.3 ]",
           "   W [  0.4    0.6 ]"])
    p.sub("a", "Find the stationary distribution pi = (pi_E, pi_W).")
    p.sub("b", "Define Delta_t = mu_t(E) - pi_E. Show that Delta_{t+1} = "
               "(1-p-q) * Delta_t, where p = 0.3 and q = 0.4, and identify "
               "the rate of convergence lambda_2 = 1-p-q.")
    p.sub("c", "If the chain starts at E (mu_0(E)=1), how many steps are "
               "needed until |Delta_t| < 0.01? (Use the formula Delta_t = "
               "lambda_2^t * Delta_0.)")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "A Markov chain on {0, 1} has transition matrix P with eigenvalues "
        "lambda_1 = 1 and lambda_2 = 1 - p - q. It can be diagonalized as "
        "P = S^(-1) D S, where D = diag(1, lambda_2).")
    p.sub("a", "For p = 0.2, q = 0.5, find D and write P in diagonalized form.")
    p.sub("b", "Use P = S^(-1) D S to derive an explicit formula for P^n, "
               "the n-step transition matrix.")
    p.sub("c", "Compute P^(33) for the entry p_{EE}^(33). Simplify using the "
               "formula p_{EE}^(n) = q/(p+q) + lambda_2^n * p/(p+q).")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "A lazy frog sits on two lily pads. To make the chain converge faster, "
        "we introduce a 'lazy' version: at each step, with probability 1/2 the "
        "frog stays in place (does nothing), and with probability 1/2 it follows "
        "the original transitions from matrix P below.")
    p.mat(["        E      W",
           "   E [  0.6    0.4 ]",
           "   W [  0.3    0.7 ]"])
    p.sub("a", "Write the transition matrix Q of the lazy chain as Q = (1/2)I + (1/2)P.")
    p.sub("b", "Find the eigenvalues of Q. How does lambda_2(Q) compare to lambda_2(P)?")
    p.sub("c", "The rate of convergence of the lazy chain is |lambda_2(Q)|. "
               "Is the lazy chain faster or slower to converge than the original? "
               "Why might one still prefer the lazy chain in practice (hint: think "
               "about periodicity)?")
    p.save(qp(S, "Question_Set_1.pdf"))


def convergence_a():
    S = "Rate_of_Convergence"
    p = ExamPDF("Rate of Convergence  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Stationary distribution (p=0.3, q=0.4):")
    p.txt("pi_E = q/(p+q) = 0.4/0.7 = 4/7 ~ 0.571\n"
          "pi_W = p/(p+q) = 0.3/0.7 = 3/7 ~ 0.429")

    p.AL("b)  Convergence derivation:")
    p.txt("Delta_t = mu_t(E) - pi_E\n\n"
          "mu_{t+1}(E) = mu_t(E)*(1-p) + mu_t(W)*q\n"
          "            = mu_t(E)*(1-p) + (1-mu_t(E))*q\n"
          "            = mu_t(E)*(1-p-q) + q\n\n"
          "So Delta_{t+1} = mu_{t+1}(E) - pi_E\n"
          "               = mu_t(E)*(1-p-q) + q  -  q/(p+q)\n"
          "               = (1-p-q)*mu_t(E) + q*(1 - 1/(p+q))  -- rearranged:\n"
          "               = (1-p-q)*(mu_t(E) - q/(p+q))\n"
          "               = (1-p-q)*Delta_t\n\n"
          "Rate of convergence: lambda_2 = 1 - p - q = 1 - 0.3 - 0.4 = 0.3")

    p.AL("c)  Number of steps needed:")
    p.txt("Delta_0 = mu_0(E) - pi_E = 1 - 4/7 = 3/7 ~ 0.4286\n"
          "Delta_t = (0.3)^t * (3/7)\n\n"
          "We need (0.3)^t * (3/7) < 0.01\n"
          "  (0.3)^t < 0.01 * 7/3 = 0.0233\n"
          "  t * ln(0.3) < ln(0.0233)\n"
          "  t > ln(0.0233)/ln(0.3) = (-3.757)/(-1.204) ~ 3.12\n\n"
          "So t >= 4 steps are sufficient. Verify:\n"
          "  t=4: (0.3)^4 * 3/7 = 0.0081 * 0.4286 ~ 0.0035 < 0.01  (OK)")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  For p=0.2, q=0.5:")
    p.txt("lambda_1 = 1,   lambda_2 = 1 - 0.2 - 0.5 = 0.3\n"
          "D = diag(1, 0.3)\n\n"
          "Eigenvector for lambda_1=1: stationary dist row = [q/(p+q), p/(p+q)]\n"
          "  = [0.5/0.7, 0.2/0.7] = [5/7, 2/7]\n"
          "Eigenvector for lambda_2=0.3: [p, -q] direction (up to scaling) = [1, -1]\n\n"
          "S = [ q/(p+q)   p/(p+q) ] = [ 5/7   2/7 ]\n"
          "    [    1         -1   ]   [  1     -1  ]")

    p.AL("b)  Explicit P^n formula:")
    p.txt("P^n = S^(-1) * D^n * S\n\n"
          "This gives:\n"
          "  p_{EE}^(n) = q/(p+q)  +  lambda_2^n * p/(p+q)\n"
          "  p_{EW}^(n) = p/(p+q)  -  lambda_2^n * p/(p+q)\n"
          "  p_{WE}^(n) = q/(p+q)  -  lambda_2^n * q/(p+q)\n"
          "  p_{WW}^(n) = p/(p+q)  +  lambda_2^n * q/(p+q)\n\n"
          "As n->inf, lambda_2^n -> 0, so all rows converge to [q/(p+q), p/(p+q)].")

    p.AL("c)  P^(33)_{EE} for p=0.2, q=0.5:")
    p.txt("p_{EE}^(33) = q/(p+q) + lambda_2^33 * p/(p+q)\n"
          "            = 5/7 + (0.3)^33 * (2/7)\n\n"
          "(0.3)^33 is extremely small (~ 5.6 x 10^(-18)), so:\n"
          "p_{EE}^(33) ~ 5/7 ~ 0.7143 (the chain has essentially converged)")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Lazy chain Q = (1/2)I + (1/2)P:")
    p.mat(["         E       W",
           "   E [  0.80    0.20 ]",
           "   W [  0.15    0.85 ]"])
    p.txt("Check: 0.5*1 + 0.5*0.6 = 0.8, 0.5*0 + 0.5*0.4 = 0.2  (OK)")

    p.AL("b)  Eigenvalues of Q:")
    p.txt("lambda_1(Q) = 1  (every stochastic matrix has eigenvalue 1)\n"
          "lambda_2(Q) = (1/2)*1 + (1/2)*lambda_2(P)\n"
          "            = 1/2 + (1/2)*(1 - 0.4 - 0.3)\n"
          "            = 1/2 + (1/2)*(0.3)\n"
          "            = 1/2 + 0.15 = 0.65\n\n"
          "Original lambda_2(P) = 1 - 0.4 - 0.3 = 0.3\n"
          "Lazy chain lambda_2(Q) = 0.65 > 0.3")

    p.AL("c)  Comparison and motivation:")
    p.txt("The lazy chain (lambda_2=0.65) converges SLOWER than the original\n"
          "(lambda_2=0.30), because the step size is halved each iteration.\n\n"
          "However, the key advantage is APERIODICITY. A chain with period d>1\n"
          "does not converge to pi (it oscillates). Adding self-loops (laziness)\n"
          "breaks any periodic structure, guaranteeing aperiodicity and hence\n"
          "true convergence to pi. The tradeoff is slower (but guaranteed)\n"
          "convergence vs. possible non-convergence without laziness.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== Folder 2026-02-26: Finite MC | Stationary Dist | Rate of Convergence ===\n")
    print("Generating Question Sets...")
    finite_mc_q()
    stationary_q()
    convergence_q()

    print("\nGenerating Answer Keys...")
    finite_mc_a()
    stationary_a()
    convergence_a()

    print("\nDone. 6 PDFs created.")
