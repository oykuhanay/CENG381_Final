#!/usr/bin/env python3
"""
CENG381 - PDF generator for folder 2026-03-12
Topics: Classifying States | Hitting Times | Gambler's Ruin | Coupon Collector
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
        """Fixed-width block for matrices, transition rules, etc."""
        self.set_font("Courier", "", 10)
        for line in lines:
            self.set_x(self.l_margin + 20)
            self.cell(0, 5.8, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def defn(self, term, meaning):
        """Notation definition: bold term, then plain meaning."""
        self.set_font("Helvetica", "B", 10.5)
        self.set_x(self.l_margin + 5)
        self.cell(42, 6.5, term)
        self.set_font("Helvetica", "", 10.5)
        self.multi_cell(0, 6.5, meaning)
        self.ln(0.5)

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
# 1.  CLASSIFYING STATES
# ==============================================================================

def classifying_q():
    S = "Classifying_States"
    p = ExamPDF("Classifying States  -  Question Set 1")
    p.add_page()

    # notation box
    p.txt("Notation used throughout this question set:")
    p.defn("P(i, j)",      "one-step probability of moving from state i to state j")
    p.defn("P^n(i, j)",    "n-step probability: probability of being in state j after "
                            "exactly n steps, starting from state i")
    p.defn("Recurrent:",   "state i is recurrent if, starting from i, the chain "
                            "returns to i with probability 1")
    p.defn("Transient:",   "state i is transient if, starting from i, the chain "
                            "has a positive probability of never returning to i")
    p.defn("Absorbing:",   "state i is absorbing if P(i, i) = 1 (the chain never leaves)")
    p.ln(2)

    # ── Q1 ──
    p.Q(1, 30, "Consider the Markov chain with the following 5x5 "
               "transition matrix P (rows = current state, "
               "columns = next state):")
    p.mat(["         0     1     2     3     4",
           "  St 0 [ 0.0   1.0   0.0   0.0   0.0 ]",
           "  St 1 [ 0.5   0.0   0.5   0.0   0.0 ]",
           "  St 2 [ 0.0   0.5   0.0   0.5   0.0 ]",
           "  St 3 [ 0.0   0.0   0.0   0.4   0.6 ]",
           "  St 4 [ 0.0   0.0   0.0   0.0   1.0 ]"])
    p.sub("a", "Draw the transition diagram. Use arrows labelled with "
               "probabilities to show all transitions with positive probability.")
    p.sub("b", "Identify all communicating classes. "
               "(Two states i and j are in the same communicating class if "
               "state i can reach state j AND state j can reach state i, "
               "i.e. P^n(i,j) > 0 and P^m(j,i) > 0 for some n, m >= 1.)")
    p.sub("c", "For each communicating class, state whether it is "
               "positive recurrent, null recurrent, or transient, and "
               "justify your answer.")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35, "A factory machine has four possible states: "
               "Running (R), Degraded (D), Under Repair (U), and Scrapped (S). "
               "Each day the machine transitions according to:")
    p.mat(["  From R: stays R with prob 0.8,  moves to D with prob 0.2",
           "  From D: stays D with prob 0.5,  moves to U with prob 0.3,  moves to S with prob 0.2",
           "  From U: returns to R with prob 0.7,  stays U with prob 0.3",
           "  From S: stays S with prob 1.0  (absorbing)"])
    p.sub("a", "Write the 4x4 transition matrix P with rows and columns "
               "in the order (R, D, U, S).")
    p.sub("b", "Identify all communicating classes and classify each one "
               "as recurrent or transient.")
    p.sub("c", "Starting from state R, what is the probability of eventually "
               "being absorbed into state S? "
               "Let h(R), h(D), h(U) denote the probability of reaching S "
               "starting from R, D, U respectively. Set up and solve the "
               "system of linear equations for h(R), h(D), h(U).")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35, "Consider the Markov chain on {0, 1, 2, 3, 4, 5} with "
               "transition matrix P given by:")
    p.mat(["         0     1     2     3     4     5",
           "  St 0 [ 1/3   2/3   0.0   0.0   0.0   0.0 ]",
           "  St 1 [ 1/3   2/3   0.0   0.0   0.0   0.0 ]",
           "  St 2 [ 0.0   3/5   1/5   1/5   0.0   0.0 ]",
           "  St 3 [ 0.0   0.0   0.0   1/4   3/4   0.0 ]",
           "  St 4 [ 0.0   0.0   0.0   1/2   1/2   0.0 ]",
           "  St 5 [ 0.0   0.0   0.0   0.0   0.0   1.0 ]"])
    p.sub("a", "Draw the transition diagram and identify all communicating "
               "classes.")
    p.sub("b", "Classify each communicating class as positive recurrent, "
               "null recurrent, or transient. Give a brief justification "
               "for each.")
    p.sub("c", "Find the limiting (long-run) state probabilities "
               "pi(0), pi(1), ..., pi(5). "
               "For each transient class, the limiting probability of each "
               "state in that class is 0. For each positive recurrent class, "
               "solve pi * P_class = pi restricted to that class, "
               "with probabilities summing to the weight of that class.")
    p.save(qp(S, "Question_Set_1.pdf"))


def classifying_a():
    S = "Classifying_States"
    p = ExamPDF("Classifying States  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Transition diagram:")
    p.txt("0 --[1.0]--> 1\n"
          "1 --[0.5]--> 0,   1 --[0.5]--> 2\n"
          "2 --[0.5]--> 1,   2 --[0.5]--> 3\n"
          "3 --[0.4]--> 3 (self-loop),   3 --[0.6]--> 4\n"
          "4 --[1.0]--> 4 (self-loop, absorbing)")

    p.AL("b)  Communicating classes:")
    p.txt("Can 0 reach 1? Yes (direct in 1 step).\n"
          "Can 1 reach 0? Yes (1 -> 0 in 1 step).\n"
          "Can 1 reach 2? Yes. Can 2 reach 1? Yes.\n"
          "=> States 0, 1, 2 all communicate: Class A = {0, 1, 2}\n\n"
          "Can 2 reach 3? Yes (2 -> 3). Can 3 reach 2? No (3 only goes to 3 or 4).\n"
          "=> State 3 does NOT communicate with {0,1,2}.\n"
          "Can 3 reach 4? Yes. Can 4 reach 3? No (4 is absorbing).\n"
          "=> Class B = {3}  (singleton).\n"
          "   Class C = {4}  (absorbing, singleton).\n\n"
          "Summary: Class A = {0,1,2},  Class B = {3},  Class C = {4}.")

    p.AL("c)  Classification of each class:")
    p.txt("Class A = {0, 1, 2}:\n"
          "  States 0, 1, 2 can reach state 3 (via 2 -> 3), and once in 3\n"
          "  they can never return to {0,1,2}. So there is a positive probability\n"
          "  of leaving and never returning. => Class A is TRANSIENT.\n\n"
          "Class B = {3}:\n"
          "  State 3 can move to state 4 (prob 0.6), which is absorbing.\n"
          "  So from state 3 there is a positive probability (0.6) of leaving\n"
          "  and never returning. => Class B is TRANSIENT.\n\n"
          "Class C = {4}:\n"
          "  State 4 is absorbing: P(4,4) = 1, it never leaves.\n"
          "  Once entered, the chain stays forever. => Class C is POSITIVE RECURRENT\n"
          "  (and absorbing). Limiting probability: pi(4) = 1.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Transition matrix P (order: R, D, U, S):")
    p.mat(["         R     D     U     S",
           "  R  [  0.8   0.2   0.0   0.0 ]",
           "  D  [  0.0   0.5   0.3   0.2 ]",
           "  U  [  0.7   0.0   0.3   0.0 ]",
           "  S  [  0.0   0.0   0.0   1.0 ]"])

    p.AL("b)  Communicating classes:")
    p.txt("R -> D (prob 0.2), D -> U (prob 0.3), U -> R (prob 0.7).\n"
          "So R, D, U all communicate with each other: Class A = {R, D, U}.\n\n"
          "S is absorbing and cannot reach R, D, or U: Class B = {S}.\n\n"
          "Class A = {R, D, U}: From D, there is a path to S (prob 0.2 direct).\n"
          "Once in S, the chain cannot return to A. => Class A is TRANSIENT.\n\n"
          "Class B = {S}: Absorbing state. => Class B is POSITIVE RECURRENT.")

    p.AL("c)  Absorption probability into S starting from each state:")
    p.txt("Let h(i) = P(eventually reach S | start in state i).\n"
          "Clearly h(S) = 1.\n\n"
          "Balance equations (condition on first step):\n\n"
          "  h(R) = P(R,R)*h(R) + P(R,D)*h(D) + P(R,U)*h(U) + P(R,S)*h(S)\n"
          "       = 0.8*h(R) + 0.2*h(D) + 0.0*h(U) + 0.0\n\n"
          "  h(D) = P(D,D)*h(D) + P(D,U)*h(U) + P(D,S)*1\n"
          "       = 0.5*h(D) + 0.3*h(U) + 0.2\n\n"
          "  h(U) = P(U,R)*h(R) + P(U,U)*h(U)\n"
          "       = 0.7*h(R) + 0.3*h(U)\n\n"
          "Simplify each equation:\n\n"
          "  From h(R): 0.2*h(R) = 0.2*h(D)  =>  h(R) = h(D)   ... (i)\n\n"
          "  From h(D): 0.5*h(D) = 0.3*h(U) + 0.2  =>  h(D) = 0.6*h(U) + 0.4   ... (ii)\n\n"
          "  From h(U): 0.7*h(U) = 0.7*h(R)  =>  h(U) = h(R)   ... (iii)\n\n"
          "From (i) and (iii): h(R) = h(D) = h(U) = h  (all equal).\n\n"
          "Substituting into (ii): h = 0.6*h + 0.4  =>  0.4*h = 0.4  =>  h = 1.\n\n"
          "Result: h(R) = h(D) = h(U) = 1.\n"
          "The machine is GUARANTEED to eventually be scrapped, regardless of\n"
          "starting state (since every class A state is transient and S is the\n"
          "only recurrent state).")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Communicating classes (from transition matrix):")
    p.txt("States 0 and 1:\n"
          "  0 -> 1 (prob 2/3 > 0), 1 -> 0 (prob 1/3 > 0) => 0 and 1 communicate.\n"
          "  Neither 0 nor 1 can reach 2, 3, 4, or 5. => Class A = {0, 1}.\n\n"
          "State 2:\n"
          "  2 -> 1 (prob 3/5) but 1 cannot reach 2. So 2 does NOT communicate\n"
          "  with class A. 2 -> 3 (prob 1/5), 3 cannot reach 2. => Class B = {2}.\n\n"
          "States 3 and 4:\n"
          "  3 -> 4 (prob 3/4), 4 -> 3 (prob 1/2) => 3 and 4 communicate.\n"
          "  Neither can reach 0, 1, 2, or 5. => Class C = {3, 4}.\n\n"
          "State 5:\n"
          "  P(5,5) = 1, absorbing. => Class D = {5}.")

    p.AL("b)  Classification:")
    p.txt("Class A = {0, 1}: A is a closed class (no transitions leave A).\n"
          "  It is finite, irreducible, so it is POSITIVE RECURRENT.\n\n"
          "Class B = {2}: State 2 can reach class A (via 2->1) and class C\n"
          "  (via 2->3). It can never return once it leaves 2 (since A and C\n"
          "  are closed or lead to D). => Class B is TRANSIENT.\n\n"
          "Class C = {3, 4}: It is finite, irreducible, and closed (3 and 4\n"
          "  only transition within {3,4}). => Class C is POSITIVE RECURRENT.\n\n"
          "Class D = {5}: Absorbing. => POSITIVE RECURRENT.")

    p.AL("c)  Limiting state probabilities:")
    p.txt("Transient states: pi(2) = 0 in the limit.\n\n"
          "The chain starting from any state will eventually be absorbed into\n"
          "class A, class C, or class D, depending on the starting state.\n"
          "Since the question asks for limiting probabilities without specifying\n"
          "a starting distribution, we find the stationary distribution within\n"
          "each recurrent class:\n\n"
          "Within Class A = {0, 1}: solve pi_A * P_A = pi_A\n"
          "  P_A = [ [1/3, 2/3], [1/3, 2/3] ]\n"
          "  pi_A(0)*(1/3) + pi_A(1)*(1/3) = pi_A(0)\n"
          "  pi_A(0) + pi_A(1) = 1\n"
          "  From row 0: (2/3)*pi_A(0) = (1/3)*pi_A(1) => pi_A(1) = 2*pi_A(0)\n"
          "  => pi_A(0) = 1/3,  pi_A(1) = 2/3\n\n"
          "Within Class C = {3, 4}: solve pi_C * P_C = pi_C\n"
          "  P_C = [ [1/4, 3/4], [1/2, 1/2] ]\n"
          "  pi_C(3) = (1/4)*pi_C(3) + (1/2)*pi_C(4)\n"
          "  pi_C(3) + pi_C(4) = 1\n"
          "  (3/4)*pi_C(3) = (1/2)*pi_C(4) => pi_C(4) = (3/2)*pi_C(3)\n"
          "  => pi_C(3) = 2/5,  pi_C(4) = 3/5\n\n"
          "Class D = {5}: pi_D(5) = 1.\n\n"
          "The overall long-run distribution depends on the starting state.\n"
          "Starting from state 2 (transient), the chain is eventually absorbed\n"
          "into A (with some probability alpha) or C or D (with prob 1-alpha).")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# 2.  HITTING PROBABILITIES AND EXPECTED HITTING TIMES
# ==============================================================================

def hitting_q():
    S = "Hitting_Times"
    p = ExamPDF("Hitting Probabilities and Expected Hitting Times  -  Question Set 1")
    p.add_page()

    p.txt("Notation used in this question set:")
    p.defn("T_A",       "the first time the chain enters set A: "
                         "T_A = min{n >= 0 : X_n is in A}")
    p.defn("h(i, A)",   "hitting probability: P(chain eventually enters A | X_0 = i)")
    p.defn("tau(i, j)", "expected hitting time: E[first time to reach j | start at i]")
    p.ln(2)

    # ── Q1 ──
    p.Q(1, 30, "Consider the Markov chain with states {1, 2, 3, 4} "
               "and transition diagram:")
    p.mat(["  1 --[1/2]--> 2,   1 --[1/2]--> 1  (self-loop)",
           "  2 --[1/2]--> 1,   2 --[1/2]--> 3",
           "  3 --[1/2]--> 2,   3 --[1/2]--> 4",
           "  4 --[1.0]--> 4  (absorbing)"])
    p.sub("a", "Write the transition matrix P for this chain.")
    p.sub("b", "Starting from state 2, what is the expected time to first "
               "reach state 4? "
               "Define tau(i) = E[steps to reach 4 | X_0 = i] for i = 1, 2, 3. "
               "Note tau(4) = 0. Set up the system of equations for tau(1), "
               "tau(2), tau(3) by conditioning on the first step.")
    p.sub("c", "Solve the system from part (b) and state tau(2).")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35, "A fair coin is flipped repeatedly. Let X_n record the last "
               "symbol seen, tracking progress toward the pattern HTH "
               "(Heads-Tails-Heads). We model this with states representing "
               "how much of the target pattern has been matched so far:")
    p.mat(["  State 0:  no progress  (starting state)",
           "  State 1:  last flip was H  (matched 'H')",
           "  State 2:  last two flips were HT  (matched 'HT')",
           "  State 3:  last three flips were HTH  (done - absorbing)"])
    p.txt("The transition probabilities (each flip is H with prob 1/2, "
          "T with prob 1/2) are:")
    p.mat(["  From state 0: flip H -> go to state 1 (prob 1/2)",
           "                flip T -> stay at state 0 (prob 1/2)",
           "  From state 1: flip T -> go to state 2 (prob 1/2)",
           "                flip H -> stay at state 1 (prob 1/2)",
           "  From state 2: flip H -> go to state 3 (prob 1/2)",
           "                flip T -> go to state 0 (prob 1/2)",
           "  From state 3: stay at state 3 (absorbing)"])
    p.sub("a", "Write the 4x4 transition matrix P.")
    p.sub("b", "Let tau(i) = expected number of additional flips to reach "
               "state 3, starting from state i. Note tau(3) = 0. "
               "Write the system of equations for tau(0), tau(1), tau(2).")
    p.sub("c", "Solve the system to find tau(0), the expected number of "
               "coin flips until the pattern HTH first appears.")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35, "Consider the Coupon Collector problem: a cereal box contains "
               "one coupon from a set of n distinct coupons, chosen uniformly "
               "at random. A collector buys boxes until they have collected "
               "all n distinct coupons.")
    p.sub("a", "Model this as a Markov chain where the state X_k = number of "
               "distinct coupons collected after k boxes. Write the transition "
               "probability P(i, i+1) and P(i, i) for 0 <= i <= n-1.")
    p.sub("b", "Let W_i = number of additional boxes needed to go from i "
               "distinct coupons to i+1 distinct coupons. "
               "Show that W_i follows a geometric distribution with success "
               "probability (n-i)/n, so that E[W_i] = n/(n-i).")
    p.sub("c", "Let T = total number of boxes needed to collect all n coupons. "
               "Show that E[T] = n * (1 + 1/2 + 1/3 + ... + 1/n). "
               "For n = 5, compute E[T] numerically.")
    p.save(qp(S, "Question_Set_1.pdf"))


def hitting_a():
    S = "Hitting_Times"
    p = ExamPDF("Hitting Probabilities and Expected Hitting Times  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Transition matrix P:")
    p.mat(["         1     2     3     4",
           "  St 1 [ 1/2   1/2   0.0   0.0 ]",
           "  St 2 [ 1/2   0.0   1/2   0.0 ]",
           "  St 3 [ 0.0   1/2   0.0   1/2 ]",
           "  St 4 [ 0.0   0.0   0.0   1.0 ]"])

    p.AL("b)  System of equations for tau(i) = E[steps to reach 4 | start at i]:")
    p.txt("Condition on the first step from each state:\n\n"
          "  tau(1) = 1 + (1/2)*tau(1) + (1/2)*tau(2)\n"
          "           [1 step taken, then either still at 1 (prob 1/2)\n"
          "            or moved to 2 (prob 1/2)]\n\n"
          "  tau(2) = 1 + (1/2)*tau(1) + (1/2)*tau(3)\n"
          "           [1 step taken, then moved to 1 or 3 with equal prob]\n\n"
          "  tau(3) = 1 + (1/2)*tau(2) + (1/2)*0\n"
          "           [1 step taken, then moved to 2 (prob 1/2) or absorbed at 4 (prob 1/2)]\n\n"
          "  tau(4) = 0  (already at target)")

    p.AL("c)  Solve the system:")
    p.txt("Rearrange each equation by moving terms with tau to the left:\n\n"
          "  tau(1) - (1/2)*tau(1) = 1 + (1/2)*tau(2)\n"
          "  (1/2)*tau(1) = 1 + (1/2)*tau(2)\n"
          "  tau(1) = 2 + tau(2)   ... (i)\n\n"
          "  tau(3) = 1 + (1/2)*tau(2)   ... (ii)\n\n"
          "  tau(2) = 1 + (1/2)*tau(1) + (1/2)*tau(3)   ... (iii)\n\n"
          "Substitute (i) into (iii):\n"
          "  tau(2) = 1 + (1/2)*(2 + tau(2)) + (1/2)*tau(3)\n"
          "  tau(2) = 1 + 1 + (1/2)*tau(2) + (1/2)*tau(3)\n"
          "  (1/2)*tau(2) = 2 + (1/2)*tau(3)   ... (iv)\n\n"
          "Substitute (ii) into (iv):\n"
          "  (1/2)*tau(2) = 2 + (1/2)*(1 + (1/2)*tau(2))\n"
          "  (1/2)*tau(2) = 2 + 1/2 + (1/4)*tau(2)\n"
          "  (1/4)*tau(2) = 5/2\n"
          "  tau(2) = 10\n\n"
          "Back-substitute:\n"
          "  tau(3) = 1 + (1/2)*10 = 6\n"
          "  tau(1) = 2 + 10 = 12\n\n"
          "Answer: tau(2) = 10 steps on average to reach state 4 from state 2.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Transition matrix P (states 0, 1, 2, 3):")
    p.mat(["         0     1     2     3",
           "  St 0 [ 1/2   1/2   0.0   0.0 ]",
           "  St 1 [ 0.0   1/2   1/2   0.0 ]",
           "  St 2 [ 1/2   0.0   0.0   1/2 ]",
           "  St 3 [ 0.0   0.0   0.0   1.0 ]"])

    p.AL("b)  System of equations for tau(i) = E[flips to reach state 3 | start at i]:")
    p.txt("  tau(0) = 1 + (1/2)*tau(0) + (1/2)*tau(1)\n"
          "           [flip T -> stay at 0; flip H -> go to 1]\n\n"
          "  tau(1) = 1 + (1/2)*tau(1) + (1/2)*tau(2)\n"
          "           [flip H -> stay at 1; flip T -> go to 2]\n\n"
          "  tau(2) = 1 + (1/2)*tau(0) + (1/2)*0\n"
          "           [flip T -> back to 0; flip H -> go to 3 (done)]\n\n"
          "  tau(3) = 0  (pattern complete, no more flips needed)")

    p.AL("c)  Solve for tau(0):")
    p.txt("Simplify each equation:\n\n"
          "  tau(0): (1/2)*tau(0) = 1 + (1/2)*tau(1)\n"
          "    => tau(0) = 2 + tau(1)   ... (i)\n\n"
          "  tau(1): (1/2)*tau(1) = 1 + (1/2)*tau(2)\n"
          "    => tau(1) = 2 + tau(2)   ... (ii)\n\n"
          "  tau(2) = 1 + (1/2)*tau(0)   ... (iii)\n\n"
          "Substitute (i) and (ii) into (iii):\n"
          "  tau(2) = 1 + (1/2)*(2 + tau(1))\n"
          "         = 1 + 1 + (1/2)*tau(1)\n"
          "         = 2 + (1/2)*(2 + tau(2))\n"
          "         = 2 + 1 + (1/2)*tau(2)\n"
          "  (1/2)*tau(2) = 3  =>  tau(2) = 6\n\n"
          "Back-substitute:\n"
          "  tau(1) = 2 + 6 = 8\n"
          "  tau(0) = 2 + 8 = 10\n\n"
          "Answer: On average, it takes 10 coin flips to see the pattern HTH.")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Transition probabilities:")
    p.txt("When the collector already has i distinct coupons (i < n):\n\n"
          "  P(i, i+1) = (n - i) / n\n"
          "    [probability that the new box contains a coupon not yet seen]\n\n"
          "  P(i, i)   = i / n\n"
          "    [probability that the new box contains a duplicate]\n\n"
          "The chain has absorbing state n (all coupons collected).")

    p.AL("b)  Geometric distribution for W_i:")
    p.txt("When currently holding i distinct coupons, each new box independently\n"
          "gives a new coupon with probability p_i = (n-i)/n, or a duplicate\n"
          "with probability 1 - p_i = i/n.\n\n"
          "W_i = number of boxes until the next new coupon is found.\n"
          "Each box is an independent Bernoulli trial with success prob p_i.\n"
          "=> W_i is Geometric(p_i), and E[W_i] = 1/p_i = n/(n-i).")

    p.AL("c)  Total expected time E[T]:")
    p.txt("T = W_0 + W_1 + W_2 + ... + W_{n-1}\n"
          "  (total boxes = sum of waiting times for each new coupon)\n\n"
          "By linearity of expectation:\n"
          "  E[T] = E[W_0] + E[W_1] + ... + E[W_{n-1}]\n"
          "       = n/n + n/(n-1) + n/(n-2) + ... + n/1\n"
          "       = n * (1/n + 1/(n-1) + ... + 1/1)\n"
          "       = n * (1 + 1/2 + 1/3 + ... + 1/n)  (OK)\n\n"
          "For n = 5:\n"
          "  E[T] = 5 * (1 + 1/2 + 1/3 + 1/4 + 1/5)\n"
          "       = 5 * (60/60 + 30/60 + 20/60 + 15/60 + 12/60)\n"
          "       = 5 * (137/60)\n"
          "       = 685/60\n"
          "  ~ 11.42 boxes on average to collect all 5 distinct coupons.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# 3.  GAMBLER'S RUIN
# ==============================================================================

def gamblers_q():
    S = "Gamblers_Ruin"
    p = ExamPDF("Gambler's Ruin  -  Question Set 1")
    p.add_page()

    p.txt("Notation used in this question set:")
    p.defn("N",        "total capital in the game (upper boundary)")
    p.defn("k",        "gambler's current fortune (starting state)")
    p.defn("R(k)",     "probability that the gambler reaches N before 0, starting with k")
    p.defn("f(k)",     "expected number of steps until absorption, starting with k")
    p.defn("p",        "probability of winning a single bet (gaining 1)")
    p.defn("q = 1-p",  "probability of losing a single bet (losing 1)")
    p.ln(2)

    # ── Q1 ──
    p.Q(1, 30, "A gambler starts with k = 3 dollars and plays a fair coin-flip "
               "game (p = q = 1/2) against an opponent who starts with N - k = 7 "
               "dollars, so N = 10. At each step the gambler wins 1 dollar (prob 1/2) "
               "or loses 1 dollar (prob 1/2). The game ends when one player is broke.")
    p.sub("a", "Write the recurrence relation for R(k), the probability of the "
               "gambler reaching N = 10 before 0, starting with k dollars. "
               "State the boundary conditions R(0) and R(N).")
    p.sub("b", "Solve the recurrence to find R(k) for all k = 0, 1, ..., 10. "
               "Use the formula for the unbiased case: R(k) = k / N.")
    p.sub("c", "What is R(3)? Interpret this result in plain language: "
               "what are the gambler's chances of winning the game?")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35, "Now consider the biased version of Gambler's Ruin with N = 6, "
               "starting fortune k = 2, winning probability p = 1/3, "
               "and losing probability q = 2/3.")
    p.sub("a", "Write the recurrence R(k) = p * R(k+1) + q * R(k-1) with "
               "boundary conditions R(0) = 0 (ruin) and R(N) = 1 (win). "
               "Show that the characteristic equation is p*r^2 - r + q = 0 "
               "with roots r_1 = 1 and r_2 = q/p.")
    p.sub("b", "Since r_1 != r_2 (because p != q), write the general solution "
               "R(k) = A * 1^k + B * (q/p)^k = A + B*(q/p)^k. "
               "Apply the boundary conditions to find A and B.")
    p.sub("c", "Compute R(2) (the gambler's probability of winning from k=2). "
               "Is this greater or less than the unbiased value of k/N = 2/6 = 1/3? "
               "Explain why.")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35, "Return to the unbiased game (p = q = 1/2) with N = 8 and "
               "starting fortune k.")
    p.sub("a", "Write the recurrence for f(k), the expected number of steps "
               "until the game ends (absorption at 0 or N), starting at k. "
               "State the boundary conditions f(0) = f(N) = 0.")
    p.sub("b", "Solve the recurrence. Note that the homogeneous part has "
               "repeated root r = 1, so the particular solution has the form "
               "c*k. Show that the full solution is f(k) = k*(N - k).")
    p.sub("c", "From which starting fortune k (among k = 1,...,7) does the "
               "game last longest on average? Compute f(k) for k = 2, 4, 6 "
               "and verify the formula f(k) = k*(8 - k).")
    p.save(qp(S, "Question_Set_1.pdf"))


def gamblers_a():
    S = "Gamblers_Ruin"
    p = ExamPDF("Gambler's Ruin  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Recurrence and boundary conditions:")
    p.txt("At each step from state k (1 <= k <= N-1), the gambler moves to\n"
          "k+1 (prob p = 1/2) or k-1 (prob q = 1/2). Conditioning on the\n"
          "first step:\n\n"
          "  R(k) = (1/2)*R(k+1) + (1/2)*R(k-1)   for k = 1, 2, ..., N-1\n\n"
          "Boundary conditions:\n"
          "  R(0) = 0   [gambler is ruined, probability of winning = 0]\n"
          "  R(N) = 1   [gambler has won all N dollars, probability of winning = 1]")

    p.AL("b)  Solution for the unbiased case:")
    p.txt("Rewrite the recurrence as:\n"
          "  2*R(k) = R(k+1) + R(k-1)\n"
          "  R(k+1) - R(k) = R(k) - R(k-1)  (constant differences)\n\n"
          "So R(k) is linear in k:\n"
          "  R(k) = A + B*k\n\n"
          "Applying boundary conditions:\n"
          "  R(0) = A = 0  =>  A = 0\n"
          "  R(N) = B*N = 1  =>  B = 1/N\n\n"
          "  R(k) = k/N   for k = 0, 1, ..., N.")

    p.AL("c)  Result for k=3, N=10:")
    p.txt("R(3) = 3/10 = 0.30\n\n"
          "Interpretation: Starting with 3 dollars against an opponent with\n"
          "7 dollars in a fair game, the gambler has only a 30% chance of\n"
          "winning all 10 dollars before going broke. The opponent, starting\n"
          "with more capital, has a 70% chance of winning. This illustrates\n"
          "how having less capital puts a gambler at a serious disadvantage,\n"
          "even in a fair game.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  Recurrence and characteristic equation:")
    p.txt("  R(k) = (1/3)*R(k+1) + (2/3)*R(k-1)\n\n"
          "Rearranging: (1/3)*R(k+1) - R(k) + (2/3)*R(k-1) = 0\n"
          "Multiply through by 3: R(k+1) - 3*R(k) + 2*R(k-1) = 0\n\n"
          "Try solution R(k) = r^k. Substituting:\n"
          "  r^(k+1) - 3*r^k + 2*r^(k-1) = 0\n"
          "  Divide by r^(k-1): r^2 - 3r + 2 = 0\n"
          "  (r - 1)(r - 2) = 0  =>  r_1 = 1, r_2 = 2\n\n"
          "Note: r_2 = 2 = q/p = (2/3)/(1/3). This matches the formula r_2 = q/p.")

    p.AL("b)  General solution and boundary conditions:")
    p.txt("General solution: R(k) = A * 1^k + B * (q/p)^k = A + B * 2^k\n\n"
          "Apply R(0) = 0:  A + B*2^0 = 0  =>  A + B = 0  =>  A = -B\n\n"
          "Apply R(N) = R(6) = 1:  A + B*2^6 = 1\n"
          "  -B + 64*B = 1  =>  63*B = 1  =>  B = 1/63\n"
          "  A = -1/63\n\n"
          "  R(k) = (-1/63) + (1/63)*2^k = (2^k - 1) / 63")

    p.AL("c)  R(2) and comparison with unbiased case:")
    p.txt("R(2) = (2^2 - 1) / 63 = (4 - 1) / 63 = 3/63 = 1/21 ~ 0.048\n\n"
          "Unbiased value would be: k/N = 2/6 = 1/3 ~ 0.333\n\n"
          "R(2) = 1/21 << 1/3: the biased game is MUCH worse for the gambler.\n\n"
          "Reason: with p = 1/3 < q = 2/3, each bet is unfavorable. The gambler\n"
          "loses money on average each step, making ruin nearly certain when\n"
          "starting with only 2 out of 6 dollars. The unfavorable odds compound\n"
          "the disadvantage of having less capital.")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  Recurrence for f(k):")
    p.txt("Conditioning on the first step (each direction with prob 1/2):\n\n"
          "  f(k) = 1 + (1/2)*f(k+1) + (1/2)*f(k-1)   for k = 1, ..., N-1\n\n"
          "  [We take 1 step, then continue from k+1 or k-1.]\n\n"
          "Boundary conditions:\n"
          "  f(0) = 0   [already absorbed at 0, game over]\n"
          "  f(N) = 0   [already absorbed at N, game over]")

    p.AL("b)  Solve the recurrence:")
    p.txt("Rearranging: (1/2)*f(k+1) - f(k) + (1/2)*f(k-1) = -1\n"
          "Multiply by 2: f(k+1) - 2*f(k) + f(k-1) = -2\n\n"
          "Homogeneous equation: f(k+1) - 2*f(k) + f(k-1) = 0\n"
          "  Characteristic equation: r^2 - 2r + 1 = (r-1)^2 = 0\n"
          "  Repeated root r = 1 => homogeneous solution: f_h(k) = A + B*k\n\n"
          "Particular solution for -2 on the right side:\n"
          "  Try f_p(k) = C*k^2 (since k^0 and k^1 already in homogeneous part)\n"
          "  Substitute: C*(k+1)^2 - 2C*k^2 + C*(k-1)^2 = -2\n"
          "  C*(k^2+2k+1 - 2k^2 + k^2-2k+1) = -2\n"
          "  C * 2 = -2  =>  C = -1\n"
          "  f_p(k) = -k^2\n\n"
          "General solution: f(k) = A + B*k - k^2\n\n"
          "Apply f(0) = 0: A = 0\n"
          "Apply f(N) = 0: B*N - N^2 = 0  =>  B = N\n\n"
          "  f(k) = N*k - k^2 = k*(N - k)  (OK)")

    p.AL("c)  Values for N=8:")
    p.txt("f(k) = k*(8 - k)\n\n"
          "  f(2) = 2*(8-2) = 2*6 = 12 steps\n"
          "  f(4) = 4*(8-4) = 4*4 = 16 steps  (maximum: k = N/2)\n"
          "  f(6) = 6*(8-6) = 6*2 = 12 steps\n\n"
          "The game lasts longest on average when the gambler starts with\n"
          "k = N/2 = 4 dollars (equal capital on both sides). By symmetry,\n"
          "f(k) = f(N-k), and the maximum expected duration is (N/2)^2 = 16\n"
          "steps when N = 8.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":
    print("\n=== Folder 2026-03-12: Classifying States | Hitting Times | Gambler's Ruin | Coupon Collector ===\n")
    print("Generating Question Sets...")
    classifying_q()
    hitting_q()
    gamblers_q()

    print("\nGenerating Answer Keys...")
    classifying_a()
    hitting_a()
    gamblers_a()

    print("\nDone. 6 PDFs created.")
