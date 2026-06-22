#!/usr/bin/env python3
"""
CENG381 - PDF generator for folder 2026-04-16
Topics: Continuous-Time Markov Chains | Birth-Death Processes | M/M/1 | M/M/inf
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
        self.cell(55, 6.5, term)
        self.set_font("Helvetica", "", 10.5)
        self.multi_cell(0, 6.5, meaning)
        self.ln(0.5)

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


def qp(s, f): return os.path.join(QQ, s, f)
def ap(s, f): return os.path.join(AK, s, f)


# ==============================================================================
# 1.  CTMC AND BIRTH-DEATH PROCESSES
# ==============================================================================

def ctmc_bd_q():
    S = "CTMC_and_Birth_Death_Processes"
    p = ExamPDF("Continuous-Time Markov Chains and Birth-Death Processes  -  Question Set 1")
    p.add_page()

    p.txt("Notation used in this question set:")
    p.defn("Q (rate matrix):",
           "an S x S matrix where Q(i,j) >= 0 for i != j is the rate of "
           "jumping from state i to state j, and Q(i,i) = -sum_{j!=i} Q(i,j). "
           "Every row of Q sums to 0.")
    p.defn("q_i = -Q(i,i):",
           "the total rate of leaving state i. The chain spends an "
           "Exponential(q_i) amount of time in state i before jumping.")
    p.defn("Embedded chain P:",
           "the discrete-time chain seen only at jump times. "
           "P(i,j) = Q(i,j) / q_i  for j != i  and  P(i,i) = 0.")
    p.defn("Global balance:",
           "pi(i) * q_i = sum_{j != i} pi(j) * Q(j,i)  for every state i. "
           "Rate of leaving state i = rate of entering state i.")
    p.defn("Detailed balance:",
           "pi(i) * Q(i,j) = pi(j) * Q(j,i)  for every pair i,j. "
           "This is a stronger condition -- it implies global balance, "
           "and if it holds the chain is called REVERSIBLE.")
    p.note("Birth-Death processes are always reversible: Q(i,j) = 0 unless "
           "|i-j| = 1. Detailed balance gives: "
           "pi(n) = pi(0) * (lam_0 * lam_1 * ... * lam_{n-1}) / "
           "(mu_1 * mu_2 * ... * mu_n).")
    p.ln(1)

    # ── Q1 ──
    p.Q(1, 30,
        "An air conditioner operates in states Off (0), Low (1), High (2). "
        "The rate matrix Q is:")
    p.mat(["           0       1       2",
           "   0  [  -1/3    1/4    1/12  ]",
           "   1  [   1/3   -1/2    1/6   ]",
           "   2  [   1/6    1/3   -1/2   ]"])
    p.sub("a",
          "For each state i, identify q_i (the total leaving rate) from the "
          "diagonal of Q. Then write down the distribution of the holding time "
          "H_i (the time the chain spends in state i before jumping). "
          "Which state has the shortest expected holding time?")
    p.sub("b",
          "Write the three global balance equations (one per state) using "
          "pi*Q = 0, i.e., for each state i: pi(i)*q_i = sum_{j!=i} pi(j)*Q(j,i). "
          "Do not solve yet -- just write them out explicitly.")
    p.sub("c",
          "Solve the system from part (b) together with pi(0)+pi(1)+pi(2) = 1 "
          "to find the stationary distribution pi. Express each pi(i) as a fraction.")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "A birth-death process on states {0, 1, 2, 3, ...} has birth rates "
        "lam_n = lambda (constant) and death rates mu_n = n*mu "
        "(proportional to the current population). This models a system "
        "where each of the n individuals independently dies at rate mu.")
    p.sub("a",
          "Write the rate matrix Q for states {0, 1, 2, 3} (a 4x4 matrix). "
          "Leave entries in terms of lambda and mu. Recall: from state n, "
          "births go to n+1 at rate lam_n and deaths go to n-1 at rate mu_n.")
    p.sub("b",
          "Apply detailed balance pi(n)*lam_n = pi(n+1)*mu_{n+1} repeatedly "
          "to derive the stationary distribution:\n"
          "  pi(n) = pi(0) * (lambda/mu)^n / n!\n"
          "Then use sum_{n=0}^{inf} pi(n) = 1 and the series e^x = sum x^n/n! "
          "to find pi(0) = e^(-lambda/mu).  Write the final form of pi(n).")
    p.sub("c",
          "Using the stationary distribution found in (b), compute E[N], "
          "the expected population size. "
          "Use E[N] = sum_{n=0}^{inf} n * pi(n) and the identity "
          "sum_{n=1}^{inf} n * r^n / n! = r * e^r to evaluate the sum. "
          "What is E[N] in terms of lambda and mu?")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "A three-state CTMC on {A, B, C} has rate matrix:")
    p.mat(["          A      B      C",
           "   A  [  -5      3      2  ]",
           "   B  [   2     -6      4  ]",
           "   C  [   1      2     -3  ]"])
    p.sub("a",
          "Check whether detailed balance holds between states A and B: "
          "compute pi(A)*Q(A,B) and pi(B)*Q(B,A) and determine whether "
          "they are equal for ANY stationary distribution pi. "
          "If Q(A,B)/Q(B,A) = pi(B)/pi(A) from detailed balance, "
          "what ratio pi(B)/pi(A) would be required?")
    p.sub("b",
          "Write the global balance equations for this chain (pi * Q = 0) "
          "as three linear equations. Use the equation for state A:\n"
          "  -5*pi(A) + 2*pi(B) + 1*pi(C) = 0")
    p.sub("c",
          "Solve the system from (b) together with pi(A)+pi(B)+pi(C) = 1. "
          "Set up a 2x2 system by expressing pi(B) and pi(C) in terms of pi(A), "
          "then substitute into the normalisation equation.")
    p.save(qp(S, "Question_Set_1.pdf"))


def ctmc_bd_a():
    S = "CTMC_and_Birth_Death_Processes"
    p = ExamPDF("CTMC and Birth-Death Processes  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Total leaving rates and holding times:")
    p.txt("q_0 = -Q(0,0) = 1/3  =>  H_0 ~ Exponential(1/3),  E[H_0] = 3 time units\n"
          "q_1 = -Q(1,1) = 1/2  =>  H_1 ~ Exponential(1/2),  E[H_1] = 2 time units\n"
          "q_2 = -Q(2,2) = 1/2  =>  H_2 ~ Exponential(1/2),  E[H_2] = 2 time units\n\n"
          "States 1 and 2 have the shortest expected holding time (2 time units each). "
          "State 0 (Off) stays off the longest on average (3 time units).")

    p.AL("b)  Global balance equations (pi*Q = 0):")
    p.txt("For each state i: (rate leaving i) = (rate entering i)\n\n"
          "State 0:  pi(0)*(1/3) = pi(1)*(1/3) + pi(2)*(1/6)\n"
          "State 1:  pi(1)*(1/2) = pi(0)*(1/4) + pi(2)*(1/3)\n"
          "State 2:  pi(2)*(1/2) = pi(0)*(1/12) + pi(1)*(1/6)")

    p.AL("c)  Solving for stationary distribution:")
    p.txt("From the State 0 equation (multiply both sides by 12):\n"
          "  4*pi(0) = 4*pi(1) + 2*pi(2)\n"
          "  => 2*pi(0) = 2*pi(1) + pi(2)   ... (i)\n\n"
          "From the State 1 equation (multiply both sides by 6):\n"
          "  3*pi(1) = (3/2)*pi(0) + 2*pi(2)\n"
          "Multiply by 2: 6*pi(1) = 3*pi(0) + 4*pi(2)   ... (ii)\n\n"
          "From normalization: pi(0) + pi(1) + pi(2) = 1   ... (iii)\n\n"
          "From (i): pi(2) = 2*pi(0) - 2*pi(1)\n"
          "Substitute into (ii):\n"
          "  6*pi(1) = 3*pi(0) + 4*(2*pi(0) - 2*pi(1))\n"
          "  6*pi(1) = 3*pi(0) + 8*pi(0) - 8*pi(1)\n"
          "  14*pi(1) = 11*pi(0)\n"
          "  pi(1) = 11/14 * pi(0)\n\n"
          "Then: pi(2) = 2*pi(0) - 2*(11/14)*pi(0) = 2*pi(0)*(1 - 11/14)\n"
          "            = 2*pi(0)*(3/14) = 3/7 * pi(0)\n\n"
          "From (iii): pi(0) + (11/14)*pi(0) + (3/7)*pi(0) = 1\n"
          "  pi(0) * [1 + 11/14 + 6/14] = 1\n"
          "  pi(0) * [14/14 + 11/14 + 6/14] = 1\n"
          "  pi(0) * 31/14 = 1\n"
          "  pi(0) = 14/31\n\n"
          "  pi(1) = (11/14) * (14/31) = 11/31\n"
          "  pi(2) = (3/7) * (14/31)  = 6/31\n\n"
          "Check: 14/31 + 11/31 + 6/31 = 31/31 = 1  (OK)")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Rate matrix Q for states {0,1,2,3}:")
    p.mat(["States: lam_n = lambda (all n), mu_n = n*mu",
           "",
           "          0           1           2           3",
           " 0  [ -lambda     lambda        0           0     ]",
           " 1  [   mu      -(lambda+mu)  lambda        0     ]",
           " 2  [   0          2*mu     -(lambda+2mu) lambda  ]",
           " 3  [   0           0          3*mu    -(lambda+3mu) ]"])
    p.txt("Each row sums to 0 by construction. Off-diagonal entries are\n"
          "non-negative (they are rates). The chain is a birth-death process\n"
          "because only neighbouring states communicate directly.")

    p.AL("b)  Stationary distribution via detailed balance:")
    p.txt("Detailed balance: pi(n) * lam_n = pi(n+1) * mu_{n+1}\n"
          "  pi(n) * lambda = pi(n+1) * (n+1)*mu\n"
          "  pi(n+1) = pi(n) * lambda / ((n+1)*mu)\n\n"
          "Apply repeatedly starting from pi(0):\n"
          "  pi(1) = pi(0) * lambda / (1*mu)  =  pi(0) * (lambda/mu)^1 / 1!\n"
          "  pi(2) = pi(1) * lambda / (2*mu)  =  pi(0) * (lambda/mu)^2 / 2!\n"
          "  pi(n) = pi(0) * (lambda/mu)^n / n!\n\n"
          "Normalise (let r = lambda/mu):\n"
          "  sum_{n=0}^{inf} pi(0) * r^n / n! = 1\n"
          "  pi(0) * e^r = 1   [using e^r = sum r^n/n!]\n"
          "  pi(0) = e^(-r) = e^(-lambda/mu)\n\n"
          "Final answer:  pi(n) = e^(-lambda/mu) * (lambda/mu)^n / n!\n\n"
          "This is a Poisson(lambda/mu) distribution -- the stationary\n"
          "distribution is Poisson with mean rho = lambda/mu.")

    p.AL("c)  Expected population E[N]:")
    p.txt("Let r = lambda/mu. With pi(n) = e^(-r) * r^n / n!:\n\n"
          "  E[N] = sum_{n=0}^{inf} n * e^(-r) * r^n / n!\n"
          "       = e^(-r) * sum_{n=1}^{inf} n * r^n / n!\n"
          "       = e^(-r) * sum_{n=1}^{inf} r^n / (n-1)!\n"
          "       = e^(-r) * r * sum_{n=1}^{inf} r^(n-1) / (n-1)!\n"
          "       = e^(-r) * r * sum_{k=0}^{inf} r^k / k!    [k = n-1]\n"
          "       = e^(-r) * r * e^r\n"
          "       = r\n\n"
          "  E[N] = lambda / mu\n\n"
          "This is the well-known result: for a Poisson(r) distribution,\n"
          "the mean equals the parameter r = lambda/mu.")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Testing detailed balance between A and B:")
    p.txt("Detailed balance would require: pi(A)*Q(A,B) = pi(B)*Q(B,A)\n"
          "  pi(A) * 3 = pi(B) * 2\n"
          "  pi(B)/pi(A) = 3/2\n\n"
          "So IF detailed balance holds, we need pi(B) = (3/2)*pi(A).\n"
          "We will verify this against the solved stationary distribution in (c).")

    p.AL("b)  Global balance equations (pi*Q = 0):")
    p.txt("(Rate leaving state i) = (Rate flowing into state i)\n\n"
          "State A:  5*pi(A) = 2*pi(B) + 1*pi(C)   ... (I)\n"
          "State B:  6*pi(B) = 3*pi(A) + 2*pi(C)   ... (II)\n"
          "State C:  3*pi(C) = 2*pi(A) + 4*pi(B)   ... (III)\n\n"
          "Note: only 2 of the 3 equations are independent (the third follows\n"
          "from the other two), so we use (I), (II), and normalisation.")

    p.AL("c)  Solving for pi:")
    p.txt("From (I):  5*pi(A) = 2*pi(B) + pi(C)  =>  pi(C) = 5*pi(A) - 2*pi(B)  ... (i)\n\n"
          "Substitute (i) into (II):\n"
          "  6*pi(B) = 3*pi(A) + 2*(5*pi(A) - 2*pi(B))\n"
          "  6*pi(B) = 3*pi(A) + 10*pi(A) - 4*pi(B)\n"
          "  10*pi(B) = 13*pi(A)\n"
          "  pi(B) = 13/10 * pi(A)   ... (ii)\n\n"
          "From (i):  pi(C) = 5*pi(A) - 2*(13/10)*pi(A)\n"
          "              = 5*pi(A) - 13/5 * pi(A)\n"
          "              = (25/5 - 13/5)*pi(A)\n"
          "              = 12/5 * pi(A)   ... (iii)\n\n"
          "Normalisation: pi(A) + pi(B) + pi(C) = 1\n"
          "  pi(A) * [1 + 13/10 + 12/5] = 1\n"
          "  pi(A) * [10/10 + 13/10 + 24/10] = 1\n"
          "  pi(A) * 47/10 = 1\n"
          "  pi(A) = 10/47\n\n"
          "  pi(B) = (13/10) * (10/47) = 13/47\n"
          "  pi(C) = (12/5)  * (10/47) = 24/47\n\n"
          "Check: 10/47 + 13/47 + 24/47 = 47/47 = 1  (OK)\n\n"
          "Now test detailed balance between A and B:\n"
          "  pi(B)/pi(A) = 13/10 = 1.3, but we need 3/2 = 1.5 for DB to hold.\n"
          "  13/10 != 3/2, so detailed balance does NOT hold between A and B.\n"
          "  The chain is NOT reversible.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# 2.  M/M/1 AND M/M/inf QUEUES
# ==============================================================================

def queue_q():
    S = "Queuing_Theory_MM1_and_MMinf"
    p = ExamPDF("M/M/1 and M/M/inf Queues  -  Question Set 1")
    p.add_page()

    p.txt("Notation used in this question set:")
    p.defn("M/M/1 queue:",
           "Poisson arrivals at rate lambda, single server with Exponential(mu) "
           "service times. Customers queue and are served one at a time (FCFS).")
    p.defn("rho = lambda/mu:",
           "the traffic intensity. If rho < 1 the queue is STABLE (a unique "
           "stationary distribution exists). If rho >= 1 the queue grows without bound.")
    p.defn("pi(n) for M/M/1:",
           "stationary probability of n customers in system: "
           "pi(n) = (1 - rho) * rho^n   for n = 0, 1, 2, ...")
    p.defn("E[N] for M/M/1:",
           "mean number of customers in the system: E[N] = rho / (1 - rho)")
    p.defn("Little's law:  E[N] = lambda * E[T]",
           "where E[T] is the mean time a customer spends in the system "
           "(waiting + service). Rearranging: E[T] = E[N] / lambda.")
    p.defn("M/M/inf queue:",
           "Poisson arrivals at rate lambda, INFINITE servers, each with rate mu. "
           "Every arriving customer immediately begins service (no waiting). "
           "Always stable regardless of lambda and mu.")
    p.defn("pi(n) for M/M/inf:",
           "pi(n) = e^(-rho) * rho^n / n!   i.e. Poisson(rho) where rho = lambda/mu. "
           "E[N] = rho = lambda/mu   (mean service time * arrival rate).")
    p.ln(1)

    # ── Q1 ──
    p.Q(1, 30,
        "Customers arrive at a bank according to a Poisson process at rate "
        "lambda = 3 per hour. The single teller serves customers at rate "
        "mu = 5 per hour (exponential service times).")
    p.sub("a",
          "Compute rho = lambda/mu. Is the queue stable? "
          "Find the probability that the teller is idle (no customers in system), "
          "and the probability that there are at least 2 customers in the system.")
    p.sub("b",
          "Find E[N], the mean number of customers in the system. "
          "Then use Little's law to find E[T], the mean time a customer "
          "spends in the system (waiting + service).")
    p.sub("c",
          "The mean time a customer WAITS in the queue (before reaching the teller) "
          "is E[T_q] = E[T] - 1/mu. Compute E[T_q] and interpret: "
          "what fraction of E[T] is spent waiting vs. in service?")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "Consider an M/M/1 queue with arrival rate lambda and service rate mu. "
        "The stationary distribution is pi(n) = (1-rho)*rho^n where rho = lambda/mu < 1.")
    p.sub("a",
          "Verify the normalisation: sum_{n=0}^{inf} pi(n) = 1. "
          "Use the geometric series sum_{n=0}^{inf} rho^n = 1/(1-rho) for |rho| < 1.")
    p.sub("b",
          "Derive E[N] = rho/(1-rho) by computing sum_{n=0}^{inf} n * pi(n). "
          "Use the identity sum_{n=0}^{inf} n*x^n = x/(1-x)^2 for |x| < 1. "
          "Show all steps.")
    p.sub("c",
          "The number of customers in the QUEUE (not counting the one in service) "
          "has mean E[N_q] = rho^2 / (1-rho). "
          "Verify that E[N_q] = E[N] - rho, and interpret: why is E[N] - E[N_q] = rho "
          "equal to the average number in service? "
          "(Hint: P(server is busy) = 1 - pi(0) = rho.)")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "A hospital emergency department has an unlimited number of doctors "
        "(M/M/inf model). Patients arrive at rate lambda = 6 per hour "
        "and each requires Exponential(mu) service with mu = 2 per hour. "
        "Since there are infinite doctors, each patient is immediately served "
        "upon arrival with no waiting.")
    p.sub("a",
          "Find rho = lambda/mu. Write the stationary distribution pi(n) "
          "and identify it as a named distribution. "
          "What is the probability that exactly 3 patients are in the system?")
    p.sub("b",
          "Find E[N] (mean number of patients in system) and E[T] "
          "(mean time a patient spends in the system). "
          "Use Little's law: E[T] = E[N]/lambda.")
    p.sub("c",
          "Compare the M/M/inf model with an M/M/1 model with the same lambda = 6 "
          "and mu = 12 (one fast doctor serving at rate 12 per hour, so rho = 0.5). "
          "For the M/M/1 model: compute E[T]. "
          "Which system gives shorter expected time in system? "
          "Which design choice is more realistic for a hospital?")
    p.save(qp(S, "Question_Set_1.pdf"))


def queue_a():
    S = "Queuing_Theory_MM1_and_MMinf"
    p = ExamPDF("M/M/1 and M/M/inf Queues  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Traffic intensity and stability:")
    p.txt("  rho = lambda/mu = 3/5 = 0.6\n\n"
          "Since rho = 0.6 < 1, the queue is STABLE.\n\n"
          "P(teller idle) = pi(0) = 1 - rho = 1 - 0.6 = 0.4\n"
          "  => the teller is idle 40% of the time.\n\n"
          "P(at least 2 customers) = 1 - P(0) - P(1)\n"
          "  pi(1) = (1-rho)*rho^1 = 0.4 * 0.6 = 0.24\n"
          "  P(N >= 2) = 1 - 0.4 - 0.24 = 0.36\n\n"
          "Alternatively: P(N >= 2) = sum_{n=2}^{inf} (1-rho)*rho^n = rho^2 = 0.36\n"
          "(using the tail of the geometric series).")

    p.AL("b)  E[N] and E[T] via Little's law:")
    p.txt("  E[N] = rho / (1-rho) = 0.6 / 0.4 = 1.5 customers on average\n\n"
          "Little's law: E[N] = lambda * E[T]  =>  E[T] = E[N] / lambda\n"
          "  E[T] = 1.5 / 3 = 0.5 hours = 30 minutes")

    p.AL("c)  Waiting time in queue E[T_q]:")
    p.txt("  E[T_q] = E[T] - 1/mu = 0.5 - 1/5 = 0.5 - 0.2 = 0.3 hours = 18 minutes\n\n"
          "Interpretation:\n"
          "  - Average time in service: 1/mu = 0.2 hrs (12 min), which is 40% of E[T]\n"
          "  - Average time waiting:    E[T_q] = 0.3 hrs (18 min), which is 60% of E[T]\n\n"
          "At rho = 0.6, a typical customer spends more time waiting than being served.\n"
          "As rho -> 1, the waiting fraction -> 100% (queue explodes).")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Normalisation of pi(n) = (1-rho)*rho^n:")
    p.txt("  sum_{n=0}^{inf} pi(n) = sum_{n=0}^{inf} (1-rho)*rho^n\n"
          "                        = (1-rho) * sum_{n=0}^{inf} rho^n\n"
          "                        = (1-rho) * 1/(1-rho)     [geometric series, |rho|<1]\n"
          "                        = 1   (OK)")

    p.AL("b)  Derivation of E[N] = rho/(1-rho):")
    p.txt("  E[N] = sum_{n=0}^{inf} n * (1-rho) * rho^n\n"
          "       = (1-rho) * sum_{n=0}^{inf} n * rho^n\n\n"
          "  Use identity: sum_{n=0}^{inf} n*x^n = x/(1-x)^2  for |x|<1\n"
          "  (Proof: start from sum x^n = 1/(1-x), differentiate both sides\n"
          "   w.r.t. x: sum n*x^(n-1) = 1/(1-x)^2, multiply by x.)\n\n"
          "  So: E[N] = (1-rho) * rho/(1-rho)^2\n"
          "           = rho / (1-rho)   (OK)")

    p.AL("c)  E[N_q] = rho^2/(1-rho) and interpretation:")
    p.txt("  E[N] - E[N_q] = rho/(1-rho) - rho^2/(1-rho)\n"
          "                = (rho - rho^2) / (1-rho)\n"
          "                = rho*(1-rho) / (1-rho)\n"
          "                = rho\n\n"
          "Interpretation: E[N] - E[N_q] = rho is the mean number of customers\n"
          "IN SERVICE (i.e. at the server, not queuing).\n\n"
          "Why is this equal to rho?\n"
          "  The server is BUSY with probability P(N >= 1) = 1 - pi(0) = 1-(1-rho) = rho.\n"
          "  Since there is only 1 server, the expected number in service at any time\n"
          "  = P(server busy) * 1 = rho.\n"
          "  This is consistent: E[N] = (mean in queue) + (mean in service) = E[N_q] + rho.")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Stationary distribution for M/M/inf:")
    p.txt("  rho = lambda/mu = 6/2 = 3\n\n"
          "  pi(n) = e^(-rho) * rho^n / n! = e^(-3) * 3^n / n!\n\n"
          "This is the Poisson(3) distribution.\n\n"
          "  P(N = 3) = e^(-3) * 3^3 / 3!\n"
          "           = e^(-3) * 27 / 6\n"
          "           = e^(-3) * 4.5\n"
          "  e^(-3) ~ 0.04979\n"
          "  P(N = 3) ~ 0.04979 * 4.5 ~ 0.2240\n\n"
          "About 22.4% chance of exactly 3 patients in the system.")

    p.AL("b)  E[N] and E[T] for M/M/inf:")
    p.txt("  E[N] = rho = 3  (mean of Poisson(3))\n\n"
          "Little's law: E[T] = E[N] / lambda = 3 / 6 = 0.5 hours = 30 min\n\n"
          "This equals 1/mu = 1/2 hour exactly -- because in M/M/inf there\n"
          "is NO WAITING. Every patient immediately begins service, so the\n"
          "only time spent is the service time itself, with mean 1/mu.")

    p.AL("c)  Comparison: M/M/inf vs M/M/1 with fast server:")
    p.txt("M/M/1 with lambda = 6, mu = 12 (rho = 6/12 = 0.5):\n"
          "  E[N]_MM1 = rho/(1-rho) = 0.5/0.5 = 1 customer\n"
          "  E[T]_MM1 = E[N]/lambda = 1/6 hours ~ 10 minutes\n\n"
          "M/M/inf with lambda = 6, mu = 2 (rho = 3):\n"
          "  E[T]_MMinf = 1/mu = 1/2 hour = 30 minutes\n\n"
          "Comparison:\n"
          "  E[T]_MM1 = 10 min  <  E[T]_MMinf = 30 min\n\n"
          "The M/M/1 with one fast doctor (mu=12) gives much shorter system time.\n\n"
          "Realism note: in a hospital, treatment time is determined by the patient's\n"
          "condition, NOT by staff capacity -- a doctor cannot simply treat patients\n"
          "3x faster (mu=6 -> mu=12) by being alone. In reality:\n"
          "  - M/M/inf better models a scenario where each patient needs their\n"
          "    own dedicated specialist for a fixed treatment duration (1/mu = 30 min).\n"
          "  - The 'fast single doctor' assumption may be unrealistic for emergencies.\n"
          "  - Trade-off: infinite servers = high staffing cost but no wait;\n"
          "    single fast server = low cost but requires doubling speed, which\n"
          "    may not be medically feasible.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":
    print("\n=== Folder 2026-04-16: CTMC | Birth-Death | M/M/1 | M/M/inf ===\n")
    print("Generating Question Sets...")
    ctmc_bd_q()
    queue_q()

    print("\nGenerating Answer Keys...")
    ctmc_bd_a()
    queue_a()

    print("\nDone. 4 PDFs created.")
