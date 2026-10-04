# Grade 6 Math – M1 Supply Exchange: Open LMS Course Build

Item-by-item course pages for the Project Hub and all eight M1 lessons in Open LMS (Moodle 5.x, Snap theme, core H5P). Each lesson uses one of the [five lesson templates](../../../standards/openlms-templates/README.md). Content comes from the [build guide](BUILD_GUIDE.md); every answer key below was solved independently (see the [audit](AUDIT.md)).

**Status:** build specification. No course pages, H5P content or student materials exist yet. Items marked **(audit)** add what an [audit](AUDIT.md) finding asks for. Drop them if the finding is declined. Items marked **(decision P2)** depend on the open supplier-mixing rule.

## How to use this file

1. Set up the course once: gradebook categories, groups and competencies, as in the [templates README](../../../standards/openlms-templates/README.md#part-1--set-up-the-template-course-once).
2. Build the **Project Hub** at the top of the M1 section.
3. For each lesson, import its template subsection and fill each item from the lesson table below. Rename it to `M1-W1-I · Week 1 · Individual — Read the kit and price the quantities`, and so on.
4. Run the template's *Before students see it* checklist.

## Conventions used in every lesson

These apply the audit's Moodle fixes (T1–T8).

| Item | Rule |
| --- | --- |
| **Teacher notes** | Hidden Page. Paste from the lesson's section of `BUILD_GUIDE.md`: *Skills taught and checked*, *Teach and model*, *Prepare and hand off*, *Mathematical practice*, the 90-minute timeline and *Standards*. Not repeated in the tables below. |
| **④ Check** | Quiz of **auto-graded items only**, so the stuck route opens as soon as the student submits. Individual evidence category; 1 attempt; deferred feedback; link the lesson's **Primary** competencies. |
| **④ Explain** | Separate Quiz with Essay questions (*Allow attachments* = 1, for a photo of paper work). Individual evidence; teacher-marked using the marking guide in the essay's *Information for graders*. Link **Primary** competencies. |
| **Quiz dates and review** | Open at lesson start; close at the end of the school day. Review options: marks and general feedback *After the quiz is closed*. |
| **Stuck route** | `If you're stuck` Page + `Recheck` Quiz. Restrict both by: Grade → `④ Check` < 70% **and** Activity completion → `④ Check` complete. Display: hidden entirely. 70% routes support; it's not a grade cutoff. |
| **Calculated questions** | Every number in `{braces}` is a wildcard. Generate 20 dataset items, include the guide's values as item 1, and check 5 by hand. Tolerance: nominal 0.005 for money, 0 for whole numbers. Confirm money displays with two decimals (e.g. `2.00`). |
| **Variant pools** | Where a formula can't produce clean values (GCF, LCM, fractions, ratios, mixed money), make one Numerical or Cloze question per variant in a question-bank category named for the item, and add a **Random question** from it. The guide's values are always variant 1. |
| **Cloze ratio answers** | Accept `3:2`, `3 : 2` and `3 to 2`. Accept fractions as `3/5`, and mixed numbers as `1 1/5` plus the decimal. |
| **H5P** | Practice category (weight 0); attempt tracking on; grading method Highest; saved state on. Completion: *Receive a grade* for scored types, *View* for presentations. |
| **Forums** | Standard forum, **No groups**. Students write their team name at the start of each post. |

## Project Hub

Build once at the top of the M1 section.

| # | Item | Type | Content | Settings |
| --- | --- | --- | --- | --- |
| 1 | `M1 Project launch` | H5P **Course Presentation** | Six slides, listed below. | Practice; completion *View* |
| 2 | `M1 Project data` | H5P **Accordion** | One panel per card, listed below. Accordion reads better than Information Wall with a screen reader. | Practice; no grade |
| 3 | `M1 Week 3 update` | Page | "Supplier A update: only **2 packs** of gold clips left. Everything else is unchanged." | Hidden until the teacher shows it in M1-W3-G |
| 4 | `M1 Final offers` | Page | Final offer cards (listed below). | Hidden until M1-W4-G |
| 5 | `M1 Team ledger` | **Wiki**: Collaborative; Separate groups; Grouping *Teams* | First page uses the ledger template below. | No grade |
| 6 | `M1 Final product` | **Assignment**: Group submission Yes; Grouping *Teams*; Rubric | The team's purchase file. Graded in M1-W4-G (Template E item 4 links here; it's not a second assignment). | Team product category |

### Launch slides (item 1)

1. **Supply Exchange.** "How can we show that our order buys enough supplies at a sensible cost?"
2. **The job.** Your team fills activity kits. Each kit needs 2 blue clips, 3 gold clips and 1/4 m of ribbon (image of one kit).
3. **The rules.** Buy whole packs only. Budget $24. No tax or shipping. (decision P2: add "You may buy one item from both suppliers.")
4. **What you'll hand in.** One purchase file: a quantity-and-cost table for 18 kits; two possible orders compared; a short recommendation; an updated order after a stock change. Each student also attaches their own calculations.
5. **What good work shows.** Enough of every item; correct units, whole packs and cost; a comparison based on what you actually get, not just the pack price; clear math explanations; a reason for every change.
6. **Quick check** (Single Choice Set): "In one kit, what's the ratio of blue clips to gold clips?" **2:3** · 2/5 · 3:2. Feedback on 2/5: "That's blue out of *all* clips."

### Data cards (item 2)

| Panel | Text |
| --- | --- |
| Kit recipe | 1 kit = 2 blue clips + 3 gold clips + 1/4 m ribbon. |
| Supplier A | Blue: pack of 12 for $2.40 · Gold: pack of 18 for $3.60 · Ribbon: 3 m spool for $1.50 · Stock: 10 of each. |
| Supplier B | Blue: pack of 10 for $1.80 · Gold: pack of 15 for $2.85 · Ribbon: 2 m spool for $1.10 · Stock: 10 of each. |
| Order rules | Whole packs and spools only. Budget $24. No tax or shipping. Counters stand in for clips and paper strips for ribbon; nothing is really bought. |

