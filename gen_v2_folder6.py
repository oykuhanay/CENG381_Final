#!/usr/bin/env python3
"""
CENG381 - V2 Generator  |  Folder 2026-04-16
Topics : CTMC & Birth-Death Processes  |  Queuing Theory (M/M/1, M/M/inf)
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
# 1.  CTMC AND BIRTH-DEATH PROCESSES
# ══════════════════════════════════════════════════════════════════════════════

def ctmc_q():
    S = "CTMC_and_Birth_Death_Processes"
    p = ExamPDF("CTMC and Birth-Death Processes  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "A machine operates in three states: "
        "0 = Idle, 1 = Working, 2 = Broken.  "
        "The continuous-time transition rates are:\n"
        "  • Idle → Working at rate 2 per hour\n"
        "  • Working → Idle at rate 3 per hour\n"
        "  • Working → Broken at rate 1 per hour\n"
        "  • Broken → Working at rate 2 per hour")
    p.sub("a",
          "Write the 3×3 rate matrix Q.  "
          "Verify that each row sums to 0.")
    p.sub("b",
          "Find the stationary distribution π by solving "
          "π·Q = 0 and π₀ + π₁ + π₂ = 1.")
    p.sub("c",
          "Interpret the result: what fraction of time is the machine "
          "idle, working, and broken?  "
          "What is the expected return time to the Working state?")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "A hospital ward has at most 3 patients at any time.  "
        "The number of patients follows a birth-death process on {0,1,2,3}:\n"
        "  • Birth rates (new admissions):  λ₀=4, λ₁=3, λ₂=2\n"
        "  • Death rates (discharges):  μ₁=2, μ₂=3, μ₃=4")
    p.sub("a",
          "Write the 4×4 rate matrix Q for this birth-death process.")
    p.sub("b",
          "Use the detailed-balance equations "
          "λₙ πₙ = μₙ₊₁ πₙ₊₁ to express π₁, π₂, π₃ in terms of π₀.  "
          "Then normalise to find all four probabilities.")
    p.sub("c",
          "Compute the expected number of patients E[N] = Σ n·πₙ.  "
          "Also find P(ward is full) = π₃.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A frog lives near a pond.  "
        "It jumps from land (state 1) to water (state 0) at rate α = 3 per hour, "
        "and from water to land at rate β = 1 per hour.")
    p.sub("a",
          "Write the rate matrix Q.  "
          "Find the stationary distribution π.  "
          "Interpret: what fraction of time does the frog spend in water?")
    p.sub("b",
          "Construct the embedded discrete-time chain P "
          "by uniformising at rate r = max(q(0), q(1)) = 3.  "
          "Verify that P has the same stationary distribution as the CTMC.")
    p.sub("c",
          "The state probabilities evolve as "
          "P₁(t) = π₁ + C·e^{λ₂ t}, "
          "where λ₂ is the non-zero eigenvalue of Q.  "
          "If the frog starts on land (P₁(0) = 1), find C and write "
          "the explicit formula for P₁(t).  "
          "How long does it take for |P₁(t) − π₁| to fall below 0.05?")

    p.save(qp(S, "Practice_1.pdf"))


def ctmc_a():
    S = "CTMC_and_Birth_Death_Processes"
    p = ExamPDF("CTMC and Birth-Death Processes  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Rate matrix Q:")
    p.mat([
        "         0      1      2",
        "  0  [  -2      2      0  ]",
        "  1  [   3     -4      1  ]",
        "  2  [   0      2     -2  ]",
    ])
    p.eqn(
        "Row sums:  0:  -2+2+0 = 0  ✓",
        "           1:   3-4+1 = 0  ✓",
        "           2:   0+2-2 = 0  ✓",
    )

    p.AL("b)  Stationary distribution  (π·Q = 0):")
    p.eqn(
        "Column equations of pi*Q=0:",
        "  j=0:  -2*pi_0 + 3*pi_1 = 0  =>  pi_1 = (2/3)*pi_0    ...(I)",
        "  j=2:   pi_1   - 2*pi_2 = 0  =>  pi_2 = pi_1/2         ...(II)",
        "         =>  pi_2 = (1/3)*pi_0",
        "  Normalise: pi_0 + (2/3)*pi_0 + (1/3)*pi_0 = 2*pi_0 = 1",
        "  pi_0 = 1/2,  pi_1 = 1/3,  pi_2 = 1/6",
    )

    p.AL("c)  Interpretation and expected return time:")
    p.txt(
        "  Idle: 50% of the time.  "
        "Working: 33.3% of the time.  "
        "Broken: 16.7% of the time.\n\n"
        "Expected return time to Working state = 1/π₁ = 3 hours.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Rate matrix Q (states 0–3):")
    p.mat([
        "         0      1      2      3",
        "  0  [  -4      4      0      0  ]",
        "  1  [   2     -5      3      0  ]",
        "  2  [   0      3     -5      2  ]",
        "  3  [   0      0      4     -4  ]",
    ])

    p.AL("b)  Detailed balance and stationary distribution:")
    p.eqn(
        "lambda_n * pi_n = mu_{n+1} * pi_{n+1}:",
        "",
        "  n=0: lambda_0*pi_0 = mu_1*pi_1  =>  4*pi_0 = 2*pi_1  =>  pi_1 = 2*pi_0",
        "  n=1: lambda_1*pi_1 = mu_2*pi_2  =>  3*2*pi_0 = 3*pi_2  =>  pi_2 = 2*pi_0",
        "  n=2: lambda_2*pi_2 = mu_3*pi_3  =>  2*2*pi_0 = 4*pi_3  =>  pi_3 = pi_0",
        "",
        "Normalise: pi_0 + 2*pi_0 + 2*pi_0 + pi_0 = 6*pi_0 = 1",
        "pi_0 = 1/6,  pi_1 = 1/3,  pi_2 = 1/3,  pi_3 = 1/6",
    )

    p.AL("c)  E[N] and P(ward full):")
    p.eqn(
        "E[N] = 0*(1/6) + 1*(1/3) + 2*(1/3) + 3*(1/6)",
        "     = 0 + 1/3 + 2/3 + 1/2 = 1 + 1/2 = 3/2",
        "",
        "P(ward full) = pi_3 = 1/6  ~=  16.7%",
    )
    p.txt("Note the symmetry: π₀ = π₃ = 1/6, π₁ = π₂ = 1/3.  "
          "This arises because the birth and death rates are mirror-symmetric "
          "around the midpoint (both increase linearly from the boundaries).")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Rate matrix and stationary distribution:")
    p.txt("States: 0 = water, 1 = land.  "
          "q(0,1) = β = 1 (water→land), q(1,0) = α = 3 (land→water).")
    p.mat([
        "       0    1",
        "  0 [ -1    1 ]",
        "  1 [  3   -3 ]",
    ])
    p.eqn(
        "pi*Q = 0:",
        "  j=0:  -pi_0 + 3*pi_1 = 0  =>  pi_0 = 3*pi_1",
        "  Normalise: 3*pi_1 + pi_1 = 1  =>  pi_1 = 1/4,  pi_0 = 3/4",
    )
    p.txt("The frog spends 75% of its time in water and 25% on land.")

    p.AL("b)  Embedded discrete chain P (r = 3):")
    p.eqn(
        "P(x,y) = q(x,y)/r  for x != y;  P(x,x) = 1 - q(x)/r",
        "",
        "P(0,1) = q(0,1)/3 = 1/3,   P(0,0) = 1 - 1/3 = 2/3",
        "P(1,0) = q(1,0)/3 = 3/3 = 1,  P(1,1) = 0",
    )
    p.txt("Stationary of P: solve π·P = π.")
    p.eqn(
        "pi_0 = (2/3)*pi_0 + 1*pi_1  =>  (1/3)*pi_0 = pi_1",
        "pi_0 + pi_1 = 1  =>  (4/3)*pi_0 = 1  =>  pi_0 = 3/4,  pi_1 = 1/4  ✓",
    )

    p.AL("c)  Eigenvalue of Q and time-evolution formula:")
    p.eqn(
        "Eigenvalues of Q: det(Q - lambda*I) = 0",
        "(-1-lambda)(-3-lambda) - 3 = 0",
        "lambda^2 + 4*lambda + 3 - 3 = 0",
        "lambda*(lambda + 4) = 0",
        "lambda_1 = 0,   lambda_2 = -4",
        "",
        "P_1(t) = pi_1 + C*e^(-4t)",
        "P_1(0) = 1 = pi_1 + C = 1/4 + C  =>  C = 3/4",
        "P_1(t) = 1/4 + (3/4)*e^(-4t)",
    )
    p.txt("Time for |P₁(t) − π₁| < 0.05:")
    p.eqn(
        "(3/4)*e^(-4t) < 0.05",
        "e^(-4t) < 0.05*(4/3) = 1/15",
        "-4t < ln(1/15) = -ln(15)",
        "t > ln(15)/4 = 2.708/4 = 0.677 hours  ~=  40.6 minutes",
    )

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 2.  QUEUING THEORY — M/M/1 AND M/M/∞
# ══════════════════════════════════════════════════════════════════════════════

def queue_q():
    S = "Queuing_Theory_MM1_and_MMinf"
    p = ExamPDF("Queuing Theory: M/M/1 and M/M/inf  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "Patients arrive at a clinic according to a Poisson process at rate "
        "λ = 4 per hour.  There is a single doctor who serves patients at rate "
        "μ = 6 per hour (exponential service times).  "
        "Model this as an M/M/1 queue.")
    p.sub("a",
          "Check the stability condition.  Compute the traffic intensity ρ = λ/μ.")
    p.sub("b",
          "For a stable M/M/1 queue the stationary distribution is "
          "πₙ = (1−ρ)·ρⁿ.  "
          "Compute π₀ (probability no patients), π₁, and "
          "P(2 or more patients in system).")
    p.sub("c",
          "Compute E[N] = ρ/(1−ρ) (expected number in system) and "
          "E[T] = 1/(μ−λ) (expected time in system, waiting plus service).  "
          "Verify Little's Law: E[N] = λ·E[T].")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "A car-wash facility has an unlimited number of bays (infinite servers).  "
        "Cars arrive at rate λ = 6 per hour (Poisson).  "
        "Each wash takes Exp(μ) time with mean 1/μ = 20 minutes = 1/3 hour, "
        "so μ = 3 per hour.  "
        "Model this as an M/M/∞ queue.")
    p.sub("a",
          "Explain why M/M/∞ is always stable regardless of λ and μ.  "
          "Write the birth-death rate structure: "
          "birth rate in state n = λ (arrival), "
          "death rate in state n = n·μ (n cars being washed simultaneously).")
    p.sub("b",
          "Using detailed balance λ·πₙ = (n+1)·μ·πₙ₊₁, show that "
          "πₙ = π₀·ρⁿ/n!  where ρ = λ/μ.  "
          "Enforce Σπₙ = 1 to find π₀ = e^{−ρ}.  "
          "State the distribution of N and compute E[N].")
    p.sub("c",
          "With λ=6 and μ=3, compute ρ, π₀, π₁, π₂, and "
          "P(3 or more cars being washed).")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A network router processes packets at service rate μ = 100 packets/second.  "
        "Packets arrive as a Poisson process.  "
        "Assume M/M/1 queuing.")
    p.sub("a",
          "When the arrival rate is λ = 80 packets/second, compute: "
          "ρ, π₀, E[N], the expected time in the system E[T], "
          "and the expected waiting time in the queue "
          "E[W] = E[T] − 1/μ.")
    p.sub("b",
          "The network SLA requires an average queue waiting time "
          "E[W] ≤ 5 ms = 0.005 seconds.  "
          "Using E[W] = λ / [μ(μ−λ)], find the maximum arrival rate λ* "
          "that satisfies this SLA.")
    p.sub("c",
          "Verify Little's Law E[N] = λ·E[T] for the case λ=80, μ=100.  "
          "Also: if a second identical router is added (M/M/2), "
          "qualitatively describe how E[W] changes compared to M/M/1.")

    p.save(qp(S, "Practice_1.pdf"))


def queue_a():
    S = "Queuing_Theory_MM1_and_MMinf"
    p = ExamPDF("Queuing Theory: M/M/1 and M/M/inf  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Stability and traffic intensity:")
    p.eqn(
        "rho = lambda/mu = 4/6 = 2/3  <  1  =>  queue is stable  ✓",
    )

    p.AL("b)  Stationary distribution:")
    p.eqn(
        "pi_n = (1 - rho) * rho^n = (1/3) * (2/3)^n",
        "",
        "pi_0 = 1/3    ~=  0.333  (no patients)",
        "pi_1 = (1/3)*(2/3) = 2/9  ~=  0.222",
        "",
        "P(N >= 2) = 1 - pi_0 - pi_1 = 1 - 1/3 - 2/9 = 1 - 5/9 = 4/9  ~=  0.444",
    )

    p.AL("c)  E[N], E[T], and Little's Law:")
    p.eqn(
        "E[N] = rho / (1 - rho) = (2/3) / (1/3) = 2 patients",
        "",
        "E[T] = 1 / (mu - lambda) = 1 / (6-4) = 1/2 hour = 30 minutes",
        "",
        "Little's Law: E[N] = lambda * E[T]",
        "  LHS = 2",
        "  RHS = 4 * (1/2) = 2  ✓",
    )

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Why M/M/∞ is always stable:")
    p.txt(
        "In state n there are n servers working simultaneously, so the total "
        "service rate is n·μ — it grows without bound as n increases.  "
        "No matter how large the queue gets, the departure rate eventually "
        "exceeds the arrival rate λ, so the queue never drifts to infinity.  "
        "Rate structure: birth rate λₙ = λ (all n); death rate μₙ = n·μ.")

    p.AL("b)  Stationary distribution derivation:")
    p.eqn(
        "Detailed balance:  lambda * pi_n = (n+1)*mu * pi_{n+1}",
        "  => pi_{n+1} = (lambda / ((n+1)*mu)) * pi_n = (rho/(n+1)) * pi_n",
        "",
        "Telescope:  pi_n = pi_0 * rho^n / n!",
        "",
        "Enforce sum = 1:",
        "  pi_0 * sum_{n=0}^{inf} rho^n/n! = pi_0 * e^{rho} = 1",
        "  => pi_0 = e^{-rho}",
        "",
        "pi_n = e^{-rho} * rho^n / n!   [Poisson(rho) distribution]",
        "E[N] = rho = lambda/mu",
    )

    p.AL("c)  Numerical values (λ=6, μ=3, ρ=2):")
    p.eqn(
        "rho = 6/3 = 2",
        "pi_0 = e^{-2}  ~=  0.1353",
        "pi_1 = e^{-2} * 2   ~=  0.2707",
        "pi_2 = e^{-2} * 4/2 = 2*e^{-2}  ~=  0.2707",
        "",
        "P(N >= 3) = 1 - pi_0 - pi_1 - pi_2",
        "          = 1 - e^{-2}*(1 + 2 + 2)",
        "          = 1 - 5*e^{-2}",
        "         ~= 1 - 5*0.1353 = 1 - 0.6767 = 0.3233",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Performance metrics (λ=80, μ=100):")
    p.eqn(
        "rho = 80/100 = 0.8",
        "pi_0 = 1 - rho = 0.2  (20% chance router is idle)",
        "",
        "E[N] = rho/(1-rho) = 0.8/0.2 = 4 packets",
        "",
        "E[T] = 1/(mu-lambda) = 1/20 = 0.05 s = 50 ms",
        "",
        "E[W] = E[T] - 1/mu = 1/20 - 1/100 = 5/100 - 1/100 = 4/100",
        "     = 0.04 s = 40 ms",
    )

    p.AL("b)  Maximum arrival rate for SLA E[W] ≤ 5 ms:")
    p.eqn(
        "E[W] = lambda / [mu*(mu - lambda)]  <=  0.005",
        "",
        "lambda / [100*(100 - lambda)]  <=  0.005",
        "lambda  <=  0.005 * 100 * (100 - lambda)",
        "lambda  <=  0.5*(100 - lambda)",
        "lambda  <=  50 - 0.5*lambda",
        "1.5*lambda  <=  50",
        "lambda*  <=  100/3  ~=  33.3 packets/second",
    )
    p.txt(
        "To maintain E[W] ≤ 5 ms, the arrival rate must not exceed "
        "100/3 ≈ 33.3 packets/second — less than half the current rate of 80.")

    p.AL("c)  Little's Law verification and M/M/2 comparison:")
    p.eqn(
        "Little's Law:  E[N] = lambda * E[T]",
        "  LHS: E[N] = 4",
        "  RHS: 80 * 0.05 = 4  ✓",
    )
    p.txt(
        "For M/M/2 (two servers, each at rate μ=100 packets/s):\n"
        "  • The effective service capacity doubles to 200/s.\n"
        "  • With λ=80, ρ = 80/(2·100) = 0.4 per server — much less loaded.\n"
        "  • E[W] for M/M/2 is substantially smaller than for M/M/1 at λ=80,\n"
        "    because there is a spare server to absorb bursts.\n"
        "  Qualitatively: adding a second server reduces congestion "
        "super-linearly — halving the load factor reduces waiting time by "
        "far more than a factor of 2 due to the nonlinear behaviour of "
        "the M/M/1 formula E[W] = λ/[μ(μ−λ)] near saturation.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== V2  |  Folder 2026-04-16 ===")
    print("Topics: CTMC & Birth-Death | Queuing Theory M/M/1 and M/M/inf\n")

    print("Generating question PDFs …")
    ctmc_q()
    queue_q()

    print("\nGenerating answer-key PDFs …")
    ctmc_a()
    queue_a()

    print("\nDone.  4 PDFs written to:")
    print(f"  {os.path.relpath(QQ, BASE)}/")
    print(f"  {os.path.relpath(AK, BASE)}/")
