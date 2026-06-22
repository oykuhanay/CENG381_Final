#!/usr/bin/env python3
"""
CENG381 - PDF generator for folder 2026-05-07
Topics: Renewal Processes | Renewal-Reward | Residual Life | Inspection Paradox
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
        self.cell(58, 6.5, term)
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
# 1.  RENEWAL PROCESSES AND ELEMENTARY RENEWAL THEOREM
# ==============================================================================

def renewal_q():
    S = "Renewal_Processes"
    p = ExamPDF("Renewal Processes and Elementary Renewal Theorem  -  Question Set 1")
    p.add_page()

    p.txt("Notation used in this question set:")
    p.defn("X_1, X_2, ...",
           "i.i.d. non-negative inter-renewal times with common CDF F, "
           "mean E[X] = mu, and second moment E[X^2].")
    p.defn("S_n = X_1 + ... + X_n:",
           "the time of the n-th renewal (S_0 = 0 by convention). "
           "The renewals happen at times S_1, S_2, S_3, ...")
    p.defn("N(t):",
           "the number of renewals in the interval (0, t]. "
           "Equivalently, N(t) = max{n >= 0 : S_n <= t}.")
    p.defn("m(t) = E[N(t)]:",
           "the renewal function. It counts the expected number of renewals "
           "by time t.")
    p.defn("Elementary Renewal Thm:",
           "m(t) / t  ->  1 / mu  as t -> infinity. "
           "The long-run rate of renewals equals 1 / (mean inter-renewal time).")
    p.note("Key identity (used to derive m(t)): "
           "E[N(t)] = sum_{n=1}^{inf} P(S_n <= t) = sum_{n=1}^{inf} F_n(t), "
           "where F_n is the n-fold convolution of F with itself.")
    p.ln(1)

    # ── Q1 ──
    p.Q(1, 30,
        "Light bulbs in a lamp are replaced immediately when they fail. "
        "Each bulb has a lifetime that is Exponential with rate lambda = 0.5 "
        "failures per hour (so E[X] = 1/lambda = 2 hours).")
    p.sub("a",
          "What type of stochastic process does N(t) (the number of replacements "
          "by time t) form? Write the distribution of N(t) and compute E[N(t)].")
    p.sub("b",
          "Use the Elementary Renewal Theorem to find the long-run average rate "
          "of replacements per hour. How many bulbs do you expect to use in "
          "a 40-hour period?")
    p.sub("c",
          "The first bulb is installed at time 0. Find the probability that "
          "at least 3 replacements occur in the first 4 hours. "
          "Since N(t) ~ Poisson(lambda*t), compute P(N(4) >= 3) using the "
          "Poisson PMF with lambda*t = 0.5 * 4 = 2.")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "Buses arrive at a stop according to a renewal process. "
        "Inter-arrival times X_n are uniformly distributed on [1, 3] minutes "
        "(so E[X] = 2 minutes, E[X^2] = integral of x^2 * (1/2) from 1 to 3).")
    p.sub("a",
          "Compute E[X] and E[X^2] for X ~ Uniform[1, 3]. "
          "Recall: for X ~ Uniform[a, b], E[X] = (a+b)/2 and "
          "E[X^2] = (a^2 + ab + b^2)/3.")
    p.sub("b",
          "By the Elementary Renewal Theorem, what is the long-run rate of "
          "bus arrivals per minute? How many buses arrive on average in a "
          "60-minute hour?")
    p.sub("c",
          "The renewal equation gives the exact renewal function for small t. "
          "For a Uniform[1,3] inter-arrival distribution, N(t) = 0 for t < 1 "
          "(the first bus cannot arrive before minute 1). "
          "For 1 <= t < 2, at most one bus has arrived, so m(t) = E[N(t)] = P(X_1 <= t). "
          "Compute m(1.5) = P(X_1 <= 1.5) for X_1 ~ Uniform[1,3].")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "A web server processes requests in batches. The time to process "
        "each batch X_n has the following distribution:\n"
        "  P(X = 1) = 0.5,   P(X = 2) = 0.3,   P(X = 4) = 0.2\n"
        "So inter-renewal times take values 1, 2, or 4 seconds.")
    p.sub("a",
          "Compute E[X] and E[X^2] for this distribution.")
    p.sub("b",
          "What is the long-run rate of batch completions per second "
          "(by the Elementary Renewal Theorem)?")
    p.sub("c",
          "Use the identity P(N(t) >= n) = P(S_n <= t) to compute:\n"
          "  (i)  P(N(3) >= 1) = P(S_1 <= 3) = P(X_1 <= 3) = P(X=1) + P(X=2)\n"
          "  (ii) P(N(3) >= 2) = P(S_2 <= 3) = P(X_1 + X_2 <= 3).\n"
          "For part (ii), enumerate all combinations of (X_1, X_2) that "
          "both take values in {1, 2, 4} and sum to at most 3.")
    p.save(qp(S, "Question_Set_1.pdf"))


def renewal_a():
    S = "Renewal_Processes"
    p = ExamPDF("Renewal Processes  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Distribution of N(t):")
    p.txt("When inter-renewal times are Exponential(lambda), the renewal process "
          "is a POISSON PROCESS with rate lambda.\n\n"
          "  N(t) ~ Poisson(lambda * t)\n\n"
          "  E[N(t)] = lambda * t\n\n"
          "This follows because the Poisson process is the unique renewal process "
          "with exponentially distributed inter-arrival times (memoryless property).")

    p.AL("b)  Long-run rate and expected count over 40 hours:")
    p.txt("Elementary Renewal Theorem:\n"
          "  Long-run rate = 1 / E[X] = 1 / (1/lambda) = lambda = 0.5 per hour\n\n"
          "Expected number of replacements in 40 hours:\n"
          "  E[N(40)] = lambda * 40 = 0.5 * 40 = 20 bulbs\n\n"
          "Interpretation: on average, one bulb is used every 2 hours, so 20 bulbs "
          "are used in a 40-hour period.")

    p.AL("c)  P(N(4) >= 3) with lambda*t = 2:")
    p.txt("N(4) ~ Poisson(lambda * 4) = Poisson(0.5 * 4) = Poisson(2)\n\n"
          "P(N(4) >= 3) = 1 - P(N(4) = 0) - P(N(4) = 1) - P(N(4) = 2)\n\n"
          "  P(N(4) = k) = e^(-2) * 2^k / k!\n\n"
          "  P(N=0) = e^(-2) * 1 / 1   = e^(-2) ~ 0.1353\n"
          "  P(N=1) = e^(-2) * 2 / 1   = 2*e^(-2) ~ 0.2707\n"
          "  P(N=2) = e^(-2) * 4 / 2   = 2*e^(-2) ~ 0.2707\n\n"
          "  P(N(4) >= 3) = 1 - e^(-2) - 2*e^(-2) - 2*e^(-2)\n"
          "               = 1 - 5*e^(-2)\n"
          "  ~ 1 - 5*0.1353 = 1 - 0.6767 = 0.3233\n\n"
          "About a 32.3% chance of 3 or more replacements in the first 4 hours.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  E[X] and E[X^2] for X ~ Uniform[1,3]:")
    p.txt("  E[X] = (1 + 3)/2 = 4/2 = 2 minutes\n\n"
          "  E[X^2] = (1^2 + 1*3 + 3^2) / 3\n"
          "         = (1 + 3 + 9) / 3\n"
          "         = 13/3 ~ 4.333 minutes^2\n\n"
          "Alternative derivation via integral:\n"
          "  E[X^2] = integral from 1 to 3 of x^2 * (1/2) dx\n"
          "         = (1/2) * [x^3/3] from 1 to 3\n"
          "         = (1/2) * (27/3 - 1/3)\n"
          "         = (1/2) * (26/3)\n"
          "         = 13/3  (OK)")

    p.AL("b)  Long-run rate and 60-minute count:")
    p.txt("  Long-run rate = 1 / E[X] = 1/2 bus per minute = 0.5 buses/min\n\n"
          "  Expected buses in 60 minutes = 60 * (1/2) = 30 buses")

    p.AL("c)  m(1.5) for Uniform[1,3]:")
    p.txt("For 1 <= t < 2, the first bus cannot arrive before t=1 (since X_1 >= 1),\n"
          "and a second bus cannot arrive before t = 1 + 1 = 2 (since X_1 + X_2 >= 2).\n"
          "So for 1 <= t < 2, N(t) is either 0 (no buses yet) or 1 (first bus arrived).\n\n"
          "  m(t) = E[N(t)] = P(N(t) >= 1) = P(X_1 <= t)   for 1 <= t < 2\n\n"
          "  m(1.5) = P(X_1 <= 1.5) = (1.5 - 1) / (3 - 1) = 0.5 / 2 = 0.25\n\n"
          "So on average, 0.25 buses have arrived by time t = 1.5 minutes. "
          "This makes sense: there's a 25% chance the first bus arrived by 1.5 min, "
          "and a 75% chance it hasn't arrived yet.")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  E[X] and E[X^2]:")
    p.txt("  E[X] = 1*0.5 + 2*0.3 + 4*0.2\n"
          "       = 0.5 + 0.6 + 0.8\n"
          "       = 1.9 seconds\n\n"
          "  E[X^2] = 1^2*0.5 + 2^2*0.3 + 4^2*0.2\n"
          "         = 0.5 + 4*0.3 + 16*0.2\n"
          "         = 0.5 + 1.2 + 3.2\n"
          "         = 4.9 seconds^2")

    p.AL("b)  Long-run rate:")
    p.txt("  Long-run rate = 1 / E[X] = 1 / 1.9 ~ 0.526 completions per second\n\n"
          "About 0.526 batch completions per second, or roughly one every 1.9 seconds.")

    p.AL("c)  P(N(3) >= 1) and P(N(3) >= 2):")
    p.txt("(i)  P(N(3) >= 1) = P(S_1 <= 3) = P(X_1 <= 3)\n"
          "   = P(X=1) + P(X=2)   [since P(X=4) corresponds to X=4 > 3]\n"
          "   = 0.5 + 0.3 = 0.8\n\n"
          "(ii) P(N(3) >= 2) = P(S_2 <= 3) = P(X_1 + X_2 <= 3)\n\n"
          "Enumerate pairs (X_1, X_2) with values in {1, 2, 4} and sum <= 3:\n"
          "  (1, 1): sum = 2 <= 3, prob = 0.5 * 0.5 = 0.25\n"
          "  (1, 2): sum = 3 <= 3, prob = 0.5 * 0.3 = 0.15\n"
          "  (2, 1): sum = 3 <= 3, prob = 0.3 * 0.5 = 0.15\n"
          "  (1, 4): sum = 5 > 3, excluded\n"
          "  (2, 2): sum = 4 > 3, excluded\n"
          "  (4, *): sum >= 5 > 3, excluded\n\n"
          "  P(S_2 <= 3) = 0.25 + 0.15 + 0.15 = 0.55\n\n"
          "Interpretation: there is a 55% chance that at least 2 batches complete\n"
          "within the first 3 seconds.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# 2.  RENEWAL-REWARD, RESIDUAL LIFE, AND INSPECTION PARADOX
# ==============================================================================

def renew_reward_q():
    S = "Renewal_Reward_and_Residual_Life"
    p = ExamPDF("Renewal-Reward Processes, Residual Life, and Inspection Paradox  -  Question Set 1")
    p.add_page()

    p.txt("Notation used in this question set:")
    p.defn("Reward R_n:",
           "a random variable earned at the n-th renewal. {R_n} are i.i.d. "
           "with mean E[R]. R_n may be a cost, profit, or duration -- "
           "any quantity that resets at each renewal.")
    p.defn("C(t):",
           "total cumulative reward earned by time t: C(t) = R_1 + R_2 + ... + R_{N(t)}.")
    p.defn("Renewal-Reward Theorem:",
           "C(t) / t  ->  E[R] / E[X]  as t -> infinity. "
           "Long-run reward rate = (mean reward per cycle) / (mean cycle length).")
    p.defn("A(t) = age (backward):",
           "time elapsed since the LAST renewal before time t: "
           "A(t) = t - S_{N(t)}. Also called the current age or backward recurrence time.")
    p.defn("B(t) = residual life (forward):",
           "time remaining until the NEXT renewal after time t: "
           "B(t) = S_{N(t)+1} - t. Also called excess life or forward recurrence time.")
    p.defn("Inspection Paradox:",
           "The interval [S_{N(t)}, S_{N(t)+1}] that CONTAINS time t tends to be "
           "LONGER than a typical inter-renewal interval. Specifically, its expected "
           "length is E[X^2] / E[X] >= E[X]  (by Jensen's inequality, since E[X^2] >= (E[X])^2).")
    p.note("For a stationary renewal process:  "
           "E[B(t)] = E[A(t)] = E[X^2] / (2 * E[X]).  "
           "Time-average of A(t) (over all t) also equals E[X^2] / (2 * E[X]) "
           "by the Renewal-Reward Theorem with reward = current age at renewal.")
    p.ln(1)

    # ── Q1 ──
    p.Q(1, 30,
        "A machine alternates between working (ON) and being repaired (OFF). "
        "ON periods have duration Exponential(mu_on) with mean 1/mu_on = 4 hours. "
        "OFF (repair) periods have duration Exponential(mu_off) with mean 1/mu_off = 1 hour. "
        "Cycles are i.i.d. A cycle = one ON period + one OFF period.")
    p.sub("a",
          "Define the renewal points as the moments when the machine starts a new "
          "ON period. What is the mean cycle length E[X] where X = ON + OFF?")
    p.sub("b",
          "Define the reward R_n for cycle n as the length of the ON period in cycle n. "
          "Apply the Renewal-Reward Theorem to find the long-run fraction of time "
          "the machine is ON. Verify this matches intuition.")
    p.sub("c",
          "What is the long-run fraction of time the machine is OFF (being repaired)? "
          "Use the Renewal-Reward Theorem with reward = OFF duration for each cycle. "
          "Check that (fraction ON) + (fraction OFF) = 1.")

    p.sep()

    # ── Q2 ──
    p.Q(2, 35,
        "Customers arrive at a shop according to a renewal process with "
        "inter-arrival times X_n ~ Uniform[0, 4] minutes "
        "(so E[X] = 2 minutes, E[X^2] = integral from 0 to 4 of x^2*(1/4)dx = 16/3).")
    p.sub("a",
          "Compute E[X] and E[X^2] for X ~ Uniform[0,4]. "
          "Recall: E[X^2] = integral from 0 to 4 of x^2 * (1/4) dx.")
    p.sub("b",
          "You arrive at the shop at a large time t (so the process is approximately "
          "in stationarity). What is the expected residual waiting time B(t) until "
          "the next customer arrives after you? Use E[B] = E[X^2] / (2*E[X]).")
    p.sub("c",
          "What is the expected TOTAL length of the inter-arrival interval that "
          "contains time t? (i.e., the interval from the last arrival before t "
          "to the next arrival after t.) Compare this to E[X] and explain the "
          "Inspection Paradox: why is the interval you land in longer on average "
          "than a typical interval?")

    p.sep()

    # ── Q3 ──
    p.Q(3, 35,
        "Bus inter-arrival times are i.i.d. with the following distribution:\n"
        "  P(X = 2) = 0.6   (short gap, 2 minutes)\n"
        "  P(X = 8) = 0.4   (long gap, 8 minutes)\n"
        "You arrive at the bus stop at a uniformly random time (large t, stationary).")
    p.sub("a",
          "Compute E[X] and E[X^2]. Show that E[X^2] / E[X] > E[X], confirming "
          "the Inspection Paradox.")
    p.sub("b",
          "In stationarity, the probability that your arrival lands in a SHORT gap "
          "(length 2) is proportional to the gap length times its probability:\n"
          "  P(land in short gap) = P(X=2)*2 / E[X]\n"
          "  P(land in long gap)  = P(X=8)*8 / E[X]\n"
          "Compute these probabilities. Notice that even though short gaps are more "
          "frequent (prob 0.6), you are more likely to land in a long gap.")
    p.sub("c",
          "Given that you land in a gap of length L, you arrive at a Uniform[0, L] "
          "point within that gap (by symmetry, your arrival is equally likely at "
          "any position within the interval). Compute E[B | short gap] = E[U | U ~ Uniform[0,2]] "
          "and E[B | long gap] = E[U | U ~ Uniform[0,8]], where B is the residual "
          "time until the next bus. Then use the law of total expectation to find E[B] "
          "and verify it equals E[X^2]/(2*E[X]).")
    p.save(qp(S, "Question_Set_1.pdf"))


def renew_reward_a():
    S = "Renewal_Reward_and_Residual_Life"
    p = ExamPDF("Renewal-Reward and Residual Life  -  Answer Key 1")
    p.add_page()

    # ── Q1 ──
    p.AH("Q1  Solution")
    p.AL("a)  Mean cycle length:")
    p.txt("A cycle consists of one ON period and one OFF period.\n"
          "ON ~ Exp(mu_on) with mean 1/mu_on = 4 hours.\n"
          "OFF ~ Exp(mu_off) with mean 1/mu_off = 1 hour.\n\n"
          "  E[X] = E[ON] + E[OFF] = 4 + 1 = 5 hours per cycle")

    p.AL("b)  Long-run fraction of time ON:")
    p.txt("Define reward R_n = length of ON period in cycle n.\n"
          "Since ON ~ Exp(mu_on): E[R] = E[ON] = 4 hours.\n\n"
          "Renewal-Reward Theorem:\n"
          "  Long-run fraction of time ON = E[R] / E[X] = 4 / 5 = 0.8\n\n"
          "Intuition check: the machine is ON for 4 hours out of every 5-hour cycle\n"
          "on average, so it should be ON 80% of the time.  (OK)")

    p.AL("c)  Long-run fraction of time OFF:")
    p.txt("Define reward R_n = length of OFF period in cycle n.\n"
          "Since OFF ~ Exp(mu_off): E[R] = E[OFF] = 1 hour.\n\n"
          "  Long-run fraction of time OFF = E[R] / E[X] = 1 / 5 = 0.2\n\n"
          "Check: fraction ON + fraction OFF = 0.8 + 0.2 = 1.0  (OK)\n\n"
          "This result also follows directly: since every moment the machine is\n"
          "either ON or OFF, the two fractions must sum to 1.")

    p.sep()

    # ── Q2 ──
    p.AH("Q2  Solution")
    p.AL("a)  E[X] and E[X^2] for X ~ Uniform[0,4]:")
    p.txt("  E[X] = (0 + 4)/2 = 2 minutes\n\n"
          "  E[X^2] = integral from 0 to 4 of x^2 * (1/4) dx\n"
          "         = (1/4) * [x^3/3] from 0 to 4\n"
          "         = (1/4) * (64/3)\n"
          "         = 64/12 = 16/3 ~ 5.333 minutes^2")

    p.AL("b)  Expected residual life E[B]:")
    p.txt("Using the stationary formula for residual life:\n\n"
          "  E[B] = E[X^2] / (2 * E[X])\n"
          "       = (16/3) / (2 * 2)\n"
          "       = (16/3) / 4\n"
          "       = 4/3 ~ 1.333 minutes\n\n"
          "Despite inter-arrival times averaging 2 minutes, you expect to wait\n"
          "only 4/3 ~ 1.33 minutes until the next customer. This is because your\n"
          "arrival is not at the START of an interval -- you land somewhere in the\n"
          "middle of a running interval.")

    p.AL("c)  Expected length of the interval containing t (Inspection Paradox):")
    p.txt("The interval containing time t has expected length:\n\n"
          "  E[A(t) + B(t)] = E[X^2] / E[X]   (in stationarity)\n"
          "                 = (16/3) / 2\n"
          "                 = 8/3 ~ 2.667 minutes\n\n"
          "Compared to E[X] = 2 minutes, the interval you land in is 33% LONGER.\n\n"
          "Inspection Paradox explanation:\n"
          "  When you arrive at a random time t, you are more likely to land in a\n"
          "  LONG interval than in a short one -- because longer intervals occupy more\n"
          "  of the time axis. A gap of length L 'covers' L units of time, so the\n"
          "  probability of landing in it is proportional to L, not to its frequency.\n"
          "  This biases the sampled interval upward: E[X^2]/E[X] >= E[X]\n"
          "  with equality only when all intervals have the same length (no variance).")

    p.sep()

    # ── Q3 ──
    p.AH("Q3  Solution")
    p.AL("a)  E[X], E[X^2], and Inspection Paradox check:")
    p.txt("  E[X] = 2*0.6 + 8*0.4 = 1.2 + 3.2 = 4.4 minutes\n\n"
          "  E[X^2] = 2^2*0.6 + 8^2*0.4 = 4*0.6 + 64*0.4 = 2.4 + 25.6 = 28.0\n\n"
          "  E[X^2]/E[X] = 28.0 / 4.4 = 70/11 ~ 6.364 minutes\n\n"
          "  Compare to E[X] = 4.4 minutes.\n"
          "  6.364 > 4.4, so E[X^2]/E[X] > E[X]  --  Inspection Paradox confirmed.\n\n"
          "The variance of X is Var[X] = E[X^2] - (E[X])^2 = 28 - 19.36 = 8.64 > 0,\n"
          "which is exactly why E[X^2] > (E[X])^2, i.e., E[X^2]/E[X] > E[X].")

    p.AL("b)  Probability of landing in short vs long gap:")
    p.txt("In stationarity, the probability of arriving in a gap of type (length L, prob p_L):\n"
          "  P(land in gap of length L) proportional to p_L * L\n\n"
          "Unnormalised weights:\n"
          "  Short gap (L=2): 0.6 * 2 = 1.2\n"
          "  Long  gap (L=8): 0.4 * 8 = 3.2\n"
          "  Total weight = E[X] = 4.4\n\n"
          "  P(land in short gap) = 1.2 / 4.4 = 12/44 = 3/11 ~ 0.273\n"
          "  P(land in long  gap) = 3.2 / 4.4 = 32/44 = 8/11 ~ 0.727\n\n"
          "Despite short gaps being more frequent (prob 0.6 > 0.4), you are MORE\n"
          "likely to land in a LONG gap (prob 0.727 > 0.273) because long gaps are\n"
          "4 times as wide and therefore catch arrivals 4 times more often per gap.")

    p.AL("c)  E[B] via total expectation and verification:")
    p.txt("If you arrive at a Uniform point within a gap of length L, the residual\n"
          "time B (time until the next bus) is Uniform[0, L], with mean L/2.\n\n"
          "  E[B | short gap] = 2/2 = 1 minute\n"
          "  E[B | long  gap] = 8/2 = 4 minutes\n\n"
          "Law of total expectation:\n"
          "  E[B] = E[B | short gap]*P(short) + E[B | long gap]*P(long)\n"
          "       = 1 * (3/11) + 4 * (8/11)\n"
          "       = 3/11 + 32/11\n"
          "       = 35/11 ~ 3.182 minutes\n\n"
          "Verify using the formula:\n"
          "  E[X^2] / (2*E[X]) = 28 / (2*4.4) = 28 / 8.8 = 35/11 ~ 3.182  (OK)\n\n"
          "Even though buses are spaced 4.4 minutes apart on average, you expect\n"
          "to wait 3.18 minutes -- more than half the average gap (2.2 minutes)\n"
          "-- because your arrival is disproportionately likely to land in a long gap.")
    p.save(ap(S, "Question_Set_1_Answers.pdf"))


# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":
    print("\n=== Folder 2026-05-07: Renewal Processes | Renewal-Reward | Residual Life ===\n")
    print("Generating Question Sets...")
    renewal_q()
    renew_reward_q()

    print("\nGenerating Answer Keys...")
    renewal_a()
    renew_reward_a()

    print("\nDone. 4 PDFs created.")
