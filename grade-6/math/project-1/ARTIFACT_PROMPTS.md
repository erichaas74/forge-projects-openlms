# Grade 6 Math – M1 Supply Exchange: Interactive Artifact Prompts

Prompts for making a living diagram or mini-game for every idea in M1 with Claude artifacts. Each one produces a single HTML file you can play in Claude, download, and upload to Open LMS.

All math in these prompts comes from the [build guide](BUILD_GUIDE.md) and was checked in the [audit](AUDIT.md). The games are **practice**: they never replace the graded ④ Check or ④ Explain items in the [course build](OPENLMS_COURSE_BUILD.md).

## How to use a prompt

1. Open a new chat at claude.ai.
2. Paste the **Shared rules** block, then the **Project data** block, then one game block, all in **one message**.
3. Play it as a student would. Try the wrong answers listed under *Test it* and check each one gets the right feedback.
4. If something is off, reply in the same chat with what to change ("the leftover label overlaps the last piece").
5. Download the HTML from the artifact's menu.
6. In Open LMS, add a **File** resource, upload the `.html` file, and set *Display* to **Embed** (or **In pop-up** if it feels cramped). Put it in the lesson slot named under *Where it goes*. If your site blocks scripts in uploaded files, ask the admin to allow them for the course.

Students can't open claude.ai links unless you publish them, so the Moodle upload is how students get the game.

## Shared rules (paste first, every time)

```
Build this as a Claude artifact: one self-contained HTML file with all CSS and JavaScript inline. No libraries, no images from the web, no network requests. Google Fonts are allowed only with a solid system-font fallback, because the file will also run offline inside our school's Moodle site.

Audience: 6th graders (age 11–12) in Tennessee, on Chromebooks and sometimes phones. Reading level: short sentences, one instruction at a time, math vocabulary kept (ratio, unit rate, quotient) but explained with a picture.

It must:
- Work with mouse, touch AND keyboard. Anything you can drag must also work with click-to-select then click-to-place, and with Tab/Enter/arrow keys.
- Announce feedback in an aria-live region. Never use color as the only signal; add a word or icon.
- Fit a 1366×768 Chromebook screen without scrolling the main play area, and stack cleanly at 400px wide.
- Respect prefers-reduced-motion (animations become instant).
- Do all money math in whole cents and all fraction math with integer numerators and denominators. Never show floating-point errors like 0.30000000000000004. Show money with two decimals.
- Open in a playable state with the first round already on screen.
- Have a "New numbers" button that makes a fresh round with clean values, and an "Example" button that steps through one worked case.
- Give feedback that names the likely mistake (listed below) instead of just "wrong", and let the student try again.
- Show a small "rounds solved" counter. No timers, no leaderboards, no grades, and nothing saved or sent anywhere. This is practice.
- Never show the answer to the team's real project order. Students must calculate those themselves; the game may check whether an order is feasible.

Visual style: a supply-room workbench look with clip packs, ribbon spools, a price card and a ledger. Blue clips and gold clips must be easy to tell apart by shape as well as color. Big, friendly numbers.
```

## Project data (paste second, every time)

```
Project: "Supply Exchange." Student teams buy supplies to fill activity kits.
- One kit needs 2 blue clips, 3 gold clips and 1/4 meter of ribbon.
- Supplier A: blue pack of 12 for $2.40; gold pack of 18 for $3.60; ribbon spool of 3 m for $1.50.
- Supplier B: blue pack of 10 for $1.80; gold pack of 15 for $2.85; ribbon spool of 2 m for $1.10.
- Stock: 10 of each pack or spool. Budget $24. Buy whole packs only. No tax or shipping.
- Week 1 order: 12 kits. Week 2 order: 18 kits.
- Week 3 change: Supplier A has only 2 gold packs left.
- Final offers (Week 4): A blue 12 for $2.64, gold 18 for $3.42, ribbon 3 m for $1.65; B blue 10 for $1.90, gold 15 for $3.00, ribbon 2 m for $1.00; stock 10 each, then A gold drops to 2 packs.
- Teacher setting, shown as a toggle on any order screen: "Allow buying one item from both suppliers" (default ON).
```

