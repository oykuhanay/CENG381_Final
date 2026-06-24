#!/usr/bin/env python3
"""
CENG381 - V2 Generator  |  Folder 2026-05-21
Topics : Martingales  |  Wald's Equality
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
        self.multi_cell(0, 7.5, f"Q{n}  ({pts} points).  {text}",
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
# 1.  MARTINGALES
# ══════════════════════════════════════════════════════════════════════════════

def mart_q():
    S = "Martingales"
    p = ExamPDF("Martingales  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "A stochastic process {Z_n; n ≥ 1} is a martingale if "
        "(i) E[|Z_n|] < ∞ for all n ≥ 1, and "
        "(ii) E[Z_n | Z_{n-1}, ..., Z_1] = Z_{n-1} for all n ≥ 2.")
    p.sub("a",
          "Let X_1, X_2, ... be i.i.d. random variables with E[X_i] = 0.  "
          "Define S_n = X_1 + X_2 + ... + X_n (S_0 = 0).  "
          "Prove that {S_n; n ≥ 0} is a martingale by verifying condition (ii).  "
          "Which property of X_i is essential, and why?")
    p.sub("b",
          "For the symmetric random walk, X_i = +1 w.p. 1/2 and −1 w.p. 1/2.  "
          "Write S_n = S_{n-1} + X_n.  Compute E[S_n | S_{n-1}] directly "
          "and confirm the martingale condition.  What is E[S_n] for all n ≥ 0?")
    p.sub("c",
          "Now suppose X_i = +1 w.p. p and −1 w.p. q = 1 − p, with p ≠ 1/2.  "
          "(i) Compute E[X_i] and E[S_n | S_{n-1},...,S_1].  "
          "(ii) Is {S_n} a martingale when p > 1/2?  "
          "Call it a sub-martingale if E[Z_n | past] ≥ Z_{n-1}.  "
          "Classify {S_n} for p > 1/2 and for p < 1/2.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "Let {S_n; n ≥ 0} be the symmetric random walk with S_0 = 0 "
        "(steps ±1 w.p. 1/2 each).  Define Z_n = S_n² − n.")
    p.sub("a",
          "Prove {Z_n; n ≥ 0} is a martingale.  "
          "Compute E[Z_n | S_{n-1}] by expanding S_n = S_{n-1} + X_n, "
          "using E[X_n] = 0 and E[X_n²] = 1.")
    p.sub("b",
          "Let T = min{n ≥ 1 : |S_n| = N} for a fixed integer N > 0 "
          "(first exit time from the interval (−N, N)).  "
          "The Optional Stopping Theorem (OST) states that for a bounded "
          "stopping time, E[Z_T] = Z_0.  "
          "Apply OST to {Z_n}: substitute Z_T = S_T² − T and Z_0 = 0 to "
          "find E[T].")
    p.sub("c",
          "By symmetry, P(S_T = +N) = P(S_T = −N) = 1/2.  "
          "Confirm this using OST applied to {S_n} (also a martingale): "
          "E[S_T] = S_0 = 0, and S_T takes values +N and −N.  "
          "Compute E[T] for N = 4.  What are the units?")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A gambler starts with $s (0 < s < N).  Each round they win $1 w.p. 1/2 "
        "or lose $1 w.p. 1/2 (fair game).  The game stops at time T when "
        "their fortune first reaches $0 (ruin) or $N (goal).")
    p.sub("a",
          "The fortune process {S_n} is a martingale.  "
          "Apply OST (E[S_T] = S_0 = s) to find the probability p_s = P(reach N | start at s).  "
          "Hint: S_T = N w.p. p_s and S_T = 0 w.p. 1 − p_s.")
    p.sub("b",
          "Apply OST to the quadratic martingale {Z_n = S_n² − n}: "
          "E[Z_T] = Z_0 = s².  "
          "Express E[S_T²] in terms of p_s and N, substitute p_s from (a), "
          "and derive E[T] = s(N − s).")
    p.sub("c",
          "A gambler starts with $3 aiming for $7 (N = 7).  "
          "Find the probability of reaching the goal, and the expected "
          "number of rounds until the game ends.")

    p.save(qp(S, "Practice_1.pdf"))


def mart_a():
    S = "Martingales"
    p = ExamPDF("Martingales  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Proving {S_n} is a martingale:")
    p.eqn(
        "E[S_n | S_{n-1}, ..., S_1]",
        "= E[S_{n-1} + X_n | S_{n-1}, ..., S_1]",
        "= E[S_{n-1} | S_{n-1}, ..., S_1] + E[X_n | S_{n-1}, ..., S_1]",
        "= S_{n-1} + E[X_n]          (X_n independent of past)",
        "= S_{n-1} + 0 = S_{n-1}  ✓",
    )
    p.txt("The essential property is E[X_i] = 0.  "
          "If the steps had non-zero mean the sum would drift and fail condition (ii).")

    p.AL("b)  Symmetric walk:")
    p.eqn(
        "E[S_n | S_{n-1}] = S_{n-1} + E[X_n] = S_{n-1} + (1/2 - 1/2) = S_{n-1}  ✓",
        "E[S_n] = E[S_0] = 0  for all n  (martingale has constant mean)",
    )

    p.AL("c)  Biased walk:")
    p.eqn(
        "E[X_i] = p*1 + q*(-1) = p - q = 2p - 1",
        "",
        "E[S_n | S_{n-1}, ..., S_1] = S_{n-1} + (2p-1)",
        "",
        "p > 1/2:  E[S_n | past] = S_{n-1} + (2p-1) > S_{n-1}",
        "  => sub-martingale (expected value tends to increase)",
        "",
        "p < 1/2:  E[S_n | past] = S_{n-1} + (2p-1) < S_{n-1}",
        "  => super-martingale (expected value tends to decrease)",
    )

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Proving {Z_n = S_n² − n} is a martingale:")
    p.eqn(
        "E[Z_n | S_{n-1}]",
        "= E[S_n^2 - n | S_{n-1}]",
        "= E[(S_{n-1} + X_n)^2 | S_{n-1}] - n",
        "= E[S_{n-1}^2 + 2*S_{n-1}*X_n + X_n^2 | S_{n-1}] - n",
        "= S_{n-1}^2 + 2*S_{n-1}*E[X_n] + E[X_n^2] - n",
        "= S_{n-1}^2 + 2*S_{n-1}*0 + 1 - n        (E[X_n^2]=1 since X_n=+-1)",
        "= S_{n-1}^2 - (n-1)",
        "= Z_{n-1}  ✓",
    )

    p.AL("b)  OST applied to {Z_n}, exit time T:")
    p.eqn(
        "E[Z_T] = Z_0 = S_0^2 - 0 = 0",
        "",
        "Z_T = S_T^2 - T,  and |S_T| = N  =>  S_T^2 = N^2",
        "",
        "E[N^2 - T] = 0",
        "N^2 - E[T] = 0",
        "E[T] = N^2",
    )

    p.AL("c)  Symmetry argument and E[T] for N=4:")
    p.eqn(
        "OST on {S_n}: E[S_T] = S_0 = 0",
        "Let alpha = P(S_T = +N).",
        "E[S_T] = alpha*N + (1-alpha)*(-N) = 0",
        "  => alpha*N = (1-alpha)*N  =>  alpha = 1/2  ✓",
        "",
        "For N = 4:  E[T] = 4^2 = 16 rounds",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Ruin probability via martingale OST:")
    p.eqn(
        "E[S_T] = S_0 = s",
        "S_T = N  w.p. p_s,   S_T = 0  w.p. 1-p_s",
        "",
        "p_s * N + (1-p_s) * 0 = s",
        "p_s = s/N",
    )

    p.AL("b)  Expected game length via quadratic martingale OST:")
    p.eqn(
        "E[Z_T] = Z_0  =>  E[S_T^2 - T] = s^2",
        "E[S_T^2] = E[T] + s^2",
        "",
        "E[S_T^2] = p_s * N^2 + (1-p_s) * 0^2 = (s/N) * N^2 = s*N",
        "",
        "s*N = E[T] + s^2",
        "E[T] = s*N - s^2 = s*(N-s)",
    )

    p.AL("c)  Gambler starting at $3, goal $7:")
    p.eqn(
        "s = 3,  N = 7",
        "",
        "P(reach 7) = p_3 = 3/7  ~=  0.429",
        "",
        "E[T] = 3*(7-3) = 3*4 = 12 rounds",
    )
    p.txt("The gambler has a 43% chance of reaching the goal and "
          "expects the game to end in 12 rounds on average.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 2.  WALD'S EQUALITY
# ══════════════════════════════════════════════════════════════════════════════

def wald_q():
    S = "Walds_Equality"
    p = ExamPDF("Wald's Equality  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Wald's Equality (Theorem 4.5.1): "
        "Let {X_n; n ≥ 1} be i.i.d. with mean X̄.  "
        "If J is a stopping time for {X_n} with E[J] < ∞, then:\n\n"
        "  E[S_J]  =  X̄ · E[J],     where  S_J = X_1 + ... + X_J")
    p.sub("a",
          "Explain in plain words what a 'stopping time' is.  "
          "Give one example of a valid stopping time and one example that "
          "is NOT a valid stopping time for a sequence X_1, X_2, ...")
    p.sub("b",
          "Let X_1, X_2, ... be i.i.d. Uniform{1, 2, 3, 4, 5, 6} dice rolls "
          "(mean X̄ = 3.5).  "
          "A player stops at J = first roll n such that S_n ≥ 21.  "
          "Simulations suggest E[J] ≈ 6.  "
          "Use Wald's equality to estimate E[S_J].  "
          "Does the result make intuitive sense for this game?")
    p.sub("c",
          "Let X_i ~ Exp(λ) (mean 1/λ).  "
          "A stopping time J = N(c) + 1 counts how many arrivals are needed "
          "to first exceed a threshold c (where N(c) is the number of arrivals by time c).  "
          "For large c, the elementary renewal theorem gives E[N(c)] ≈ λc.  "
          "Approximate E[J] and then use Wald's equality to find E[S_J].  "
          "Interpret the overshoot E[S_J] − c.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "A biased coin gives +1 w.p. p and −1 w.p. q = 1 − p, with p > 1/2.  "
        "Let S_n = X_1 + ... + X_n (S_0 = 0).  "
        "Define J = min{n ≥ 1 : S_n = 1} (first time the gambler is ahead by 1).")
    p.sub("a",
          "Let θ = P(J < ∞).  Derive the equation θ = p + q θ² by "
          "conditioning on the first flip: "
          "either S_1 = 1 (done, w.p. p) or S_1 = −1 "
          "(w.p. q), after which the gambler must make two independent "
          "comebacks from −1 to 0 and from 0 to 1, each succeeding w.p. θ.")
    p.sub("b",
          "Solve the quadratic (1 − p)θ² − θ + p = 0.  "
          "For p > 1/2, show that both roots are θ₁ = 1 and θ₂ = p/q.  "
          "Explain why we must choose θ = 1 when p > 1/2 "
          "(Hint: for p > 1/2, p/q > 1 which is not a valid probability).  "
          "What is θ when p < 1/2?")
    p.sub("c",
          "For p > 1/2, E[J] satisfies E[J] = p · 1 + q · (1 + 2 E[J]).  "
          "Solve to find E[J] = 1/(2p − 1).  "
          "Then verify Wald's equality: E[S_J] = E[X] · E[J] = (2p − 1) · "
          "1/(2p − 1) = 1 ✓.  "
          "For p = 2/3: compute θ, E[J], and E[S_J].  "
          "What happens to E[J] as p → 1/2 from above?")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A quality inspector samples items one by one.  "
        "Each item is defective independently w.p. q = 0.2 "
        "(good w.p. p = 0.8).  "
        "Let X_i = 1 if item i is defective, 0 if good.  "
        "The inspector uses two different stopping rules.")
    p.sub("a",
          "Stopping rule A: stop after finding exactly 4 defective items.  "
          "This is a Negative Binomial stopping rule: J_A ~ NegBin(4, 0.2).  "
          "Compute E[J_A] = 4/q.  "
          "Apply Wald's equality to verify E[S_{J_A}] = 4 (four defectives found).")
    p.sub("b",
          "The inspector also counts the number of good items inspected: "
          "G = J_A − S_{J_A} (total inspected minus defectives).  "
          "Find E[G].  "
          "Also, what is E[G] / E[J_A] (the long-run fraction of good items)?  "
          "Verify it equals p = 0.8.")
    p.sub("c",
          "Stopping rule B: stop at J_B = min{n : S_n ≥ 3}, "
          "but now defect rate changes to q' = 1/4.  "
          "Using Wald's equality, compute E[J_B].  "
          "Suppose additionally X_i ~ Bernoulli(1/4) but the inspector stops at "
          "the first time S_n ≥ 6 instead.  How does E[J_B] scale with the target?")

    p.save(qp(S, "Practice_1.pdf"))


def wald_a():
    S = "Walds_Equality"
    p = ExamPDF("Wald's Equality  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Stopping time definition and examples:")
    p.txt(
        "A stopping time J is a random variable such that the event {J = n} "
        "depends only on the observed values X_1, ..., X_n — you can decide "
        "to stop at time n using only the information available up to time n "
        "(no 'peeking into the future').")
    p.txt("Valid stopping time: J = first n such that S_n > 10.  "
          "The decision depends only on X_1, ..., X_n.")
    p.txt("NOT a valid stopping time: J = last n before the sum exceeds 10.  "
          "Deciding which is 'last' requires knowledge of future X_{n+1}, X_{n+2}, ...")

    p.AL("b)  Dice rolls, stop at S_n >= 21:")
    p.eqn(
        "X_bar = (1+2+3+4+5+6)/6 = 3.5",
        "E[J] ~= 6  (given)",
        "",
        "Wald's equality:  E[S_J] = X_bar * E[J] = 3.5 * 6 = 21",
    )
    p.txt("Intuitive: the game aims to reach 21, so the expected sum at "
          "stopping should be around 21.  Wald's equality confirms this exactly "
          "(any overshoot is accounted for in E[J]~=6).")

    p.AL("c)  Exponential inter-arrivals, threshold c:")
    p.eqn(
        "E[N(c)] ~= lambda*c  by the elementary renewal theorem",
        "E[J] = E[N(c)+1] ~= lambda*c + 1",
        "",
        "Wald's equality:  E[S_J] = (1/lambda) * (lambda*c + 1) = c + 1/lambda",
        "",
        "Overshoot = E[S_J] - c = 1/lambda = E[X]",
    )
    p.txt("On average the sum overshoots the threshold c by exactly one mean "
          "inter-arrival time.  This is the 'excess life' of the renewal process "
          "and is another way to see the inspection paradox.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Recurrence for theta:")
    p.txt("Condition on the first flip:")
    p.eqn(
        "theta = P(J < inf)",
        "     = P(S_1=1)*1  +  P(S_1=-1)*P(two comebacks both succeed)",
        "     = p * 1       +  q * theta^2",
        "     = p + q*theta^2",
    )
    p.txt("The factor θ² appears because from S_1=−1 the gambler must "
          "first return to 0 (probability θ), then advance from 0 to 1 "
          "(another independent probability θ), giving θ².")

    p.AL("b)  Solving the quadratic:")
    p.eqn(
        "q*theta^2 - theta + p = 0",
        "(1-p)*theta^2 - theta + p = 0",
        "",
        "Discriminant: 1 - 4*(1-p)*p = 1 - 4p + 4p^2 = (1-2p)^2",
        "Roots: theta = [1 +- (1-2p)] / (2*(1-p))",
        "  theta_1 = [1 + (1-2p)] / (2*(1-p)) = 2*(1-p)/(2*(1-p)) = 1",
        "  theta_2 = [1 - (1-2p)] / (2*(1-p)) = 2p/(2*(1-p)) = p/q",
        "",
        "For p > 1/2: p/q > 1, not a valid probability  =>  theta = 1",
        "For p < 1/2: p/q < 1, theta = p/q < 1 (game ends with prob < 1)",
    )

    p.AL("c)  E[J] and verification:")
    p.eqn(
        "E[J] = p*1 + q*(1 + 2*E[J])",
        "E[J] = p + q + 2*q*E[J]",
        "E[J] - 2*q*E[J] = 1",
        "E[J]*(1 - 2*q) = 1",
        "E[J]*(2p - 1) = 1",
        "E[J] = 1/(2p-1)",
        "",
        "Wald's equality: E[X] = p*1 + q*(-1) = 2p-1",
        "E[S_J] = (2p-1) * 1/(2p-1) = 1 = S_J  ✓",
        "",
        "For p = 2/3:  q = 1/3,  theta = 1",
        "  E[J] = 1/(2*(2/3)-1) = 1/(4/3-1) = 1/(1/3) = 3",
        "  E[S_J] = 1  ✓",
        "",
        "As p --> 1/2+:  E[J] = 1/(2p-1) --> +inf",
        "(The game takes longer and longer as the bias vanishes.)",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Stopping rule A — Negative Binomial:")
    p.eqn(
        "q = 0.2,  target = 4 defectives",
        "J_A ~ NegBin(4, 0.2)  =>  E[J_A] = 4/q = 4/0.2 = 20",
        "",
        "Wald's equality: E[X_i] = q = 0.2",
        "E[S_{J_A}] = 0.2 * 20 = 4  ✓",
        "  (exactly 4 defectives found, by construction)",
    )

    p.AL("b)  Good items inspected:")
    p.eqn(
        "G = J_A - S_{J_A}  (total inspected minus defectives)",
        "E[G] = E[J_A] - E[S_{J_A}] = 20 - 4 = 16 good items",
        "",
        "Long-run fraction good = E[G]/E[J_A] = 16/20 = 0.8 = p  ✓",
    )

    p.AL("c)  Stopping rule B — target 3 defectives, then 6:")
    p.eqn(
        "q' = 1/4,  target k = 3",
        "E[J_B] = k/q' = 3/(1/4) = 12",
        "",
        "[Verify: Wald's equality  E[S_{J_B}] = (1/4)*12 = 3  ✓]",
        "",
        "For target k = 6 (same q' = 1/4):",
        "E[J_B] = 6/(1/4) = 24  (scales linearly with target)",
        "",
        "General rule: E[J] = target / E[X] = k/q'",
    )

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== V2  |  Folder 2026-05-21 ===")
    print("Topics: Martingales | Wald's Equality\n")

    print("Generating question PDFs …")
    mart_q()
    wald_q()

    print("\nGenerating answer-key PDFs …")
    mart_a()
    wald_a()

    print("\nDone.  4 PDFs written to:")
    print(f"  {os.path.relpath(QQ, BASE)}/")
    print(f"  {os.path.relpath(AK, BASE)}/")
