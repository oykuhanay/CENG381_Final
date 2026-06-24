#!/usr/bin/env python3
"""
CENG381 - V2 Generator  |  Folder 2026-03-05
Topics : Irreducibility & Periodicity  |  Random Walks on Graphs
         |  Random Mapping Representation
Outputs: Generated_Questions_V2/   and   Answer_Keys_V2/
"""
import os
from fpdf import FPDF

BASE = "/Users/apple/Desktop/CENG381"
QQ   = os.path.join(BASE, "Generated_Questions_V2")
AK   = os.path.join(BASE, "Answer_Keys_V2")
SFNS = "/System/Library/Fonts/SFNS.ttf"
MONO = "/System/Library/Fonts/SFNSMono.ttf"

# Unsupported chars in SFNSMono — translate before mono rendering
_MONO_SUB = str.maketrans(
    "₀₁₂₃₄₅₆₇₈₉ᵗᵀ⁰¹²³⁴⁵⁶⁷⁸⁹ⁿₙ",
    "0123456789tT0123456789nn"
)

# ── PDF helper ────────────────────────────────────────────────────────────────
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
        self.set_text_color(0, 0, 0)
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
# 1.  IRREDUCIBILITY AND PERIODICITY
# ══════════════════════════════════════════════════════════════════════════════

def irred_period_q():
    S = "Irreducibility_and_Periodicity"
    p = ExamPDF("Irreducibility and Periodicity  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Consider the Markov chain on states {1, 2, 3, 4} whose "
        "transition matrix is the deterministic cyclic shift:")
    p.mat([
        "        1    2    3    4",
        "  1  [  0    1    0    0  ]",
        "  2  [  0    0    1    0  ]",
        "  3  [  0    0    0    1  ]",
        "  4  [  1    0    0    0  ]",
    ])
    p.sub("a",
          "Draw the transition diagram.  Is the chain irreducible?  "
          "Justify by verifying that every state is reachable from every "
          "other state.")
    p.sub("b",
          "Find the period of state 1.  Recall: the period is "
          "gcd{ t ≥ 1 : P^t(1,1) > 0 }.  "
          "List the set T(1) and compute its gcd.")
    p.sub("c",
          "Compute P⁴ and P⁵.  Does the chain converge to its stationary "
          "distribution π = (1/4, 1/4, 1/4, 1/4)?  "
          "Explain why the period prevents convergence.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "Consider the Markov chain on states {0, 1, 2, 3} with:")
    p.mat([
        "  P(0,1) = 1,   P(1,2) = 1,   P(2,3) = 1",
        "  P(3,0) = 1/2,              P(3,2) = 1/2",
        "  All other entries are 0.",
    ])
    p.sub("a",
          "Write the 4×4 transition matrix P explicitly.  "
          "Is the chain irreducible?")
    p.sub("b",
          "Find the period of state 0.  "
          "Identify all return times T(0) = { t : P^t(0,0) > 0 } "
          "and compute gcd(T(0)).")
    p.sub("c",
          "Find the stationary distribution π by solving π·P = π.  "
          "What is the expected return time to state 0?")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "Take the chain from Q2.  Because it has period > 1, it does not "
        "converge.  Define the lazy version  Q = (1/2)·I + (1/2)·P.")
    p.sub("a",
          "Write the 4×4 matrix Q explicitly.")
    p.sub("b",
          "Show that state 0 has period 1 in Q, i.e., that "
          "Q(0,0) > 0 so T(0) contains t=1, making gcd(T(0))=1.")
    p.sub("c",
          "The stationary distribution of Q is the same as P.  "
          "Verify this: show that if π satisfies π·P = π, "
          "then π also satisfies π·Q = π.  "
          "State the long-run fraction of time the chain spends in each state.")

    p.save(qp(S, "Practice_1.pdf"))