---

## Project Hub

### G0. Supply Chain Map (living diagram)

*Where it goes:* Project Hub, after the launch presentation. *Idea:* how kits, needs, packs, cost and budget connect.

```
Make an animated diagram called "Supply Chain Map".

Show a left-to-right flow: KITS → NEEDS → PACKS → COST → BUDGET.
- A kits slider (1 to 24, starting at 6) drives everything.
- NEEDS shows blue, gold and ribbon totals growing as little stacks (2 × kits, 3 × kits, kits ÷ 4 meters as a fraction and a decimal).
- PACKS shows, for a supplier the student picks (A or B), how many whole packs are needed, with the unused clips drawn faded as "leftover".
- COST adds line costs into a total; BUDGET is a $24 bar that fills and turns to a striped "over budget" pattern with the words "Over budget" past $24.
- Hovering or focusing any arrow explains it in one sentence (e.g. "Packs come in whole numbers, so we round UP").
Include a "What changes?" mode: the student clicks a number in the diagram (for example the gold pack size) and sees every downstream number update with a short pulse.
Do not label any total as "the answer" for 12 or 18 kits.
```

*Test it:* at 6 kits supplier A, needs are 12 / 18 / 1.5 m and packs 1 / 1 / 1. Moving the slider by 1 kit never shows fractional packs.

---

## Week 1 · Individual (M1-W1-I)

### G1. Kit Builder — ratio or fraction?

*Where it goes:* ② Teach, after the worked example. *Standard:* 6.RP.A.1.

```
Make a mini-game called "Kit Builder".

Play area: a kit tray. The student adds blue and gold clips (buttons + drag). Under the tray, two live readouts update:
- "blue : gold" as a ratio, with the two groups circled in the picture,
- "blue out of all clips" as a fraction, with ALL clips circled.
Building 2 blue + 3 gold shows 2:3 and 2/5 side by side, with a sentence explaining the difference.

Rounds: show a bag of counters in two colors (red/green, blue/gold, star/heart). Ask either "ratio of X to Y" or "fraction of all counters that are X". The student types the answer (accept 3:2, 3 : 2, 3 to 2; fractions as 3/5).
Make 2–6 of each color; vary which color is asked first.

Feedback for likely mistakes:
- Gives the ratio when asked for a fraction (3:2 for "fraction red") → "That compares red to green. The fraction compares red to ALL the counters." Circle all of them.
- Gives part/other-part as a fraction (2/3 for blue of 2 blue, 3 gold) → "2/3 compares blue to gold. How many clips are there in all?"
- Reverses the order (2:3 when asked red:green with 3 red) → "Read the order: red first."
Bonus round: "Scale it": the student builds 3 kits and the table shows 6:9 and 6/15, with a note that both simplify back to 2:3 and 2/5.
```

*Test it:* 3 red, 2 green → 3:2 and 3/5. Typing 2/3 for "fraction blue" in a 2-blue/3-gold bag gives the "how many in all?" hint.

### G2. Price Per Clip

*Where it goes:* ③ Work warm-up or Stuck route. *Standard:* 6.RP.A.2.

```
Make a mini-game called "Price Per Clip".

Show a pack of clips and its price card. Pressing "Open the pack" animates the price splitting evenly into one coin stack per clip, landing on a "per clip" label. Start with Supplier A blue: 12 clips for $2.40 → $0.20 per clip. Then Supplier B blue: 10 for $1.80 → $0.18.

Rounds: random packs where price = clips × a whole-cent unit price (clips 4–20, unit price 5¢–45¢). The student types the price per clip.

Comparison round: two packs side by side; the student taps the one that is cheaper PER CLIP, then answers "Which costs less for exactly N clips if you must buy whole packs?" Pick N so the per-clip winner is NOT always the cheaper order (for example 36 blue clips: A 3 packs $7.20 vs B 4 packs $7.20, a tie).

Trap card (every 5th round): "0 packs for $5. What is the price per pack?" Correct choice: "There isn't one: you can't share $5 among 0 packs." Explain in one sentence why the second number in a rate can't be zero.

Feedback for likely mistakes:
- Divides clips by price (12 ÷ 2.40 = 5) → "That's clips per dollar. We want dollars per clip."
- Forgets the dollar unit or writes $20 → "Check the size: one clip should cost less than the whole pack."
```

