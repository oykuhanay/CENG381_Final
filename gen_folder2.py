#!/usr/bin/env python3
"""
CENG381 — PDF generator for folder 2026-03-05
Topics: Irreducibility & Periodicity | Random Walks on Graphs | Random Mapping Representation
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
# 1.  IRREDUCIBILITY AND PERIODICITY
# ==============================================================================

def irred_period_q():
    S = "Irreducibility_and_Periodicity"
    p = ExamPDF("Irreducibility and Periodicity  -  Question Set 1")
    p.add_page()

    # ── Q1 ──
    p.Q(1, 30, "Consider the Markov chain with transition matrix:")
    p.mat(["        0     1     2     3",
           "   0 [  0.0   1.0   0.0   0.0 ]",
           "   1 [  0.5   0.0   0.5   0.0 ]",
           "   2 [  0.0   0.5   0.0   0.5 ]",
           "   3 [  0.0   0.0   1.0   0.0 ]"])
    p.sub("a", "Draw the transition diagram for this chain.")
    p.sub("b", "Is the chain irreducible? Justify your answer by identifying "
               "whether every state can reach every other state.")
    p.sub("c", "Compute the period of each state. (Recall: the period of state x "
               "is d(x) = gcd{t >= 1 : P^t(x,x) > 0}.) Is the chain aperiodic?")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35, "Consider the random walk on a 4-cycle: states {0, 1, 2, 3} "
               "arranged in a cycle, where from any state the chain moves "
               "clockwise or counter-clockwise each with probability 1/2.")
    p.sub("a", "Write the transition matrix P for this chain.")
    p.sub("b", "Show that P^2 has a block structure. What does this tell you "
               "about the period of the chain?")
    p.sub("c", "Now consider the lazy version: at each step, with probability "
               "1/2 the chain stays put, and with probability 1/2 it takes a "
               "step on the 4-cycle. Write the new transition matrix Q = "
               "(1/2)I + (1/2)P and show it is aperiodic.")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35, "The PageRank algorithm models web surfing as a Markov chain "
               "on the graph of web pages. It requires the chain to be both "
               "irreducible and aperiodic to guarantee convergence to a unique "
               "stationary distribution.")
    p.sub("a", "Consider a web graph with 4 pages and transition matrix:")
    p.mat(["        1     2     3     4",
           "   1 [  0.0   1.0   0.0   0.0 ]",
           "   2 [  0.5   0.0   0.5   0.0 ]",
           "   3 [  0.0   0.0   0.0   1.0 ]",
           "   4 [  1.0   0.0   0.0   0.0 ]"])
    p.sub("b", "Is this chain irreducible? Identify all communicating classes.")
    p.sub("c", "The standard PageRank fix uses the 'damping factor' d = 0.85: "
               "replace P with P' = (1-d)*(1/n)*J + d*P, where J is the all-ones "
               "matrix and n=4. Write P' and explain why P' is now irreducible "
               "and aperiodic.")
    p.save(qp(S, "Question_Set_1.pdf"))


def irred_period_a():
    S = "Irreducibility_and_Periodicity"
    p = ExamPDF("Irreducibility and Periodicity  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Transition diagram:")
    p.txt("0 <-> 1 <-> 2 <-> 3  (a path graph with bidirectional edges)\n"
          "0 --[1]--> 1 --[0.5]--> 0  and  1 --[0.5]--> 2\n"
          "2 --[0.5]--> 1  and  2 --[0.5]--> 3\n"
          "3 --[1]--> 2")
    p.AL("b)  Irreducibility:")
    p.txt("From 0: 0->1->2->3 (reachable in 3 steps)\n"
          "From 3: 3->2->1->0 (reachable in 3 steps)\n"
          "Every state can reach every other state => the chain is IRREDUCIBLE.")
    p.AL("c)  Periods:")
    p.txt("State 0: can return to 0 in 2 steps (0->1->0), 4 steps, 6 steps, ...\n"
          "         T(0) = {2, 4, 6, ...}  =>  d(0) = gcd(2,4,6,...) = 2\n\n"
          "State 1: can return to 1 in 2 steps (1->0->1 or 1->2->1)\n"
          "         T(1) = {2, 4, 6, ...}  =>  d(1) = 2\n\n"
          "State 2: same argument  =>  d(2) = 2\n\n"
          "State 3: can return to 3 in 2 steps (3->2->3)\n"
          "         T(3) = {2, 4, 6, ...}  =>  d(3) = 2\n\n"
          "All states have period 2. The chain is PERIODIC (not aperiodic).\n"
          "This means the chain alternates between even and odd states and\n"
          "does NOT converge to the stationary distribution.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Transition matrix for random walk on 4-cycle:")
    p.mat(["        0     1     2     3",
           "   0 [  0.0   0.5   0.0   0.5 ]",
           "   1 [  0.5   0.0   0.5   0.0 ]",
           "   2 [  0.0   0.5   0.0   0.5 ]",
           "   3 [  0.5   0.0   0.5   0.0 ]"])
    p.AL("b)  P^2 block structure:")
    p.txt("P^2 row 0: P[0][.] * P = (0.5*P[1] + 0.5*P[3])\n"
          "  = 0.5*(0.5,0,0.5,0) + 0.5*(0.5,0,0.5,0) = (0.5, 0, 0.5, 0)\n"
          "P^2 row 1: (0, 0.5, 0, 0.5)\n"
          "P^2 row 2: (0.5, 0, 0.5, 0)\n"
          "P^2 row 3: (0, 0.5, 0, 0.5)\n\n"
          "P^2 has zero entries wherever P had non-zero entries => the even\n"
          "states {0,2} and odd states {1,3} never communicate in 2 steps.\n"
          "This confirms period d = 2 for all states (returns only happen\n"
          "in even numbers of steps).")
    p.AL("c)  Lazy chain Q = (1/2)I + (1/2)P:")
    p.mat(["        0      1      2      3",
           "   0 [  0.50   0.25   0.00   0.25 ]",
           "   1 [  0.25   0.50   0.25   0.00 ]",
           "   2 [  0.00   0.25   0.50   0.25 ]",
           "   3 [  0.25   0.00   0.25   0.50 ]"])
    p.txt("Aperiodicity of Q: State 0 has P(return to 0 in 1 step) = Q[0][0] = 0.5 > 0.\n"
          "So T(0) contains 1, and gcd of any set containing 1 equals 1.\n"
          "Therefore d(0) = 1, and by irreducibility all states have period 1.\n"
          "The lazy chain is aperiodic. (OK)")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("b)  Communicating classes of the web graph:")
    p.txt("From page 1: 1->2->3->4->1  (cycle: 1 reaches 2, 3, 4)\n"
          "From page 2: 2->1->2 and 2->3->4->1->2 (2 reaches 1,3,4)\n"
          "From page 3: 3->4->1->2->3 (3 reaches 4,1,2)\n"
          "From page 4: 4->1->2->3->4 (4 reaches 1,2,3)\n\n"
          "All 4 pages form one communicating class => the chain IS irreducible.\n"
          "However, it has period 4 (can only return in multiples of 4 steps).\n"
          "So it is irreducible but periodic.")
    p.AL("c)  PageRank fix with damping d = 0.85, n = 4:")
    p.txt("P' = 0.15*(1/4)*J + 0.85*P\n"
          "   = 0.0375*J + 0.85*P\n\n"
          "Each entry of P' = 0.0375 + 0.85*P[i][j]\n"
          "For example, P'[1][1] = 0.0375 + 0.85*0.0 = 0.0375\n"
          "             P'[1][2] = 0.0375 + 0.85*1.0 = 0.8875\n"
          "             P'[1][3] = 0.0375 + 0.85*0.0 = 0.0375\n"
          "             P'[1][4] = 0.0375 + 0.85*0.0 = 0.0375\n\n"
          "Why irreducible: every entry of P' is > 0 (since 0.0375 > 0),\n"
          "so P'^1(i,j) > 0 for ALL pairs (i,j). Every state reaches every\n"
          "other state in exactly one step.\n\n"
          "Why aperiodic: P'[i][i] >= 0.0375 > 0, so T(i) contains 1,\n"
          "meaning gcd = 1 for all states => aperiodic.\n\n"
          "Therefore P' is both irreducible and aperiodic, guaranteeing\n"
          "convergence of the PageRank vector to a unique stationary distribution.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# 2.  RANDOM WALKS ON GRAPHS
# ==============================================================================

def rw_graphs_q():
    S = "Random_Walks_on_Graphs"
    p = ExamPDF("Random Walks on Graphs  -  Question Set 1")
    p.add_page()

    # ── Q1 ──
    p.Q(1, 30, "Consider a simple random walk on a graph G = (V, E). At each "
               "step, if the current state is vertex x, the chain moves to a "
               "uniformly chosen neighbour of x.")
    p.sub("a", "Write a formula for the transition probability P(x, y) in "
               "terms of the degree deg(x) of vertex x.")
    p.sub("b", "Show that the stationary distribution of this random walk is "
               "pi(x) = deg(x) / (2|E|), where |E| is the number of edges.")
    p.sub("c", "Consider the graph below (a 'star' with hub H and leaves "
               "A, B, C, D): H is connected to A, B, C, D; there are no other "
               "edges. Write the transition matrix and find pi for each vertex.")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35, "The random walk on the n-cycle has state space Z_n = {0, 1, ..., n-1} "
               "with transition probabilities:")
    p.mat(["  P(j, k) = 1/2  if k = j+1 mod n",
           "  P(j, k) = 1/2  if k = j-1 mod n",
           "  P(j, k) = 0    otherwise"])
    p.sub("a", "For n = 5 (5-cycle), write the full 5x5 transition matrix P.")
    p.sub("b", "Verify that the uniform distribution pi(j) = 1/5 for all j "
               "is stationary by checking pi * P = pi.")
    p.sub("c", "What is the period of any state in the 5-cycle? Is the period "
               "the same for the 4-cycle? Explain the difference between odd "
               "and even cycles.")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35, "A random mapping representation of a Markov chain with "
               "transition matrix P on state space X is a function "
               "f: X x Lambda -> X together with a Lambda-valued random variable Z, "
               "satisfying P{f(x, Z) = y} = P(x, y) for all x, y.")
    p.sub("a", "For the simple random walk on the 3-cycle (states {0, 1, 2}), "
               "let Lambda = {-1, +1} with Z equally likely to be -1 or +1. "
               "Define f(x, z) = (x + z) mod 3. "
               "Verify that this is a valid random mapping representation.")
    p.sub("b", "Suppose Z_1, Z_2, ... are i.i.d. copies of Z and X_0 has "
               "some distribution mu. Define X_n = f(X_{n-1}, Z_n). "
               "Show that (X_0, X_1, ...) is a Markov chain with transition "
               "matrix P and initial distribution mu.")
    p.sub("c", "For the general n-cycle, propose a random mapping representation "
               "using Z uniform on {-1, +1} and f(x, z) = (x + z) mod n. "
               "What is P(j, k) under this representation?")
    p.save(qp(S, "Question_Set_1.pdf"))


def rw_graphs_a():
    S = "Random_Walks_on_Graphs"
    p = ExamPDF("Random Walks on Graphs  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Transition probability:")
    p.txt("From vertex x, the walk moves to each neighbour y of x with equal\n"
          "probability. There are deg(x) neighbours, so:\n\n"
          "  P(x, y) = 1/deg(x)   if y is a neighbour of x\n"
          "  P(x, y) = 0           otherwise")

    p.AL("b)  Stationary distribution pi(x) = deg(x) / (2|E|):")
    p.txt("We verify pi * P = pi. For any vertex y:\n\n"
          "  (pi * P)(y) = sum_{x} pi(x) * P(x, y)\n"
          "              = sum_{x ~ y} [deg(x)/(2|E|)] * [1/deg(x)]\n"
          "              = sum_{x ~ y} 1/(2|E|)\n"
          "              = deg(y) / (2|E|)\n"
          "              = pi(y)  (OK)\n\n"
          "where the sum is over all x adjacent to y (there are deg(y) such x).\n"
          "Also sum_x pi(x) = sum_x deg(x) / (2|E|) = 2|E|/(2|E|) = 1  (OK)\n"
          "(using the handshaking lemma: sum of degrees = 2|E|).")

    p.AL("c)  Star graph: hub H, leaves A, B, C, D:")
    p.txt("Degrees: deg(H) = 4,  deg(A) = deg(B) = deg(C) = deg(D) = 1\n"
          "Number of edges: |E| = 4\n\n"
          "Transition matrix:\n"
          "  From H: go to A, B, C, or D each with prob 1/4\n"
          "  From A: go to H with prob 1 (only neighbour)\n"
          "  (same for B, C, D)\n")
    p.mat(["        H     A     B     C     D",
           "   H [  0    1/4   1/4   1/4   1/4 ]",
           "   A [  1     0     0     0     0  ]",
           "   B [  1     0     0     0     0  ]",
           "   C [  1     0     0     0     0  ]",
           "   D [  1     0     0     0     0  ]"])
    p.txt("Stationary distribution:\n"
          "  pi(H) = 4/(2*4) = 4/8 = 1/2\n"
          "  pi(A) = pi(B) = pi(C) = pi(D) = 1/(2*4) = 1/8\n\n"
          "Interpretation: the hub is visited 50% of the time in the long run.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  5-cycle transition matrix (states 0,1,2,3,4):")
    p.mat(["        0     1     2     3     4",
           "   0 [  0    1/2    0     0    1/2 ]",
           "   1 [ 1/2    0    1/2    0     0  ]",
           "   2 [  0    1/2    0    1/2    0  ]",
           "   3 [  0     0    1/2    0    1/2 ]",
           "   4 [ 1/2    0     0    1/2    0  ]"])
    p.AL("b)  Verify pi(j) = 1/5 is stationary:")
    p.txt("(pi * P)(y) = sum_j pi(j) * P(j, y)\n"
          "            = (1/5) * sum_j P(j, y)\n"
          "            = (1/5) * (column sum of P at column y)\n\n"
          "Each column of P sums to 1 (each state y has exactly 2 neighbours,\n"
          "each contributing 1/2):\n"
          "  column sum = 1/2 + 1/2 = 1\n"
          "  (pi * P)(y) = (1/5) * 1 = 1/5 = pi(y)  (OK)\n\n"
          "So pi = uniform(1/5) is stationary for the 5-cycle.")

    p.AL("c)  Periods - odd vs even cycles:")
    p.txt("5-cycle (odd n=5):\n"
          "  From state 0, returns are possible in steps 2, 4, 5, 6, ...\n"
          "  In 2 steps: 0->1->0 or 0->4->0  (OK)\n"
          "  In 5 steps: 0->1->2->3->4->0    (OK)\n"
          "  gcd(2, 5) = 1  =>  period d = 1  (aperiodic!)\n\n"
          "4-cycle (even n=4):\n"
          "  Returns from state 0 happen only in even steps: 2, 4, 6, ...\n"
          "  (must travel an even number of edges to return on an even cycle)\n"
          "  gcd(2, 4, ...) = 2  =>  period d = 2\n\n"
          "Key insight: odd cycles are aperiodic; even cycles have period 2.\n"
          "Adding self-loops (lazy version) fixes even-cycle periodicity.")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Verify f(x,z) = (x+z) mod 3 for 3-cycle:")
    p.txt("Lambda = {-1, +1}, P(Z = -1) = P(Z = +1) = 1/2.\n\n"
          "For any state x in {0,1,2} and any state y in {0,1,2}:\n"
          "  P{f(x, Z) = y} = P{(x + Z) mod 3 = y}\n\n"
          "Case y = x+1 mod 3: need Z = +1, prob = 1/2 = P(x, x+1 mod 3)  (OK)\n"
          "Case y = x-1 mod 3: need Z = -1, prob = 1/2 = P(x, x-1 mod 3)  (OK)\n"
          "Case other y:       impossible since Z in {-1,+1}, prob = 0      (OK)\n\n"
          "This matches the 3-cycle transition matrix, so f is a valid\n"
          "random mapping representation.")

    p.AL("b)  (X_0, X_1, ...) is a Markov chain:")
    p.txt("Given X_0, X_1, ..., X_{n-1} = x_{n-1}, we have:\n"
          "  P(X_n = y | X_0,...,X_{n-1}) = P(f(X_{n-1}, Z_n) = y | X_{n-1} = x_{n-1})\n"
          "  = P(f(x_{n-1}, Z_n) = y)   [since Z_n is independent of past]\n"
          "  = P(x_{n-1}, y)             [by the representation property]\n\n"
          "This depends only on X_{n-1}, not the full history => Markov property.\n"
          "The transition matrix is exactly P, and initial dist is mu. (OK)")

    p.AL("c)  General n-cycle representation:")
    p.txt("f(x, z) = (x + z) mod n,  Z uniform on {-1, +1}.\n\n"
          "For any j in Z_n:\n"
          "  P(j, j+1 mod n) = P(Z=+1) = 1/2\n"
          "  P(j, j-1 mod n) = P(Z=-1) = 1/2\n"
          "  P(j, k) = 0  for all other k\n\n"
          "This is exactly the random walk on the n-cycle transition matrix.\n"
          "The key insight is that the i.i.d. sequence (Z_n) generates the\n"
          "chain via the deterministic function f, which is often more\n"
          "convenient for analysis and simulation.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":
    print("\n=== Folder 2026-03-05: Irreducibility/Periodicity | RW on Graphs | Random Mapping ===\n")
    print("Generating Question Sets...")
    irred_period_q()
    rw_graphs_q()

    print("\nGenerating Answer Keys...")
    irred_period_a()
    rw_graphs_a()

    print("\nDone. 4 PDFs created.")
