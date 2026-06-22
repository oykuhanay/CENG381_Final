#!/usr/bin/env python3
"""
CENG381 - 5 Mixed Exam PDFs + Answer Keys
Improved notation: gray-background equation blocks, colored definition bars,
parenthetical subscripts throughout (S(n) not S_n).
"""
import os
from fpdf import FPDF

BASE = "/Users/apple/Desktop/CENG381"
ME   = os.path.join(BASE, "Mixed_Exams")
MAK  = os.path.join(BASE, "Mixed_Exam_Answer_Keys")

# ── PDF helper (improved notation) ───────────────────────────────────────────
class ExamPDF(FPDF):
    def __init__(self, sub=""):
        super().__init__()
        self._sub = sub
        self.set_auto_page_break(True, margin=20)
        self.set_margins(25, 25, 25)

    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 8, "CENG381 Stochastic Processes  --  Mixed Exam",
                  align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 10)
        self.cell(0, 6, self._sub, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    # ── core text ──
    def Q(self, n, pts, text):
        self.set_font("Helvetica", "B", 11)
        self.multi_cell(0, 7, f"Q{n}  ({pts} points).  {text}")
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

    # ── IMPROVED: gray-background Courier equation block ──
    def eqn(self, *lines):
        """One or more formula lines rendered in Courier on a light-gray background."""
        self.set_fill_color(242, 242, 242)
        self.set_font("Courier", "", 10.5)
        xi = self.l_margin + 12
        avail = self.w - self.r_margin - xi
        for line in lines:
            self.set_x(xi)
            self.multi_cell(avail, 6.5, line, fill=True)
        self.set_fill_color(255, 255, 255)
        self.ln(3)

    # ── IMPROVED: matrix block ──
    def mat(self, lines):
        self.set_font("Courier", "", 10)
        for line in lines:
            self.set_x(self.l_margin + 22)
            self.cell(0, 5.8, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    # ── IMPROVED: notation definition with blue left bar ──
    def defn(self, term, meaning):
        y0 = self.get_y()
        self.set_font("Helvetica", "B", 10.5)
        self.set_x(self.l_margin + 8)
        tw = 56
        self.cell(tw, 6.5, term)
        self.set_font("Helvetica", "", 10.5)
        avail = self.w - self.r_margin - (self.l_margin + 8 + tw)
        self.multi_cell(avail, 6.5, meaning)
        y1 = self.get_y()
        # blue left bar
        self.set_draw_color(60, 100, 200)
        old_lw = self.line_width
        self.set_line_width(1.8)
        self.line(self.l_margin + 2, y0, self.l_margin + 2, y1)
        self.set_line_width(old_lw)
        self.set_draw_color(0)
        self.ln(1.5)

    def note(self, text):
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


def qp(n): return os.path.join(ME,  f"Mixed_Exam_{n}.pdf")
def ap(n): return os.path.join(MAK, f"Mixed_Exam_{n}_Answers.pdf")


# ══════════════════════════════════════════════════════════════════════════════
# MIXED EXAM 1
# Topics: Markov Chains  |  Biased Random Walk & Gambler's Ruin  |  Poisson
# ══════════════════════════════════════════════════════════════════════════════

def exam1_q():
    p = ExamPDF("Mixed Exam 1  --  Markov Chains | Biased Random Walk | Poisson Process")
    p.add_page()
    p.txt("Duration: 90 minutes.  Total: 100 points.  Show all working.")
    p.txt("Notation:  P(i,j) = one-step transition probability from state i to j.  "
          "pi(i) = stationary probability of state i.  "
          "S(n) = position after n steps.  "
          "N(t) = number of Poisson arrivals by time t.")
    p.ln(2)

    p.Q(1, 30, "A Markov chain has three states {A, B, C} with transition matrix:")
    p.mat(["         A      B      C",
           "   A  [ 0.5    0.3    0.2 ]",
           "   B  [ 0.1    0.6    0.3 ]",
           "   C  [ 0.4    0.1    0.5 ]"])
    p.sub("a", "Is this chain irreducible? Explain by showing that every state "
          "can reach every other state in one or more steps.")
    p.sub("b", "Find the stationary distribution pi = (pi(A), pi(B), pi(C)) "
          "by solving the system pi * P = pi together with "
          "pi(A) + pi(B) + pi(C) = 1. "
          "Set up the three linear equations explicitly before solving.")
    p.sub("c", "Starting in state A, what is the expected number of steps "
          "to return to A for the first time?  "
          "Use the formula:  E[return time to A] = 1 / pi(A).")

    p.sep()

    p.Q(2, 35, "A particle performs a biased random walk on {0, 1, 2, 3, 4, 5}. "
        "At each interior state k (with 1 <= k <= 4) the particle moves right "
        "with probability p = 2/3 and left with probability q = 1/3. "
        "States 0 and 5 are absorbing (the particle stops on arrival).")
    p.sub("a", "Write the hitting probability recurrence for "
          "h(k) = P(reach 5 before 0 | start at k):\n"
          "  h(k) = p * h(k+1) + q * h(k-1)    for k = 1, 2, 3, 4\n"
          "with boundary conditions h(0) = 0 and h(5) = 1.\n"
          "The general solution is  h(k) = A + B * r^k  where r = q/p. "
          "Identify r and use the boundary conditions to find A and B.")
    p.sub("b", "Compute h(2) = P(reach 5 before 0 | start at k = 2). "
          "Compare with the symmetric walk result h_sym(2) = 2/5.")
    p.sub("c", "For the symmetric walk (p = q = 1/2, starting at k = 2, N = 5): "
          "use the Optional Stopping Theorem with martingale S(n) "
          "to confirm h_sym(2) = 2/5, and with martingale S(n)^2 - n "
          "to find E[T | start k = 2] where T is the absorption time.")

    p.sep()

    p.Q(3, 35, "Customers arrive at a coffee shop according to a Poisson process "
        "with rate lambda = 4 per hour. Each customer independently "
        "orders a latte with probability p = 0.25.")
    p.sub("a", "State the Thinning Property: what is the rate lambda_L of "
          "the latte-ordering sub-process? What distribution does N_L(t) "
          "(number of latte orders by time t) follow?")
    p.sub("b", "Find the probability that NO latte is ordered in the first 30 minutes "
          "(t = 0.5 hours). Use the Poisson PMF with n = 0:\n"
          "  P(N_L(0.5) = 0) = e^(-lambda_L * 0.5)")
    p.sub("c", "Given that exactly 8 customers arrive in the first hour, "
          "what is the conditional distribution of the number of latte orders? "
          "State the distribution by name and give its parameters. "
          "Find the conditional expected number of latte orders.")
    p.save(qp(1))


def exam1_a():
    p = ExamPDF("Mixed Exam 1  --  Answer Key")
    p.add_page()

    p.AH("Q1  Solution  (30 points)")
    p.AL("a)  Irreducibility:")
    p.txt("A chain is irreducible if every state can reach every other state.\n"
          "From the transition matrix, every entry is strictly positive, so in ONE "
          "step every state can reach every other state directly. Therefore the chain "
          "is irreducible.")

    p.AL("b)  Stationary distribution pi * P = pi:")
    p.txt("The equations pi(i) = sum_j pi(j)*P(j,i) give:")
    p.eqn("pi(A) = 0.5*pi(A) + 0.1*pi(B) + 0.4*pi(C)   ... (I)",
          "pi(B) = 0.3*pi(A) + 0.6*pi(B) + 0.1*pi(C)   ... (II)",
          "pi(C) = 0.2*pi(A) + 0.3*pi(B) + 0.5*pi(C)   ... (III)",
          "pi(A) + pi(B) + pi(C) = 1                    ... (IV)")
    p.txt("Simplify (I):  0.5*pi(A) = 0.1*pi(B) + 0.4*pi(C)\n"
          "              5*pi(A) = pi(B) + 4*pi(C)   ... (I')\n\n"
          "Simplify (II): 0.4*pi(B) = 0.3*pi(A) + 0.1*pi(C)\n"
          "               4*pi(B) = 3*pi(A) + pi(C)  ... (II')\n\n"
          "From (I'): pi(B) = 5*pi(A) - 4*pi(C)\n"
          "Sub into (II'): 4*(5*pi(A) - 4*pi(C)) = 3*pi(A) + pi(C)\n"
          "  20*pi(A) - 16*pi(C) = 3*pi(A) + pi(C)\n"
          "  17*pi(A) = 17*pi(C)  =>  pi(C) = pi(A)\n\n"
          "Then: pi(B) = 5*pi(A) - 4*pi(A) = pi(A)\n\n"
          "From (IV): pi(A) + pi(A) + pi(A) = 1  =>  pi(A) = 1/3\n\n"
          "  pi(A) = pi(B) = pi(C) = 1/3  (uniform stationary distribution)")

    p.AL("c)  Expected return time to A:")
    p.eqn("E[return time to A] = 1 / pi(A) = 1 / (1/3) = 3 steps")

    p.sep()

    p.AH("Q2  Solution  (35 points)")
    p.AL("a)  Solving the hitting probability recurrence:")
    p.txt("The characteristic equation of  h(k) = (2/3)*h(k+1) + (1/3)*h(k-1)  gives:")
    p.eqn("r = q/p = (1/3)/(2/3) = 1/2")
    p.txt("General solution:  h(k) = A + B*(1/2)^k\n\n"
          "Apply boundary conditions:\n"
          "  h(0) = 0:   A + B*(1/2)^0 = 0  =>  A + B = 0  =>  B = -A\n"
          "  h(5) = 1:   A + B*(1/2)^5 = 1  =>  A - A*(1/32) = 1\n"
          "              A*(1 - 1/32) = 1  =>  A*(31/32) = 1  =>  A = 32/31\n\n"
          "So B = -32/31 and:")
    p.eqn("h(k) = (32/31) * [1 - (1/2)^k]  =  (2^5 - 2^(5-k)) / (2^5 - 1)")

    p.AL("b)  h(2) for the biased walk:")
    p.eqn("h(2) = (32/31) * [1 - (1/2)^2] = (32/31) * (3/4) = 24/31 ~ 0.774")
    p.txt("Symmetric walk: h_sym(2) = 2/5 = 0.4.\n"
          "The upward bias (p=2/3) dramatically increases the probability of "
          "reaching 5 before 0: from 40% to 77.4%.")

    p.AL("c)  Symmetric walk OST -- h_sym(2) and E[T]:")
    p.txt("Martingale S(n), OST (T bounded): E[S(T)] = S(0) = 2")
    p.eqn("5 * h_sym(2) + 0 * (1 - h_sym(2)) = 2  =>  h_sym(2) = 2/5  (OK)")
    p.txt("Martingale M(n) = S(n)^2 - n, OST: E[M(T)] = M(0) = 4 - 0 = 4")
    p.eqn("E[S(T)^2] - E[T] = 4",
          "S(T)^2 = 25 with prob 2/5,  S(T)^2 = 0 with prob 3/5",
          "E[S(T)^2] = 25*(2/5) + 0 = 10",
          "10 - E[T] = 4  =>  E[T] = 6 steps")

    p.sep()

    p.AH("Q3  Solution  (35 points)")
    p.AL("a)  Thinning property:")
    p.eqn("lambda_L = lambda * p = 4 * 0.25 = 1 latte order per hour",
          "N_L(t) ~ Poisson(lambda_L * t) = Poisson(t)")

    p.AL("b)  P(no latte in 30 minutes):")
    p.eqn("P(N_L(0.5) = 0) = e^(-lambda_L * 0.5) = e^(-1 * 0.5) = e^(-0.5) ~ 0.6065")
    p.txt("About a 60.7% chance of no latte being ordered in the first 30 minutes.")

    p.AL("c)  Conditional distribution given 8 arrivals:")
    p.txt("Given exactly n = 8 customers arrive, each independently orders a latte "
          "with probability p = 0.25. The number of latte orders is:")
    p.eqn("Binomial(n = 8, p = 0.25)")
    p.txt("Conditional expected number of latte orders:")
    p.eqn("E[latte orders | 8 arrivals] = n * p = 8 * 0.25 = 2 orders")
    p.save(ap(1))


# ══════════════════════════════════════════════════════════════════════════════
# MIXED EXAM 2
# Topics: CTMC & Birth-Death  |  M/M/1 Queue  |  Chapman-Kolmogorov & Diag
# ══════════════════════════════════════════════════════════════════════════════

def exam2_q():
    p = ExamPDF("Mixed Exam 2  --  CTMC | M/M/1 Queue | Chapman-Kolmogorov & Diagonalization")
    p.add_page()
    p.txt("Duration: 90 minutes.  Total: 100 points.  Show all working.")
    p.txt("Notation:  Q(i,j) = rate from state i to state j in a CTMC.  "
          "q(i) = -Q(i,i) = total leaving rate from state i.  "
          "rho = lambda/mu = traffic intensity.  "
          "P^n(i,j) = n-step transition probability.")
    p.ln(2)

    p.Q(1, 30, "A server switches between Idle (state 0), Busy (state 1), and "
        "Overloaded (state 2). The rate matrix is:")
    p.mat(["           0       1       2",
           "   0  [  -2.0    1.5    0.5  ]",
           "   1  [   1.0   -3.0    2.0  ]",
           "   2  [   0.5    1.5   -2.0  ]"])
    p.sub("a", "Verify that each row sums to 0. Then find q(0), q(1), q(2) "
          "(the total leaving rate from each state) and state the distribution "
          "of the holding time H(i) in each state.")
    p.sub("b", "Write the global balance equations pi * Q = 0 for this chain "
          "and solve for the stationary distribution pi(0), pi(1), pi(2).")
    p.sub("c", "Check whether detailed balance holds between states 0 and 2: "
          "compute pi(0)*Q(0,2) and pi(2)*Q(2,0) using your answer from (b).")

    p.sep()

    p.Q(2, 35, "A single-server queue (M/M/1) has Poisson arrivals at rate "
        "lambda = 5 customers per hour and exponential service at rate "
        "mu = 8 customers per hour.")
    p.sub("a", "Compute rho = lambda/mu and verify the queue is stable. "
          "Find pi(0) = P(server idle) and pi(n) for general n. "
          "What is P(more than 3 customers in system)?")
    p.sub("b", "Compute E[N] (mean number in system) and use Little's law "
          "E[N] = lambda * E[T] to find E[T] (mean time in system). "
          "Then find E[T_q] = E[T] - 1/mu (mean waiting time in queue).")
    p.sub("c", "The server takes a short break when the queue empties. "
          "This creates an M/M/1 variant where the server only starts work "
          "when there are at least 2 customers waiting. "
          "Would you expect E[N] to increase or decrease compared to the standard "
          "M/M/1? Give a qualitative explanation (no calculation needed).")

    p.sep()

    p.Q(3, 35, "A Markov chain on {0, 1} has transition matrix:")
    p.mat(["         0       1",
           "   0  [  0.6    0.4  ]",
           "   1  [  0.3    0.7  ]"])
    p.sub("a", "Use the Chapman-Kolmogorov equation P^(2) = P * P to compute "
          "P^2(0, 0) directly (the probability of being in state 0 after 2 steps, "
          "starting from state 0).")
    p.sub("b", "Find the two eigenvalues of P. Recall that for a 2x2 stochastic "
          "matrix with P(0,1) = p and P(1,0) = q, the eigenvalues are "
          "lambda(1) = 1 and lambda(2) = 1 - p - q.")
    p.sub("c", "Using the diagonalization formula for the n-step probability:")
    p.eqn("P^n(0,0) = q/(p+q)  +  lambda(2)^n * p/(p+q)")
    p.txt("where p = P(0,1) = 0.4 and q = P(1,0) = 0.3, compute P^3(0,0) "
          "and find the limit as n -> infinity.")
    p.save(qp(2))


def exam2_a():
    p = ExamPDF("Mixed Exam 2  --  Answer Key")
    p.add_page()

    p.AH("Q1  Solution  (30 points)")
    p.AL("a)  Row sums and holding times:")
    p.txt("Row 0: -2.0 + 1.5 + 0.5 = 0  (OK)\n"
          "Row 1:  1.0 - 3.0 + 2.0 = 0  (OK)\n"
          "Row 2:  0.5 + 1.5 - 2.0 = 0  (OK)")
    p.eqn("q(0) = 2.0  =>  H(0) ~ Exponential(2.0),  E[H(0)] = 0.5 time units",
          "q(1) = 3.0  =>  H(1) ~ Exponential(3.0),  E[H(1)] = 1/3 time units",
          "q(2) = 2.0  =>  H(2) ~ Exponential(2.0),  E[H(2)] = 0.5 time units")
    p.txt("State 1 (Busy) has the shortest expected holding time.")

    p.AL("b)  Stationary distribution from pi * Q = 0:")
    p.txt("Balance equations (rate in = rate out for each state):")
    p.eqn("2.0*pi(0)  =  1.0*pi(1) + 0.5*pi(2)   ... (I)",
          "3.0*pi(1)  =  1.5*pi(0) + 1.5*pi(2)   ... (II)",
          "2.0*pi(2)  =  0.5*pi(0) + 2.0*pi(1)   ... (III)")
    p.txt("From (II): pi(1) = 0.5*pi(0) + 0.5*pi(2)  ... (II')\n"
          "Sub into (I): 2*pi(0) = 0.5*pi(0) + 0.5*pi(2) + 0.5*pi(2)\n"
          "  2*pi(0) = 0.5*pi(0) + pi(2)  =>  pi(2) = 1.5*pi(0)\n"
          "From (II'): pi(1) = 0.5*pi(0) + 0.5*(1.5*pi(0)) = 0.5*pi(0) + 0.75*pi(0) = 1.25*pi(0)\n"
          "Normalise: pi(0) + 1.25*pi(0) + 1.5*pi(0) = 1  =>  3.75*pi(0) = 1")
    p.eqn("pi(0) = 4/15,   pi(1) = 5/15 = 1/3,   pi(2) = 6/15 = 2/5")
    p.txt("Check: 4/15 + 5/15 + 6/15 = 15/15 = 1  (OK)")

    p.AL("c)  Detailed balance test between states 0 and 2:")
    p.eqn("pi(0) * Q(0,2) = (4/15) * 0.5  = 2/15",
          "pi(2) * Q(2,0) = (6/15) * 0.5  = 3/15")
    p.txt("2/15 != 3/15, so detailed balance does NOT hold between 0 and 2.\n"
          "The chain is NOT reversible.")

    p.sep()

    p.AH("Q2  Solution  (35 points)")
    p.AL("a)  rho, pi(n), P(N > 3):")
    p.eqn("rho = lambda/mu = 5/8 = 0.625  <  1  =>  queue is stable",
          "pi(n) = (1 - rho) * rho^n = 0.375 * (0.625)^n",
          "pi(0) = 0.375  (server idle 37.5% of the time)")
    p.txt("P(more than 3 customers) = P(N >= 4) = rho^4:")
    p.eqn("P(N >= 4) = rho^4 = (0.625)^4 = 0.1526  (about 15.3%)")

    p.AL("b)  E[N], E[T], E[T_q]:")
    p.eqn("E[N] = rho / (1 - rho) = 0.625 / 0.375 = 5/3 ~ 1.667 customers",
          "E[T] = E[N] / lambda = (5/3) / 5 = 1/3 hour = 20 minutes",
          "E[T_q] = E[T] - 1/mu = 1/3 - 1/8 = 8/24 - 3/24 = 5/24 hour ~ 12.5 minutes")

    p.AL("c)  Server vacation effect (qualitative):")
    p.txt("Waiting to accumulate 2 customers before starting service means customers "
          "who arrive when 0 or 1 are in the system must wait even though the server "
          "is idle. This increases the average waiting time and E[N] compared to "
          "the standard M/M/1 where service begins immediately.")

    p.sep()

    p.AH("Q3  Solution  (35 points)")
    p.AL("a)  P^2(0,0) via Chapman-Kolmogorov:")
    p.eqn("P^2(0,0) = P(0,0)*P(0,0) + P(0,1)*P(1,0)",
          "         = 0.6*0.6 + 0.4*0.3",
          "         = 0.36 + 0.12 = 0.48")

    p.AL("b)  Eigenvalues of P:")
    p.txt("With p = P(0,1) = 0.4 and q = P(1,0) = 0.3:")
    p.eqn("lambda(1) = 1",
          "lambda(2) = 1 - p - q = 1 - 0.4 - 0.3 = 0.3")

    p.AL("c)  P^n(0,0) using diagonalization:")
    p.eqn("P^n(0,0) = q/(p+q) + lambda(2)^n * p/(p+q)",
          "         = 0.3/0.7 + (0.3)^n * 0.4/0.7",
          "         = 3/7 + (4/7) * (0.3)^n")
    p.txt("For n = 3:")
    p.eqn("P^3(0,0) = 3/7 + (4/7)*(0.3)^3 = 3/7 + (4/7)*0.027",
          "         = 3/7 + 0.108/7 = (3 + 0.108)/7 = 3.108/7 ~ 0.444")
    p.txt("As n -> infinity:  (0.3)^n -> 0, so:")
    p.eqn("P^n(0,0) -> 3/7 ~ 0.429  =  pi(0)  (stationary probability of state 0)")
    p.save(ap(2))


# ══════════════════════════════════════════════════════════════════════════════
# MIXED EXAM 3
# Topics: Classifying States  |  Renewal Processes  |  Martingales & OST
# ══════════════════════════════════════════════════════════════════════════════

def exam3_q():
    p = ExamPDF("Mixed Exam 3  --  Classifying States | Renewal Processes | Martingales")
    p.add_page()
    p.txt("Duration: 90 minutes.  Total: 100 points.  Show all working.")
    p.txt("Notation:  f(i) = P(ever return to i | start at i).  "
          "m(t) = E[N(t)] = renewal function.  "
          "M(n) = martingale value at time n.  "
          "T = stopping time.")
    p.ln(2)

    p.Q(1, 30, "A Markov chain on states {0, 1, 2, 3} has transition matrix:")
    p.mat(["         0      1      2      3",
           "   0  [ 0.5    0.5    0.0    0.0 ]",
           "   1  [ 0.5    0.0    0.5    0.0 ]",
           "   2  [ 0.0    0.0    0.3    0.7 ]",
           "   3  [ 0.0    0.0    0.7    0.3 ]"])
    p.sub("a", "Identify the communicating classes of this chain. "
          "Which states communicate with each other? "
          "Draw (or describe) the communication structure.")
    p.sub("b", "Classify each communicating class as recurrent or transient. "
          "Use the criterion: a class is recurrent if and only if once you "
          "enter it, you never leave with probability 1.")
    p.sub("c", "For the recurrent class(es), find the stationary distribution "
          "restricted to that class. For the transient class, what is the "
          "probability that the chain eventually leaves it?")

    p.sep()

    p.Q(2, 35, "Machines in a factory fail and are repaired. "
        "The time between failures (inter-renewal times) has the distribution:")
    p.eqn("P(X = 2) = 0.4,   P(X = 5) = 0.4,   P(X = 8) = 0.2")
    p.txt("Time is measured in days.")
    p.sub("a", "Compute E[X] and E[X^2]. "
          "By the Elementary Renewal Theorem, what is the long-run rate "
          "of failures per day?")
    p.sub("b", "The factory wants to schedule a preventive maintenance window "
          "at the end of day 10. Using N(10) ~ Poisson(m(10)) as an approximation "
          "where m(10) ~ 10/E[X], estimate P(N(10) >= 5) using the Poisson approximation.")
    p.sub("c", "In stationarity, what is the expected residual time B(t) until "
          "the next failure after a random inspection time t? "
          "Use the formula E[B] = E[X^2] / (2 * E[X]).\n"
          "Is E[B] greater or less than E[X]/2? Explain the Inspection Paradox.")

    p.sep()

    p.Q(3, 35, "Let X(1), X(2), ... be i.i.d. with P(X(i) = +1) = p and "
        "P(X(i) = -1) = q = 1 - p, and define S(n) = X(1) + ... + X(n), S(0) = 0.")
    p.sub("a", "For p = q = 1/2 (symmetric walk), define M(n) = S(n)^2 - n. "
          "Show M(n) is a martingale by computing E[M(n+1) | S(0),...,S(n)].\n"
          "Use: S(n+1) = S(n) + X(n+1), E[X(n+1)] = 0, E[X(n+1)^2] = 1.")
    p.sub("b", "For p = q = 1/2, let T = first time |S(n)| = N for some fixed N > 0 "
          "(the walk first exits the interval (-N, N)). "
          "Apply the OST to M(n) = S(n)^2 - n to find E[T]. "
          "Note that S(T)^2 = N^2 always at stopping.")
    p.sub("c", "Now let p != 1/2. Define M(n) = r^{S(n)} where r = q/p "
          "(De Moivre's martingale). Verify E[M(n+1) | F(n)] = M(n) by computing "
          "E[r^{X(n+1)}] = p * r^{+1} + q * r^{-1} and showing it equals 1.")
    p.save(qp(3))


def exam3_a():
    p = ExamPDF("Mixed Exam 3  --  Answer Key")
    p.add_page()

    p.AH("Q1  Solution  (30 points)")
    p.AL("a)  Communicating classes:")
    p.txt("State i communicates with state j (written i <-> j) if i can reach j "
          "AND j can reach i.\n\n"
          "From 0: 0 -> 0 (self), 0 -> 1, 1 -> 0. So {0, 1} communicate.\n"
          "From 0: 0 cannot reach 2 or 3 directly; P(0,2)=0, P(0,3)=0.\n"
          "From 1: 1 -> 2 but can 2 reach 1? P(2,0)=P(2,1)=0, so 2 CANNOT reach 1.\n"
          "From 2: 2 -> 3 and 3 -> 2. So {2, 3} communicate.\n"
          "From 1: 1 -> 2 (one step), but 2 cannot return to 1 or 0.\n\n"
          "Communicating classes:  {0, 1}  and  {2, 3}.")

    p.AL("b)  Recurrent / Transient classification:")
    p.txt("Class {2, 3}: once the chain enters states 2 or 3, all transitions "
          "stay within {2, 3} (P(2,0)=P(2,1)=P(3,0)=P(3,1)=0). The chain "
          "NEVER leaves this class => {2, 3} is RECURRENT (closed class).\n\n"
          "Class {0, 1}: from state 1, P(1,2)=0.5 > 0, so there is a positive "
          "probability of jumping to {2,3} and never returning. "
          "=> {0, 1} is TRANSIENT.")

    p.AL("c)  Stationary distribution of recurrent class {2,3}:")
    p.txt("Solve pi(2) = 0.3*pi(2) + 0.7*pi(3) and pi(2) + pi(3) = 1:")
    p.eqn("0.7*pi(2) = 0.7*pi(3)  =>  pi(2) = pi(3) = 1/2")
    p.txt("For the transient class {0,1}: starting in {0,1}, the chain eventually "
          "leaves with probability 1 (since {0,1} is transient). The chain "
          "transitions to {2,3} and stays there forever.")

    p.sep()

    p.AH("Q2  Solution  (35 points)")
    p.AL("a)  E[X], E[X^2], and long-run failure rate:")
    p.eqn("E[X] = 2*0.4 + 5*0.4 + 8*0.2 = 0.8 + 2.0 + 1.6 = 4.4 days",
          "E[X^2] = 4*0.4 + 25*0.4 + 64*0.2 = 1.6 + 10.0 + 12.8 = 24.4 days^2",
          "Long-run failure rate = 1/E[X] = 1/4.4 ~ 0.227 failures per day")

    p.AL("b)  P(N(10) >= 5) using Poisson approximation:")
    p.eqn("m(10) ~ 10 / E[X] = 10 / 4.4 ~ 2.27",
          "N(10) approx Poisson(2.27)")
    p.txt("P(N(10) >= 5) = 1 - P(N=0) - P(N=1) - P(N=2) - P(N=3) - P(N=4)")
    p.eqn("P(N=k) = e^(-2.27) * (2.27)^k / k!,   e^(-2.27) ~ 0.1033",
          "P(N=0) ~ 0.1033,  P(N=1) ~ 0.2345,  P(N=2) ~ 0.2662",
          "P(N=3) ~ 0.2011,  P(N=4) ~ 0.1141",
          "P(N>=5) ~ 1 - 0.9192 ~ 0.0808  (about 8.1%)")

    p.AL("c)  Expected residual life E[B] and Inspection Paradox:")
    p.eqn("E[B] = E[X^2] / (2*E[X]) = 24.4 / (2*4.4) = 24.4 / 8.8 ~ 2.77 days")
    p.txt("Compare E[X]/2 = 4.4/2 = 2.2 days.\n"
          "Since E[B] = 2.77 > 2.2 = E[X]/2, the expected wait is longer than "
          "half the average gap.\n\n"
          "Inspection Paradox: at a random time t, you are more likely to land "
          "inside a LONG inter-failure interval than a short one (because long "
          "intervals occupy more of the time axis). This biases the observed "
          "interval upward, so both the age A(t) and the residual life B(t) "
          "have mean E[X^2]/(2*E[X]) > E[X]/2.")

    p.sep()

    p.AH("Q3  Solution  (35 points)")
    p.AL("a)  M(n) = S(n)^2 - n is a martingale:")
    p.eqn("E[M(n+1) | F(n)] = E[S(n+1)^2 - (n+1) | F(n)]",
          "= E[(S(n) + X(n+1))^2 | F(n)] - (n+1)",
          "= S(n)^2 + 2*S(n)*E[X(n+1)] + E[X(n+1)^2] - (n+1)",
          "= S(n)^2 + 0 + 1 - n - 1",
          "= S(n)^2 - n = M(n)  (OK)")

    p.AL("b)  E[T] using OST on M(n) = S(n)^2 - n:")
    p.txt("At stopping time T: |S(T)| = N, so S(T)^2 = N^2 always.")
    p.eqn("E[M(T)] = E[M(0)]  =>  E[S(T)^2 - T] = S(0)^2 - 0 = 0",
          "E[N^2 - T] = 0  =>  E[T] = N^2")
    p.txt("The expected time for a symmetric walk to first exit (-N, N) is N^2 steps.")

    p.AL("c)  De Moivre's martingale -- verify E[r^{X(n+1)}] = 1:")
    p.eqn("r = q/p",
          "E[r^{X(n+1)}] = p * r^{+1} + q * r^{-1}",
          "              = p * (q/p) + q * (p/q)",
          "              = q + p = 1  (OK)")
    p.txt("Since E[r^{X(n+1)}] = 1 and X(n+1) is independent of F(n):")
    p.eqn("E[M(n+1) | F(n)] = E[r^{S(n+1)} | F(n)]",
          "= E[r^{S(n)} * r^{X(n+1)} | F(n)]",
          "= r^{S(n)} * E[r^{X(n+1)}]  =  r^{S(n)} * 1  =  M(n)  (OK)")
    p.save(ap(3))


# ══════════════════════════════════════════════════════════════════════════════
# MIXED EXAM 4
# Topics: Renewal-Reward & Residual Life | Birth-Death & M/M/inf | Wald + De Moivre
# ══════════════════════════════════════════════════════════════════════════════

def exam4_q():
    p = ExamPDF("Mixed Exam 4  --  Renewal-Reward | Birth-Death & Queues | Wald & De Moivre")
    p.add_page()
    p.txt("Duration: 90 minutes.  Total: 100 points.  Show all working.")
    p.txt("Notation:  C(t) = total reward by time t.  "
          "B(t) = residual life at time t.  "
          "r = q/p = De Moivre ratio.  "
          "T = random stopping time with E[T] < inf.")
    p.ln(2)

    p.Q(1, 30, "A city bus runs on a loop. Each round-trip has two phases: "
        "Outbound (O) with random duration U(O) ~ Uniform[20, 40] minutes, "
        "and Return (R) with duration U(R) ~ Exponential with mean 25 minutes. "
        "Each trip earns a revenue of R(n) = 50 * U_O(n) dollars (proportional to "
        "outbound time). Cycles are i.i.d. Define the renewal point as the "
        "start of each outbound trip.")
    p.sub("a", "Compute E[X] (mean cycle length) and E[R] (mean revenue per cycle). "
          "For U(O) ~ Uniform[20,40]: E[U(O)] = 30 and E[U(R)] = 25.")
    p.sub("b", "Apply the Renewal-Reward Theorem to find the long-run revenue "
          "rate (dollars per minute):\n"
          "  Long-run rate = E[R] / E[X]\n"
          "How many dollars per hour does the bus earn on average in the long run?")
    p.sub("c", "Compute E[X^2] for the cycle length. "
          "Use Var[U(O)] = (40-20)^2/12 for uniform, Var[U(R)] = 25^2 for exponential, "
          "and E[X^2] = Var[X] + (E[X])^2. Assume U(O) and U(R) are independent.\n"
          "Then compute E[B] = E[X^2]/(2*E[X]), the expected residual time until "
          "the next departure for a random passenger arrival.")

    p.sep()

    p.Q(2, 35, "A hospital ward has n beds. Patients arrive at rate lambda = 6 per hour "
        "and each occupies a bed for an Exponential duration with mean 1/mu = 0.5 hours. "
        "The ward has INFINITE capacity (M/M/inf model).")
    p.sub("a", "State the M/M/inf stationary distribution pi(n) "
          "and identify it as a named distribution with parameter rho = lambda/mu. "
          "Compute rho and find P(ward has 0 patients) and P(ward has exactly 3 patients).")
    p.sub("b", "Find E[N] (mean occupancy) and E[T] (mean time each patient spends). "
          "Compare E[T] to 1/mu: are patients spending time waiting, or just being treated?")
    p.sub("c", "The hospital considers switching to a single-doctor model (M/M/1) "
          "where one doctor treats patients at rate mu' = lambda + 1 = 7 per hour "
          "(just above the arrival rate to ensure stability). "
          "Compute rho', E[N'] and E[T'] for this M/M/1 queue. "
          "Which model gives shorter E[T]: M/M/inf with mu=2 or M/M/1 with mu'=7?")

    p.sep()

    p.Q(3, 35, "A gambler plays a biased coin: heads (+1) with probability p = 2/3, "
        "tails (-1) with probability q = 1/3. Starting fortune: k = 4. "
        "Absorbing barriers at 0 (ruin) and N = 10 (goal).")
    p.sub("a", "Compute r = q/p. Write De Moivre's martingale M(n) = r^{S(n)}. "
          "Verify it is a martingale by showing E[r^{X(n+1)}] = 1.")
    p.sub("b", "Apply OST to M(n) with stopping time T = first hit of {0, 10}. "
          "Let h = P(reach 10 before 0 | start k = 4). Set up and solve:")
    p.eqn("r^10 * h + 1 * (1 - h) = r^4")
    p.sub("c", "The gambler's total winnings at stopping is S(T). "
          "Using Wald's equality E[S(T)] = E[X] * E[T] where E[X] = p - q,\n"
          "express E[T] in terms of h, k, N, p, q, and E[S(T)].\n"
          "Compute E[S(T)] = 10*h + 0*(1-h) = 10h, then find E[T].")
    p.save(qp(4))


def exam4_a():
    p = ExamPDF("Mixed Exam 4  --  Answer Key")
    p.add_page()

    p.AH("Q1  Solution  (30 points)")
    p.AL("a)  E[X] and E[R]:")
    p.eqn("E[X] = E[U(O)] + E[U(R)] = 30 + 25 = 55 minutes per cycle",
          "E[R] = E[50 * U(O)] = 50 * E[U(O)] = 50 * 30 = 1500 dollars per cycle")

    p.AL("b)  Long-run revenue rate:")
    p.eqn("Long-run rate = E[R] / E[X] = 1500 / 55 = 300/11 ~ 27.27 dollars/minute",
          "Per hour: 27.27 * 60 ~ 1636.4 dollars/hour")

    p.AL("c)  E[X^2] and E[B]:")
    p.txt("Cycle X = U(O) + U(R), with U(O) and U(R) independent:")
    p.eqn("Var[X] = Var[U(O)] + Var[U(R)]",
          "Var[U(O)] = (40-20)^2 / 12 = 400/12 = 100/3 ~ 33.33",
          "Var[U(R)] = (1/mu)^2 = 25^2 = 625   [Exp(1/25) has Var = mean^2]",
          "Var[X] = 100/3 + 625 = 100/3 + 1875/3 = 1975/3 ~ 658.33",
          "E[X^2] = Var[X] + (E[X])^2 = 1975/3 + 55^2 = 1975/3 + 3025",
          "       = 1975/3 + 9075/3 = 11050/3 ~ 3683.3",
          "E[B] = E[X^2] / (2*E[X]) = (11050/3) / (2*55) = 11050 / 330 ~ 33.5 min")
    p.txt("A random passenger arriving at the bus stop expects to wait about "
          "33.5 minutes for the next departure -- more than E[X]/2 = 27.5 minutes "
          "due to the Inspection Paradox.")

    p.sep()

    p.AH("Q2  Solution  (35 points)")
    p.AL("a)  M/M/inf stationary distribution:")
    p.eqn("rho = lambda/mu = 6 / (1/0.5) = 6 / 2 = 3",
          "pi(n) = e^(-rho) * rho^n / n!  =  e^(-3) * 3^n / n!   [Poisson(3)]",
          "pi(0) = e^(-3) ~ 0.0498",
          "pi(3) = e^(-3) * 27 / 6 = e^(-3) * 4.5 ~ 0.2240")

    p.AL("b)  E[N] and E[T]:")
    p.eqn("E[N] = rho = 3 patients  (mean of Poisson(3))",
          "E[T] = E[N] / lambda = 3 / 6 = 0.5 hours = 30 minutes = 1/mu")
    p.txt("E[T] = 1/mu exactly: patients spend ZERO time waiting (infinite servers "
          "=> immediate service), so the entire stay is treatment time.")

    p.AL("c)  Comparison with M/M/1 (mu' = 7):")
    p.eqn("rho' = lambda/mu' = 6/7 ~ 0.857",
          "E[N'] = rho'/(1-rho') = (6/7)/(1/7) = 6 patients",
          "E[T'] = E[N']/lambda = 6/6 = 1 hour = 60 minutes")
    p.txt("M/M/inf (mu=2): E[T] = 30 minutes\n"
          "M/M/1   (mu'=7): E[T'] = 60 minutes\n\n"
          "M/M/inf gives half the waiting time despite having a slower server, "
          "because infinite servers eliminate queuing entirely.")

    p.sep()

    p.AH("Q3  Solution  (35 points)")
    p.AL("a)  De Moivre's martingale:")
    p.eqn("r = q/p = (1/3)/(2/3) = 1/2",
          "M(n) = r^{S(n)} = (1/2)^{S(n)}",
          "E[r^{X(n+1)}] = p*r^{+1} + q*r^{-1} = (2/3)*(1/2) + (1/3)*(2)",
          "              = 1/3 + 2/3 = 1  (OK)  =>  M(n) is a martingale")

    p.AL("b)  Hitting probability h via OST:")
    p.eqn("r^4 = E[M(0)] = E[M(T)] = r^10 * h + r^0 * (1-h)",
          "(1/2)^4 = (1/2)^10 * h + 1*(1-h)",
          "1/16 = h/1024 + 1 - h",
          "h - h/1024 = 1 - 1/16",
          "h * (1023/1024) = 15/16",
          "h = (15/16) * (1024/1023) = 15360/16368 = 960/1023 ~ 0.9384")
    p.txt("The upward-biased gambler (p=2/3) has about a 93.8% chance of "
          "reaching N=10 before ruin, starting at k=4.")

    p.AL("c)  E[T] via Wald's equality:")
    p.eqn("E[X] = p - q = 2/3 - 1/3 = 1/3  (mean step size, upward drift)",
          "E[S(T)] = 10*h + 0*(1-h) = 10h = 10*(960/1023) = 9600/1023 ~ 9.384")
    p.txt("Wald's equality: E[S(T)] = E[X] * E[T]")
    p.eqn("E[T] = E[S(T)] / E[X] = (9600/1023) / (1/3) = 28800/1023 ~ 28.15 steps")
    p.save(ap(4))


# ══════════════════════════════════════════════════════════════════════════════
# MIXED EXAM 5
# Topics: Comprehensive -- full chain analysis, CTMC to queue, OST application
# ══════════════════════════════════════════════════════════════════════════════

def exam5_q():
    p = ExamPDF("Mixed Exam 5  --  Comprehensive (All Topics)")
    p.add_page()
    p.txt("Duration: 90 minutes.  Total: 100 points.  Show all working.")
    p.txt("This exam covers all course topics. Each question integrates multiple areas.")
    p.ln(2)

    p.Q(1, 30, "A 4-state Markov chain on {A, B, C, D} models a system's "
        "health status. The transition matrix is:")
    p.mat(["         A      B      C      D",
           "   A  [ 0.6    0.4    0.0    0.0 ]",
           "   B  [ 0.2    0.3    0.5    0.0 ]",
           "   C  [ 0.0    0.0    0.7    0.3 ]",
           "   D  [ 0.0    0.0    0.4    0.6 ]"])
    p.sub("a", "Identify all communicating classes and label each as "
          "recurrent or transient. Is the full chain irreducible?")
    p.sub("b", "Find the stationary distribution of the recurrent class. "
          "Set up and solve the balance equations restricted to the recurrent states.")
    p.sub("c", "The rate of convergence to stationarity is governed by the "
          "second-largest eigenvalue of the transition matrix WITHIN the recurrent class. "
          "For the recurrent class with transition matrix P_r, the eigenvalues are "
          "1 and lambda(2) = P_r(C,C) + P_r(D,D) - 1 = 0.7 + 0.6 - 1 = 0.3. "
          "After how many steps is the total variation distance to stationarity "
          "below 0.01? Use the bound: d(n) <= (1/2) * |lambda(2)|^n "
          "and solve (1/2)*(0.3)^n < 0.01.")

    p.sep()

    p.Q(2, 35, "A server for a cloud application can be in three states: "
        "Idle (I), Processing (P), and Crashed (C). "
        "The CTMC rate matrix is:")
    p.mat(["            I        P        C",
           "   I  [  -3.0      3.0      0.0  ]",
           "   P  [   1.0     -4.0      3.0  ]",
           "   C  [   2.0      0.0     -2.0  ]"])
    p.sub("a", "Identify q(I), q(P), q(C) and write the embedded chain P "
          "(divide each off-diagonal row entry by the row's total leaving rate).")
    p.sub("b", "Find the stationary distribution pi of the CTMC by solving "
          "pi * Q = 0 with pi(I) + pi(P) + pi(C) = 1.")
    p.sub("c", "The server is 'available' only when in state I or P. "
          "Use the Renewal-Reward Theorem to find the long-run fraction of time "
          "the server is available. Define reward R(n) = time spent in I or P "
          "during cycle n, where a cycle starts at each entry into I.\n"
          "Alternatively: the fraction of time in I = pi(I) and in P = pi(P); "
          "compute pi(I) + pi(P) directly from (b).")

    p.sep()

    p.Q(3, 35, "A player starts with k = 3 chips in a casino game. "
        "At each turn the player either gains 1 chip (prob p = 0.5) "
        "or loses 1 chip (prob q = 0.5). The game ends when the player "
        "has either 0 chips (ruin) or N = 7 chips (win). "
        "Let S(n) = chips at turn n.")
    p.sub("a", "Define the three processes: (i) S(n), (ii) S(n)^2 - n, and "
          "(iii) for a biased walk with p != 1/2, (q/p)^{S(n)}. "
          "State (without proof) which of these are martingales and under what "
          "conditions on p.")
    p.sub("b", "Apply the OST to martingale S(n) (symmetric walk, p = 1/2) "
          "to find the win probability h(3) = P(reach 7 before 0 | start 3). "
          "Then apply OST to S(n)^2 - n to find E[T | start 3], "
          "the expected game length.")
    p.sub("c", "The player considers a modified stopping rule: they stop early "
          "if they reach 5 chips even if they haven't reached 7. "
          "The new stopping time is T' = min{T, T_5} where T_5 = first time S(n)=5. "
          "Without calculation, explain why E[S(T')] = 3 still holds by OST "
          "and what this tells us about P(reach 5 before 0 | start 3).")
    p.save(qp(5))


def exam5_a():
    p = ExamPDF("Mixed Exam 5  --  Answer Key")
    p.add_page()

    p.AH("Q1  Solution  (30 points)")
    p.AL("a)  Communicating classes:")
    p.txt("Check reachability:\n"
          "  A -> B (direct), B -> A (direct): A <-> B  =>  {A, B} communicate.\n"
          "  B -> C (direct), C -> D (direct), D -> C (direct): {C, D} communicate.\n"
          "  Can C reach A or B? P(C,A) = P(C,B) = 0, P(D,A) = P(D,B) = 0: NO.\n"
          "  Can A reach C? A -> B -> C: YES (2 steps). But C cannot return to A.\n\n"
          "  Classes: {A, B} (transient -- can escape to C, D) "
          "and {C, D} (recurrent -- closed).\n"
          "The chain is NOT irreducible (two separate classes).")

    p.AL("b)  Stationary distribution of recurrent class {C, D}:")
    p.txt("Restricted transition matrix:")
    p.mat(["         C      D",
           "   C  [ 0.7    0.3 ]",
           "   D  [ 0.4    0.6 ]"])
    p.txt("Balance: pi(C) = 0.7*pi(C) + 0.4*pi(D)  =>  0.3*pi(C) = 0.4*pi(D)")
    p.eqn("pi(D) = (0.3/0.4)*pi(C) = (3/4)*pi(C)",
          "pi(C) + (3/4)*pi(C) = 1  =>  (7/4)*pi(C) = 1  =>  pi(C) = 4/7",
          "pi(D) = 3/7")
    p.txt("Check: 4/7 + 3/7 = 1  (OK)")

    p.AL("c)  Number of steps for convergence:")
    p.txt("Solve (1/2)*(0.3)^n < 0.01:")
    p.eqn("(0.3)^n < 0.02",
          "n * log(0.3) < log(0.02)",
          "n > log(0.02) / log(0.3)   [inequality flips because log(0.3) < 0]",
          "n > (-3.912) / (-1.204) ~ 3.25")
    p.txt("So n >= 4 steps is sufficient. After 4 steps the total variation distance "
          "to stationarity is below 0.01.")

    p.sep()

    p.AH("Q2  Solution  (35 points)")
    p.AL("a)  Leaving rates and embedded chain P:")
    p.eqn("q(I) = 3.0,   q(P) = 4.0,   q(C) = 2.0")
    p.txt("Embedded chain (divide off-diagonal entries by leaving rate):")
    p.mat(["          I        P        C",
           "   I  [  0       1.0       0    ]   (only jump: I->P)",
           "   P  [ 1/4      0        3/4   ]",
           "   C  [ 1.0      0        0     ]   (only jump: C->I)"])

    p.AL("b)  Stationary distribution of the CTMC:")
    p.txt("Global balance equations (rate out = rate in):")
    p.eqn("3*pi(I)  =  1*pi(P) + 2*pi(C)       ... (I)",
          "4*pi(P)  =  3*pi(I)                  ... (II)",
          "2*pi(C)  =  3*pi(P)                  ... (III)")
    p.txt("From (II): pi(P) = (3/4)*pi(I)\n"
          "From (III): pi(C) = (3/2)*pi(P) = (3/2)*(3/4)*pi(I) = (9/8)*pi(I)\n"
          "Normalise: pi(I) + (3/4)*pi(I) + (9/8)*pi(I) = 1")
    p.eqn("pi(I) * (8/8 + 6/8 + 9/8) = 1  =>  pi(I) * (23/8) = 1",
          "pi(I) = 8/23,   pi(P) = 6/23,   pi(C) = 9/23")
    p.txt("Check: 8 + 6 + 9 = 23  (OK)")

    p.AL("c)  Long-run availability:")
    p.eqn("Fraction of time available = pi(I) + pi(P) = 8/23 + 6/23 = 14/23 ~ 0.609")
    p.txt("The server is available (Idle or Processing) about 60.9% of the time.")

    p.sep()

    p.AH("Q3  Solution  (35 points)")
    p.AL("a)  Martingale classification:")
    p.txt("(i)  S(n) is a martingale iff E[X(i)] = 0, i.e., p = q = 1/2.\n"
          "(ii) S(n)^2 - n is a martingale iff p = q = 1/2 and Var[X(i)] = 1 (which holds since steps are +-1).\n"
          "(iii) (q/p)^{S(n)} is a martingale for ANY p != 1/2 (De Moivre's martingale). "
          "When p = 1/2, r = q/p = 1 and the martingale is trivially 1 everywhere.")

    p.AL("b)  Win probability and expected game length:")
    p.txt("OST on S(n) (symmetric, T bounded):")
    p.eqn("E[S(T)] = S(0) = 3",
          "7 * h(3) + 0 * (1 - h(3)) = 3",
          "h(3) = 3/7 ~ 0.429")
    p.txt("OST on S(n)^2 - n:")
    p.eqn("E[S(T)^2 - T] = S(0)^2 - 0 = 9",
          "E[S(T)^2] = 49*(3/7) + 0*(4/7) = 21",
          "21 - E[T] = 9  =>  E[T] = 12 steps")

    p.AL("c)  Modified stopping time T' = min(T, T_5):")
    p.txt("T' is a stopping time (minimum of two stopping times is a stopping time).\n"
          "T' is bounded: T' <= T <= N^2 = 49 steps (it can be shown T is a.s. finite).\n"
          "The increments |S(n+1) - S(n)| = 1 are bounded.\n"
          "All OST conditions are satisfied, so E[S(T')] = S(0) = 3.\n\n"
          "At stopping time T':\n"
          "  S(T') = 5  if the player reaches 5 before 0 or 7  (prob = P(T_5 < T))\n"
          "  S(T') = 7  if the player reaches 7 (bypassing 5 -- not possible going "
          "from 3 to 7; they MUST pass through 5 first since steps are +-1)\n"
          "  Actually: to go from 3 to 7, the player MUST pass through 5.\n"
          "  So T' = T_5 whenever h(3) > 0, meaning the player always hits 5 on "
          "the way to 7 (but may also hit 5 and then eventually reach 0).\n\n"
          "More precisely: E[S(T')] = 5*P(reach 5 before 0) + 0*P(reach 0 before 5) = 3\n"
          "  => P(reach 5 before 0 | start 3) = 3/5.\n\n"
          "Interpretation: the OST value E[S(T')] = 3 encodes the probability of "
          "reaching the nearer boundary (5 or 0) directly -- showing that the "
          "probability of reaching 5 before 0 is 3/5, as expected by symmetry "
          "for a symmetric walk with barrier at 5 and ruin at 0 starting from 3.")
    p.save(ap(5))


# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":
    print("\n=== CENG381 Mixed Exams 1-5 ===\n")
    print("Generating Question Papers...")
    exam1_q(); exam2_q(); exam3_q(); exam4_q(); exam5_q()
    print("\nGenerating Answer Keys...")
    exam1_a(); exam2_a(); exam3_a(); exam4_a(); exam5_a()
    print(f"\nDone. 10 PDFs written to:")
    print(f"  {os.path.relpath(ME,  BASE)}/")
    print(f"  {os.path.relpath(MAK, BASE)}/")