*Test it:* A blue gives $0.20; B blue $0.18; the 36-clip round shows the $7.20 tie.

### G3. Division Machine

*Where it goes:* W1-I ② Teach, and as a retrieval game in W1-G and W3-I. *Standard:* 6.NS.B.2.

```
Make a mini-game called "Division Machine" for multi-digit whole-number division with a 2-digit divisor.

Two modes the student can switch between:
1. "Partial groups": the dividend is shown as a pile of base-ten blocks. The student picks a chunk size (×10, ×20, ×5, ×2, ×1 of the divisor) to take away, the blocks animate out, and a running list records each chunk. When the pile is empty, the chunks add up to the quotient.
2. "Standard algorithm": a long-division layout with place-value columns. The student fills in one digit at a time (quotient digit, product, difference, bring down). Only the box being filled is active; a wrong digit gets a specific hint.

Problems: divisor 12–29, quotient 21–49, no remainder. Start with 936 ÷ 24 = 39 (the class example), then random.

Feedback for likely mistakes:
- Quotient digit too big (product bigger than what's left) → "24 × 4 = 96 is more than 93. Try one less."
- Digit placed in the wrong column → "This digit tells how many TENS of 24 fit. Line it up over the tens."
- Forgets to bring down → highlight the next digit with an arrow.
After each solve, show the check: divisor × quotient = dividend.
```

*Test it:* 936 ÷ 24 = 39; 864 ÷ 24 = 36; 672 ÷ 21 = 32; 924 ÷ 22 = 42.

---

## Week 1 · Group (M1-W1-G)

### G4. Ribbon Cutter

*Where it goes:* W1-G ② Teach and Stuck route; W4-I fraction workshop. *Standard:* 6.NS.A.1.

```
Make a mini-game called "Ribbon Cutter" for dividing a fraction by a fraction.

Show a ribbon strip lying on a cutting mat with meter marks. The strip is a/b meters long. The question: "How many pieces of c/d meter can you cut?" Ticks mark the common denominator so pieces line up exactly.
The student types a prediction (accept 6/5, 1 1/5 or 1.2), then presses "Cut". Scissors animate along the strip, each full piece lights up and is counted, and any leftover is shaded and labeled as a fraction OF A PIECE (not of a meter). Finish with the multiplication check: (c/d) × quotient = a/b.

Start with these, in order: 3/4 ÷ 1/4 = 3; 2/3 ÷ 3/4 = 8/9; 3/5 ÷ 1/2 = 6/5; 3/4 ÷ 1/2 = 3/2; 5/6 ÷ 1/3 = 5/2; 3/4 ÷ 2/3 = 9/8. Also a kit story: "A 3 m spool. Each kit needs 1/4 m. How many kits?" = 12. Then random problems with denominators 2–12, strip length up to 3 m, quotient up to 6.

Feedback for likely mistakes:
- Multiplies instead of divides → "You multiplied. Dividing asks how many pieces FIT."
- Flips the problem (piece ÷ strip) → "That's how much of the strip one piece is. Count pieces in the strip."
- Leftover written in meters (e.g. 1 1/10 for 3/5 ÷ 1/2) → "1/10 is in meters. Compare the leftover to one whole piece: it's 1/5 of a piece."
- Expects the answer to be smaller → "Dividing by a piece shorter than 1 m can give a bigger number. Count them!"
```

*Test it:* 3/5 ÷ 1/2 shows 1 full piece and a leftover of 1/5 of a piece; typing 1 1/10 gets the "meters" hint.

### G5. Ledger Line-Up

*Where it goes:* W1-G ② Teach and Stuck route. *Standard:* 6.NS.B.3 (add and subtract).