def irred_period_a():
    S = "Irreducibility_and_Periodicity"
    p = ExamPDF("Irreducibility and Periodicity  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Transition diagram and irreducibility:")
    p.txt(
        "The diagram is a single directed 4-cycle:  1 → 2 → 3 → 4 → 1.\n"
        "Irreducible: from state i, after j−i (mod 4) steps you reach state j.  "
        "Every pair of states communicates.  ✓")

    p.AL("b)  Period of state 1:")
    p.txt(
        "P^t(1,1) > 0 iff t is a multiple of 4 (the chain returns to 1 "
        "only after completing full 4-cycles).\n"
        "T(1) = {4, 8, 12, 16, …}")
    p.eqn("period(1) = gcd{4, 8, 12, …} = 4")

    p.AL("c)  P⁴ and P⁵:")
    p.txt(
        "Since the chain traverses the 4-cycle deterministically, "
        "after exactly 4 steps every state returns to itself:")
    p.mat([
        "P⁴ = I  (4×4 identity matrix)",
        "P⁵ = P  (one full cycle plus one extra step)",
    ])
    p.txt(
        "The chain does NOT converge to π = (1/4,1/4,1/4,1/4).  "
        "Starting from state 1, the distribution at time t is always a "
        "point mass: it cycles 1→2→3→4→1→… deterministically.  "
        "A periodic chain of period d > 1 oscillates; the limit "
        "lim_{n→∞} P^n does not exist (it depends on n mod 4).")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Transition matrix and irreducibility:")
    p.mat([
        "        0      1      2      3",
        "  0  [  0      1      0      0  ]",
        "  1  [  0      0      1      0  ]",
        "  2  [  0      0      0      1  ]",
        "  3  [ 1/2     0     1/2     0  ]",
    ])
    p.txt(
        "Irreducible: 0→1→2→3→0 (prob 1/2) and 3→2→3 (prob 1/2).  "
        "Every state can reach state 0 via the path … → 3 → 0.  "
        "State 0 can reach any state by following 0→1→2→3→2→…  "
        "→ All states communicate.  ✓")

    p.AL("b)  Period of state 0:")
    p.txt(
        "A path must start and end at 0.  Possible return paths:\n"
        "  0→1→2→3→0  (length 4,  prob 1/2)\n"
        "  0→1→2→3→2→3→0  (length 6,  prob 1/4)\n"
        "  0→1→2→3→2→3→2→3→0  (length 8,  prob 1/8),  …\n\n"
        "So T(0) = {4, 6, 8, 10, …}  (all even integers ≥ 4).")
    p.eqn("period(0) = gcd{4, 6, 8, 10, …} = gcd(4, 6) = 2")
    p.txt("The chain has period 2.  (Even steps stay in {0,2}; odd steps stay in {1,3}.)")

    p.AL("c)  Stationary distribution:")
    p.eqn(
        "Balance equations  π·P = π:",
        "  π₀ = (1/2)·π₃              ... (I)",
        "  π₁ = π₀                    ... (II)",
        "  π₂ = π₁ + (1/2)·π₃        ... (III)",
        "  π₃ = π₂                    ... (IV)",
        "  π₀+π₁+π₂+π₃ = 1           ... (V)",
    )
    p.txt(
        "From (I):   π₃ = 2π₀\n"
        "From (II):  π₁ = π₀\n"
        "From (IV):  π₃ = π₂  →  π₂ = 2π₀\n"
        "From (V):   π₀ + π₀ + 2π₀ + 2π₀ = 1  →  6π₀ = 1")
    p.eqn(
        "π = (1/6,  1/6,  1/3,  1/3)",
        "E[return time to 0] = 1/π₀ = 6 steps",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Lazy chain Q = (1/2)·I + (1/2)·P:")
    p.mat([
        "         0      1      2      3",
        "  0  [ 1/2    1/2     0      0  ]",
        "  1  [  0    1/2    1/2     0  ]",
        "  2  [  0     0    1/2    1/2  ]",
        "  3  [ 1/4    0    1/4   1/2  ]",
    ])

    p.AL("b)  Aperiodicity of state 0 in Q:")
    p.eqn(
        "Q(0,0) = (1/2)·I(0=0) + (1/2)·P(0,0) = 1/2 + 0 = 1/2 > 0",
        "Since Q(0,0) > 0,  T(0) contains t=1.",
        "gcd(T(0)) divides 1  →  period(0) in Q = 1  (aperiodic).  ✓",
    )

    p.AL("c)  Stationary distribution of Q:")
    p.txt("Suppose π·P = π.  Then:")
    p.eqn(
        "π·Q = π·[(1/2)·I + (1/2)·P]",
        "     = (1/2)·(π·I) + (1/2)·(π·P)",
        "     = (1/2)·π     + (1/2)·π",
        "     = π   ✓",
    )
    p.txt(
        "So π = (1/6, 1/6, 1/3, 1/3) is also the stationary distribution of Q.\n\n"
        "Long-run fractions:  state 0 → 16.7%,  state 1 → 16.7%,  "
        "state 2 → 33.3%,  state 3 → 33.3%.\n"
        "Unlike the original chain, Q is aperiodic and irreducible, so "
        "P^n(Q) converges to π regardless of starting state.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 2.  RANDOM WALKS ON GRAPHS
# ══════════════════════════════════════════════════════════════════════════════

def rw_graphs_q():
    S = "Random_Walks_on_Graphs"
    p = ExamPDF("Random Walks on Graphs  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Consider the star graph K₁,₄ with a centre vertex C and four "
        "leaf vertices {L₁, L₂, L₃, L₄}.  "
        "Every edge connects C to exactly one leaf; leaves are not "
        "connected to each other.  "
        "The simple random walk at each step moves to a uniformly "
        "chosen neighbour.")
    p.sub("a",
          "Write the 5×5 transition matrix P for the random walk "
          "(state order: C, L₁, L₂, L₃, L₄).")
    p.sub("b",
          "Using the formula  π(v) = deg(v) / (2|E|),  "
          "find the stationary distribution π for all five vertices.")
    p.sub("c",
          "Is the chain irreducible?  Find the period of state C.  "
          "Does the random walk converge to π?  If not, what is the "
          "standard fix?")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "Consider the 4-cycle graph C₄ with vertices {0, 1, 2, 3} "
        "and edges {0–1, 1–2, 2–3, 3–0}.  "
        "The simple random walk at each step moves to one of the two "
        "neighbouring vertices with equal probability.")
    p.sub("a",
          "Write the 4×4 transition matrix P for the random walk on C₄.")
    p.sub("b",
          "Find the stationary distribution π using π(v) = deg(v)/(2|E|).  "
          "What is the period of state 0?  "
          "Explain why the walk does NOT converge to π.")
    p.sub("c",
          "Construct the lazy walk  Q = (1/2)·I + (1/2)·P.  "
          "Write Q explicitly.  Verify that state 0 has period 1 in Q, "
          "and confirm that π is still the stationary distribution of Q.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "Consider the complete graph K₄ on vertices {A, B, C, D}: "
        "every pair of distinct vertices is connected by an edge.  "
        "The simple random walk moves to each of the three neighbours "
        "with equal probability 1/3.")
    p.sub("a",
          "Write the 4×4 transition matrix P.  "
          "Find π using π(v) = deg(v)/(2|E|).  "
          "Is the chain irreducible?  What is the period of state A?")
    p.sub("b",
          "The n-step return probability for vertex A is given by:\n"
          "  p_{AA}⁽ⁿ⁾ = 1/4  +  (3/4)·(−1/3)ⁿ\n"
          "Verify this formula for n = 1 and n = 2 by direct computation "
          "from the transition matrix.")
    p.sub("c",
          "Using the formula from (b), find the smallest n for which "
          "|p_{AA}⁽ⁿ⁾ − π_A| < 0.01.  "
          "Does the walk converge to π?  What drives this convergence "
          "even though K₄ has no self-loops?")

    p.save(qp(S, "Practice_1.pdf"))


def rw_graphs_a():
    S = "Random_Walks_on_Graphs"
    p = ExamPDF("Random Walks on Graphs  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Transition matrix P (order: C, L₁, L₂, L₃, L₄):")
    p.mat([
        "         C     L1    L2    L3    L4",
        "  C  [   0    1/4   1/4   1/4   1/4 ]",
        "  L1 [   1     0     0     0     0  ]",
        "  L2 [   1     0     0     0     0  ]",
        "  L3 [   1     0     0     0     0  ]",
        "  L4 [   1     0     0     0     0  ]",
    ])
    p.txt("Each leaf has only one neighbour (C), so from any leaf the walk "
          "always returns to C.  From C, each leaf is equally likely.")

    p.AL("b)  Stationary distribution:")
    p.txt("Graph has |E| = 4 edges.  Degrees:  deg(C)=4,  deg(Li)=1.")
    p.eqn(
        "π(C)  = deg(C)  / (2|E|) = 4/8 = 1/2",
        "π(Li) = deg(Li) / (2|E|) = 1/8  for i = 1,2,3,4",
        "Check: 1/2 + 4×(1/8) = 1/2 + 1/2 = 1  ✓",
    )

    p.AL("c)  Irreducibility, period, convergence:")
    p.txt(
        "Irreducible: from C reach any Li in 1 step; from any Li reach C "
        "in 1 step; from Li reach Lj via C in 2 steps.  "
        "→ All states communicate.  ✓\n\n"
        "Period of C:  return paths from C:  C→Li→C (length 2).  "
        "Can C return in 1 step?  P(C,C)=0, so no.  "
        "In 3 steps?  C→L1→C→Li→C – that's 4 steps, not 3.  "
        "T(C) = {2, 4, 6, …}  →  period(C) = 2.\n\n"
        "The walk does NOT converge because it is periodic (period 2).  "
        "Fix: use the lazy walk  Q = (1/2)I + (1/2)P, which adds "
        "self-loops and makes the chain aperiodic.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Transition matrix P for C₄:")
    p.mat([
        "        0      1      2      3",
        "  0  [  0    1/2     0    1/2  ]",
        "  1  [ 1/2    0    1/2     0   ]",
        "  2  [  0    1/2    0    1/2   ]",
        "  3  [ 1/2    0    1/2    0    ]",
    ])

    p.AL("b)  Stationary distribution and period:")
    p.txt("All vertices have degree 2;  |E|=4.")
    p.eqn("π(v) = 2/(2×4) = 1/4  for all v in {0,1,2,3}  →  uniform.")
    p.txt(
        "Period of state 0:  The 4-cycle is bipartite with parts {0,2} and {1,3}.  "
        "From 0, the walk can only be at {0,2} after an even number of steps.  "
        "T(0) = {2, 4, 6, …}  →  period(0) = 2.\n\n"
        "Since the chain is periodic, it oscillates between the two parts "
        "and P^n does not converge.  (E.g. starting from 0: at even times "
        "only states 0 or 2 can be visited.)")

    p.AL("c)  Lazy walk Q and aperiodicity:")
    p.mat([
        "Q = (1/2)·I + (1/2)·P:",
        "        0      1      2      3",
        "  0  [ 1/2   1/4     0    1/4  ]",
        "  1  [ 1/4   1/2   1/4     0   ]",
        "  2  [  0    1/4   1/2   1/4   ]",
        "  3  [ 1/4    0    1/4   1/2   ]",
    ])
    p.eqn(
        "Q(0,0) = 1/2 > 0  →  t=1 in T(0)  →  period(0) in Q = 1  (aperiodic).  ✓",
        "",
        "Stationary: π·Q = π·[(1/2)I+(1/2)P] = (1/2)π+(1/2)π = π  ✓",
        "π = (1/4, 1/4, 1/4, 1/4) is also the stationary dist of Q.",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Transition matrix, stationary distribution, period:")
    p.mat([
        "        A      B      C      D",
        "  A  [  0    1/3    1/3    1/3  ]",
        "  B  [ 1/3    0    1/3    1/3   ]",
        "  C  [ 1/3   1/3    0    1/3    ]",
        "  D  [ 1/3   1/3   1/3    0     ]",
    ])
    p.txt("All degrees = 3;  |E| = 6.")
    p.eqn("π(v) = 3/(2×6) = 1/4  for all v.  Uniform distribution.")
    p.txt(
        "Irreducible: every pair of vertices is directly connected.  ✓\n\n"
        "Period of A:  \n"
        "  Return in 2 steps: A→B→A (prob 1/3 × 1/3 = 1/9 > 0). So t=2 is in T(A).\n"
        "  Return in 3 steps: A→B→C→A (prob 1/27 > 0). So t=3 is in T(A).\n"
        "  gcd(2,3) = 1  →  period(A) = 1  (aperiodic).  ✓")

    p.AL("b)  Verify p_{AA}⁽ⁿ⁾ = 1/4 + (3/4)·(−1/3)ⁿ:")
    p.txt("n = 1:")
    p.eqn(
        "Direct: P(A,A) = 0.",
        "Formula: 1/4 + (3/4)·(−1/3)¹ = 1/4 − 1/4 = 0.  ✓",
    )
    p.txt("n = 2:")
    p.eqn(
        "Direct: p_{AA}⁽²⁾ = P(A,B)·P(B,A)+P(A,C)·P(C,A)+P(A,D)·P(D,A)",
        "       = (1/3)(1/3)+(1/3)(1/3)+(1/3)(1/3) = 3×(1/9) = 1/3.",
        "Formula: 1/4+(3/4)·(1/9) = 1/4+1/12 = 3/12+1/12 = 4/12 = 1/3.  ✓",
    )

    p.AL("c)  Smallest n with |p_{AA}⁽ⁿ⁾ − π_A| < 0.01:")
    p.eqn(
        "|p_{AA}⁽ⁿ⁾ − 1/4| = (3/4)·|−1/3|ⁿ = (3/4)·(1/3)ⁿ",
    )
    p.txt("Solve (3/4)·(1/3)ⁿ < 0.01:")
    p.eqn(
        "(1/3)ⁿ < 0.01×(4/3) = 0.01333",
        "n·ln(1/3) < ln(0.01333)",
        "n > ln(0.01333)/ln(1/3) = (−4.317)/(−1.099) ≈ 3.93",
        "Minimum n = 4 steps.",
        "",
        "Check n=4: (3/4)·(1/3)⁴ = (3/4)·(1/81) = 1/108 ≈ 0.00926 < 0.01  ✓",
    )
    p.txt(
        "Yes, the walk converges to π = (1/4,1/4,1/4,1/4).  "
        "Despite having no self-loops, K₄ is aperiodic because it has "
        "both even-length (2) and odd-length (3) cycles, making gcd=1.  "
        "The second eigenvalue is λ₂ = −1/3, so |λ₂| = 1/3 governs convergence.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 3.  RANDOM MAPPING REPRESENTATION
# ══════════════════════════════════════════════════════════════════════════════

def rmp_q():
    S = "Random_Mapping_Representation"
    p = ExamPDF("Random Mapping Representation  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Consider the random walk on the 3-cycle C₃ with states "
        "X = {0, 1, 2} (integers mod 3).  "
        "The transition probability is:")
    p.mat([
        "  P(j, k) = 1/2   if k = j+1 mod 3",
        "  P(j, k) = 1/2   if k = j−1 mod 3",
        "  P(j, k) = 0     otherwise",
    ])
    p.sub("a", "Write the 3×3 matrix P explicitly.")
    p.sub("b",
          "Define the random mapping  f(j, Z) = (j + Z) mod 3,  "
          "where Z is uniform on Λ = {−1, +1}.  "
          "Verify that this is a valid representation by checking "
          "P{ f(j, Z) = k } = P(j, k)  for every j and k.")
    p.sub("c",
          "Starting from X₀ = 0, let Xₙ = f(Xₙ₋₁, Zₙ) "
          "with Z₁, Z₂, … i.i.d. uniform on {−1, +1}.  "
          "Compute P(X₁ = 1) and P(X₂ = 0).")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "Consider the random walk on the 4-cycle C₄ with states "
        "X = {0, 1, 2, 3} (integers mod 4) and transition probabilities "
        "P(j, k) = 1/2 if k = j±1 mod 4, and 0 otherwise.")
    p.sub("a",
          "Give a random mapping representation: define f: X×Λ → X "
          "and a noise distribution for Z, and verify "
          "P{ f(j, Z) = k } = P(j, k).")
    p.sub("b",
          "Starting from X₀ = 0 and using the representation "
          "Xₙ = (X₀ + Z₁ + Z₂ + … + Zₙ) mod 4, write a closed-form "
          "expression for Xₙ in terms of the partial sums Sₙ = Z₁+…+Zₙ.")
    p.sub("c",
          "Suppose two copies of the chain are driven by the same noise: "
          "X₀ = 0 and Y₀ = 2, with Xₙ = Sₙ mod 4 and Yₙ = (2 + Sₙ) mod 4.  "
          "Show that Xₙ − Yₙ = −2 mod 4 for all n ≥ 0.  "
          "What does this imply about coupling and convergence for this chain?")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "Consider the Markov chain on states {0, 1, 2} with transition matrix:")
    p.mat([
        "        0      1      2",
        "  0  [ 1/3    1/3    1/3 ]",
        "  1  [ 1/2    1/2     0  ]",
        "  2  [  0     1/2    1/2 ]",
    ])
    p.sub("a",
          "Construct a random mapping representation using Z ~ Uniform[0,1] "
          "(continuous).  For each state x, define f(x, z) by partitioning "
          "[0,1] into intervals corresponding to the outgoing transitions.")
    p.sub("b",
          "Is the chain irreducible?  Is it aperiodic?  "
          "Find the stationary distribution π.")
    p.sub("c",
          "Starting from X₀ = 0, compute the two-step distribution "
          "μ₂ = μ₀·P² by first finding μ₁ = μ₀·P, then μ₂ = μ₁·P.  "
          "Is the chain already close to π after 2 steps?")

    p.save(qp(S, "Practice_1.pdf"))


def rmp_a():
    S = "Random_Mapping_Representation"
    p = ExamPDF("Random Mapping Representation  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Transition matrix P for C₃:")
    p.mat([
        "        0      1      2",
        "  0  [  0    1/2    1/2 ]",
        "  1  [ 1/2    0     1/2 ]",
        "  2  [ 1/2   1/2     0  ]",
    ])

    p.AL("b)  Verification of the random mapping f(j,Z) = (j+Z) mod 3:")
    p.txt("For each starting state j, check all reachable states k:")
    p.eqn(
        "j=0:  P{f(0,Z)=1} = P{(0+Z) mod 3 = 1} = P{Z=1}  = 1/2 = P(0,1)  ✓",
        "      P{f(0,Z)=2} = P{(0+Z) mod 3 = 2} = P{Z=−1} = 1/2 = P(0,2)  ✓",
        "      P{f(0,Z)=0} = P{(0+Z) mod 3 = 0} = 0 (Z is never 0)     ✓",
        "",
        "j=1:  P{f(1,Z)=2} = P{Z=+1} = 1/2 = P(1,2)  ✓",
        "      P{f(1,Z)=0} = P{Z=−1} = 1/2 = P(1,0)  ✓",
        "",
        "j=2:  P{f(2,Z)=0} = P{Z=+1} = 1/2 = P(2,0)  ✓",
        "      P{f(2,Z)=1} = P{Z=−1} = 1/2 = P(2,1)  ✓",
    )
    p.txt("Valid representation.  ✓")

    p.AL("c)  Computing P(X₁=1) and P(X₂=0):")
    p.eqn(
        "P(X₁=1 | X₀=0) = P{(0+Z₁) mod 3 = 1} = P{Z₁=1} = 1/2",
        "",
        "P(X₂=0 | X₀=0) = P(0,0)·P^1_entry... use P²:",
        "p_{00}⁽²⁾ = P(0,1)·P(1,0) + P(0,2)·P(2,0)",
        "           = (1/2)(1/2) + (1/2)(1/2) = 1/4 + 1/4 = 1/2",
        "",
        "So P(X₂=0) = 1/2.",
    )

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Random mapping representation for C₄:")
    p.txt(
        "Define  f(j, Z) = (j + Z) mod 4  with Z uniform on Λ = {−1, +1}.\n"
        "Verification (same logic as Q1 for C₃):")
    p.eqn(
        "P{f(j,Z) = j+1 mod 4} = P{Z=+1} = 1/2 = P(j, j+1 mod 4)  ✓",
        "P{f(j,Z) = j−1 mod 4} = P{Z=−1} = 1/2 = P(j, j−1 mod 4)  ✓",
    )

    p.AL("b)  Closed-form expression for Xₙ:")
    p.eqn(
        "X₁ = (X₀ + Z₁) mod 4 = (0 + Z₁) mod 4 = Z₁ mod 4",
        "X₂ = (X₁ + Z₂) mod 4 = (Z₁ + Z₂) mod 4",
        "  ...",
        "Xₙ = (Z₁ + Z₂ + ... + Zₙ) mod 4 = Sₙ mod 4",
    )

    p.AL("c)  Coupling argument and convergence:")
    p.txt(
        "With X₀=0 and Y₀=2 driven by the same noise sequence Z₁,Z₂,…:")
    p.eqn(
        "Xₙ = Sₙ mod 4",
        "Yₙ = (2 + Sₙ) mod 4",
        "",
        "Xₙ − Yₙ = Sₙ − (2+Sₙ) = −2  (mod 4)  for ALL n ≥ 0.",
    )
    p.txt(
        "The two chains never couple: they maintain a constant offset of 2 "
        "modulo 4 for every realisation of the noise.\n\n"
        "Implication: because the C₄ random walk has period 2, using the "
        "same noise does not bring together paths started 2 apart.  "
        "A standard coupling proof of convergence requires coupling, but "
        "here the chains never meet.  This is consistent with the fact that "
        "the C₄ walk is PERIODIC (period 2) and does NOT converge to π.  "
        "To fix this, one would use the lazy chain or a different coupling.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Continuous random mapping representation:")
    p.txt("For each state x, partition [0,1] into intervals proportional to transition probabilities:")
    p.mat([
        "  f(0, z):  z in [0,   1/3) → next state 0",
        "            z in [1/3, 2/3) → next state 1",
        "            z in [2/3, 1  ] → next state 2",
        "",
        "  f(1, z):  z in [0,   1/2) → next state 0",
        "            z in [1/2, 1  ] → next state 1",
        "",
        "  f(2, z):  z in [0,   1/2) → next state 1",
        "            z in [1/2, 1  ] → next state 2",
    ])
    p.txt(
        "Since Z ~ Uniform[0,1], P{f(x,Z)=y} = length of interval = P(x,y).  ✓\n"
        "(This is the standard 'quantile / inverse-CDF' representation.)")

    p.AL("b)  Irreducibility, aperiodicity, stationary distribution:")
    p.txt(
        "Irreducible:  0→1 (direct),  0→2 (direct),  1→0 (direct),  "
        "2→1→0 (2 steps).  2 can reach 0 in 2 steps.  All states communicate.  ✓\n\n"
        "Aperiodic:  P(0,0)=1/3>0 and P(1,1)=1/2>0, so both 0 and 1 "
        "have self-loops  →  T(0) contains t=1  →  period=1.  ✓")
    p.eqn(
        "Balance equations π·P = π:",
        "  π₀ = (1/3)π₀ + (1/2)π₁            ... (I)",
        "  π₁ = (1/3)π₀ + (1/2)π₁ + (1/2)π₂  ... (II)",
        "  π₂ = (1/3)π₀            + (1/2)π₂  ... (III)",
        "  π₀ + π₁ + π₂ = 1",
    )
    p.txt(
        "From (I):  (2/3)π₀ = (1/2)π₁  →  π₁ = (4/3)π₀\n"
        "From (III): (1/2)π₂ = (1/3)π₀  →  π₂ = (2/3)π₀\n"
        "Sum: π₀ + (4/3)π₀ + (2/3)π₀ = π₀·(3/3+4/3+2/3) = 3π₀ = 1")
    p.eqn("π = (1/3,  4/9,  2/9)  ≈  (0.333,  0.444,  0.222)")

    p.AL("c)  Two-step distribution from X₀=0:")
    p.eqn(
        "μ₀ = (1, 0, 0)  (start at state 0)",
        "",
        "μ₁ = μ₀·P = (1/3,  1/3,  1/3)",
        "",
        "μ₂[0] = (1/3)(1/3)+(1/3)(1/2)+(1/3)(0) = 1/9+1/6 = 2/18+3/18 = 5/18",
        "μ₂[1] = (1/3)(1/3)+(1/3)(1/2)+(1/3)(1/2)= 1/9+1/6+1/6 = 2/18+3/18+3/18 = 8/18",
        "μ₂[2] = (1/3)(1/3)+(1/3)(0)  +(1/3)(1/2)= 1/9+0+1/6 = 2/18+3/18 = 5/18",
        "",
        "μ₂ = (5/18,  8/18,  5/18)  ≈  (0.278,  0.444,  0.278)",
    )
    p.txt(
        "Compare to π = (0.333, 0.444, 0.222).  "
        "After only 2 steps, μ₂[1] already equals π₁ = 4/9 exactly, "
        "while μ₂[0] = 5/18 ≈ 0.278 vs π₀ = 1/3 ≈ 0.333.  "
        "The chain is converging but not yet fully mixed after 2 steps.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== V2  |  Folder 2026-03-05 ===")
    print("Topics: Irreducibility & Periodicity | Random Walks on Graphs "
          "| Random Mapping Representation\n")

    print("Generating question PDFs …")
    irred_period_q()
    rw_graphs_q()
    rmp_q()

    print("\nGenerating answer-key PDFs …")
    irred_period_a()
    rw_graphs_a()
    rmp_a()

    print("\nDone.  6 PDFs written to:")
    print(f"  {os.path.relpath(QQ, BASE)}/")
    print(f"  {os.path.relpath(AK, BASE)}/")