**Final offers (item 4):** Supplier A: blue 12 for $2.64; gold 18 for $3.42; ribbon 3 m for $1.65. Supplier B: blue 10 for $1.90; gold 15 for $3.00; ribbon 2 m for $1.00. Stock 10 of each.

### Ledger template (item 5)

Create one heading per stage: *12-kit order (Week 1)*, *18-kit comparison (Week 2)*, *Stock-change revision (Week 3)*, *Final exchange (Week 4)*. Put this table under each heading:

| Item | Need | Supplier | Packs | Items bought | Leftover | Price per pack | Line cost | Calculated by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Blue clips | | | | | | | | |
| Gold clips | | | | | | | | |
| Ribbon (m) | | | | | | | | |
| **Total** | | | | | | | | |
| **Budget left** ($24 − total) | | | | | | | | |

Under the table: "**Fill check:** we can fill every kit because…"

### Final product rubric (item 6)

Levels: **Secure** / **Developing** / **Not yet evidenced** (descriptive; no points unless the school sets them).

| Criterion | Secure looks like |
| --- | --- |
| Enough of every item | Every quantity meets or exceeds need for 18 kits; stock limits respected. |
| Units, whole packs and cost | Whole packs only; units on every line; totals and budget-left correct. |
| Comparison | Two feasible orders compared on what they actually supply and cost, not pack price alone. |
| Mathematical explanation | Unit rates, quantities and costs explained with the team's own numbers. |
| Justified revision | The stock-change revision names the failed constraint and proves the new order works. |

## Lesson-to-template map

