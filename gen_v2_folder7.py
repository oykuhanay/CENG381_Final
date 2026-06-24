#!/usr/bin/env python3
"""
CENG381 - V2 Generator  |  Folder 2026-05-07
Topics : Renewal Processes  |  Renewal-Reward & Residual Life
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
# 1.  RENEWAL PROCESSES
# ══════════════════════════════════════════════════════════════════════════════

def renewal_q():
    S = "Renewal_Processes"
    p = ExamPDF("Renewal Processes  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "A factory installs a new lightbulb each time one burns out.  "
        "Bulb lifetimes are i.i.d. with distribution X, where "
        "E[X] = 400 hours and Var(X) = 160000 hours².")
    p.sub("a",
          "State the Elementary Renewal Theorem.  "
          "What is the long-run rate of bulb replacements (bulbs per hour)?")
    p.sub("b",
          "Approximately how many bulbs will be replaced in one year "
          "(8760 operating hours)?  "
          "Using E[X²] = Var(X) + (E[X])², compute E[X²].")
    p.sub("c",
          "Explain the sandwich inequality used to prove the theorem:\n\n"
          "  N(t) / S_{N(t)}  ≥  N(t) / t  ≥  N(t) / S_{N(t)+1}\n\n"
          "What does each ratio converge to by the Strong Law of Large Numbers, "
          "and how does this establish N(t)/t → 1/E[X]?")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "A server alternates between Busy periods (duration Exp(μ=2) hours) "
        "and Idle periods (duration Exp(λ=3) hours).  "
        "Each Busy+Idle cycle is one renewal.  "
        "A reward R = 1 is earned per unit time while the server is Busy; "
        "R = 0 while Idle.")
    p.sub("a",
          "Find E[busy period] and E[idle period].  "
          "Hence find E[cycle length] = E[X].")
    p.sub("b",
          "By the renewal-reward theorem, the long-run fraction of time "
          "the server is busy equals E[reward per cycle] / E[X].  "
          "Compute this fraction.")
    p.sub("c",
          "Verify your answer using the CTMC stationary distribution.  "
          "Model the server as a 2-state CTMC with rate μ (Busy→Idle) and "
          "rate λ (Idle→Busy).  Solve π·Q = 0 to find π_busy.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "A hospital bed has occupancy times following an Erlang(2, 1) "
        "distribution — equivalently, the sum of two i.i.d. Exp(1) durations.  "
        "E[X] = 2 days, Var(X) = 2 days², so E[X²] = 6 days².")
    p.sub("a",
          "What is the long-run bed-turnover rate (discharges per day)?  "
          "In a 30-day month, how many patients do you expect to occupy this bed?")
    p.sub("b",
          "Compute the time-average residual occupancy "
          "Y = E[X²] / (2·E[X]).  "
          "This is the expected remaining stay for a patient currently in the bed, "
          "sampled at a random time.")
    p.sub("c",
          "Suppose instead the occupancy times were Exp(1/2) (also mean 2 days).  "
          "Compute E[X²] and the resulting residual occupancy.  "
          "Which distribution gives a shorter residual occupancy, and why?")

    p.save(qp(S, "Practice_1.pdf"))


def renewal_a():
    S = "Renewal_Processes"
    p = ExamPDF("Renewal Processes  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Elementary Renewal Theorem and replacement rate:")
    p.txt(
        "Elementary Renewal Theorem: for i.i.d. inter-renewal times X with "
        "finite mean E[X],")
    p.eqn(
        "N(t)/t  -->  1/E[X]   almost surely as t --> inf",
        "",
        "Long-run replacement rate = 1/E[X] = 1/400  bulbs per hour",
        "                          = 0.0025 bulbs/hour",
    )

    p.AL("b)  Expected replacements in 8760 hours and E[X²]:")
    p.eqn(
        "E[N(8760)] = 8760 / E[X] = 8760 / 400 = 21.9  ~=  22 bulbs",
        "",
        "E[X^2] = Var(X) + (E[X])^2 = 160000 + 160000 = 320000 hours^2",
    )

    p.AL("c)  Sandwich argument:")
    p.txt("Since S_{N(t)} ≤ t < S_{N(t)+1}, dividing through by N(t):")
    p.eqn(
        "S_{N(t)} / N(t)  <=  t / N(t)  <=  S_{N(t)+1} / N(t)",
        "",
        "By the SLLN:  S_n / n  -->  E[X]  as n --> inf",
        "  Left side:  S_{N(t)} / N(t) --> E[X]  (as t -> inf, N(t) -> inf)",
        "  Right side: S_{N(t)+1} / N(t) = S_{N(t)+1}/(N(t)+1) * (N(t)+1)/N(t)",
        "              --> E[X] * 1 = E[X]",
        "",
        "By the squeeze theorem: t/N(t) --> E[X]",
        "Equivalently: N(t)/t --> 1/E[X]  ✓",
    )

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Expected periods and cycle length:")
    p.eqn(
        "E[busy] = 1/mu = 1/2 hour",
        "E[idle] = 1/lambda = 1/3 hour",
        "E[cycle] = E[X] = 1/2 + 1/3 = 3/6 + 2/6 = 5/6 hour",
    )

    p.AL("b)  Long-run fraction busy (renewal-reward):")
    p.eqn(
        "E[reward per cycle] = E[busy period] = 1/2",
        "",
        "Long-run fraction busy = E[R] / E[X] = (1/2) / (5/6)",
        "                       = (1/2) * (6/5) = 3/5  =  60%",
    )

    p.AL("c)  CTMC verification:")
    p.txt(
        "2-state CTMC: state 1 = Busy, state 0 = Idle.  "
        "Rate Busy→Idle = μ=2, rate Idle→Busy = λ=3.")
    p.eqn(
        "Q = [[-3,  3],",
        "     [ 2, -2]]",
        "",
        "pi * Q = 0:",
        "  -3*pi_0 + 2*pi_1 = 0  =>  pi_1 = (3/2)*pi_0",
        "  pi_0 + pi_1 = 1  =>  (5/2)*pi_0 = 1  =>  pi_0 = 2/5",
        "  pi_1 = 3/5  ✓  (matches renewal-reward result)",
    )

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.AH("Q3  Solution")

    p.AL("a)  Turnover rate and expected patients per month:")
    p.eqn(
        "Turnover rate = 1/E[X] = 1/2 discharges per day",
        "",
        "Expected patients in 30 days = 30 * (1/2) = 15 patients",
    )

    p.AL("b)  Time-average residual occupancy (Erlang):")
    p.eqn(
        "Y = E[X^2] / (2*E[X]) = 6 / (2*2) = 6/4 = 3/2 = 1.5 days",
    )
    p.txt(
        "At a random moment, the patient currently occupying the bed "
        "is expected to stay for another 1.5 days.")

    p.AL("c)  Comparison with Exp(1/2) (mean 2 days):")
    p.eqn(
        "For X ~ Exp(1/2):  E[X] = 2,  E[X^2] = 2/lambda^2 = 2/(1/4) = 8",
        "",
        "Y_Exp = 8 / (2*2) = 2 days",
        "",
        "Y_Erlang = 1.5 days  <  Y_Exp = 2 days",
    )
    p.txt(
        "The Erlang(2,1) gives a shorter residual occupancy because it has "
        "less variability than the exponential (Var=2 vs Var=4).  "
        "The inspection paradox is weaker when stays are more regular: "
        "the ratio E[X²]/E[X] = E[X] + Var(X)/E[X] grows with the "
        "coefficient of variation.  Regular arrivals reduce the excess wait.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# 2.  RENEWAL-REWARD AND RESIDUAL LIFE
# ══════════════════════════════════════════════════════════════════════════════

def rrrl_q():
    S = "Renewal_Reward_and_Residual_Life"
    p = ExamPDF("Renewal-Reward and Residual Life  —  Practice 1")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.Q(1, 30,
        "The time-average residual life (expected wait for the next renewal "
        "when arriving at a random time) is given by:\n\n"
        "  Y  =  E[X²] / (2·E[X])\n\n"
        "Compute Y for each of the following inter-renewal distributions "
        "and compare with E[X]/2.")
    p.sub("a",
          "Deterministic: X = 6 minutes (every renewal happens exactly "
          "6 minutes apart).  Compute Y.  "
          "Explain geometrically why Y = E[X]/2 in this case.")
    p.sub("b",
          "Exponential: X ~ Exp(1/6) (rate 1/6, mean 6 minutes).  "
          "Recall E[X²] = 2/λ² for Exp(λ).  Compute Y.  "
          "Why is Y = E[X] rather than E[X]/2 for an exponential distribution?")
    p.sub("c",
          "Uniform: X ~ Uniform[0, 12] (mean 6 minutes).  "
          "Recall E[X²] = (b³−a³) / (3(b−a)) for Uniform[a,b].  "
          "Compute E[X²] and Y.  "
          "Is Y greater or less than E[X]/2?  Explain the inspection paradox.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.Q(2, 35,
        "The inspection paradox: the renewal interval L containing a fixed "
        "large time t satisfies E[L] = E[X²]/E[X] ≥ E[X].  "
        "The interval 'looks longer than average' because you are more "
        "likely to land inside a long interval.")
    p.sub("a",
          "Let X take value 1 with probability 1/2 and value 5 with "
          "probability 1/2.  Compute E[X], E[X²], and E[L].  "
          "By how much does E[L] exceed E[X] in absolute and relative terms?")
    p.sub("b",
          "For X ~ Exp(λ = 1/6): compute E[L] = E[X²]/E[X].  "
          "Express E[L] as a multiple of E[X].  "
          "Explain this result using the lack-of-memory property of the exponential.")
    p.sub("c",
          "For X ~ Erlang(2, λ = 1/3) "
          "(sum of two i.i.d. Exp(1/3) r.v.'s; mean 6, variance 18): "
          "compute E[X²] and E[L].  "
          "Compare E[L] with the exponential case from (b) "
          "and explain the difference in terms of variability.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────────────────────────────
    p.Q(3, 35,
        "Buses arrive at a stop according to a renewal process with "
        "inter-arrival times X ~ Uniform[4, 16] minutes "
        "(mean E[X] = 10 minutes).")
    p.sub("a",
          "Compute E[X²] using the formula for Uniform[a,b]: "
          "E[X²] = (a² + ab + b²)/3.  "
          "Find the time-average residual life Y (expected wait from a "
          "random arrival time).")
    p.sub("b",
          "If buses arrived deterministically every 10 minutes, "
          "the expected wait would be 5 minutes.  "
          "By how much does the random schedule increase the expected wait?  "
          "Relate this excess to the variance Var(X) = (b−a)²/12.")
    p.sub("c",
          "A commuter arrives at the stop and observes that the last bus left "
          "s = 2 minutes ago (age Z(t) = 2).  "
          "Using the conditional formula:\n\n"
          "  P(Y > y | Z = s) = P(X > y+s) / P(X > s)\n\n"
          "compute P(Y > 3 | Z = 2) for the Uniform[4,16] distribution.")

    p.save(qp(S, "Practice_1.pdf"))


def rrrl_a():
    S = "Renewal_Reward_and_Residual_Life"
    p = ExamPDF("Renewal-Reward and Residual Life  —  Practice 1  (Answer Key)")
    p.add_page()

    # ── Q1 ─────────────────────────────────────────────────────────────────
    p.AH("Q1  Solution")

    p.AL("a)  Deterministic X=6:")
    p.eqn(
        "E[X] = 6,   E[X^2] = 6^2 = 36",
        "Y = 36 / (2*6) = 3 = E[X]/2  ✓",
    )
    p.txt(
        "Geometrically: between two renewals at 0 and 6, the residual life "
        "Y(t) = 6−t decreases linearly from 6 to 0.  "
        "The time average of a decreasing line from 6 to 0 is exactly 3 = 6/2.")

    p.AL("b)  Exponential X ~ Exp(1/6):")
    p.eqn(
        "E[X] = 6,   E[X^2] = 2/lambda^2 = 2/(1/6)^2 = 2*36 = 72",
        "Y = 72 / (2*6) = 6 = E[X]",
    )
    p.txt(
        "Y = E[X] rather than E[X]/2 because the exponential is memoryless.  "
        "At any time t, the remaining life has the same Exp(1/6) distribution "
        "as the full lifetime X — the distribution does not depend on how long "
        "you have already waited.  This is the defining property of the exponential.")

    p.AL("c)  Uniform[0,12]:")
    p.eqn(
        "E[X] = 6,   E[X^2] = (0^2 + 0*12 + 12^2)/3 = 144/3 = 48",
        "Y = 48 / (2*6) = 4  >  E[X]/2 = 3",
    )
    p.txt(
        "Y > E[X]/2: this is the inspection paradox.  "
        "If you arrive at a random time, you are more likely to land "
        "inside a long inter-renewal interval than a short one (long intervals "
        "cover more time).  On average the interval you land in is longer "
        "than a typical interval, and therefore the expected remaining wait "
        "exceeds half the mean interval length.")

    p.sep()

    # ── Q2 ─────────────────────────────────────────────────────────────────
    p.AH("Q2  Solution")

    p.AL("a)  Two-point distribution (X = 1 w.p. 1/2, X = 5 w.p. 1/2):")
    p.eqn(
        "E[X] = (1+5)/2 = 3",
        "E[X^2] = (1^2 + 5^2)/2 = (1+25)/2 = 13",
        "E[L] = E[X^2]/E[X] = 13/3  ~=  4.33",
        "",
        "Excess: E[L] - E[X] = 13/3 - 3 = 4/3  ~=  1.33 (absolute)",
        "        E[L]/E[X]   = (13/3)/3 = 13/9  ~=  1.44  (44% longer)",
    )
    p.txt(
        "The interval of length 5 is 5 times longer than the interval of length 1, "
        "so it 'catches' 5 times as many random arrivals.  "
        "The observed interval is heavily biased towards the longer type.")

    p.AL("b)  Exponential X ~ Exp(1/6):")
    p.eqn(
        "E[X] = 6,   E[X^2] = 72",
        "E[L] = 72/6 = 12 = 2*E[X]",
    )
    p.txt(
        "The observed interval is twice as long as the average interval.  "
        "Interpretation: you arrive in an interval of length X, "
        "with your position uniform in [0,X] (since arrivals are Poisson/memoryless).  "
        "Given you are in interval X, your remaining wait is Exp(1/6) with mean 6, "
        "and the time already elapsed is also Exp(1/6) with mean 6 — "
        "making the total interval length 12 = 2·E[X] on average.")

    p.AL("c)  Erlang(2, 1/3):")
    p.eqn(
        "E[X] = 6,   Var(X) = 18,   E[X^2] = 18 + 36 = 54",
        "E[L] = 54/6 = 9",
    )
    p.txt(
        "Erlang E[L]=9 vs Exp E[L]=12 (both mean 6).  "
        "The Erlang has smaller variance (18 vs 36 for Exp), "
        "so the inspection paradox is less extreme.  "
        "In general: E[L] = E[X] + Var(X)/E[X].  "
        "Less variability → smaller Var(X)/E[X] → observed interval closer "
        "to the true mean.")

    p.sep()

    # ── Q3 ─────────────────────────────────────────════════════════════════
    p.AH("Q3  Solution")

    p.AL("a)  E[X²] and time-average residual life:")
    p.eqn(
        "X ~ Uniform[4, 16]:  a=4, b=16",
        "E[X] = (4+16)/2 = 10",
        "E[X^2] = (a^2 + a*b + b^2)/3 = (16 + 64 + 256)/3 = 336/3 = 112",
        "",
        "Y = E[X^2] / (2*E[X]) = 112 / 20 = 5.6 minutes",
    )

    p.AL("b)  Comparison with deterministic and connection to variance:")
    p.eqn(
        "Deterministic (X=10):  Y_det = 10/2 = 5.0 minutes",
        "Random (U[4,16]):      Y_rnd = 5.6 minutes",
        "Excess = 5.6 - 5.0 = 0.6 minutes",
        "",
        "Var(X) = (b-a)^2/12 = 144/12 = 12",
        "Excess = Var(X) / (2*E[X]) = 12/20 = 0.6  ✓",
        "  [since Y = E[X]/2 + Var(X)/(2*E[X])]",
    )
    p.txt(
        "The formula Y = E[X]/2 + Var(X)/(2E[X]) shows that variability "
        "always increases the expected wait above the deterministic baseline.  "
        "This is the inspection paradox quantified.")

    p.AL("c)  Conditional residual life P(Y>3 | Z=2):")
    p.txt("For X ~ Uniform[4,16] and F_X(x) = (x−4)/12 for 4 ≤ x ≤ 16:")
    p.eqn(
        "P(X > x) = (16-x)/12   for 4 <= x <= 16",
        "P(X > x) = 1            for x < 4",
        "",
        "P(Y > 3 | Z = 2) = P(X > 3+2) / P(X > 2)",
        "                  = P(X > 5) / P(X > 2)",
        "                  = [(16-5)/12] / 1",
        "                  = 11/12  ~=  0.917",
        "",
        "[P(X>2)=1 since the minimum inter-arrival time is 4 > 2]",
    )
    p.txt(
        "There is a 91.7% chance of waiting more than 3 more minutes "
        "given the bus left only 2 minutes ago.  "
        "This makes sense: since X ≥ 4, any interval containing time t "
        "must last at least 4 minutes total, so 3 more minutes of wait "
        "is very likely when only 2 minutes have passed.")

    p.save(ap(S, "Practice_1_Answers.pdf"))


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== V2  |  Folder 2026-05-07 ===")
    print("Topics: Renewal Processes | Renewal-Reward & Residual Life\n")

    print("Generating question PDFs …")
    renewal_q()
    rrrl_q()

    print("\nGenerating answer-key PDFs …")
    renewal_a()
    rrrl_a()

    print("\nDone.  4 PDFs written to:")
    print(f"  {os.path.relpath(QQ, BASE)}/")
    print(f"  {os.path.relpath(AK, BASE)}/")