```
Make a mini-game called "Ledger Line-Up" for adding and subtracting money with the standard algorithm.

Show an order ledger with columns labeled dollars (tens, ones) | . | dimes | pennies. The student drags each price card into the grid; it snaps by its decimal point. Then they fill in the sum or difference digit by digit, right to left, with regroup "carry" and "borrow" marks animated.

Start with the class model: $4.80 + $7.20 + $1.50 = $13.50, then $24.00 − $13.50 = $10.50. Then random two- and three-line problems in whole cents (amounts $1.05–$19.95), including subtraction from a whole-dollar budget ($15–$25).

A "messy ledger" round shows a calculation lined up by the right-hand digit instead of the decimal point (7.85 + 4.6 written as 7.85 over 46) and asks the student to find and fix the mistake.

Feedback for likely mistakes:
- Misaligned decimal → "Line up the decimal points. Pennies go under pennies."
- Missed regroup → highlight the column and show 10 pennies turning into 1 dime.
- Subtracting the smaller digit from the larger in each column → "You can't take 5 pennies from 0 pennies. Borrow a dime first."
```

*Test it:* $7.85 + $4.60 = $12.45; $20.00 − $12.45 = $7.55; $6.70 − $2.85 = $3.85.

### G6. First Order

*Where it goes:* W1-G ③ Work, beside the team ledger. *Standards:* 6.RP.A.2, 6.NS.B.3.

```
Make an order simulator called "First Order".

The student sets the number of kits (start at 12). For each item (blue, gold, ribbon) they choose how many packs to buy from A and from B with +/− steppers (respect the mixing toggle from the project data).
Live visuals:
- A fill gauge per item: needed amount as a line, bought amount as a bar, leftover shown faded beyond the line.
- A one-kit "assembly" animation that builds kits from the bought supplies until something runs out, then shows "Short by N gold clips" with the missing clips outlined.
- A ledger table with packs, items bought, leftover, price per pack and line cost, plus total and budget left.
- A budget bar with $24 marked.
A "Check order" button reports only: enough of every item (yes/no per item), within stock (yes/no), within budget (yes/no). It must NOT say whether the order is the cheapest.
```

*Test it:* any order shows correct leftovers; buying 1 A gold pack for 12 kits shows "Short by 18 gold clips".

---

## Week 2 · Individual (M1-W2-I)

### G7. Three Views

*Where it goes:* W2-I ② Teach and ③ Work. *Standard:* 6.RP.A.3a.

```
Make a linked-representations explorer called "Three Views".

Three panels that always show the same relationship:
1. a table of (clips, cost) rows,
2. a coordinate graph (clips on x, cost in dollars on y, labeled axes, equal-interval scales),
3. a rule c = k × n.
Selecting a supplier and item (start with Supplier A blue: (12, 2.40), (24, 4.80), (36, 7.20)) fills all three. Adding a row to the table drops a point onto the graph with a short animation; tapping a point highlights its table row and shows the rule's substitution.
Show only whole-pack points as solid dots (12, 24, 36…), and draw the rule's line as a faint dashed guide labeled "price-per-clip rule". Add a note: "You can only buy whole packs, so only the dots are real orders."
Comparison mode: plot A gold (18 for $3.60) and B gold (15 for $2.85) together. The student finds the cost of 90 gold clips from each (90 is on both tables) and the steeper line is labeled "costs more per clip".
Challenge: one table row has a missing value; one point is deliberately off the line ("Which row doesn't belong?").

Feedback for likely mistakes:
- Adding the same amount to both columns (12 → 13, 2.40 → 3.40) → show the point leaving the line and say "Both columns must be MULTIPLIED by the same number."
- Swapped axes → "Clips go across, cost goes up."
```

*Test it:* the rules are c = 0.20n (A blue and A gold) and c = 0.19n (B gold); 90 gold costs $18.00 from A and $17.10 from B.

### G8. Decimal Scaler

*Where it goes:* W2-I ② Teach and Stuck route. *Standard:* 6.NS.B.3 (multiply and divide).

