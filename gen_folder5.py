#!/usr/bin/env python3
"""
CENG381 - PDF generator for folder 2026-04-09
Topics: Chapman-Kolmogorov Equations | Diagonalization of P | Poisson Process
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
        self.cell(52, 6.5, term)
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
# 1.  CHAPMAN-KOLMOGOROV EQUATIONS AND DIAGONALIZATION OF P
# ==============================================================================

def ck_diag_q():
    S = "Chapman_Kolmogorov_and_Diagonalization"
    p = ExamPDF("Chapman-Kolmogorov Equations and Diagonalization of P  -  Question Set 1")
    p.add_page()

    p.txt("Notation used in this question set:")
    p.defn("P^n(i, j)",
           "the n-step transition probability: the probability of being in "
           "state j after exactly n steps, starting from state i")
    p.defn("C-K equation:",
           "P^(n+m)(i, j) = sum over all intermediate states k of "
           "P^n(i, k) * P^m(k, j).  In matrix form: P^(n+m) = P^n * P^m")
    p.defn("Eigenvalue lam of P:",
           "a scalar such that P*v = lam*v for some non-zero vector v "
           "(called the corresponding eigenvector)")
    p.defn("Diagonalization:",
           "if P has eigenvalues lam1, lam2 and corresponding eigenvectors, "
           "it can be written as P = S_inv * D * S, where D = diag(lam1, lam2) "
           "is the diagonal matrix of eigenvalues and S_inv, S are change-of-basis "
           "matrices. Then P^n = S_inv * D^n * S, and D^n = diag(lam1^n, lam2^n).")
    p.ln(1)

    # ── Q1 ──
    p.Q(1, 30,
        "Consider the Markov chain on states {E, W} (East and West lily pads) "
        "with transition matrix:")
    p.mat(["         E       W",
           "   E  [  0.7     0.3  ]",
           "   W  [  0.4     0.6  ]"])
    p.txt("Here p = 0.3 is the probability of jumping from E to W, "
          "and q = 0.4 is the probability of jumping from W to E.")
    p.sub("a",
          "State the Chapman-Kolmogorov equation for P^(n+m)(E, E) and "
          "use it with n = m = 1 to compute P^2(E, E) directly from P.")
    p.sub("b",
          "The two eigenvalues of P are lam1 = 1 and lam2 = 1 - p - q. "
          "Compute lam2 for p = 0.3, q = 0.4. Verify that lam2 is indeed "
          "an eigenvalue by checking det(P - lam2 * I) = 0.")
    p.sub("c",
          "Use the diagonalization formula to write down P^n(E, E) explicitly:\n"
          "   P^n(E, E) = q/(p+q)  +  lam2^n * p/(p+q)\n"
          "Verify this matches P^2(E, E) from part (a). "
          "What does P^n(E, E) approach as n -> infinity?")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "A 3-state Markov chain models an air conditioner that is either "
        "Off (state 0), running at Low power (state 1), or running at "
        "High power (state 2). The transition rate matrix Q is given by:")
    p.mat(["          0      1      2",
           "   0  [ -1/3   1/4   1/12 ]",
           "   1  [  1/3  -1/2    1/6 ]",
           "   2  [  1/6   1/3  -1/2  ]"])
    p.note("Q is a RATE matrix (not a probability matrix). Each off-diagonal "
           "entry Q(i,j) >= 0 is the rate of jumping from state i to state j. "
           "Each diagonal entry Q(i,i) = -(sum of off-diagonal entries in row i) "
           "so that each row of Q sums to 0.")
    p.sub("a",
          "Verify that each row of Q sums to 0 (check rows 0, 1, and 2).")
    p.sub("b",
          "The embedded (jump) chain has transition matrix P where "
          "P(i, j) = Q(i, j) / |Q(i, i)|  for i != j  (i.e., divide each "
          "off-diagonal entry by the total rate out of state i). "
          "Compute P for this chain.")
    p.sub("c",
          "Using the Chapman-Kolmogorov equation P^2 = P * P, compute "
          "P^2(0, 2), the probability of being in state 2 after 2 jumps "
          "of the embedded chain, starting from state 0.")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "A Markov chain on the infinite state space {0, 1, 2, 3, ...} "
        "has transition probabilities:")
    p.mat(["  P(i, 0)   = 1 / (i + 1)      for all i >= 0",
           "  P(i, i+1) = i / (i + 1)      for all i >= 0",
           "  P(i, j)   = 0                for all other j"])
    p.sub("a",
          "Verify that each row sums to 1: show that P(i, 0) + P(i, i+1) = 1 "
          "for all i >= 0.")
    p.sub("b",
          "Apply the Chapman-Kolmogorov equation to compute "
          "P^2(0, 0) = sum over all intermediate states k of P(0, k) * P(k, 0). "
          "Note that from state 0, the chain can only go to state 0 (with prob 1) "
          "or state 1 (with prob 0) -- re-examine P(0, .): since i=0, "
          "P(0, 0) = 1/(0+1) = 1. So state 0 is absorbing? "
          "Re-read the problem and discuss.")
    p.sub("c",
          "Now consider a modified chain where P(0, 1) = 1 (state 0 always "
          "moves to state 1). For state i >= 1, define P(i, 0) = 1/(i+1) and "
          "P(i, i+1) = i/(i+1). Is state 0 recurrent or transient? "
          "Compute the probability that the chain started at state 1 ever "
          "returns to state 0 by summing 1/(1*2) + 1/(2*3) + ... and "
          "using the telescoping identity 1/(k*(k+1)) = 1/k - 1/(k+1).")
    p.save(qp(S, "Question_Set_1.pdf"))


def ck_diag_a():
    S = "Chapman_Kolmogorov_and_Diagonalization"
    p = ExamPDF("Chapman-Kolmogorov Equations and Diagonalization  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  C-K equation and P^2(E,E):")
    p.txt("The Chapman-Kolmogorov equation for n=m=1 states:\n\n"
          "  P^2(E, E) = sum over k in {E, W} of  P^1(E, k) * P^1(k, E)\n"
          "            = P(E,E)*P(E,E)  +  P(E,W)*P(W,E)\n"
          "            = 0.7 * 0.7      +  0.3 * 0.4\n"
          "            = 0.49 + 0.12\n"
          "            = 0.61")

    p.AL("b)  Eigenvalue lam2 = 1 - p - q:")
    p.txt("  lam2 = 1 - 0.3 - 0.4 = 0.3\n\n"
          "Verify lam2 = 0.3 is an eigenvalue via det(P - lam2*I) = 0:\n\n"
          "  P - 0.3*I = [ 0.7-0.3   0.3  ] = [ 0.4   0.3 ]\n"
          "              [ 0.4      0.6-0.3]   [ 0.4   0.3 ]\n\n"
          "  det(P - 0.3*I) = 0.4*0.3 - 0.3*0.4 = 0.12 - 0.12 = 0  (OK)\n\n"
          "So lam2 = 0.3 is indeed an eigenvalue of P.")

    p.AL("c)  Closed-form P^n(E,E) via diagonalization:")
    p.txt("With p = 0.3, q = 0.4, p+q = 0.7, lam2 = 0.3:\n\n"
          "  P^n(E, E) = q/(p+q)  +  lam2^n * p/(p+q)\n"
          "            = 0.4/0.7  +  (0.3)^n * 0.3/0.7\n"
          "            = 4/7      +  (0.3)^n * 3/7\n\n"
          "Check for n=2:\n"
          "  P^2(E,E) = 4/7 + (0.09)*(3/7) = 4/7 + 0.27/7 = 4.27/7 ~ 0.610  (OK)\n\n"
          "As n -> infinity:  (0.3)^n -> 0, so P^n(E,E) -> 4/7 ~ 0.571.\n"
          "This is exactly pi(E) = q/(p+q), the stationary probability of E.\n"
          "The chain converges to its stationary distribution regardless of\n"
          "where it starts, at an exponential rate governed by |lam2| = 0.3.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Row sums of Q:")
    p.txt("Row 0:  -1/3  + 1/4  + 1/12\n"
          "      = -4/12 + 3/12 + 1/12 = 0/12 = 0  (OK)\n\n"
          "Row 1:   1/3  - 1/2  + 1/6\n"
          "      =  2/6  - 3/6  + 1/6 = 0/6 = 0  (OK)\n\n"
          "Row 2:   1/6  + 1/3  - 1/2\n"
          "      =  1/6  + 2/6  - 3/6 = 0/6 = 0  (OK)")

    p.AL("b)  Embedded chain P  (divide off-diagonal entries by total rate out):")
    p.txt("Total rate out of state 0: |Q(0,0)| = 1/3\n"
          "  P(0, 1) = Q(0,1) / (1/3) = (1/4) / (1/3) = 3/4\n"
          "  P(0, 2) = Q(0,2) / (1/3) = (1/12)/ (1/3) = 1/4\n"
          "  P(0, 0) = 0  (no self-loops in the jump chain)\n\n"
          "Total rate out of state 1: |Q(1,1)| = 1/2\n"
          "  P(1, 0) = Q(1,0) / (1/2) = (1/3) / (1/2) = 2/3\n"
          "  P(1, 2) = Q(1,2) / (1/2) = (1/6) / (1/2) = 1/3\n\n"
          "Total rate out of state 2: |Q(2,2)| = 1/2\n"
          "  P(2, 0) = Q(2,0) / (1/2) = (1/6) / (1/2) = 1/3\n"
          "  P(2, 1) = Q(2,1) / (1/2) = (1/3) / (1/2) = 2/3\n")
    p.mat(["Embedded chain P:",
           "         0      1      2",
           "   0  [  0     3/4    1/4  ]",
           "   1  [ 2/3     0     1/3  ]",
           "   2  [ 1/3    2/3     0   ]"])

    p.AL("c)  P^2(0, 2) using C-K:")
    p.txt("P^2(0, 2) = sum over k in {0,1,2} of P(0,k) * P(k,2)\n\n"
          "          = P(0,0)*P(0,2) + P(0,1)*P(1,2) + P(0,2)*P(2,2)\n"
          "          = 0 * (1/4)     + (3/4)*(1/3)    + (1/4)*0\n"
          "          = 0 + 1/4 + 0\n"
          "          = 1/4 = 0.25\n\n"
          "So starting from Off (state 0), there is a 25% chance of being\n"
          "in High power (state 2) after exactly 2 jumps of the embedded chain.")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Row sum verification:")
    p.txt("For any i >= 0:\n"
          "  P(i, 0) + P(i, i+1) = 1/(i+1) + i/(i+1) = (1+i)/(i+1) = 1  (OK)\n\n"
          "Every row sums to exactly 1, confirming P is a valid stochastic matrix.")

    p.AL("b)  P^2(0,0) and discussion:")
    p.txt("At state i = 0:\n"
          "  P(0, 0) = 1/(0+1) = 1  and  P(0, 0+1) = P(0,1) = 0/(0+1) = 0\n\n"
          "So from state 0, the chain STAYS at state 0 with probability 1.\n"
          "State 0 is therefore an ABSORBING state under this definition.\n\n"
          "P^2(0, 0) = P(0,0)*P(0,0) + P(0,1)*P(1,0) = 1*1 + 0*(1/2) = 1.\n\n"
          "Interpretation: once the chain reaches state 0 it never leaves,\n"
          "making state 0 absorbing (positive recurrent).")

    p.AL("c)  Modified chain -- is state 0 recurrent?")
    p.txt("Modified: P(0,1)=1 (state 0 always moves to state 1).\n"
          "For i >= 1: P(i,0) = 1/(i+1),  P(i,i+1) = i/(i+1).\n\n"
          "Starting from state 1, the probability of EVER returning to state 0 is:\n\n"
          "  h(1) = P(1,0) + P(1,2)*h(2)\n"
          "       = 1/2 + (1/2)*h(2)\n\n"
          "  h(i) = P(i,0) + P(i,i+1)*h(i+1) = 1/(i+1) + i/(i+1)*h(i+1)\n\n"
          "We compute the probability of absorption at 0 starting from each state.\n"
          "Using the result for infinite random walks with decreasing return probs:\n\n"
          "  P(return to 0 from state 1) = sum_{n=1}^{inf} P(first reach 0 at step n)\n\n"
          "A simpler approach: the probability of going from state k directly to 0\n"
          "is 1/(k+1). The probability of NEVER returning to 0, starting from 1,\n"
          "satisfies a system. For this chain it can be shown that:\n\n"
          "  sum_{k=1}^{inf} 1/(k*(k+1))  using telescoping:\n"
          "  1/(k*(k+1)) = 1/k - 1/(k+1)\n\n"
          "  sum_{k=1}^{N} [1/k - 1/(k+1)] = 1 - 1/(N+1) -> 1 as N -> inf\n\n"
          "This sum equals 1, which indicates that starting from state 1,\n"
          "the chain returns to state 0 with probability 1.\n"
          "=> State 0 is RECURRENT in the modified chain.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# 2.  POISSON PROCESS
# ==============================================================================

def poisson_q():
    S = "Poisson_Process"
    p = ExamPDF("Poisson Process  -  Question Set 1")
    p.add_page()

    p.txt("Notation used in this question set:")
    p.defn("N(t)",
           "the number of arrivals (events) that have occurred by time t. "
           "N(t) is always a non-negative integer and is non-decreasing in t.")
    p.defn("lambda",
           "the arrival rate: average number of arrivals per unit time. "
           "Units match the time unit chosen (e.g. arrivals per minute).")
    p.defn("Poisson PMF:",
           "P(N(t) = n) = (lambda*t)^n * e^(-lambda*t) / n!   "
           "for n = 0, 1, 2, ...")
    p.defn("Inter-arrival time X_k:",
           "the waiting time between the (k-1)-th and k-th arrival. "
           "Each X_k ~ Exponential(lambda), meaning P(X_k > t) = e^(-lambda*t).")
    p.defn("S_n = X_1 + ... + X_n:",
           "the time of the n-th arrival. "
           "{N(t) >= n} is the same event as {S_n <= t}.")
    p.note("Key properties: (1) Arrivals in non-overlapping time intervals are "
           "INDEPENDENT. (2) The number of arrivals in an interval of length t "
           "depends only on t, not on when the interval starts (stationary increments).")
    p.ln(1)

    # ── Q1 ──
    p.Q(1, 30,
        "Customers arrive at a bookshop according to a Poisson process "
        "with rate lambda = 5 customers per hour. Each customer independently "
        "buys a book with probability p = 0.4.")
    p.sub("a",
          "The sales process (counting only buying customers) is also a "
          "Poisson process with rate lambda' = lambda * p. "
          "Compute lambda' and find the expected time until the 10th book sale.")
    p.sub("b",
          "What is the probability that the shop makes NO sales in the "
          "first hour? Use the Poisson PMF with t = 1 hour and n = 0.")
    p.sub("c",
          "What is the probability that the shop makes exactly 3 sales "
          "in the first 2 hours? Use the Poisson PMF with t = 2 hours.")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "Calls arrive at a call centre according to a Poisson process "
        "with rate lambda = 4 calls per hour.")
    p.sub("a",
          "Let S_1 be the time of the first call. Show that S_1 follows "
          "an Exponential(lambda) distribution by computing "
          "P(S_1 > t) = P(N(t) = 0) using the Poisson PMF with n = 0.")
    p.sub("b",
          "What is the probability that the first call arrives within "
          "15 minutes? "
          "(Convert: 15 minutes = 0.25 hours, and use P(S_1 <= 0.25) = 1 - e^(-lambda*0.25).)")
    p.sub("c",
          "Given that the first call arrives at time S_1, what is the "
          "distribution of the waiting time until the SECOND call (i.e. "
          "the time from S_1 to S_2)? State the key property of the "
          "Poisson process that justifies your answer (memoryless / "
          "independent increments). Compute E[S_2].")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "The Poisson process can be derived as the limit of a Bernoulli "
        "process in continuous time. Consider the following setup: divide "
        "the interval [0, T] into m sub-intervals each of length Delta = T/m. "
        "In each sub-interval, one arrival occurs with probability "
        "lambda * Delta (and no arrival with probability 1 - lambda * Delta), "
        "independently of all other sub-intervals.")
    p.sub("a",
          "Let X_m be the total number of arrivals in [0, T] under this "
          "Bernoulli model. Write the PMF of X_m as a Binomial(m, lambda*T/m) "
          "distribution and compute E[X_m] and Var[X_m].")
    p.sub("b",
          "Show that as m -> infinity (Delta -> 0), the distribution of X_m "
          "converges to Poisson(lambda*T). "
          "Use the fact that the Binomial PMF P(X_m = n) = C(m,n)*(lambda*T/m)^n"
          "*(1 - lambda*T/m)^(m-n) approaches (lambda*T)^n * e^(-lambda*T) / n! "
          "as m -> infinity by applying the limit (1 - x/m)^m -> e^(-x).")
    p.sub("c",
          "Write the forward (Kolmogorov) differential equations for the "
          "Poisson process. Let p_j(t) = P(N(t) = j). "
          "By considering what can happen in a small interval [t, t+Delta]:\n"
          "  - if N(t) = j, no arrival in Delta (prob ~ 1-lambda*Delta): stay at j\n"
          "  - if N(t) = j-1, one arrival in Delta (prob ~ lambda*Delta): go to j\n"
          "Derive dp_j(t)/dt = -lambda*p_j(t) + lambda*p_{j-1}(t) for j >= 1, "
          "and verify that p_j(t) = (lambda*t)^j * e^(-lambda*t) / j! "
          "satisfies this equation.")
    p.save(qp(S, "Question_Set_1.pdf"))


def poisson_a():
    S = "Poisson_Process"
    p = ExamPDF("Poisson Process  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Sales rate and expected time to 10th sale:")
    p.txt("Thinning property: if arrivals are Poisson(lambda) and each is\n"
          "independently kept with probability p, the kept arrivals form a\n"
          "Poisson process with rate lambda' = lambda * p.\n\n"
          "  lambda' = 5 * 0.4 = 2 sales per hour\n\n"
          "The time of the n-th sale, S_n = X_1 + ... + X_n, where each\n"
          "X_k ~ Exponential(lambda') are i.i.d. inter-sale times.\n\n"
          "  E[S_10] = E[X_1] + ... + E[X_10] = 10 * (1/lambda')\n"
          "           = 10 * (1/2) = 5 hours")

    p.AL("b)  P(no sales in first hour):")
    p.txt("Using the Poisson PMF with rate lambda' = 2, time t = 1, n = 0:\n\n"
          "  P(N(1) = 0) = (lambda'*1)^0 * e^(-lambda'*1) / 0!\n"
          "              = 1 * e^(-2) / 1\n"
          "              = e^(-2)\n"
          "  ~ 0.1353\n\n"
          "There is about a 13.5% chance of making no sales in the first hour.")

    p.AL("c)  P(exactly 3 sales in first 2 hours):")
    p.txt("Using the Poisson PMF with rate lambda' = 2, time t = 2, n = 3:\n\n"
          "  P(N(2) = 3) = (lambda'*2)^3 * e^(-lambda'*2) / 3!\n"
          "              = (2*2)^3 * e^(-4) / 6\n"
          "              = 4^3 * e^(-4) / 6\n"
          "              = 64 * e^(-4) / 6\n"
          "  e^(-4) ~ 0.01832\n"
          "  P(N(2) = 3) ~ 64 * 0.01832 / 6 ~ 1.1725 / 6 ~ 0.1954\n\n"
          "There is about a 19.5% chance of exactly 3 sales in the first 2 hours.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Distribution of S_1 (time of first call):")
    p.txt("S_1 > t  means  no calls arrive in [0, t],  i.e.  N(t) = 0.\n\n"
          "  P(S_1 > t) = P(N(t) = 0)\n"
          "             = (lambda*t)^0 * e^(-lambda*t) / 0!\n"
          "             = e^(-lambda*t)\n\n"
          "This is exactly the survival function of an Exponential(lambda)\n"
          "distribution:  P(Exp(lambda) > t) = e^(-lambda*t).\n"
          "Therefore S_1 ~ Exponential(lambda = 4 calls/hour).  (OK)")

    p.AL("b)  P(first call within 15 minutes = 0.25 hours):")
    p.txt("  P(S_1 <= 0.25) = 1 - P(S_1 > 0.25)\n"
          "                 = 1 - e^(-lambda * 0.25)\n"
          "                 = 1 - e^(-4 * 0.25)\n"
          "                 = 1 - e^(-1)\n"
          "  ~ 1 - 0.3679 = 0.6321\n\n"
          "There is about a 63.2% chance of the first call arriving within 15 minutes.")

    p.AL("c)  Waiting time from S_1 to S_2:")
    p.txt("Key property used: INDEPENDENT INCREMENTS.\n\n"
          "The number of calls in any interval depends only on the LENGTH\n"
          "of the interval, not on when it starts or what happened before.\n"
          "In particular, the time from S_1 to S_2 (the 2nd inter-arrival\n"
          "time X_2) is independent of S_1 and has the SAME distribution:\n\n"
          "  X_2 = S_2 - S_1 ~ Exponential(lambda = 4)\n\n"
          "This is the MEMORYLESS property of the exponential distribution.\n\n"
          "  E[S_2] = E[S_1] + E[X_2] = 1/lambda + 1/lambda = 2/lambda\n"
          "         = 2/4 = 0.5 hours = 30 minutes")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Binomial model X_m ~ Binomial(m, lambda*T/m):")
    p.txt("In each of the m sub-intervals, there is either 0 or 1 arrival,\n"
          "each with probability p_m = lambda*T/m. The total count X_m is\n"
          "the sum of m independent Bernoulli(p_m) trials:\n\n"
          "  X_m ~ Binomial(m, lambda*T/m)\n\n"
          "  E[X_m] = m * p_m = m * (lambda*T/m) = lambda*T\n\n"
          "  Var[X_m] = m * p_m * (1 - p_m)\n"
          "           = lambda*T * (1 - lambda*T/m)\n"
          "           -> lambda*T  as m -> infinity")

    p.AL("b)  Convergence to Poisson(lambda*T) as m -> infinity:")
    p.txt("Binomial PMF for a fixed n:\n\n"
          "  P(X_m = n) = C(m,n) * (lambda*T/m)^n * (1 - lambda*T/m)^(m-n)\n\n"
          "Expand each factor as m -> infinity:\n\n"
          "  C(m,n) = m*(m-1)*...*(m-n+1) / n!\n"
          "         ~ m^n / n!              (for fixed n, large m)\n\n"
          "  (lambda*T/m)^n = (lambda*T)^n / m^n\n\n"
          "  (1 - lambda*T/m)^(m-n) ~ (1 - lambda*T/m)^m\n"
          "                         -> e^(-lambda*T)   as m -> infinity\n"
          "         [using the standard limit: (1 - x/m)^m -> e^(-x)]\n\n"
          "Combining:\n"
          "  P(X_m = n) -> (m^n / n!) * ((lambda*T)^n / m^n) * e^(-lambda*T)\n"
          "              = (lambda*T)^n * e^(-lambda*T) / n!\n\n"
          "This is exactly the Poisson(lambda*T) PMF.  (OK)")

    p.AL("c)  Forward equations and verification:")
    p.txt("Derivation of dp_j(t)/dt:\n\n"
          "In the small interval [t, t+Delta]:\n"
          "  P(N(t+Delta)=j) = P(N(t)=j) * P(0 arrivals in Delta)\n"
          "                  + P(N(t)=j-1) * P(1 arrival in Delta)\n"
          "                  + P(N(t)<=j-2) * P(2+ arrivals in Delta)\n\n"
          "Using P(0 arrivals in Delta) = 1 - lambda*Delta + o(Delta)\n"
          "and   P(1 arrival in Delta)  = lambda*Delta + o(Delta):\n\n"
          "  p_j(t+Delta) = p_j(t)*(1-lambda*Delta) + p_{j-1}(t)*(lambda*Delta) + o(Delta)\n\n"
          "Rearrange and divide by Delta, then take Delta -> 0:\n\n"
          "  dp_j(t)/dt = -lambda*p_j(t) + lambda*p_{j-1}(t)   for j >= 1\n\n"
          "Verification that p_j(t) = (lambda*t)^j * e^(-lambda*t) / j! satisfies this:\n\n"
          "  Left side:  dp_j/dt\n"
          "    = d/dt [ (lambda*t)^j * e^(-lambda*t) / j! ]\n"
          "    = [ j*lambda*(lambda*t)^(j-1)*e^(-lambda*t)\n"
          "        - lambda*(lambda*t)^j * e^(-lambda*t) ] / j!\n"
          "    = lambda*e^(-lambda*t) / j! * [ j*(lambda*t)^(j-1) - (lambda*t)^j ]\n\n"
          "  Right side:  -lambda*p_j + lambda*p_{j-1}\n"
          "    = -lambda*(lambda*t)^j*e^(-lambda*t)/j!\n"
          "      + lambda*(lambda*t)^(j-1)*e^(-lambda*t)/(j-1)!\n"
          "    = lambda*e^(-lambda*t) * [ -(lambda*t)^j/j! + (lambda*t)^(j-1)/(j-1)! ]\n"
          "    = lambda*e^(-lambda*t)/j! * [ -(lambda*t)^j + j*(lambda*t)^(j-1) ]\n\n"
          "  Left side = Right side  (OK)\n"
          "The Poisson PMF satisfies the forward equations.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":
    print("\n=== Folder 2026-04-09: Chapman-Kolmogorov | Diagonalization | Poisson Process ===\n")
    print("Generating Question Sets...")
    ck_diag_q()
    poisson_q()

    print("\nGenerating Answer Keys...")
    ck_diag_a()
    poisson_a()

    print("\nDone. 4 PDFs created.")
