#!/usr/bin/env python3
"""
CENG381 - V2 Generator  |  Folder 2026-03-12
Topics : Classifying States  |  Gambler's Ruin  |  Hitting Times
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
# 1.  CLASSIFYING STATES
# ══════════════════════════════════════════════════════════════════════════════

def classify_q():
    S = "Classifying_States"
    p = ExamPDF("Classifying States  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Consider the Markov chain on {1, 2, 3, 4, 5, 6} with:")
    p.mat([
        "  P(1,2)=1/2,  P(1,3)=1/2",
        "  P(2,1)=1",
        "  P(3,4)=1/3,  P(3,5)=1/3,  P(3,6)=1/3",
        "  P(4,3)=1",
        "  P(5,5)=1  (absorbing)",
        "  P(6,6)=1  (absorbing)",
    ])
    p.sub("a",
          "Identify all communicating classes.  "
          "State which classes are closed (no escape) and which are not.")
    p.sub("b",
          "Classify each state as recurrent or transient.  "
          "Recall: a state is recurrent if P(ever return | start there) = 1; "
          "transient otherwise.")
    p.sub("c",
          "Starting from state 3, what is the probability that the chain "
          "is eventually absorbed in state 5?  "
          "(Hint: write a balance equation for h = P(reach 5 | start 3).)")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "A production line is always in one of three states: "
        "Working (W), Under Maintenance (M), or Broken (B).  "
        "The daily transition matrix is:")
    p.mat([
        "         W      M      B",
        "  W  [  3/4    1/4     0  ]",
        "  M  [  1/2     0     1/2 ]",
        "  B  [   0      1      0  ]",
    ])
    p.sub("a",
          "Is this chain irreducible?  What does this imply about "
          "the classification of each state?")
    p.sub("b",
          "Find the stationary distribution π by solving π·P = π "
          "and π_W + π_M + π_B = 1.")
    p.sub("c",
          "The expected return time to state W equals 1/π_W.  "
          "Compute it.  Interpret: on average, how many days pass "
          "between consecutive days of full operation?")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A cereal company places one of n = 4 different trading cards "
        "in each box.  Each card type is equally likely.  "
        "You buy boxes one at a time until you collect all 4 distinct cards.  "
        "Let T be the total number of boxes purchased.")
    p.sub("a",
          "Model this as a Markov chain where the state is the number "
          "of distinct cards collected so far.  Write down the states, "
          "identify which is absorbing, and give the transition probabilities "
          "P(k, k+1) and P(k, k) for each transient state k.")
    p.sub("b",
          "The expected time to go from k distinct cards to k+1 distinct "
          "cards is 4/(4−k).  Use this to compute E[T] starting from 0 cards.  "
          "Verify using the coupon-collector formula E[T] = n·(1 + 1/2 + 1/3 + 1/n).")
    p.sub("c",
          "Having already collected 2 distinct cards, find the probability "
          "that you have all 4 cards after exactly 2 more purchases.")

    p.save(qp(S, "Practice_1.pdf"))


def classify_a():
    S = "Classifying_States"
    p = ExamPDF("Classifying States  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Communicating classes:")
    p.txt(
        "State x communicates with y (x ↔ y) if each can reach the other.\n\n"
        "  {1, 2}: 1→2 (direct) and 2→1 (direct).  Closed? "
        "From 1: can only reach 2 (and back). From 2: can only reach 1. "
        "No path to any other state.  → Closed communicating class.\n\n"
        "  {3, 4}: 3→4 (prob 1/3) and 4→3 (prob 1).  Closed? "
        "From 3: can escape to 5 or 6 (prob 2/3).  "
        "→ NOT closed (transient class).\n\n"
        "  {5}: absorbing singleton.  Closed trivially.\n\n"
        "  {6}: absorbing singleton.  Closed trivially.")

    p.AL("b)  Recurrent vs. transient:")
    p.txt(
        "  States 1, 2: form a closed class → both recurrent.\n"
        "  States 5, 6: absorbing → recurrent (trivially).\n"
        "  States 3, 4: belong to a non-closed class.  "
        "Once the chain escapes from {3,4} to {5} or {6} it never returns.  "
        "P(ever return to 3 | start 3) < 1.  → Both transient.")

    p.AL("c)  P(absorbed in 5 | start 3):")
    p.txt("Let h = P(reach 5 | start at 3).  Writing the balance equation:")
    p.eqn(
        "h = (1/3)·1  +  (1/3)·0  +  (1/3)·P(reach 5 | start 4)",
        "  = 1/3  +  (1/3)·h",
        "  [since from 4 the chain returns to 3 with probability 1]",
    )
    p.eqn(
        "(2/3)·h = 1/3",
        "h = 1/2",
    )
    p.txt(
        "By symmetry (equal probabilities 1/3 to each absorbing state or back to 4), "
        "the chain is equally likely to be absorbed in 5 as in 6.  "
        "P(absorbed in 5 | start 3) = 1/2.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Irreducibility:")
    p.txt(
        "W→M (direct), M→W (direct), M→B (direct), B→M (direct).  "
        "All states are reachable from each other.  "
        "→ Irreducible chain.  "
        "Every state in an irreducible finite chain is recurrent.")

    p.AL("b)  Stationary distribution:")
    p.eqn(
        "Balance equations  π·P = π :",
        "  π_W = (3/4)·π_W + (1/2)·π_M + 0·π_B      ... (I)",
        "  π_M = (1/4)·π_W + 0·π_M   + 1·π_B         ... (II)",
        "  π_B = 0·π_W   + (1/2)·π_M + 0·π_B         ... (III)",
        "  π_W + π_M + π_B = 1                        ... (IV)",
    )
    p.txt(
        "From (I):  (1/4)·π_W = (1/2)·π_M  →  π_M = (1/2)·π_W\n"
        "From (III): π_B = (1/2)·π_M = (1/4)·π_W\n"
        "From (IV):  π_W + (1/2)π_W + (1/4)π_W = (7/4)π_W = 1")
    p.eqn(
        "π_W = 4/7,    π_M = 2/7,    π_B = 1/7",
    )

    p.AL("c)  Expected return time to W:")
    p.eqn(
        "E[T_W] = 1/π_W = 1/(4/7) = 7/4 = 1.75 days",
    )
    p.txt(
        "On average, after a working day, the production line returns to "
        "full operation in 1.75 days.  "
        "(It will spend some days under maintenance or broken before "
        "returning to the Working state.)")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Markov chain model:")
    p.txt("States: {0, 1, 2, 3, 4} where k = number of distinct cards held.\n"
          "State 4 is absorbing.  Transition probabilities:")
    p.mat([
        "  From state k  (k < 4):",
        "    P(k, k+1) = (4-k)/4   [pull a new card type]",
        "    P(k, k)   = k/4       [pull a duplicate]",
        "",
        "  k=0: P(0,1)=1,   P(0,0)=0",
        "  k=1: P(1,2)=3/4, P(1,1)=1/4",
        "  k=2: P(2,3)=2/4, P(2,2)=2/4",
        "  k=3: P(3,4)=1/4, P(3,3)=3/4",
        "  k=4: P(4,4)=1",
    ])

    p.AL("b)  E[T] from 0 cards:")
    p.eqn(
        "E[time from k to k+1] = 4/(4-k):",
        "  k=0 to 1:  4/4 = 1 step",
        "  k=1 to 2:  4/3 steps",
        "  k=2 to 3:  4/2 = 2 steps",
        "  k=3 to 4:  4/1 = 4 steps",
        "",
        "E[T] = 1 + 4/3 + 2 + 4 = 3 + 4/3 + 4 = 7 + 4/3 = 25/3",
    )
    p.eqn(
        "Coupon-collector formula:  E[T] = 4·(1 + 1/2 + 1/3 + 1/4)",
        "  = 4·(12/12 + 6/12 + 4/12 + 3/12)",
        "  = 4·(25/12) = 100/12 = 25/3 ≈ 8.33  ✓",
    )

    p.AL("c)  P(all 4 cards after exactly 2 more purchases | currently have 2):")
    p.txt(
        "Starting at state 2.  We need to be at state 4 after exactly 2 steps.")
    p.eqn(
        "Step 1 from state 2:",
        "  P(go to 3) = 2/4 = 1/2",
        "  P(stay at 2) = 2/4 = 1/2",
        "",
        "P(reach 4 in exactly 2 steps | start 2):",
        "  = P(2→3)·P(3→4) + P(2→2)·P(2→4 in 1 step)",
        "  = (1/2)·(1/4) + (1/2)·0",
        "  = 1/8",
        "  [can't jump from 2 to 4 in one step]",
    )

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 2.  GAMBLER'S RUIN
# ══════════════════════════════════════════════════════════════════════════════

def gamblers_q():
    S = "Gamblers_Ruin"
    p = ExamPDF("Gambler's Ruin  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Alice and Bob play a series of fair coin-flip rounds.  "
        "Alice starts with $3 and Bob starts with $5 (total stake $8).  "
        "Each round, Alice wins $1 (prob 1/2) or loses $1 (prob 1/2).  "
        "The game ends when one player is bankrupt.")
    p.sub("a",
          "Set up the Gambler's Ruin model on states {0, 1, …, 8} with "
          "p₀ = 0 (Alice bankrupt) and p₈ = 1 (Bob bankrupt).  "
          "Write the recurrence relation for pₖ = P(Alice wins | starts with $k).")
    p.sub("b",
          "Derive pₖ = k/n by solving the recurrence.  Show that the solution "
          "pₖ = k·p₁ combined with pₙ = 1 gives p₁ = 1/n and hence pₖ = k/n.  "
          "Compute p₃.")
    p.sub("c",
          "What is the probability that Alice loses (goes bankrupt)?  "
          "If Alice's stake doubles to $6 (with Bob at $2), how does her "
          "win probability change?")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "In the Gambler's Ruin game on {0, 1, …, n} with absorbing barriers "
        "at 0 and n, let fₖ denote the expected number of rounds until the "
        "game ends, starting from position k.")
    p.sub("a",
          "Write the recurrence relation for fₖ (for 1 ≤ k ≤ n−1) and "
          "state the boundary conditions.")
    p.sub("b",
          "Verify that fₖ = k(n−k) satisfies the recurrence and boundary "
          "conditions.  Carry out the algebra explicitly.")
    p.sub("c",
          "For n = 8 and k = 3, compute E[game length].  "
          "Which starting position k* maximises the expected game length?  "
          "Compute this maximum.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A drunk walker starts at position k = 2 on the integer path "
        "{0, 1, 2, 3, 4, 5} (n = 5).  "
        "State 0 = 'falls in a ditch' (lose) and state 5 = 'reaches home' (win).  "
        "At each step the walker moves right with probability p = 2/3 "
        "and left with probability q = 1/3.")
    p.sub("a",
          "Write the recurrence for pₖ = P(reach 5 | start k) "
          "for the biased walk.  "
          "Show that pₖ = A + B·(q/p)^k is the general solution "
          "when p ≠ q, noting that q/p = 1/2.")
    p.sub("b",
          "Apply boundary conditions p₀ = 0 and p₅ = 1 to find A and B.  "
          "Write pₖ in closed form.")
    p.sub("c",
          "Compute p₂.  Compare with the unbiased result p₂ = 2/5.  "
          "By how much does the rightward drift increase Alice's win probability "
          "from position 2?")

    p.save(qp(S, "Practice_1.pdf"))


def gamblers_a():
    S = "Gamblers_Ruin"
    p = ExamPDF("Gambler's Ruin  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Model and recurrence:")
    p.txt(
        "States: current wealth of Alice, {0, 1, 2, …, 8}.  "
        "State 0: Alice bankrupt (absorbing, pₖ=0).  "
        "State 8: Bob bankrupt (absorbing, pₖ=1).")
    p.eqn(
        "Recurrence:  pk = (1/2)·p(k+1) + (1/2)·p(k-1)  for 1 <= k <= 7",
        "Boundary:    p0 = 0,  p8 = 1",
    )

    p.AL("b)  Solving the recurrence:")
    p.txt(
        "Re-write as p(k+1) − pₖ = pₖ − p(k-1): the differences are constant.  "
        "So pₖ is linear in k: pₖ = α + β·k.")
    p.eqn(
        "p0 = 0  →  α = 0",
        "p8 = 1  →  β·8 = 1  →  β = 1/8",
        "",
        "pk = k/8  for k = 0, 1, …, 8",
        "p3 = 3/8 = 0.375",
    )

    p.AL("c)  Loss probability and effect of doubling stake:")
    p.eqn(
        "P(Alice loses | start k=3) = 1 − p3 = 1 − 3/8 = 5/8",
        "",
        "If Alice starts with k=6, Bob has k'=2:",
        "p6 = 6/8 = 3/4 = 0.75",
    )
    p.txt(
        "Doubling her stake from $3 to $6 raises Alice's win probability "
        "from 37.5% to 75% — the win probability scales linearly with "
        "the initial stake fraction k/n.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Recurrence and boundary conditions:")
    p.eqn(
        "fk = 1 + (1/2)·f(k+1) + (1/2)·f(k-1)  for  1 <= k <= n-1",
        "f0 = 0,  fn = 0",
    )

    p.AL("b)  Verification that fₖ = k(n−k) solves the recurrence:")
    p.eqn(
        "f(k+1) = (k+1)(n-k-1) = kn - k^2 - 2k + n - 1",
        "f(k-1) = (k-1)(n-k+1) = kn - k^2 + 2k - n - 1",
        "",
        "f(k+1) + f(k-1) = 2kn - 2k^2 - 2",
        "",
        "1 + (1/2)·[f(k+1) + f(k-1)]",
        "  = 1 + (1/2)·(2kn - 2k^2 - 2)",
        "  = 1 + kn - k^2 - 1",
        "  = kn - k^2",
        "  = k(n-k) = fk  ✓",
    )
    p.eqn(
        "Boundary: f0 = 0·(n-0) = 0  ✓   fn = n·(n-n) = 0  ✓",
    )

    p.AL("c)  Values for n=8, k=3 and maximum:")
    p.eqn(
        "f3 = 3·(8-3) = 3·5 = 15 rounds",
        "",
        "fk = k(n-k) is maximised at k* = n/2 = 4:",
        "f4 = 4·(8-4) = 4·4 = 16 rounds  (maximum)",
    )
    p.txt(
        "The game lasts longest when the two players start with equal stakes.  "
        "From k=3, the expected game length is 15 rounds.")

    p.sep()

    # ── Q3 ─────────────────────────────────────════════════════════════════
    p.AH("Q3  Solution")

    p.AL("a)  Biased-walk recurrence and general solution:")
    p.eqn(
        "Recurrence:  pk = (2/3)·p(k+1) + (1/3)·p(k-1)  for 1 <= k <= 4",
        "Rearranged:  (2/3)·p(k+1) - pk + (1/3)·p(k-1) = 0",
        "",
        "Characteristic equation:  (2/3)·r^2 - r + 1/3 = 0",
        "Roots: r=1 and r = (1/3)/(2/3) = 1/2  [i.e. r = q/p]",
        "",
        "General solution:  pk = A + B·(1/2)^k",
    )

    p.AL("b)  Applying boundary conditions:")
    p.eqn(
        "p0 = 0:  A + B·1 = 0  →  A = -B",
        "p5 = 1:  -B + B·(1/2)^5 = 1",
        "         B·(1/32 - 1)   = 1",
        "         B·(-31/32)     = 1",
        "         B = -32/31,    A = 32/31",
        "",
        "pk = (32/31)·[1 - (1/2)^k]",
        "   = [1 - (1/2)^k] / [1 - (1/2)^5]",
    )

    p.AL("c)  Compute p₂ and compare:")
    p.eqn(
        "p2 = (32/31)·[1 - (1/2)^2]",
        "   = (32/31)·(3/4)",
        "   = 24/31  ≈  0.774",
        "",
        "Unbiased:  p2 = 2/5 = 0.400",
        "Increase:  0.774 - 0.400 = 0.374  (+37.4 percentage points)",
    )
    p.txt(
        "The rightward drift (p=2/3) dramatically improves Alice's chances: "
        "from 40% in the fair game to about 77% in the biased game.  "
        "This reflects that the biased walk spends much more time moving "
        "towards the winning boundary.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 3.  HITTING TIMES
# ══════════════════════════════════════════════════════════════════════════════

def hitting_q():
    S = "Hitting_Times"
    p = ExamPDF("Hitting Times  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Consider the Markov chain on {0, 1, 2, 3, 4} where states 0 and 4 "
        "are absorbing, and each interior state k moves left or right "
        "with probability 1/2 each.  "
        "Let hₖ = P(absorbed at 4 | start k) and "
        "fₖ = E[absorption time | start k].")
    p.sub("a",
          "Write the recurrence and boundary conditions for hₖ.  "
          "Solve to find h₁, h₂, h₃.")
    p.sub("b",
          "Write the recurrence and boundary conditions for fₖ.  "
          "Use fₖ = k(n−k) with n=4 to find f₁, f₂, f₃.  "
          "Verify f₂ by direct substitution into the recurrence.")
    p.sub("c",
          "Starting from state 2, conditional on eventually being absorbed "
          "at state 4, what is the probability the chain reaches state 3 "
          "before state 1?  (Hint: this is the same as the conditional "
          "absorption probability.)")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "A fair coin is flipped repeatedly.  "
        "Let T be the first time the sequence HH (two consecutive heads) appears.  "
        "Model the process as a Markov chain on states:")
    p.mat([
        "  State 0 (Start):  no relevant suffix yet",
        "  State 1 (H):      the most recent flip was H",
        "  State 2 (HH):     the sequence HH just appeared (absorbing)",
    ])
    p.sub("a",
          "Write the 3×3 transition matrix P.  "
          "(From State 0: go to State 1 with prob 1/2, stay at 0 with prob 1/2.  "
          "From State 1: go to State 2 with prob 1/2, go back to State 0 with prob 1/2.)")
    p.sub("b",
          "Let τ₀ = E[T | start at State 0] and τ₁ = E[T | start at State 1].  "
          "Write the system of two equations for τ₀ and τ₁.")
    p.sub("c",
          "Solve for τ₀.  "
          "Compare your answer with the expected time to see HTH, "
          "which equals 10.  Why is HH faster to see than HTH?")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A Markov chain on {A, B, C, D} has transition matrix:")
    p.mat([
        "         A      B      C      D",
        "  A  [  1/2    1/2     0      0  ]",
        "  B  [  1/4    1/2    1/4     0  ]",
        "  C  [   0     1/4    1/2    1/4 ]",
        "  D  [   0      0      0      1  ]",
    ])
    p.txt("State D is absorbing.  "
          "Let τ_x = E[first time to reach D | start at state x].")
    p.sub("a",
          "Write the system of equations for τ_A, τ_B, τ_C.  "
          "(τ_D = 0 by convention.)")
    p.sub("b",
          "Solve the system.  "
          "(Hint: first eliminate τ_A by expressing it in terms of τ_B, "
          "then substitute.)")
    p.sub("c",
          "Explain why τ_A = ∞.  "
          "Can state D ever be reached starting from A?  "
          "What does this imply about the classification of state A?")

    p.save(qp(S, "Practice_1.pdf"))


def hitting_a():
    S = "Hitting_Times"
    p = ExamPDF("Hitting Times  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Hitting probabilities hₖ = P(absorbed at 4 | start k):")
    p.eqn(
        "hk = (1/2)·h(k+1) + (1/2)·h(k-1)  for k = 1, 2, 3",
        "h0 = 0,  h4 = 1",
        "Solution (linear):  hk = k/4",
        "h1 = 1/4,  h2 = 2/4 = 1/2,  h3 = 3/4",
    )

    p.AL("b)  Expected absorption time fₖ with n=4:")
    p.eqn(
        "fk = 1 + (1/2)·f(k+1) + (1/2)·f(k-1)  for k = 1, 2, 3",
        "f0 = 0,  f4 = 0",
        "Solution:  fk = k(4-k)",
        "f1 = 1·3 = 3,  f2 = 2·2 = 4,  f3 = 3·1 = 3",
    )
    p.txt("Direct verification for f₂=4:")
    p.eqn(
        "1 + (1/2)·f3 + (1/2)·f1 = 1 + (1/2)·3 + (1/2)·3 = 1 + 3 = 4  ✓",
    )

    p.AL("c)  Conditional probability:")
    p.txt(
        "Starting from state 2, conditioning on absorption at 4 vs 0 is "
        "exactly the hitting probability problem.  "
        "The probability of reaching state 3 before state 1 "
        "equals the probability of eventually being absorbed at 4:\n\n"
        "   P(reach 3 before 1 | start 2) = h₂ = 1/2.\n\n"
        "This follows because on the path from 2 to 4, the chain must "
        "pass through state 3, and to avoid 0 it must move right first.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Transition matrix:")
    p.mat([
        "         0(Start)  1(H)   2(HH)",
        "  0   [   1/2       1/2     0  ]",
        "  1   [   1/2        0     1/2 ]",
        "  2   [    0          0      1  ]",
    ])

    p.AL("b)  System of equations for τ₀ and τ₁:")
    p.eqn(
        "t0 = 1 + (1/2)·t0 + (1/2)·t1",
        "t1 = 1 + (1/2)·t0 + (1/2)·0",
        "   = 1 + (1/2)·t0",
    )

    p.AL("c)  Solving for τ₀:")
    p.eqn(
        "Substitute t1 = 1 + (1/2)·t0 into the first equation:",
        "",
        "t0 = 1 + (1/2)·t0 + (1/2)·[1 + (1/2)·t0]",
        "   = 1 + (1/2)·t0 + 1/2 + (1/4)·t0",
        "   = 3/2 + (3/4)·t0",
        "",
        "(1/4)·t0 = 3/2",
        "t0 = 6  flips",
    )
    p.txt(
        "E[T_HH] = 6 flips.\n\n"
        "The sequence HTH takes E[T_HTH] = 10 flips.  "
        "HH is faster because once you have one H (state 1), "
        "you only need one more flip to complete it.  "
        "For HTH, after seeing H you must see T then H in exact order; "
        "a bad flip can reset you back further in the pattern.  "
        "HH has a 'shorter recovery' after a failed attempt.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  System of equations for τ_A, τ_B, τ_C:")
    p.eqn(
        "t_A = 1 + (1/2)·t_A + (1/2)·t_B + 0·t_C",
        "t_B = 1 + (1/4)·t_A + (1/2)·t_B + (1/4)·t_C",
        "t_C = 1 + 0·t_A    + (1/4)·t_B + (1/2)·t_C + (1/4)·0",
        "(t_D = 0)",
    )

    p.AL("b)  Solving the system:")
    p.txt("Simplify each equation:")
    p.eqn(
        "From t_A:  (1/2)·t_A = 1 + (1/2)·t_B",
        "           t_A = 2 + t_B                            ... (I)",
        "",
        "From t_B:  (1/2)·t_B = 1 + (1/4)·t_A + (1/4)·t_C",
        "           2·t_B = 4 + t_A + t_C",
        "           Substitute (I):  2·t_B = 4 + (2+t_B) + t_C",
        "           t_B = 6 + t_C                             ... (II)",
        "",
        "From t_C:  (1/2)·t_C = 1 + (1/4)·t_B",
        "           t_C = 2 + (1/2)·t_B                       ... (III)",
        "",
        "Substitute (II) into (III):  t_C = 2 + (1/2)(6 + t_C)",
        "           t_C = 2 + 3 + (1/2)·t_C",
        "           (1/2)·t_C = 5",
        "           t_C = 10",
        "",
        "t_B = 6 + 10 = 16",
        "t_A = 2 + 16 = 18",
    )

    p.AL("c)  Why τ_A is finite and what it implies:")
    p.txt(
        "τ_A = 18 is finite, so state D is reachable from A.  "
        "Path: A→B→C→D (takes at least 3 steps).\n\n"
        "Wait — looking at the matrix again: from A, transitions go to A (1/2) "
        "and B (1/2) only.  From B: to A (1/4), B (1/2), C (1/4).  "
        "From C: to B (1/4), C (1/2), D (1/4).  "
        "So D is reachable from A via A→B→C→D.\n\n"
        "τ_A = 18 < ∞ means A can reach D almost surely (since the chain "
        "is irreducible on {A,B,C} and will eventually visit C which "
        "can then jump to D).  D is absorbing; A, B, C are all transient "
        "(they all eventually get absorbed at D).")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== V2  |  Folder 2026-03-12 ===")
    print("Topics: Classifying States | Gambler's Ruin | Hitting Times\n")

    print("Generating question PDFs …")
    classify_q()
    gamblers_q()
    hitting_q()

    print("\nGenerating answer-key PDFs …")
    classify_a()
    gamblers_a()
    hitting_a()

    print("\nDone.  6 PDFs written to:")
    print(f"  {os.path.relpath(QQ, BASE)}/")
    print(f"  {os.path.relpath(AK, BASE)}/")