```
Make a mini-game called "Decimal Scaler".

Part 1, Multiply: an area model on a grid shows 2.40 × 3 as three strips of 2.40, then the standard algorithm with the decimal place counted. Random problems: a 2-decimal number (1.05–9.95) × a whole number 2–9. Also show the estimate first ("about 2 × 3 = 6").

Part 2, Divide by a decimal: show the problem 7.20 ÷ 0.20 on a "scaler" with a ×10 button. Each press multiplies BOTH numbers by 10, animating the decimal points sliding right together, until the divisor is whole: 72 ÷ 2 = 36. A sentence explains "same quotient, friendlier numbers." Random problems use divisors 0.2, 0.25, 0.4, 0.5, 0.6, 0.75 and whole-number quotients 4–60.

Feedback for likely mistakes:
- Only the divisor scaled → "You changed only one number. Scale both to keep the same quotient."
- Decimal point placed by "lining up" in multiplication → "Count the decimal places in the factors."
```

*Test it:* 3.25 × 4 = 13.00; 13.00 ÷ 0.25 = 52; 4.8 ÷ 0.6 = 8; 7.20 ÷ 0.20 = 36.

### G9. Delivery Van

*Where it goes:* W2-I ② Teach. *Standard:* 6.RP.A.3b (constant speed).

```
Make a living diagram called "Delivery Van" using a double number line.

Top line: kilometers. Bottom line: minutes. A van drives along the top while a clock hand sweeps along the bottom, at constant speed, so the two stay linked. Start with the class card: 6 km in 30 minutes. The student drags a marker to 60 minutes and the van stops at 12 km; at 45 minutes it shows 9 km. Show "12 km per hour" and "0.2 km per minute" as unit rates.
Rounds alternate between:
- "How far in T minutes?" (e.g. 8 km in 40 minutes → distance in 60 minutes = 12 km),
- "How long to drive D km?" (time for a given distance).
Random speeds: 1–3 km every 10 minutes; times are multiples of 10 or 15 minutes.
Add a "constant speed?" toggle that makes the van speed up and slow down, and a sentence explaining why the double number line only works when the speed is constant.

Feedback for likely mistakes:
- Adding the same number to both lines (6 km/30 min → 36 km/60 min) → "Doubling the time doubles the distance."
```

*Test it:* 8 km / 40 min → 12 km in 60 min; 9 km at 12 km/h takes 45 minutes.

---

## Week 2 · Group (M1-W2-G)

### G10. Percent Bar

*Where it goes:* W2-G ② Teach and Stuck route. *Standard:* 6.RP.A.3c.

```
Make a mini-game called "Percent Bar".

A long bar labeled 0% to 100% sits above a matching bar labeled 0 to the WHOLE amount. A 10×10 hundred-grid can be toggled on. Dragging a slider shades both bars together.
Two kinds of rounds:
1. "Find the part": 25% of 24 counters → shade 25% and the counters split into 4 equal groups; answer 6.
2. "Find the whole": 6 is 25% of what? → the student drags the whole-bar's right end until 6 lines up with 25%; answer 24.
Stock-card rounds use the project: "Supplier B has 10 gold packs. Your order uses 4. What percent?" (40%) and "4 packs is 40% of the stock. How many packs?" (10).
Random rounds: percents that are multiples of 5; wholes chosen so every part is a whole number.

Feedback for likely mistakes:
- Treats 25% as 25 items → "25% means 25 out of every 100. What's the whole here?"
- Whole answer smaller than the part → "The whole has to be bigger than its 25% part."
```

*Test it:* 30% of 40 = 12; 15 is 25% of 60; 8 is 20% of 40.

### G11. Unit Converter

*Where it goes:* W2-G ② Teach and ③ Work. *Standard:* 6.RP.A.3d.

