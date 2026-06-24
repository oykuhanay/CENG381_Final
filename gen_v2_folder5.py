#!/usr/bin/env python3
"""
CENG381 - V2 Generator  |  Folder 2026-04-09
Topics : Chapman-Kolmogorov & Diagonalization  |  Poisson Process
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
# 1.  CHAPMAN-KOLMOGOROV AND DIAGONALIZATION
# ══════════════════════════════════════════════════════════════════════════════

def ckd_q():
    S = "Chapman_Kolmogorov_and_Diagonalization"
    p = ExamPDF("Chapman-Kolmogorov & Diagonalization  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "A 2-state weather Markov chain has states {S = Sunny, R = Rainy} "
        "with daily transition matrix:")
    p.mat([
        "          S      R",
        "  S  [  0.7    0.3  ]",
        "  R  [  0.5    0.5  ]",
    ])
    p.sub("a",
          "Compute P² = P·P directly by matrix multiplication.  "
          "Show all arithmetic.")
    p.sub("b",
          "State the Chapman-Kolmogorov equation for P^(n+m)(i,j) in terms "
          "of P^n and P^m.  "
          "Using P² from part (a), apply C-K to compute P⁴ = P²·P².")
    p.sub("c",
          "Verify one entry:  show that P⁴(S,S) from part (b) equals "
          "the (S,S) entry you get from multiplying P²·P² directly.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "Continuing with the same chain (p = 0.3, q = 0.5, so p+q = 0.8).  "
        "Use diagonalization to derive a closed-form expression for P^n.")
    p.sub("a",
          "Find the eigenvalues of P by solving det(P − λI) = 0.  "
          "Show that λ₁ = 1 and λ₂ = 1 − p − q = 0.2.")
    p.sub("b",
          "For a 2-state chain with P(S,S)=1−p and P(R,S)=q, the n-step "
          "return probability is:\n\n"
          "  P^n(S,S) = q/(p+q)  +  (1−p−q)^n · p/(p+q)\n\n"
          "Verify this formula for n=1 by checking it recovers P(S,S)=0.7.")
    p.sub("c",
          "Use the formula to compute P⁴(S,S).  "
          "Confirm it matches the result from Q1(b).")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "Still using the weather chain (p=0.3, q=0.5).  "
        "The closed-form P^n(S,S) = 5/8 + (3/8)·(0.2)^n allows us to "
        "study long-run behaviour precisely.")
    p.sub("a",
          "Find the stationary distribution π by taking the limit "
          "P^n(S,S) → π_S as n → ∞.  Verify π by solving π·P = π.")
    p.sub("b",
          "Find the smallest integer n* such that "
          "|P^n(S,S) − π_S| < 0.01.  "
          "Show your work using the formula.")
    p.sub("c",
          "The second eigenvalue λ₂ = 0.2 governs the speed of convergence.  "
          "Suppose instead λ₂ = 0.9 (a nearly-periodic chain).  "
          "How would n* change?  Explain qualitatively why chains with "
          "λ₂ closer to 1 mix more slowly.")

    p.save(qp(S, "Practice_1.pdf"))


def ckd_a():
    S = "Chapman_Kolmogorov_and_Diagonalization"
    p = ExamPDF("Chapman-Kolmogorov & Diagonalization  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  P² by direct multiplication:")
    p.eqn(
        "P^2(S,S) = P(S,S)*P(S,S) + P(S,R)*P(R,S)",
        "         = 0.7*0.7 + 0.3*0.5 = 0.49 + 0.15 = 0.64",
        "",
        "P^2(S,R) = P(S,S)*P(S,R) + P(S,R)*P(R,R)",
        "         = 0.7*0.3 + 0.3*0.5 = 0.21 + 0.15 = 0.36",
        "",
        "P^2(R,S) = P(R,S)*P(S,S) + P(R,R)*P(R,S)",
        "         = 0.5*0.7 + 0.5*0.5 = 0.35 + 0.25 = 0.60",
        "",
        "P^2(R,R) = P(R,S)*P(S,R) + P(R,R)*P(R,R)",
        "         = 0.5*0.3 + 0.5*0.5 = 0.15 + 0.25 = 0.40",
    )
    p.mat([
        "        S      R",
        "  S  [ 0.64   0.36 ]",
        "  R  [ 0.60   0.40 ]",
    ])

    p.AL("b)  Chapman-Kolmogorov and P⁴ = P²·P²:")
    p.txt(
        "C-K: P^(n+m)(i,j) = sum_k P^n(i,k) * P^m(k,j)  (matrix product P^n * P^m).")
    p.eqn(
        "P^4(S,S) = P^2(S,S)*P^2(S,S) + P^2(S,R)*P^2(R,S)",
        "         = 0.64*0.64 + 0.36*0.60",
        "         = 0.4096 + 0.2160 = 0.6256",
        "",
        "P^4(S,R) = 0.64*0.36 + 0.36*0.40 = 0.2304 + 0.1440 = 0.3744",
        "P^4(R,S) = 0.60*0.64 + 0.40*0.60 = 0.3840 + 0.2400 = 0.6240",
        "P^4(R,R) = 0.60*0.36 + 0.40*0.40 = 0.2160 + 0.1600 = 0.3760",
    )

    p.AL("c)  Verification of P⁴(S,S):")
    p.txt(
        "Direct: multiply row S of P² by column S of P²:")
    p.eqn(
        "[0.64  0.36] * [0.64, 0.60]^T = 0.64*0.64 + 0.36*0.60 = 0.6256  ✓",
    )

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Eigenvalues:")
    p.eqn(
        "det(P - lambda*I) = 0",
        "",
        "| 0.7-lambda   0.3  |",
        "| 0.5          0.5-lambda | = 0",
        "",
        "(0.7-lambda)(0.5-lambda) - 0.3*0.5 = 0",
        "0.35 - 1.2*lambda + lambda^2 - 0.15 = 0",
        "lambda^2 - 1.2*lambda + 0.20 = 0",
        "(lambda - 1)(lambda - 0.2) = 0",
        "",
        "lambda_1 = 1,   lambda_2 = 0.2 = 1-p-q  ✓",
    )

    p.AL("b)  Verification of the formula for n=1:")
    p.eqn(
        "P^n(S,S) = q/(p+q) + (1-p-q)^n * p/(p+q)",
        "         = 0.5/0.8 + (0.2)^n * 0.3/0.8",
        "         = 5/8     + (3/8)*(0.2)^n",
        "",
        "n=1:  5/8 + (3/8)*0.2 = 5/8 + 3/40 = 25/40 + 3/40 = 28/40 = 0.70",
        "      = P(S,S)  ✓",
    )

    p.AL("c)  P⁴(S,S) from formula vs Q1:")
    p.eqn(
        "P^4(S,S) = 5/8 + (3/8)*(0.2)^4",
        "         = 5/8 + (3/8)*0.0016",
        "         = 0.6250 + 0.0006 = 0.6256  ✓  (matches Q1)",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Stationary distribution:")
    p.eqn(
        "lim_{n->inf} P^n(S,S) = 5/8 + 0 = 5/8",
        "pi_S = 5/8 = 0.625,    pi_R = 1 - 5/8 = 3/8 = 0.375",
    )
    p.txt("Verify π·P = π:")
    p.eqn(
        "(pi*P)_S = (5/8)*0.7 + (3/8)*0.5 = 35/80 + 15/80 = 50/80 = 5/8  ✓",
        "(pi*P)_R = (5/8)*0.3 + (3/8)*0.5 = 15/80 + 15/80 = 30/80 = 3/8  ✓",
    )

    p.AL("b)  Smallest n* such that |P^n(S,S) − π_S| < 0.01:")
    p.eqn(
        "|P^n(S,S) - 5/8| = (3/8)*(0.2)^n  <  0.01",
        "(0.2)^n  <  0.01 * 8/3 = 0.02667",
        "n * ln(0.2)  <  ln(0.02667)",
        "n  >  ln(0.02667) / ln(0.2) = (-3.625) / (-1.609) = 2.25",
        "Smallest integer: n* = 3",
        "",
        "Check n=3: (3/8)*(0.2)^3 = (3/8)*0.008 = 0.003 < 0.01  ✓",
        "Check n=2: (3/8)*(0.2)^2 = (3/8)*0.04  = 0.015 > 0.01  ✗",
    )

    p.AL("c)  Effect of λ₂ on mixing speed:")
    p.eqn(
        "If lambda_2 = 0.9:",
        "|P^n(S,S) - pi_S| = C*(0.9)^n  <  0.01",
        "(0.9)^n < 0.01/C",
        "n > log(0.01/C) / log(0.9)  =>  n* ~ 44 steps  (much larger)",
    )
    p.txt(
        "When λ₂ is close to 1, the term λ₂^n decays slowly — many "
        "steps are needed before the chain 'forgets' its starting state.  "
        "Geometrically, the chain almost never mixes because the "
        "spectral gap (1−|λ₂|) is tiny.  "
        "A spectral gap of 1−0.2=0.8 gives very fast mixing; "
        "a gap of 1−0.9=0.1 is 8× slower.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 2.  POISSON PROCESS
# ══════════════════════════════════════════════════════════════════════════════

def poisson_q():
    S = "Poisson_Process"
    p = ExamPDF("Poisson Process  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Emails arrive at a server according to a Poisson process with "
        "rate λ = 3 emails per hour.")
    p.sub("a",
          "Write the PMF of N(t), the number of emails arriving in t hours.  "
          "State also E[N(t)] and Var(N(t)).")
    p.sub("b",
          "Compute P(N(2) = 6) and P(N(2) ≤ 1).  "
          "Leave your answers in exact form (powers of e) and also "
          "give decimal approximations.")
    p.sub("c",
          "Using the counting-process connection, express the event "
          "{first email arrives after time t} in terms of N(t).  "
          "Find P(first email arrives after t = 1/2 hour).")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "Customers arrive at a coffee shop at rate λ = 10 per hour "
        "(Poisson).  "
        "Each customer independently orders a latte with probability p = 0.4.  "
        "Separately, a rival coffee truck parked nearby attracts customers "
        "at rate μ = 6 per hour (independent Poisson).")
    p.sub("a",
          "The latte-ordering process is a thinned Poisson process.  "
          "State its rate.  "
          "Find P(exactly 3 lattes ordered in 1 hour).")
    p.sub("b",
          "A health inspector monitors the total traffic — coffee shop plus "
          "truck combined.  State the distribution and rate of the combined "
          "arrival process.  "
          "Find P(at least 2 arrivals in 15 minutes).")
    p.sub("c",
          "It is now 9 AM and N_shop(1) = 4 (4 customers arrived in the "
          "first hour).  "
          "Using the independent-increments property, find "
          "E[N_shop(3) | N_shop(1) = 4].")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "This question connects the Poisson process to its "
        "differential-equation characterisation.")
    p.sub("a",
          "From the infinitesimal description — "
          "P(one arrival in (t, t+Δ)) = λΔ + o(Δ) and "
          "P(two or more arrivals in (t, t+Δ)) = o(Δ) — "
          "derive the Kolmogorov forward equation:\n\n"
          "  P_j′(t)  =  −λ P_j(t)  +  λ P_{j−1}(t)\n\n"
          "where P_j(t) = P(N(t) = j).")
    p.sub("b",
          "Verify that P_j(t) = (λt)^j · e^{−λt} / j! satisfies the "
          "forward equation.  "
          "(Differentiate with respect to t and substitute.)")
    p.sub("c",
          "A Poisson process with rate λ = 2 models bus arrivals at a stop.  "
          "You arrive at the stop at time 0.  "
          "Find P(you wait more than 45 minutes for the first bus).  "
          "Also compute the expected wait.  "
          "Express your answer in exact form and give a decimal approximation.")

    p.save(qp(S, "Practice_1.pdf"))


def poisson_a():
    S = "Poisson_Process"
    p = ExamPDF("Poisson Process  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  PMF, mean, and variance:")
    p.eqn(
        "P(N(t) = n) = (lambda*t)^n * e^(-lambda*t) / n!,  n = 0, 1, 2, ...",
        "",
        "E[N(t)] = lambda*t",
        "Var(N(t)) = lambda*t",
        "(For a Poisson distribution, mean = variance = lambda*t.)",
    )

    p.AL("b)  Specific probabilities for t=2, λ=3 → λt=6:")
    p.eqn(
        "P(N(2)=6) = 6^6 * e^(-6) / 6!  =  46656 * e^(-6) / 720",
        "           = 64.8 * e^(-6)  ~=  64.8 * 0.002479  ~=  0.1606",
        "",
        "P(N(2)<=1) = P(N(2)=0) + P(N(2)=1)",
        "           = e^(-6) + 6*e^(-6) = 7*e^(-6)",
        "           ~= 7 * 0.002479 = 0.01735",
    )

    p.AL("c)  First email after time t:")
    p.eqn(
        "{first email after t} = {N(t) = 0}",
        "",
        "P(first email after t=1/2) = P(N(1/2)=0)",
        "  = e^(-lambda*(1/2)) = e^(-3/2) = e^(-1.5)  ~=  0.2231",
    )

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Thinned Poisson (latte orders):")
    p.eqn(
        "Thinning property: Poisson(lambda) thinned by p -> Poisson(lambda*p)",
        "Latte rate = 10 * 0.4 = 4 per hour",
        "",
        "P(3 lattes in 1 hr) = 4^3 * e^(-4) / 3! = 64 * e^(-4) / 6",
        "                    = 32/3 * e^(-4)  ~=  10.667 * 0.01832  ~=  0.1954",
    )

    p.AL("b)  Superposition (combined arrivals):")
    p.eqn(
        "Superposition: Poisson(lambda) + Poisson(mu) -> Poisson(lambda+mu)",
        "Combined rate = 10 + 6 = 16 per hour",
        "In 15 min = 1/4 hour:  mean = 16 * (1/4) = 4 arrivals",
        "",
        "P(at least 2 in 15 min) = 1 - P(N(1/4)=0) - P(N(1/4)=1)",
        "                        = 1 - e^(-4) - 4*e^(-4)",
        "                        = 1 - 5*e^(-4)",
        "                       ~= 1 - 5*0.01832 = 1 - 0.09158 = 0.9084",
    )

    p.AL("c)  Conditional expectation using independent increments:")
    p.txt(
        "The Poisson process has independent increments: "
        "N_shop(3)−N_shop(1) is independent of N_shop(1).")
    p.eqn(
        "E[N_shop(3) | N_shop(1)=4]",
        "  = E[N_shop(1) | N_shop(1)=4]  +  E[N_shop(3)-N_shop(1) | N_shop(1)=4]",
        "  = 4  +  E[N_shop(3)-N_shop(1)]     [by independence]",
        "  = 4  +  lambda*(3-1)",
        "  = 4  +  10*2  =  4 + 20  =  24",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Derivation of the forward equation:")
    p.eqn(
        "P_j(t+Delta) = P(N(t+Delta)=j)",
        "             = P(no arrival in (t,t+Delta)) * P(N(t)=j)",
        "             + P(one arrival in (t,t+Delta)) * P(N(t)=j-1)",
        "             + o(Delta)",
        "             = (1 - lambda*Delta + o(Delta))*P_j(t)",
        "             + (lambda*Delta + o(Delta))*P_{j-1}(t) + o(Delta)",
        "",
        "P_j(t+Delta) - P_j(t) = -lambda*Delta*P_j(t)",
        "                       + lambda*Delta*P_{j-1}(t) + o(Delta)",
        "",
        "Divide by Delta and take Delta->0:",
        "  P_j'(t) = -lambda*P_j(t) + lambda*P_{j-1}(t)  ✓",
    )

    p.AL("b)  Verification that the Poisson PMF satisfies the forward equation:")
    p.txt("Let P_j(t) = (λt)^j e^{−λt} / j!.  Differentiate:")
    p.eqn(
        "d/dt [(lambda*t)^j * e^(-lambda*t) / j!]",
        "  = [j*(lambda*t)^(j-1)*lambda * e^(-lambda*t)",
        "     + (lambda*t)^j * (-lambda) * e^(-lambda*t)] / j!",
        "  = lambda*e^(-lambda*t) * [(lambda*t)^(j-1)/(j-1)!",
        "                           - (lambda*t)^j / j!]",
        "  = lambda * P_{j-1}(t) - lambda * P_j(t)",
        "  = -lambda*P_j(t) + lambda*P_{j-1}(t)  ✓",
    )

    p.AL("c)  Bus waiting time (λ=2, t=3/4 hour for 45 min):")
    p.eqn(
        "P(first bus after 45 min) = P(N(3/4) = 0)",
        "  = e^(-lambda * 3/4) = e^(-2 * 3/4) = e^(-3/2)  ~=  0.2231",
        "",
        "E[wait time] = 1/lambda = 1/2 hour = 30 minutes",
    )
    p.txt(
        "The inter-arrival time X₁ is Exponential(λ=2).  "
        "P(X₁ > 3/4) = P(N(3/4)=0) = e^{−3/2} ≈ 22.3%.  "
        "The expected wait is 1/λ = 30 min regardless of how long you "
        "have already waited (memoryless property of the exponential).")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== V2  |  Folder 2026-04-09 ===")
    print("Topics: Chapman-Kolmogorov & Diagonalization | Poisson Process\n")

    print("Generating question PDFs …")
    ckd_q()
    poisson_q()

    print("\nGenerating answer-key PDFs …")
    ckd_a()
    poisson_a()

    print("\nDone.  4 PDFs written to:")
    print(f"  {os.path.relpath(QQ, BASE)}/")
    print(f"  {os.path.relpath(AK, BASE)}/")
