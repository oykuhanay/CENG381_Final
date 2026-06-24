#!/usr/bin/env python3
"""
CENG381 - V2 Generator  |  Folder 2026-06-04  (final folder)
Topics : De Moivre's Martingale
         Product-Form Martingales and Jensen's Inequality
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
# 1.  DE MOIVRE'S MARTINGALE
# ══════════════════════════════════════════════════════════════════════════════

def dm_q():
    S = "De_Moivres_Martingale"
    p = ExamPDF("De Moivre's Martingale  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Consider a biased random walk with steps X_i = +1 w.p. p and "
        "X_i = −1 w.p. q = 1−p (p ≠ 1/2).  "
        "The drift per step is μ = p − q = 2p − 1.  "
        "Define the compensated random walk  Y_n = S_n − n(p − q).")
    p.sub("a",
          "Show that {Y_n; n ≥ 0} is a martingale.  "
          "Write Y_n = Y_{n-1} + (X_n − (p−q)) and compute "
          "E[X_n − (p−q)] to verify the martingale condition.")
    p.sub("b",
          "What is E[S_n | S_0 = 0]?  What is E[Y_n]?  "
          "Interpret Y_n as S_n with its expected growth removed.")
    p.sub("c",
          "For p = 0.7 (biased towards +1): "
          "(i) Compute the drift μ = p − q. "
          "(ii) A gambler starts at S_0 = 5.  "
          "Write down Y_n for this case and compute E[S_{100} | S_0 = 5].")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "De Moivre's Martingale: for a biased random walk (p ≠ 1/2) with "
        "S_0 = k, define  M_n = (q/p)^{S_n}.")
    p.sub("a",
          "Prove {M_n} is a martingale.  "
          "Use the factorization  M_n = M_{n-1} · (q/p)^{X_n}  "
          "and compute  E[(q/p)^{X_n}]  "
          "(where X_n = +1 w.p. p and −1 w.p. q).  "
          "Show the result equals 1.")
    p.sub("b",
          "A gambler starts with $k and plays until reaching $0 (ruin) or "
          "$N (goal).  Let J be the stopping time and p_k = P(reach N | S_0 = k).  "
          "Apply the Optional Stopping Theorem to M_n: "
          "E[M_J] = M_0.  "
          "At time J, either S_J = N (prob p_k) or S_J = 0 (prob 1−p_k).  "
          "Derive the formula for p_k.")
    p.sub("c",
          "Check: for the symmetric walk p = 1/2, the formula p_k = [(q/p)^k−1]/[(q/p)^N−1] "
          "is indeterminate (0/0).  Set r = q/p and apply L'Hôpital's rule as r → 1 "
          "to show that p_k → k/N.  Verify this matches the fair-martingale result "
          "from the previous topic.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "Apply De Moivre's formula  p_k = [(q/p)^k − 1] / [(q/p)^N − 1]  "
        "to the following Gambler's Ruin problems.")
    p.sub("a",
          "Favorable game: p = 2/3, q = 1/3.  "
          "Gambler starts at $2 with goal $4 (N = 4).  "
          "Compute q/p, then find p_2.  "
          "Sanity check: is p_2 > 1/2?  (It should be, since p > 1/2.)")
    p.sub("b",
          "Unfavorable game: p = 1/3, q = 2/3.  "
          "Gambler starts at $3 with goal $5 (N = 5).  "
          "Compute q/p, then find p_3.  "
          "Express p_3 as a fraction and check p_3 < 1/2.")
    p.sub("c",
          "For the unfavorable game in (b), also compute p_1 and p_4.  "
          "Verify that p_k is a decreasing function of k "
          "(more money does not help when the game is unfavorable).  "
          "Hint: check whether dp_k/dk < 0 or simply compare p_1, p_3, p_4 numerically.")

    p.save(qp(S, "Practice_1.pdf"))


def dm_a():
    S = "De_Moivres_Martingale"
    p = ExamPDF("De Moivre's Martingale  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Compensated walk is a martingale:")
    p.eqn(
        "Y_n = Y_{n-1} + X_n - (p-q)",
        "",
        "E[Y_n | Y_{n-1}, ..., Y_1]",
        "= Y_{n-1} + E[X_n - (p-q)]",
        "= Y_{n-1} + E[X_n] - (p-q)",
        "= Y_{n-1} + (p-q) - (p-q)",
        "= Y_{n-1}  ✓",
    )

    p.AL("b)  Expected values:")
    p.eqn(
        "E[S_n | S_0=0] = n*(p-q)   (drift n*(p-q) per step)",
        "E[Y_n] = E[S_n - n*(p-q)] = n*(p-q) - n*(p-q) = 0",
    )
    p.txt("Y_n is S_n with its expected trend removed.  "
          "A martingale has constant expectation; subtracting the drift achieves this.")

    p.AL("c)  Numerical example with p = 0.7:")
    p.eqn(
        "mu = p - q = 0.7 - 0.3 = 0.4",
        "",
        "(i)  Drift per step = 0.4",
        "",
        "(ii) S_0 = 5  =>  Y_n = S_n - 5 - n*0.4  (using Y_0 = S_0 - 0*(p-q) = 5)",
        "     Actually Y_n = S_n - n*(p-q), so Y_0 = S_0 = 5 if S_0=5,",
        "     and Y_n = S_n - n*0.4.",
        "",
        "     E[S_100 | S_0=5] = 5 + 100*0.4 = 45",
    )

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Proof that {M_n = (q/p)^{S_n}} is a martingale:")
    p.eqn(
        "M_n = (q/p)^{S_{n-1} + X_n} = (q/p)^{S_{n-1}} * (q/p)^{X_n} = M_{n-1} * (q/p)^{X_n}",
        "",
        "E[(q/p)^{X_n}]",
        "= p * (q/p)^1   +   q * (q/p)^{-1}",
        "= p * (q/p)     +   q * (p/q)",
        "= q             +   p",
        "= 1",
        "",
        "E[M_n | M_{n-1},...] = M_{n-1} * E[(q/p)^{X_n}] = M_{n-1} * 1 = M_{n-1}  ✓",
    )

    p.AL("b)  Gambler's Ruin formula via OST:")
    p.eqn(
        "E[M_J] = M_0 = (q/p)^k",
        "",
        "At stopping: M_J = (q/p)^N w.p. p_k,   M_J = (q/p)^0 = 1 w.p. 1-p_k",
        "",
        "p_k * (q/p)^N + (1-p_k) * 1 = (q/p)^k",
        "p_k * [(q/p)^N - 1] = (q/p)^k - 1",
        "",
        "p_k  =  [(q/p)^k - 1] / [(q/p)^N - 1]",
    )

    p.AL("c)  Limiting case p = 1/2 (r = q/p --> 1):")
    p.eqn(
        "Let r = q/p.  As r --> 1, both numerator r^k-1 and denominator r^N-1 --> 0.",
        "",
        "L'Hopital:  d/dr[r^k - 1] = k*r^{k-1}",
        "            d/dr[r^N - 1] = N*r^{N-1}",
        "",
        "lim_{r->1} (r^k-1)/(r^N-1) = k*1^{k-1} / (N*1^{N-1}) = k/N",
        "",
        "So p_k = k/N for p=1/2, matching the fair-martingale OST result.  ✓",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Favorable game: p=2/3, k=2, N=4:")
    p.eqn(
        "q/p = (1/3)/(2/3) = 1/2",
        "",
        "p_2 = [(1/2)^2 - 1] / [(1/2)^4 - 1]",
        "    = [1/4 - 1]     / [1/16 - 1]",
        "    = [-3/4]        / [-15/16]",
        "    = (3/4) * (16/15)",
        "    = 48/60 = 4/5 = 0.80",
        "",
        "Sanity check: p_2 = 0.80 > 0.50  ✓  (favorable game)",
    )

    p.AL("b)  Unfavorable game: p=1/3, k=3, N=5:")
    p.eqn(
        "q/p = (2/3)/(1/3) = 2",
        "",
        "p_3 = [2^3 - 1] / [2^5 - 1]",
        "    = [8 - 1]   / [32 - 1]",
        "    = 7/31  ~=  0.226",
        "",
        "Sanity check: p_3 = 7/31 < 1/2  ✓  (unfavorable game)",
    )

    p.AL("c)  Comparing p_1, p_3, p_4 (unfavorable game, q/p=2, N=5):")
    p.eqn(
        "p_1 = [2^1 - 1] / [2^5 - 1] = 1/31  ~=  0.032",
        "p_3 = [2^3 - 1] / [2^5 - 1] = 7/31  ~=  0.226",
        "p_4 = [2^4 - 1] / [2^5 - 1] = 15/31 ~=  0.484",
        "",
        "p_1 < p_3 < p_4 < 1/2",
    )
    p.txt("Even starting with $4 out of $5, the probability of reaching "
          "the goal is only 48.4% when p=1/3.  "
          "The function p_k is increasing in k (more starting capital helps "
          "even in an unfavorable game), but always stays below 1/2 when p < 1/2.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 2.  PRODUCT-FORM MARTINGALES AND JENSEN'S INEQUALITY
# ══════════════════════════════════════════════════════════════════════════════

def pmj_q():
    S = "Product_Martingales_and_Jensens_Inequality"
    p = ExamPDF("Product-Form Martingales and Jensen's Inequality  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Let X_1, X_2, ... be i.i.d. random variables with E[X_i] = 1.  "
        "Define the product-form process  Z_n = X_1 · X_2 · ... · X_n  (Z_0 = 1).")
    p.sub("a",
          "Prove that {Z_n; n ≥ 0} is a martingale by computing "
          "E[Z_n | Z_{n-1}, ..., Z_1].  "
          "Factor out Z_{n-1} and use independence of X_n from the past.")
    p.sub("b",
          "Let X_n = 2 w.p. 1/2  and  X_n = 0 w.p. 1/2  (so E[X_n] = 1).  "
          "Compute E[Z_n] and P(Z_n > 0) for each n.  "
          "What is Z_n almost surely as n → ∞?  "
          "Does the limit Z_∞ = lim Z_n satisfy E[Z_∞] = lim E[Z_n]?")
    p.sub("c",
          "The example in (b) shows a martingale with constant expectation 1 "
          "that converges almost surely to 0.  "
          "Explain: why does this NOT contradict the definition of a martingale?  "
          "What additional condition (uniform integrability) would guarantee "
          "E[Z_∞] = lim E[Z_n]?")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "Jensen's Inequality: if g is a convex function and X has finite mean, "
        "then  E[g(X)] ≥ g(E[X]).")
    p.sub("a",
          "Let g(x) = x².  "
          "(i) Verify g is convex (g''(x) ≥ 0).  "
          "(ii) Apply Jensen: E[X²] ≥ (E[X])².  "
          "What familiar quantity is E[X²] − (E[X])²?  "
          "What does Jensen say about this quantity?")
    p.sub("b",
          "Let g(x) = e^x (convex everywhere).  "
          "Jensen says E[e^X] ≥ e^{E[X]}.  "
          "For X ~ Normal(μ, σ²):  E[e^X] = e^{μ + σ²/2}.  "
          "Verify Jensen holds: show e^{μ + σ²/2} ≥ e^μ and explain why equality "
          "holds only when σ² = 0.")
    p.sub("c",
          "Let g(x) = −log(x) for x > 0 (convex since g''(x) = 1/x² > 0).  "
          "Let X take values a_1, a_2, ..., a_n with equal probability 1/n each.  "
          "Apply Jensen to derive the AM–GM inequality:  "
          "(a_1 · a_2 · ... · a_n)^{1/n}  ≤  (a_1 + a_2 + ... + a_n) / n.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A stochastic process {W_n} is a sub-martingale if "
        "E[W_n | W_{n-1}, ..., W_1] ≥ W_{n-1} for all n ≥ 2 "
        "(the process tends to increase on average).")
    p.sub("a",
          "Prove: if {Z_n} is a martingale and h is a convex function with "
          "E[|h(Z_n)|] < ∞, then {h(Z_n)} is a sub-martingale.  "
          "Use Jensen's inequality applied to the conditional expectation.")
    p.sub("b",
          "Let {S_n} be the symmetric random walk (steps ±1 w.p. 1/2, S_0 = 0).  "
          "(i) Show {S_n²} is a sub-martingale by computing E[S_n² | S_{n-1}].  "
          "(ii) Since {S_n² − n} is a martingale (proved earlier), "
          "what is E[S_n²] for all n?")
    p.sub("c",
          "Show {|S_n|} is also a sub-martingale by the same Jensen argument "
          "(h(x) = |x| is convex).  "
          "Is E[|S_n|] an increasing sequence?  "
          "For large n, the Central Limit Theorem gives S_n ≈ sqrt(n)·Z where Z ~ N(0,1), "
          "so E[|S_n|] ≈ sqrt(n) · E[|Z|] = sqrt(2n/π).  "
          "Check: is this consistent with {|S_n|} being a sub-martingale?")

    p.save(qp(S, "Practice_1.pdf"))


def pmj_a():
    S = "Product_Martingales_and_Jensens_Inequality"
    p = ExamPDF("Product-Form Martingales and Jensen's Inequality  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Product-form martingale proof:")
    p.eqn(
        "Z_n = Z_{n-1} * X_n",
        "",
        "E[Z_n | Z_{n-1}, ..., Z_1]",
        "= E[Z_{n-1} * X_n | Z_{n-1}, ..., Z_1]",
        "= Z_{n-1} * E[X_n | Z_{n-1}, ..., Z_1]",
        "= Z_{n-1} * E[X_n]           (X_n independent of past)",
        "= Z_{n-1} * 1 = Z_{n-1}  ✓",
    )

    p.AL("b)  Example X_n = 2 w.p. 1/2, 0 w.p. 1/2:")
    p.eqn(
        "E[X_n] = 2*(1/2) + 0*(1/2) = 1  ✓",
        "",
        "Z_n = X_1 * ... * X_n",
        "   = 2^n  if all X_i = 2  (prob (1/2)^n)",
        "   = 0    if any X_i = 0  (prob 1 - (1/2)^n)",
        "",
        "E[Z_n] = 2^n * (1/2)^n + 0 = 1  for all n",
        "P(Z_n > 0) = (1/2)^n --> 0  as n --> inf",
        "",
        "Z_n --> 0  almost surely  (eventually some X_i = 0, making product 0)",
        "E[Z_inf] = E[0] = 0  ≠  lim E[Z_n] = 1",
    )

    p.AL("c)  Why this does not contradict the martingale definition:")
    p.txt(
        "The martingale definition only requires E[Z_n | past] = Z_{n-1} for "
        "each finite n — it says nothing about what happens at n = ∞.  "
        "The martingale convergence theorem guarantees Z_n → Z_∞ a.s. under "
        "certain conditions, but does NOT guarantee E[Z_∞] = lim E[Z_n] "
        "unless {Z_n} is also uniformly integrable.")
    p.txt(
        "Uniform integrability (UI) fails here: the distribution of Z_n is "
        "increasingly concentrated on the single very large value 2^n "
        "(with tiny probability 2^{-n}), making the tails unbounded.  "
        "UI would require sup_n E[Z_n · 1_{Z_n > M}] → 0 as M → ∞, which fails.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Jensen for g(x) = x²:")
    p.eqn(
        "(i) g''(x) = 2 > 0  =>  g is convex  ✓",
        "",
        "(ii) Jensen: E[X^2] >= (E[X])^2",
        "  => E[X^2] - (E[X])^2 >= 0",
        "  => Var(X) >= 0  (variance is always non-negative)  ✓",
    )

    p.AL("b)  Jensen for g(x) = e^x, X ~ Normal(mu, sigma^2):")
    p.eqn(
        "Jensen: E[e^X] >= e^{E[X]} = e^mu",
        "",
        "For X ~ N(mu, sigma^2):  E[e^X] = e^{mu + sigma^2/2}",
        "",
        "Check: e^{mu + sigma^2/2} >= e^mu",
        "  iff  mu + sigma^2/2  >=  mu",
        "  iff  sigma^2/2 >= 0  ✓  (always true)",
        "",
        "Equality holds iff sigma^2 = 0 (X is deterministic = mu).",
    )

    p.AL("c)  Jensen for g(x) = -log(x); AM-GM inequality:")
    p.eqn(
        "g''(x) = 1/x^2 > 0  =>  g is convex for x > 0  ✓",
        "",
        "X = a_i w.p. 1/n for i=1,...,n",
        "E[X] = (a_1+...+a_n)/n  =  AM",
        "E[g(X)] = (1/n)*(-log a_1 - ... - log a_n) = -log(GM)",
        "  where GM = (a_1*...*a_n)^{1/n}",
        "",
        "Jensen: E[g(X)] >= g(E[X])",
        "  -log(GM)  >=  -log(AM)",
        "   log(GM)  <=   log(AM)",
        "       GM   <=   AM  ✓",
        "",
        "(a_1*a_2*...*a_n)^{1/n}  <=  (a_1+a_2+...+a_n)/n",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Submartingale via Jensen:")
    p.eqn(
        "E[h(Z_n) | Z_{n-1}, ..., Z_1]",
        ">=  h(E[Z_n | Z_{n-1}, ..., Z_1])    [Jensen, since h convex]",
        " =  h(Z_{n-1})                        [martingale condition]",
        "",
        "So E[h(Z_n) | past] >= h(Z_{n-1}), i.e., {h(Z_n)} is a sub-martingale.  ✓",
    )

    p.AL("b)  {S_n^2} is a submartingale:")
    p.eqn(
        "(i)  E[S_n^2 | S_{n-1}]",
        "   = E[(S_{n-1} + X_n)^2 | S_{n-1}]",
        "   = S_{n-1}^2 + 2*S_{n-1}*E[X_n] + E[X_n^2]",
        "   = S_{n-1}^2 + 0 + 1",
        "   = S_{n-1}^2 + 1  >=  S_{n-1}^2  ✓  (sub-martingale)",
        "",
        "(ii) {S_n^2 - n} is a martingale  =>  E[S_n^2 - n] = E[S_0^2 - 0] = 0",
        "     E[S_n^2] = n",
    )

    p.AL("c)  {|S_n|} is a submartingale; CLT check:")
    p.eqn(
        "h(x) = |x| is convex (V-shape; h''(x) = 0 for x != 0 and",
        "  the kink at 0 satisfies the convexity condition).",
        "",
        "By Jensen applied to the martingale {S_n}:",
        "  E[|S_n| | S_{n-1}, ...] >= |E[S_n | S_{n-1}, ...]| = |S_{n-1}|",
        "So {|S_n|} is a sub-martingale.  ✓",
        "",
        "E[|S_n|] is increasing in n (as required for a sub-martingale).",
        "",
        "CLT check: E[|S_n|] ~= sqrt(2n/pi)  which is increasing in n  ✓",
        "  (The sequence grows like sqrt(n), consistent with the walk spreading out.)",
    )

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== V2  |  Folder 2026-06-04  (final folder) ===")
    print("Topics: De Moivre's Martingale | Product Martingales & Jensen's Inequality\n")

    print("Generating question PDFs ...")
    dm_q()
    pmj_q()

    print("\nGenerating answer-key PDFs ...")
    dm_a()
    pmj_a()

    print("\nDone.  4 PDFs written to:")
    print(f"  {os.path.relpath(QQ, BASE)}/")
    print(f"  {os.path.relpath(AK, BASE)}/")