```
Make a mini-game called "Unit Converter" with ratio tables.

Two benches: Metric (meters ↔ centimeters, 1 : 100) and Customary (yards ↔ feet, 1 : 3). Never convert between systems.
Each round shows a ribbon or tape and a two-column ratio table. The student fills in the missing value, and the ribbon redraws in the new unit with tick marks (450 cm on the same length as 4.5 m).
Project rounds: 18 kits need 4.5 m of ribbon = 450 cm; a 3 m spool = 300 cm; "Gift-box tape comes in 2-yard rolls; each box uses 1 foot; how many boxes per roll?" = 6.
"Units through the math" round: show a calculation like $0.19 per clip × 60 clips and let the student drag unit tiles so "per clip" and "clips" cancel, leaving dollars.

Feedback for likely mistakes:
- Divides when it should multiply (4.5 m → 0.045 cm) → "Centimeters are smaller, so you need MORE of them."
- Uses 1 yd = 12 ft or 1 m = 10 cm → show the ruler picture with the right count.
```

*Test it:* 1.25 m = 125 cm; 4 yd = 12 ft; 2.5 yd = 7.5 ft; 3 m = 300 cm.

### G12. Scale Up

*Where it goes:* W2-G ③ Work. *Standards:* 6.RP.A.3, 6.NS.B.3.

```
Make an order comparer called "Scale Up".

Start from a 12-kit order that the student enters (or a sample 12-kit order marked "example"). A "Scale to 18 kits" button animates the needs growing by 50% (24 → 36 blue, 36 → 54 gold, 3 m → 4.5 m) with a ratio table showing 12 : 18 = 2 : 3 per item.
The student then builds two different feasible 18-kit orders in two columns ("Order 1", "Order 2"). For each: items bought, leftovers, total cost, budget left. A comparison strip below shows which uses fewer leftovers and which costs less, but never declares a "best" order.
Highlight a discovery moment when it happens: if both orders buy blue for the same cost (3 A packs and 4 B packs both cost $7.20), show "Same cost, different leftovers. Cheaper per clip didn't win here!"
```

*Test it:* needs scale to 36 / 54 / 4.5 m; 3 A blue and 4 B blue both show $7.20.

---

## Week 3 · Individual (M1-W3-I)

### G13. Bundle Sorter (GCF)

*Where it goes:* W3-I ② Teach. *Standard:* 6.NS.B.4.

```
Make a mini-game called "Bundle Sorter" for the greatest common factor.

Show two piles: 24 blue and 36 gold clips. The student picks a bundle count (1–36); the clips animate into that many identical bundles. If any clip is left over, it bounces back with "Not equal bundles." The game keeps a list of bundle counts that worked (common factors) and lights up the biggest: 12 bundles of 2 blue + 3 gold.
Then random pairs with both numbers ≤ 100 and a GCF of at least 2.
Show the factor lists for both numbers with common factors circled.

Feedback for likely mistakes:
- Picks a common MULTIPLE → "Multiples are bigger than the numbers. Bundles split the clips into smaller groups."
- Picks a common factor that isn't greatest → "That works! Can you make even more bundles?"
```

*Test it:* GCF(24, 36) = 12; GCF(30, 45) = 15; GCF(18, 30) = 6; GCF(36, 54) = 18.

### G14. Restock Calendar (LCM)

*Where it goes:* W3-I ② Teach. *Standard:* 6.NS.B.4.

```
Make a living diagram called "Restock Calendar" for the least common multiple.

A 40-day calendar strip. Blue restocks every 6 days, gold every 8 days. Pressing "Play" lights blue truck icons on days 6, 12, 18… and gold on 8, 16, 24…; the first day both trucks arrive bursts with "Both on day 24!" The student predicts before pressing Play.
Random rounds with both numbers ≤ 12.
A final "GCF or LCM?" sorting round: six short situations (equal bundles, next shared day, largest square tile, first time two lights blink together…) to drop into GCF or LCM bins.

Feedback for likely mistakes:
- Multiplies the numbers (6 × 8 = 48) → show day 24 lighting up first: "48 works, but there's an earlier shared day."
```

*Test it:* LCM(6, 8) = 24; LCM(4, 10) = 20; LCM(3, 8) = 24; LCM(6, 9) = 18.

### G15. Factor the Sum

*Where it goes:* W3-I ② Teach. *Standard:* 6.NS.B.4 (distributive property).