| Week | Individual | Group |
| --- | --- | --- |
| 1 | [M1-W1-I](#m1-w1-i--read-the-kit-and-price-the-quantities) · Template A | [M1-W1-G](#m1-w1-g--model-fractional-supply-and-place-the-first-order) · Template B |
| 2 | [M1-W2-I](#m1-w2-i--compare-suppliers-with-linked-representations) · Template A | [M1-W2-G](#m1-w2-g--scale-the-order-and-interpret-percent) · Template B |
| 3 | [M1-W3-I](#m1-w3-i--plan-packs-and-interpret-powers) · Template A | [M1-W3-G](#m1-w3-g--respond-to-a-stock-change) · Template C |
| 4 | [M1-W4-I](#m1-w4-i--finish-and-defend-an-individual-recommendation) · Template D | [M1-W4-G](#m1-w4-g--run-the-supply-exchange) · Template E |

---

## M1-W1-I — Read the kit and price the quantities

Template A · Week 1 · Individual · Competencies: Primary 6.RP.A.1, 6.RP.A.2 · Supporting 6.NS.B.2

**Subsection description:** "Today you'll build one supply kit with counters, work out what 12 kits need, and find which supplier's blue clips cost less each."

| # | Slot | Item | Type | Content |
| --- | --- | --- | --- | --- |
| 1 | ① 0–10 | `M1-W1-I ① Warm-up` | H5P **Question Set** (Fill in the Blanks) | 6 × 3 = **18** · 4 × 1/4 = **1** · $2.40 + $2.40 = **$4.80** · 96 ÷ 8 = **12** |
| 2 | ① | `M1-W1-I ① Today's brief` | Text and media | Subsection description, plus "Open the Project Hub kit recipe and supplier cards." |
| 3 | ② 10–30 | `M1-W1-I ② Worked example` | H5P **Interactive Book**, 4 pages | Listed below. |
| 4 | ② | `M1-W1-I ② Resources` | URL | Link to `M1 Project data`. "Read the kit recipe and the 6 price rows. Get counters." |
| 5 | ③ 30–70 | `M1-W1-I ③ Project work` | Assignment, individual; Checklist | Listed below. |
| 6 | ④ 70–85 | `M1-W1-I ④ Check` | Quiz, auto | Listed below. |
| 7 | ④ | `M1-W1-I ④ Explain` | Quiz, essay | Listed below. |
| 8 | Stuck | `M1-W1-I If you're stuck: ratios and division` | Page, restricted | Listed below. |
| 9 | Stuck | `M1-W1-I Recheck` | Quiz, restricted | Listed below. |
| 10 | ⑤ 85–90 | `M1-W1-I ⑤ Carry forward` | Text and media | "Save your 12-kit table. Your team uses it next lesson." |

**② Worked example pages** (six-kit numbers only; never the 12-kit answers):

1. *Six kits:* table 12 blue, 18 gold, 1.5 m ribbon. Fill in the Blanks: 6 × 2 = \*12\*, 6 × 3 = \*18\*, 6 × 1/4 = \*1.5\* m.
2. *Ratio or fraction?* blue:gold = 2:3 compares two groups; blue/all clips = 2/5 compares a part with the whole. Drag the Words: "2:3 is a \*ratio\*; 2/5 is a \*fraction\* of all the clips."
3. *Price per clip:* $2.40 ÷ 12 = $0.20 (A) and $1.80 ÷ 10 = $0.18 (B). Fill in the Blanks for both. Note: "Cheaper per clip doesn't always mean a cheaper order. You'll test that later."
4. *Dividing big numbers:* 936 ÷ 24 by partial groups (24 × 30 = 720, 24 × 9 = 216, 30 + 9 = 39), then the same problem by the standard algorithm. Fill in the Blanks: quotient \*39\*.

**③ Project work** — steps: 1. Build one kit with counters; write one sentence for the ratio and one for the fraction. 2. Make the 12-kit table. 3. Find and label both blue unit prices; explain why the cheaper clip might not give the cheapest order. 4. Add one purchasing question. *Checklist:* 24 blue, 36 gold, 3 m ribbon with units · $0.20 and $0.18 labeled per clip · explanation present · question present.

**④ Check** (auto):

| Q | Type | Question | Answer / setup |
| --- | --- | --- | --- |
| 1 | Cloze (variant pool) | "A bag has 3 red and 2 green counters. Ratio of red to green: ___ . Fraction of all counters that are red: ___" | 3:2 and 3/5. Variants: 5 red 1 green (5:1, 5/6); 2 red 7 green (2:7, 2/9); 4 red 3 green (4:3, 4/7). |
| 2 | Calculated | "A pack of {n} clips costs ${p}. What is the price per clip? Round to the nearest cent." | `{p}/{n}`; n 4–12 (0 dp), p 1.00–6.00 (2 dp). Guide item: n = 8, p = 2.00 → 0.25. |
| 3 | Calculated | "Use a standard algorithm: {={d}*{q}} ÷ {d}" | `{q}`; d 12–29, q 21–49 (0 dp). Guide item: d = 24, q = 36 (864 ÷ 24). |
| 4 | Multiple choice **(audit P4)** | "A supplier's card says '0 packs for $5'. What is the price per pack?" | **"There isn't one: you can't share $5 among 0 packs."** Distractors: $0; $5; $0.50. |

**④ Explain** — Essay 1: "Explain the difference between your ratio and your fraction in Q1." Marking guide: names both groups for the ratio; names the whole for the fraction. Essay 2 (attachment): "Upload a photo of 864 ÷ 24 worked with the standard algorithm." Marking guide: 36 with place-value steps shown. This is baseline evidence, not a fluency judgement.

**Stuck page:** "Circle all 5 counters. Put a ring round each colour group. A ratio like 2:3 compares the two groups. A fraction like 2/5 compares one group to *all* the counters." Then "Division slipping? Rebuild the number in tens and ones before you divide." Link back to Worked example pages 2 and 4.

**Recheck:** Cloze: 4 blue and 1 gold → **4:1** and **4/5**. Calculated: 672 ÷ 21 = **32** (same setup as Check Q3, with guide item d = 21, q = 32).

---

## M1-W1-G — Model fractional supply and place the first order

Template B · Week 1 · Group · Competencies: Primary 6.NS.A.1, 6.NS.B.3 · Supporting 6.RP.A.1, 6.RP.A.2, 6.NS.B.2

**Subsection description:** "Your team places the first order for 12 kits. You'll use fraction strips for the ribbon and a ledger for the cost."

| # | Slot | Item | Type | Content |
| --- | --- | --- | --- | --- |
| 1 | ① 0–10 | `M1-W1-G ① Team brief` | Page | Description, plus "Read the 6 supplier rows and the ribbon problem: how many 1/4 m pieces fit in a 3/4 m strip?" |
| 2 | ① | `M1-W1-G ① Team roles` | H5P **Dialog Cards** | **Calculator:** works out each line. **Checker:** redoes one line another way. **Explainer:** says why the order fills every kit. Back of every card: "Rotate roles. Everyone calculates at least one line by hand." |
| 3 | ② 10–30 | `M1-W1-G ② Mini-model` | H5P **Interactive Video** (or Interactive Book if not recorded) | Listed below. |
| 4 | ③ 30–70 | `M1-W1-G ③ Team task` | Text and media; link to `M1 Team ledger` | Listed below. |
| 5 | ③ | `M1-W1-G ③ Team product update` | Assignment, group; Checklist | Ledger section *12-kit order* complete. *Checklist:* whole packs only · enough of every item · line costs and total correct · fill check written. |
| 6 | ④ 70–85 | `M1-W1-G ④ Private check` | Quiz, auto | Listed below. Open it from the start of ③; due by the end of ④. |
| 7 | ④ | `M1-W1-G ④ Explain` | Quiz, essay | Listed below. |
| 8–9 | Stuck | `If you're stuck: fraction division and decimals` + `Recheck` | Page + Quiz, restricted | Listed below. |
| 10 | ⑤ 85–90 | `M1-W1-G ⑤ Team challenge` | Forum (standard, no groups) | "Post your order total and one ledger line that proves you have enough ribbon. Then ask another team one question about their order." Completion: 1 discussion + 1 reply. |

**② Mini-model** (2–5 min, with captions; one pause question after each step):

1. 3/4 m cut into 1/4 m pieces gives 3 pieces. *Pause:* "How many pieces?" → **3**.
2. 2/3 ÷ 3/4 on a strip marked in twelfths: 8/12 of the 9/12 piece, so 8/9 of a piece. Check: (3/4)(8/9) = 2/3. *Pause (True/False):* "8/9 means 8/9 of a meter." → **False**: it's 8/9 of a 3/4 m piece.
3. $4.80 + $7.20 + $1.50 = $13.50 and $24 − $13.50 = $10.50, lined up by place value. *Pause (Fill in the Blanks):* $24.00 − $13.50 = \*10.50\*.

**③ Team task** — 1. Each student models a ribbon quotient with strips before talking. 2. Choose whole packs for 12 kits; record quantities, cost and leftovers in the ledger. 3. Rotate roles so everyone does one line by hand. 4. Check one full kit can be filled; fix any shortage.
*Teacher key:* cheapest is 2 A blue + 2 A gold + 1 A spool = **$13.50**, with $10.50 left and no leftovers. Other feasible orders are fine.

**④ Private check** (auto):

| Q | Type | Question | Answer / setup |
| --- | --- | --- | --- |
| 1 | Calculated | "Add: ${a} + ${b}" | `{a}+{b}`; a, b 1.05–9.95 (2 dp). Guide item: 7.85 + 4.60 = 12.45. |
| 2 | Calculated | "Subtract: ${t}.00 − ${s}" | `{t}-{s}`; t 15–25 (0 dp), s 5.05–14.95 (2 dp). Guide item: 20 − 12.45 = 7.55. |
| 3 | Calculated | "Use a standard algorithm: {={d}*{q}} ÷ {d}" | `{q}`; guide item: 756 ÷ 21 = 36. |
| 4 | Cloze (variant pool) | "(3/5) ÷ (1/2) = ___" | **6/5** (accept 1 1/5, 1.2). Variants: (2/3) ÷ (1/2) = 4/3; (3/4) ÷ (1/3) = 9/4; (2/5) ÷ (1/2) = 4/5. |

**④ Explain** (attachment): "A strip is 3/5 m long. How many 1/2 m pieces fit? Draw it with fraction strips, upload a photo, and check your answer with multiplication." Marking guide: shows **1 and 1/5 half-meter pieces**, not 1 1/5 meters; check (1/2)(6/5) = 3/5.

**Stuck page:** "Dividing by a fraction can give a *bigger* number. How many half-meter pieces are in 1 whole meter? Two!" Then: "Decimal points slipping? Write money in a dollars | dimes | pennies grid, lined up at the point."
**Recheck:** Cloze (3/4) ÷ (1/2) = **3/2**; Calculated $6.70 − $2.85 = **$3.85** (same setup as Q2).

---

## M1-W2-I — Compare suppliers with linked representations

Template A · Week 2 · Individual · Competencies: Primary 6.RP.A.3, 6.NS.B.3 · Supporting 6.RP.A.2

**Subsection description:** "Today you'll show each supplier's prices as a table, a graph and a rule, and use them to decide which costs less for 90 gold clips. You'll also work out a delivery time."

| # | Slot | Item | Type | Content |
| --- | --- | --- | --- | --- |
| 1 | ① 0–10 | `M1-W2-I ① Warm-up` | H5P **Question Set** | Retrieval from W1-G: $3.60 + $2.85 = **$6.45** · $10.00 − $6.45 = **$3.55** · gold clips for 12 kits = **36** · $2.40 ÷ 12 = **$0.20** |
| 2 | ① | `M1-W2-I ① Today's brief` | Text and media | Description. |
| 3 | ② 10–35 | `M1-W2-I ② Worked example` | H5P **Interactive Book**, 4 pages | Listed below. |
| 4 | ② | `M1-W2-I ② Resources` | Page | Link to `M1 Project data`, printable equal-scale axes and decimal grid, and the delivery card: "The van drives 6 km in 30 minutes at a constant speed." |
| 5 | ③ 35–70 | `M1-W2-I ③ Project work` | Assignment, individual; Online text + File; Checklist | Listed below. |
| 6 | ④ 70–85 | `M1-W2-I ④ Check` | Quiz, auto | Listed below. |
| 7 | ④ | `M1-W2-I ④ Explain` | Quiz, essay | Listed below. |
| 8–9 | Stuck | `If you're stuck: scaling ratios and decimal division` + `Recheck` | Page + Quiz, restricted | Listed below. |
| 10 | ⑤ 85–90 | `M1-W2-I ⑤ Carry forward` | Text and media | "Keep your gold tables and graph. Next lesson your team scales the order to 18 kits, starting with a quick decimal check." |

**② Worked example pages:**

1. *Table:* A blue packs → (12, $2.40), (24, $4.80), (36, $7.20). Fill in the Blanks: 48 clips → \*$9.60\*. "Both columns are multiplied by the same number."
2. *Graph and rule:* image of the three points on quantity (x) vs cost (y) axes, plus B blue points (10, $1.80), (20, $3.60), (30, $5.40). Rule for A: c = 0.20n. Note: "You can only buy whole packs, so only the dots are real orders." Single Choice: "Which rule fits supplier B blue?" **c = 0.18n** · c = 1.80n · c = 0.10n.
3. *Decimal algorithms:* 2.40 × 3 = 7.20, then 7.20 ÷ 0.20 → multiply both by 10 → 72 ÷ 2 = 36. Drag the Words: "Multiplying both numbers by \*10\* gives the \*same\* quotient."
4. *Speed:* double number line 6 km ↔ 30 min, 12 km ↔ 60 min, 9 km ↔ 45 min. Fill in the Blanks: speed = \*12\* km per hour.

**③ Project work** — 1. Make quantity/cost tables for A gold and B gold, each with one missing entry for you to fill. 2. Plot both on the same axes, label the axes and write each rule. 3. Find the cost of 90 gold clips both ways. 4. Add a delivery estimate for 9 km and say what "constant speed" assumes. Upload a photo of the graph.
*Checklist:* tables correct · points match tables, axes labeled with units · rules c = 0.20n (A) and c = 0.19n (B) · 90 gold: A 5 packs **$18.00**, B 6 packs **$17.10** · delivery **45 minutes** with the assumption stated · units carried through each step (e.g. $/clip × clips = $) **(audit P5)**.

**④ Check** (auto):

| Q | Type | Question | Answer / setup |
| --- | --- | --- | --- |
| 1 | Calculated | "A van drives {={r}*{k}} km in {={k}*10} minutes at a constant speed. How far does it drive in 60 minutes?" | `6*{r}`; r 1–3, k 2–5 (0 dp). Guide item: r = 2, k = 4 (8 km in 40 min → 12 km). |
| 2 | Calculated | "Multiply: {a} × {b}" | `{a}*{b}`; a 1.05–9.95 (2 dp), b 2–9 (0 dp). Guide item: 3.25 × 4 = 13.00. |
| 3 | Calculated | "Divide: {={q}*{k}*0.25} ÷ {={k}*0.25}" | `{q}`; q 12–60, k 1–3 (0 dp); divisors are 0.25, 0.5 or 0.75. Guide item: q = 52, k = 1 (13 ÷ 0.25 = 52). |
| 4 | Calculated | "{n} pens cost ${p}. At the same price, how much do {={n}*{m}} pens cost?" | `{p}*{m}`; n 2–6, m 2–5 (0 dp), p 1.00–5.00 (2 dp). |
| 5 | Calculated, optional **(audit P7)** | "At {r} km every 10 minutes, how many minutes does {={r}*{k}} km take?" | `10*{k}` |

**④ Explain** (attachment): "Upload your gold graph. Explain how one point on it matches a row in your table and your rule." Marking guide: the named point appears in the table; substituting it into the rule gives the same cost; axes labeled.

**Stuck page:** "If you *added* the same amount to both numbers, try a tape diagram. One pack is 4 items for $3; two packs is 8 items for $6. Both numbers are multiplied." Then: "Dividing by a decimal? Multiply both numbers by 10 until the divisor is whole: 4.8 ÷ 0.6 = 48 ÷ 6."
**Recheck:** 4 items for $3 → 12 items for **$9**; 4.8 ÷ 0.6 = **8**.

---

## M1-W2-G — Scale the order and interpret percent

Template B · Week 2 · Group · Competencies: Primary 6.RP.A.3 · Supporting 6.RP.A.1, 6.RP.A.2, 6.NS.A.1, 6.NS.B.3

**Subsection description:** "The order grows to 18 kits. Your team rebuilds the ledger, compares two orders, and uses percents and unit conversions to check the details."

| # | Slot | Item | Type | Content |
| --- | --- | --- | --- | --- |
| 1 | ① 0–10 | `M1-W2-G ① Team brief` | Page | "New order: **18 kits**." Plus the 4 short prompts used in ③ (stock card and conversion card, listed below). |
| 2 | ① | `M1-W2-G ① Team roles` | H5P **Dialog Cards** | **Ledger keeper**, **Percent checker**, **Unit checker**, **Explainer**. Back of every card: "Rotate. Everyone does one line by hand." |
| 3 | ② 10–30 | `M1-W2-G ② Mini-model` | H5P **Interactive Video** or **Course Presentation** | Listed below. |
| 4 | ③ 30–70 | `M1-W2-G ③ Team task` | Text and media; link to ledger | Listed below. |
| 5 | ③ | `M1-W2-G ③ Team product update` | Assignment, group; Checklist | *18-kit comparison* section complete. *Checklist:* 36 blue, 54 gold, 4.5 m · two feasible whole-pack orders with leftovers · totals correct · comparison names what each order supplies, not just its price. |
| 6 | ③ | `M1-W2-G ③ My order line` | Assignment, individual; Online text; Marking guide | "Paste one ledger line you calculated by hand, with your working." Guide: quantity ≥ need; whole packs; line cost correct; units shown. |
| 7 | ④ 70–85 | `M1-W2-G ④ Private check` | Quiz, auto | Listed below. |
| 8 | ④ | `M1-W2-G ④ Explain` | Quiz, essay | "Show the ratio table you used for one conversion in the check." Marking guide: table pairs the units correctly (1 m : 100 cm or 1 yd : 3 ft) and scales both columns. |
| 9–10 | Stuck | `If you're stuck: percent and units` + `Recheck` | Page + Quiz, restricted | Listed below. |
| 11 | ⑤ 85–90 | `M1-W2-G ⑤ Team challenge` | Forum (standard, no groups) | "Post your two 18-kit totals and the one you'd choose. Question another team's choice." |

**② Mini-model** (one pause question per step):

1. A bar of 24 counters split into 4 equal parts. 25% of 24 = **6**. *Pause:* 25% of 40 = \*10\*.
2. The same bar backward: 6 is 25% of what? → **24**. *Pause (Single Choice):* "Is the whole bigger or smaller than its 25% part?" → **Bigger**.
3. Ratio tables: 1 m : 100 cm, so 4.5 m = **450 cm**; 1 yd : 3 ft, so 2.5 yd = **7.5 ft**. *Pause:* 2 m = \*200\* cm.
4. "4.5 m of ribbon is needed, but spools are whole: A sells 3 m and B sells 2 m."

**③ Team task** — 1. Scale your 12-kit ledger to 18 kits: 36 blue, 54 gold, 4.5 m ribbon. 2. Write two feasible whole-pack orders with leftovers and compare them. 3. Each member answers one stock-card question: *"Supplier B has 10 gold packs. Your order uses 4. What percent of B's gold stock is that?"* (**40%**); *"If 4 packs is 40% of a supplier's stock, how many packs did they have?"* (**10**). 4. Write the ribbon need in centimeters (**450 cm**). Then the customary card: *"Gift-box tape comes in 2-yard rolls. Each box uses 1 foot. How many boxes per roll?"* (**6**).

*Teacher key (decision P2):* if suppliers may be mixed within an item, cheapest is **$20.60** (blue 3 A *or* 4 B at $7.20 each; gold 3 A $10.80; ribbon 1 A + 1 B $2.60). With one supplier per item, it's **$21.00** (ribbon 2 A spools $3.00). Point out the blue tie: B is cheaper per clip, but both orders cost $7.20.

**④ Private check** (auto):

| Q | Type | Question | Answer / setup |
| --- | --- | --- | --- |
| 1 | Calculated | "Find {={k}*5}% of {={m}*20}." | `{k}*{m}`; k 1–19, m 1–5 (0 dp). Guide item: k = 6, m = 2 (30% of 40 = 12). |
| 2 | Calculated | "{={k}*{m}} is {={k}*5}% of what number?" | `{m}*20`; guide item: k = 5, m = 3 (15 is 25% of 60). |
| 3 | Calculated | "Convert {x} m to centimeters." | `100*{x}`; x 0.25–9.75 (2 dp). Guide item: 1.25 m = 125 cm. |
| 4 | Calculated | "Convert {y} yd to feet." | `3*{y}`; y 2–20 (0 dp). Guide item: 4 yd = 12 ft. |

**Stuck page:** "25% isn't 25 things. It means 25 out of every 100. Shade a 100-grid, then ask: what's the whole here?" Then: "Units mixed up? Write the ratio table with labels: m | cm, then 1 | 100."
**Recheck:** 8 is 20% of what number? → **40**; 3 m = **300** cm.

---

## M1-W3-I — Plan packs and interpret powers

Template A · Week 3 · Individual · Competencies: Primary 6.NS.B.4, 6.EE.A.1 · Supporting 6.NS.B.2, 6.NS.B.3

**Subsection description:** "Today you'll use factors to pack clips into equal bundles, find when two restock schedules line up, and learn what an exponent really means."

| # | Slot | Item | Type | Content |
| --- | --- | --- | --- | --- |
| 1 | ① 0–10 | `M1-W3-I ① Warm-up` | H5P **Question Set** | Retrieval from W2-G: 20% of 50 = **10** · 12 is 50% of **24** · 2 m = **200** cm · 3 yd = **9** ft |
| 2 | ① | `M1-W3-I ① Today's brief` | Text and media | Description. |
| 3 | ② 10–30 | `M1-W3-I ② Worked example` | H5P **Interactive Book**, 4 pages | Listed below. |
| 4 | ② | `M1-W3-I ② Resources` | Page | Sorting card: "Pack 24 blue and 36 gold clips into identical bundles with nothing left over." Restock card: "Blue restocks every 6 days, gold every 8 days." Counters; square-array paper. |
| 5 | ③ 30–70 | `M1-W3-I ③ Project work` | Assignment, individual; Checklist | Listed below. |
| 6 | ④ 70–85 | `M1-W3-I ④ Check` | Quiz, auto | Listed below. |
| 7 | ④ | `M1-W3-I ④ Explain` | Quiz, essay | Listed below. |
| 8–9 | Stuck | `If you're stuck: GCF, LCM and powers` + `Recheck` | Page + Quiz, restricted | Listed below. |
| 10 | ⑤ 85–90 | `M1-W3-I ⑤ Carry forward` | Text and media | "Keep your backup paragraph. Next lesson starts with a factor and power warm-up, then a stock change hits." |

**② Worked example pages:**

1. *GCF:* 24 blue and 36 gold → 12 identical bundles, each with 2 blue and 3 gold. Fill in the Blanks: GCF(24, 36) = \*12\*.
2. *LCM:* number line of days 6, 12, 18, **24** and 8, 16, **24**. Drag the Words: "Equal bundles use the \*GCF\*; the first shared restock day uses the \*LCM\*."
3. *Factored sum:* 24 + 36 = 12 × 2 + 12 × 3 = 12(2 + 3). Fill in the Blanks: 12(\*2\* + \*3\*).
4. *Powers:* square array 3 × 3 = 3² = 9, next to 3 × 2 = 6. "An exponent counts factors; it doesn't multiply by the exponent." Evaluate 2 + 3² × 4: power first (9), then multiply (36), then add (**38**). Drag the Words to order the steps.

**③ Project work** — 1. Propose equal bundle sizes for your order using the GCF, and a shared restock day using the LCM. 2. Write a factored sum for your bundles. 3. Packing codes: write 2 × 2 × 2 as a power and evaluate it (2³ = 8); a crate holds 3 layers × 3 rows × 3 bundles, so write and evaluate that as a power (3³ = 27). 4. Backup paragraph: if a supplier runs low, which supplier or quantity changes?
*Checklist:* GCF and LCM used for the right purpose · factored sum correct · both powers written and evaluated · backup paragraph names a specific change.

**④ Check** (auto):

| Q | Type | Question | Answer / setup |
| --- | --- | --- | --- |
| 1 | Numerical (variant pool) | "Find GCF(30, 45)." | **15**. Variants: (18, 42) = 6; (28, 70) = 14; (36, 60) = 12. |
| 2 | Numerical (variant pool) | "Find LCM(4, 10)." | **20**. Variants: (6, 8) = 24; (9, 12) = 36; (8, 10) = 40. All numbers ≤ 12. |
| 3 | Cloze (variant pool) **(audit P6)** | "Write the sum using its greatest common factor: 30 + 45 = ___( ___ + ___ ). Keep the addends in the same order." | **15(2 + 3)**. Variants: 36 + 8 = 4(9 + 2); 20 + 35 = 5(4 + 7); 48 + 18 = 6(8 + 3). |
| 4 | Calculated | "Evaluate \\( {a} + {b}^3 \times {c} \\)" | `{a}+pow({b},3)*{c}`; a 2–9, b 2–4, c 2–5 (0 dp). Guide item: 5 + 2³ × 3 = 29. |
| 5 | Cloze **(audit P3)** | "5 × 5 × 5 × 5 = 5^___ = ___" and "7¹ = ___" | **4**, **625**, **7** |
| 6 | Calculated | "Use a standard algorithm: {={d}*{q}} ÷ {d}" | `{q}`; guide item: 924 ÷ 22 = 42. |

**④ Explain** — Essay 1: "What did the GCF tell you about the bundles, and what did the LCM tell you about restock days?" Marking guide: GCF = largest equal group with none left over; LCM = first day both happen; each linked to its situation. Essay 2 (attachment): "Show 5 + 2³ × 3 step by step." Marking guide: 2³ expanded as 2 × 2 × 2 or an array; power, then multiply, then add.

**Stuck page:** "GCF and LCM mixed up? Sort 12 and 18 counters into equal piles: the biggest pile size that works is the GCF. Then list delivery days for each: the first shared day is the LCM." Then: "Is 2³ equal to 6? Write three 2s and multiply them: 2 × 2 × 2."
**Recheck:** GCF(18, 30) = **6**; LCM(3, 8) = **24**; 3³ = **27**.

---

## M1-W3-G — Respond to a stock change

Template C · Week 3 · Group · Competencies: Primary 6.NS.B.3, 6.NS.B.4, 6.EE.A.1 · Supporting 6.RP.A.2, 6.RP.A.3

**Subsection description:** "Supplier A just called: they're nearly out of gold clips. Your team must fix the order and prove the new one works."

Before class: show `M1 Week 3 update` in the Project Hub.

| # | Slot | Item | Type | Content |
| --- | --- | --- | --- | --- |
| 1 | ① 0–10 | `M1-W3-G ① The curveball` | H5P **Branching Scenario** | Listed below. |
| 2 | ② 10–25 | `M1-W3-G ② Spot the mistake` | H5P **Find Multiple Hotspots** | Image of a plan buying 3 A gold packs for $10.80. Hotspots: the unavailable third pack; the claim "A is cheapest per clip" (B is $0.19 vs A's $0.20); the missing leftover check. Provide alt text and a text list of the three errors. |
| 3 | ③ 25–70 | `M1-W3-G ③ Revise the plan` | Text and media; link to ledger | 1. Mark the failed stock constraint. 2. Calculate at least two feasible replacements; update all totals and leftovers. 3. Rotate explanation roles; challenge one unsupported claim. 4. Each student takes the Quick audit during work conferences. Keep the original order next to the revision. |
| 4 | ③ | `M1-W3-G ③ Before and after` | Assignment, group; Checklist | Original and revised ledgers side by side. *Checklist:* uses no more than 2 A gold packs · at least 54 gold · all totals updated · change explained. |
| 5 | ③–④ | `M1-W3-G ④ Quick audit` | Quiz, auto; **open from the start of ③** | Listed below. |
| 6 | ④ 70–85 | `M1-W3-G ④ My justification` | Assignment, individual; Online text; Marking guide | "Which revised order did your team choose? Prove it meets the stock limit and has enough gold." Guide: stock limit respected with numbers; written algorithms accurate; quantity and cost both used. |
| 7 | Stuck | `If you're stuck` + `Recheck` | Page + Quiz, restricted on the Quick audit | Listed below. |
| 8 | ⑤ 85–90 | `M1-W3-G ⑤ What changed?` | Text and media | "What did the stock change teach you about choosing the cheapest option?" |

**① Branching Scenario:** Intro: "Supplier A calls: only **2 gold packs** left!" Decision: "You need 54 gold clips. What do you do?"
- *Buy 3 A packs anyway* → "Not possible: only 2 are in stock."
- *Switch all gold to B* → "Works: 4 B packs = 60 clips for $11.40."
- *Mix suppliers* → "Works: 2 A + 2 B = 66 clips for $12.90. 1 A + 3 B = 63 clips for $12.15 also works."

End screen: "Which feasible order is better for your kits, and why?" (Teacher key: 4 B is the cheapest gold option at $11.40.)

**④ Quick audit** (auto):

| Q | Type | Question | Answer |
| --- | --- | --- | --- |
| 1 | Numerical (variants) | 2.85 × 4 | **11.40** |
| 2 | Numerical (variants) | 11.40 ÷ 15 | **0.76** (audit P1: if approved, use 11.40 ÷ 2.85 = **4** instead) |
| 3 | Numerical (variants) | 7.20 + 11.40 + 3.00 | **21.60** |
| 4 | Numerical (variants) | 24.00 − 21.60 | **2.40** |
| 5 | Numerical (variants) | GCF(36, 54) | **18** (variant GCF(24, 40) = 8) |
| 6 | Numerical (variants) | LCM(6, 9) | **18** (variant LCM(4, 6) = 12) |
| 7 | Cloze (variants) | 36 + 54 = ___( ___ + ___ ) | **18(2 + 3)** (variant 36 + 8 = 4(9 + 2), audit P6) |
| 8 | Numerical (variants) | 2 + 2³ | **10** (variants 3 + 2³ = 11; 1 + 3² = 10) |

Each variant pool has the guide value plus 2 more. Use numerical variants, not calculated questions, because computed money values can lose their trailing zero.

**Stuck page:** "Cover the prices. First check: is there enough stock, and enough clips? Only then compare cost." Then: "For 2 + 2³, only the 2 under the exponent gets multiplied by itself: 2 + (2 × 2 × 2)."
**Recheck:** Single Choice: "You need 3 packs and the supplier has 2. Can you buy this offer?" → **No**. Then 4 + 3² = **13**.

---

## M1-W4-I — Finish and defend an individual recommendation

Template D · Week 4 · Individual · Competencies: Primary 6.RP.A.3, 6.NS.A.1 · Supporting 6.RP.A.1, 6.RP.A.2

**Subsection description:** "Today you'll close any gaps, finish your own part of the purchase file, and write a recommendation you can defend with numbers."

**Routing:** use PLD. For each Where-am-I quiz: *grade < 70%* → add the student to group `Workshop: ratios` or `Workshop: fractions`. Also add students still flagged from the Week 1–3 rechecks (teachers can add by hand from Participants → Groups).

| # | Slot | Item | Type | Content |
| --- | --- | --- | --- | --- |
| 1 | ① 0–5 | `M1-W4-I ① Where am I? Ratios` | Quiz, Practice category; immediate feedback | "2 notebooks cost $3.00 at one shop and 3 cost $4.20 at another. How much do 6 notebooks cost at each?" → **$9.00** and **$8.40** |
| 2 | ① | `M1-W4-I ① Where am I? Fractions` | Quiz, same settings | (2/3) ÷ (1/6) = **4** |
| 3 | ② 5–20 | `M1-W4-I ② Workshop: ratio representation` | H5P **Interactive Book**; restricted to group *Workshop: ratios* | Model on new numbers: 4 pens for $3.00 → table rows (4, 3.00), (8, 6.00), (12, 9.00); rule c = 0.75n; point (8, 6.00) on a graph. Fill in the Blanks at each step. |
| 4 | ② | `M1-W4-I ② Workshop: fraction model` | H5P **Interactive Book**; restricted to group *Workshop: fractions* | (5/6) ÷ (1/3) = 5/2 with strips in sixths; check (1/3)(5/2) = 5/6. |
| 5 | ② | `M1-W4-I ② Improve your explanation` | Page; shown to students in neither group | "A strong recommendation names the quantity, the cost, and a reason to reject the other offer. Find your weakest sentence and add a number to it." |
| 6 | ③ 20–55 | `M1-W4-I ③ Write your recommendation` | H5P **Structure Strip** | Strips: *My recommendation* · *The numbers that prove it* · *Why not the other supplier* · *How I checked it's enough*. 4–6 sentences total. |
| 7 | ③ | `M1-W4-I ③ Final individual file` | Assignment, individual; Rubric | 1. Audit your file against the Project Hub "What good work shows" list. 2. Paste your recommendation under the final table. 3. Revise one weak representation. Rubric rows (Secure / Developing / Not yet evidenced): feasibility justified · choice uses the student's own calculations · representations linked. |
| 8 | ④ 55–85 | `M1-W4-I ④ Transfer check` | Quiz, auto | Listed below. |
| 9 | ④ | `M1-W4-I ④ Explain` | Quiz, essay | Listed below. |
| 10 | ⑤ 85–90 | `M1-W4-I ⑤ Still to work on` | Text and media | "Anything not yet secure gets one more check in the supply exchange and carries into M2." |

**④ Transfer check** (auto):

| Q | Type | Question | Answer |
| --- | --- | --- | --- |
| 1 | Cloze (variant pool) | "Ticket booth A: 3 tickets for $2.40. Booth B: 5 tickets for $4.25. Cost of 15 tickets at A: ___ ; at B: ___ ; cheaper booth: ___" | **12.00**, **12.75**, **A**. Variants: 4 for $3.00 vs 6 for $4.20, 12 tickets → 9.00, 8.40, B; 2 for $1.70 vs 5 for $4.00, 10 tickets → 8.50, 8.00, B. |
| 2 | Cloze | "Write a rule for booth A: c = ___ × n" | **0.80** (variants 0.75; 0.85) |

**④ Explain** — Essay 1 (attachment): "Show your 15-ticket comparison as a table, and plot one pair." Marking guide: table rows scale both columns; plotted point matches a row. Essay 2 (attachment): "Interpret (3/4) ÷ (2/3) = 9/8 with a model and a multiplication check." Marking guide: quotient described as 1 1/8 groups of 2/3; check (2/3)(9/8) = 3/4.

**Recheck routes:** only students flagged earlier for percent, speed, conversion or algorithms. Reuse those lessons' Recheck quizzes with new dataset items; don't build a new test.

---

## M1-W4-G — Run the supply exchange

Template E · Week 4 · Group · Competencies: Primary 6.RP.A.2, 6.RP.A.3 · Supporting 6.RP.A.1, 6.NS.B.3

**Subsection description:** "The exchange is open. New prices, one surprise, and your team's best order. Then you'll defend your own decision."

| # | Slot | Item | Type | Content |
| --- | --- | --- | --- | --- |
| 1 | ① 0–5 | `M1-W4-G ① Performance brief` | Page | Show `M1 Final offers`. "Prepare an 18-kit order. Record it in the *Final exchange* section of the ledger." Event order: plan → change → revise → swap → private slip. |
| 2 | ③ 5–40 | `M1-W4-G ③ The change` | Page, hidden until the teacher shows it | "Supplier A now has only **2 gold packs**." |
| 3 | ③ | `M1-W4-G ③ Live session` | BigBlueButton, separate groups | Online classes only. |
| 4 | ③ | → `M1 Final product` (Project Hub item 6) | Link only | Initial and revised 18-kit ledgers; graded with the Hub rubric. |
| 5 | ③ 40–50 | `M1-W4-G ③ Peer challenge` | Forum (standard, no groups) | One member posts the team's revised ledger. The teacher names the reviewing team. Reviewers reply: "Is there enough of every item? Are the whole packs right?" |
| 6 | ④ 50–70 | `M1-W4-G ④ Decision slip` | Quiz, auto | Listed below. |
| 7 | ④ | `M1-W4-G ④ Explain` | Quiz, essay | "Justify your team's revised order with your own numbers." Marking guide: names the constraint; quantity ≥ need; cost compared with one alternative; units. |
| 8 | ④ | `M1-W4-G ④ Teacher observation` | Assignment, no submission; Checklist; graded live in Open Grader | Explains one team ledger line · uses units · names a tradeoff. |
| 9 | Stuck 70–85 | `M1-W4-G Solo recheck` | Quiz, restricted on the Decision slip | Listed below. |
| 10 | ⑤ 85–90 | `M1-W4-G ⑤ Project reflection` | Questionnaire | "What did you get better at in this project? What do you still want to practice?" Plus "Open items carry into M2 Week 1 retrieval." |

**Teacher key** (multiple valid orders accepted):

| Case | Order | Cost |
| --- | --- | --- |
| Before the change, all A | 3 blue, 3 gold, 2 spools | **$21.48** |
| Before the change, cheapest | 4 B blue $7.60 · 3 A gold $10.26 · ribbon 1 A + 1 B $2.65 | **$20.51** ($20.86 with one supplier per item: 3 B spools $3.00) |
| After the change, cheapest | 4 B blue $7.60 · 4 B gold $12.00 · ribbon $2.65 | **$22.25** ($22.60 with one supplier per item) |

**④ Decision slip** (auto):

| Q | Type | Question | Answer |
| --- | --- | --- | --- |
| 1 | Numerical (variants) | "Supplier B sells gold in packs of 15 for $3.00. What is the price per clip?" | **0.20** |
| 2 | Numerical (variants) | "You can buy only 2 A gold packs (36 clips) and need 54. How many B packs of 15 cover the rest?" | **2** (18 more clips; 2 packs = 30) |
| 3 | Single Choice | "Which gold order is cheaper: 2 A + 2 B ($12.84) or 4 B ($12.00)?" | **4 B** |

**Solo recheck** (variant pool): "You need 7 items. Packs of 4 cost $1.20. Packs: ___ · Cost: ___ · Spare items: ___" → **2**, **$2.40**, **1**. Variants: 11 items, packs of 4 at $1.50 → 3, $4.50, 1; 9 items, packs of 5 at $2.25 → 2, $4.50, 1.

---

## Build checklist for the whole project

- [ ] Gradebook: Individual evidence (all ④ items, ③ individual assignments, rechecks); Team product (group assignments, M1 Final product); Practice (all H5P and Where-am-I quizzes).
- [ ] Every ④ Check is auto-graded only; every essay is in a separate ④ Explain.
- [ ] Each calculated question's dataset item 1 uses the guide's values and gives the guide's answer.
- [ ] Stuck routes tested with one test student below 70% and one above.
- [ ] `M1 Week 3 update`, `M1 Final offers` and `M1-W4-G ③ The change` are hidden until their lesson.
- [ ] Forums are No groups; group assignments use the Teams grouping.
- [ ] Math displays in H5P and quizzes (test \\(\frac{3}{4}\\) and \\(2^3\\)).
- [ ] Videos captioned; hotspot image has alt text and a text list; drag activities have a keyboard route; Brickfield check run.
- [ ] Competencies linked: Primary on ④ Check and ④ Explain, Supporting on ③ Work.