```
Make a living diagram called "Factor the Sum" using area models.

Show 24 + 36 as two rectangles of unit squares. The student chooses a shared height (a common factor); both rectangles reshape to that height and slide together into one rectangle labeled height × (width1 + width2). At the GCF the result is 12 × (2 + 3) and the inner sum has no common factor; at a smaller common factor (6 × (4 + 6)) a note says "4 and 6 still share a factor. Keep going."
Rounds must vary the inner sum. Include 36 + 8 = 4(9 + 2), 20 + 35 = 5(4 + 7), 48 + 18 = 6(8 + 3), 30 + 45 = 15(2 + 3). Random pairs: both ≤ 100, GCF ≥ 2.
The student types the answer in the form k(a + b); accept either addend order.
```

*Test it:* 36 + 8 → 4(9 + 2); 6(4 + 6) for 24 + 36 gets the "keep going" note.

### G16. Power Builder

*Where it goes:* W3-I ② Teach and Stuck route. *Standard:* 6.EE.A.1.

```
Make a mini-game called "Power Builder" for whole-number exponents.

Part 1, Build: the student picks a base (1–6) and exponent (1–3). Exponent 2 builds a square of tiles; exponent 3 stacks it into a cube; exponent 1 shows a single row. The expanded form (3 × 3 × 3) and the value appear as it builds. A side-by-side panel always shows base × exponent (3 × 3 = 9 vs 3 × 2 = 6) so the difference is visible.
Part 2, Write it: show repeated multiplication (5 × 5 × 5 × 5, packing crates of 3 layers × 3 rows × 3 bundles) and the student writes it as a power.
Part 3, Order machine: an expression like 2 + 3² × 4 goes through a machine that only lets the student choose the next step. Wrong order sparks a "jam" with the reason. Answer 38. Random: a + b³ × c with small numbers (2 + 2³ = 10, 5 + 2³ × 3 = 29, 4 + 3² = 13).

Feedback for likely mistakes:
- 2³ = 6 → "That's 2 × 3. The exponent says how many 2s to multiply: 2 × 2 × 2."
- Adds before the power → "Powers come first."
```

*Test it:* 3² = 9, 3³ = 27, 7¹ = 7; 2 + 3² × 4 = 38; 5 + 2³ × 3 = 29.

---

## Week 3 · Group (M1-W3-G)

### G17. Curveball

*Where it goes:* W3-G ① Launch (alternative to the H5P Branching Scenario) and ③ Work. *Standards:* 6.NS.B.3, 6.RP.A.3.

```
Make a story mini-game called "Curveball".

Scene 1: a phone rings. "Supplier A here: we have only 2 gold packs left!" Show the student's 18-kit gold need of 54 clips.
Scene 2: three choices: "Buy 3 A packs anyway", "Switch all gold to B", "Mix suppliers". Each plays a short consequence:
- 3 A packs → the third pack is greyed out: "Not possible: only 2 in stock."
- 4 B packs → 60 clips for $11.40, 6 leftover.
- 2 A + 2 B → 66 clips for $12.90; also show 1 A + 3 B → 63 clips for $12.15.
Scene 3, Spot the mistake: a worked plan picture with three errors to tap: uses 3 A gold packs; claims "A is cheapest per clip" (B is $0.19, A is $0.20); has no leftover check. Each error tapped reveals the fix.
Scene 4: the student revises a ledger (same order builder as "First Order") and the game checks only feasibility and the stock limit.
End: "Which feasible order is better for your kits? Write one reason," with a text box that stays on screen (not saved).
```

*Test it:* the 3-A-pack option is impossible; 4 B packs show $11.40; all three errors can be found with the keyboard.

---

## Week 4 · Individual (M1-W4-I)

### G18. Recommendation Builder

*Where it goes:* W4-I ③ Work, beside the Structure Strip. *Standards:* 6.RP.A.3, 6.RP.A.1.

```
Make a mini-game called "Recommendation Builder".

Part 1, Compare: two ticket booths. Booth A: 3 tickets for $2.40. Booth B: 5 tickets for $4.25. The student fills a ratio table for each until both reach 15 tickets ($12.00 vs $12.75), and plots one pair from each on a small graph. A third card shows the rule c = 0.80 × n for Booth A.
Random variants: 4 for $3.00 vs 6 for $4.20 at 12 tickets; 2 for $1.70 vs 5 for $4.00 at 10 tickets.
Part 2, Build the argument: four sentence frames: "I recommend…", "The numbers that prove it are…", "I didn't choose the other option because…", "I checked it's enough by…". The student types into each. A checker highlights any frame with no number in it and says "Add a number that proves this."
Nothing is saved; add a "Copy my recommendation" button.
```

*Test it:* 15 tickets cost $12.00 at A and $12.75 at B; a frame with no digits gets the "add a number" prompt.

---

## Week 4 · Group (M1-W4-G)

### G19. Supply Exchange Live

*Where it goes:* W4-G ③ Work, projected for the class or used by each team. *Standards:* 6.RP.A.2, 6.RP.A.3.

```
Make a classroom simulation called "Supply Exchange Live" using the FINAL offers from the project data.

Phase 1, Plan: teams build an 18-kit order with the order builder (needs gauges, ledger, budget bar, mixing toggle). "Lock order" freezes it.
Phase 2, The change: a teacher button "Release the change" flashes a news ticker: "Supplier A now has only 2 gold packs." Any locked order that breaks the new stock limit shows the broken line in red with the word "Over stock".
Phase 3, Revise: teams unlock and fix the order. The before and after ledgers sit side by side.
Phase 4, Challenge: a "swap" view hides one team's totals and asks the other team two questions: "Is there enough of every item?" and "Are the whole packs right?"
A teacher panel (opened with a small gear and the word "Teacher") shows the answer key: before the change the all-A order costs $21.48 and the cheapest is $20.51 ($20.86 if mixing within an item is off); after the change the cheapest is $22.25 ($22.60 with mixing off). Keep the key hidden by default.
```

*Test it:* the all-A order shows $21.48; releasing the change flags any order with 3 A gold packs.

### G20. Pack Rounding Sprint

*Where it goes:* W4-G Solo recheck, and any week's warm-up. *Standard:* 6.RP.A.2 (whole packs).

```
Make a quick mini-game called "Pack Rounding Sprint".

Each round: "You need N items. Packs of P cost $X." The student enters packs, total cost and spare items. Then items fly into pack boxes, the last box shows the spares faded, and the cost adds up.
Start with: 7 items, packs of 4 at $1.20 → 2 packs, $2.40, 1 spare. Then random: N 5–60, P 3–18, prices in whole cents.
No timer; a streak counter only.

Feedback for likely mistakes:
- Rounds down (1 pack for 7 items) → show the missing items outlined: "Short by 3."
- Gives N ÷ P as a decimal (1.75 packs) → "You can only buy whole packs. Round UP."
```

*Test it:* 7 / 4 / $1.20 → 2, $2.40, 1; 11 / 4 / $1.50 → 3, $4.50, 1.

---

## Coverage

| Standard | Games |
| --- | --- |
| 6.RP.A.1 ratio language | G1, G18 |
| 6.RP.A.2 unit rate | G2, G6, G20 |
| 6.RP.A.3 tables, graphs, speed, percent, conversion | G7, G9, G10, G11, G12, G18, G19 |
| 6.NS.A.1 fraction division | G4 |
| 6.NS.B.2 whole-number division | G3 |
| 6.NS.B.3 decimal operations | G5, G8, G12, G17 |
| 6.NS.B.4 GCF, LCM, distributive | G13, G14, G15 |
| 6.EE.A.1 exponents | G16 |

## Before students use a game

- [ ] Every number in *Test it* gives the stated result.
- [ ] Each listed mistake gets its own feedback.
- [ ] Playable with the keyboard alone, and at phone width.
- [ ] Opens and plays from the Moodle File resource with the network turned off (fonts may fall back; nothing else should break).
- [ ] No game reveals the team's real 12- or 18-kit order.
