"""Build one BUILD_GUIDE.md per Grade 6 math project.

Reads the maintained math project teaching documents in
standards/scope-and-sequence/math-projects/ and writes a lesson build guide
into grade-6/math/project-N/. The guide keeps only what a teacher needs to
build the lessons: project overview, project data, materials to make, the
eight full lessons, the required learning per standard, and what remains to
build. Tennessee/Common Core comparisons, Forge IDs, match-review and audit
tables are left in the source documents.

Rerun after the project documents change:
    python3 standards/curriculum-build/project-build-guides/build_math_guides.py
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SOURCE_DIR = REPO / "standards" / "scope-and-sequence" / "math-projects"
OUTPUT_DIR = REPO / "grade-6" / "math"

PROJECTS = [
    ("project-1", "M1_SUPPLY_EXCHANGE.md"),
    ("project-2", "M2_COORDINATE_RESCUE.md"),
    ("project-3", "M3_FOLD_TO_FIT_CARGO.md"),
    ("project-4", "M4_DATA_CLAIMS_HEARING.md"),
]

# Source lesson field -> build-guide label, in output order.
LESSON_FIELDS = [
    ("Focus and project connection", "Focus and project connection"),
    ("Skills and prerequisite", "Skills taught and checked"),
    ("Resources and reading", "Resources and reading"),
    ("Teacher instruction and modeling", "Teach and model"),
    ("Activity design", "Activity steps"),
    ("Individual work to collect / assessment prompt", "Individual work to collect"),
    ("How this work is judged", "How the work is judged"),
    ("Difficulty: observable signal, response and fresh recheck", "If students struggle"),
    ("Preparation and handoff", "Prepare and hand off"),
    ("Mathematical practice", "Mathematical practice"),
    ("Sequential clock", "90-minute timeline"),
    ("Standards match", "Standards"),
]

# Project-level reference paragraphs kept under "How to run every lesson".
ROUTINE_FIELDS = [
    ("Reading/access plan", "Reading and access"),
    ("Assessment routine", "Recording evidence"),
    ("Response to difficulty and extension", "Support and extension"),
    ("Outside work", "Outside work"),
]

FIELD_RE = re.compile(r"^\*\*(.+?):\*\*\s*(.*)$")


def split_sections(text, level):
    """Split markdown into {heading: body} at the given heading level."""
    marker = "#" * level + " "
    sections, current, lines = {}, "_preamble", []
    for line in text.splitlines():
        if line.startswith(marker):
            sections[current] = "\n".join(lines).strip()
            current, lines = line[len(marker):].strip(), []
        else:
            lines.append(line)
    sections[current] = "\n".join(lines).strip()
    return sections


def fields(block):
    """Return {label: text} for **Label:** paragraphs; continuation lines join the field."""
    found, label = {}, None
    for line in block.splitlines():
        m = FIELD_RE.match(line)
        if m:
            label = m.group(1)
            found[label] = m.group(2).strip()
        elif label and line.strip() and not line.startswith(("[", "<a ", "#", "|")):
            found[label] += " " + line.strip()
        elif not line.strip():
            label = None
    return found


def standards_line(text):
    """Keep 'Primary: ... Supporting: ...' and drop the verification boilerplate."""
    primary = re.search(r"Primary:\s*([^.]+(?:\.[A-Z0-9][^.]*)*)\.", text)
    supporting = re.search(r"Supporting:\s*([^.]+(?:\.[A-Z0-9][^.]*)*)\.", text)
    parts = []
    if primary:
        parts.append(f"Primary {primary.group(1).strip()}")
    if supporting:
        parts.append(f"supporting {supporting.group(1).strip()}")
    return "; ".join(parts) + "." if parts else text


def numbered_steps(text):
    """Turn '1. a 2. b' run-on activity text into a markdown list."""
    steps = re.split(r"\s*(?=\b\d\.\s)", text)
    steps = [s.strip() for s in steps if s.strip()]
    if len(steps) < 2 or not steps[0][:1].isdigit():
        return text
    return "\n" + "\n".join(steps)


def timeline(text):
    """Turn '0-10: a; 10-30: b; ... Total 90 minutes.' into a table."""
    body = re.sub(r"\s*Total 90 minutes\.?\s*$", "", text)
    rows = []
    for part in (p.strip() for p in body.split(";")):
        m = re.match(r"^(\d+-\d+):\s*(.*)$", part)
        if m:
            rows.append([m.group(1), m.group(2)])
        elif rows and part:
            rows[-1][1] += "; " + part  # note that belongs to the previous time slot
    if not rows:
        return text
    out = ["", "", "| Minutes | Activity |", "| --- | --- |"]
    for mins, act in rows:
        out.append(f"| {mins} | {act.rstrip('.')} |")
    return "\n".join(out)


def standards_table(block, project_id):
    """Keep standard code, required learning and lessons; drop Forge IDs and course role."""
    out = ["| Standard | What students must learn | Lessons |", "| --- | --- | --- |"]
    for line in block.splitlines():
        if not line.startswith("| FF."):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        code = cells[0].split("/")[-1].strip()
        lessons = ", ".join(
            f"[{lid}](#{lid.lower()})" for lid in re.findall(r"M\d-W\d-[IG]", cells[2])
        )
        out.append(f"| {code} | {cells[1]} | {lessons} |")
    return "\n".join(out)


def build(project_dir, source_name):
    text = (SOURCE_DIR / source_name).read_text(encoding="utf-8")
    top = split_sections(text, 2)
    title = re.search(r"^# (.+)$", text, re.M).group(1).replace("Grade 6 Math - ", "")
    project_id = title.split()[0]
    head = fields(top["_preamble"])

    reference = split_sections(top["Teacher reference and resources"], 3)
    brief = reference["Project design brief"]
    materials_block = reference["Materials to build in Step 6"]
    materials = [
        p.strip()
        for p in materials_block.split("\n\n")
        if p.strip() and not p.startswith(("**", "All examples"))
    ]
    no_login = "No outside website login or paid reading is required." in materials_block
    routines = fields(materials_block)

    lessons = split_sections(top["Lessons"], 3)
    lesson_ids = [h for h in lessons if re.match(r"M\d-W\d-[IG] ", h)]
    if len(lesson_ids) != 8:
        raise SystemExit(f"{source_name}: expected 8 lessons, found {len(lesson_ids)}")

    md = [
        f"# Grade 6 Math – {title}: Lesson Build Guide",
        "",
        f"Project {project_dir[-1]} of 4 · four weeks · eight 90-minute lessons (one individual, then one group, each week).",
        "",
        f"Built from the [{project_id} teacher plan](../../../standards/scope-and-sequence/math-projects/{source_name}). "
        "Rerun `standards/curriculum-build/project-build-guides/build_math_guides.py` after that plan changes; do not edit this file by hand.",
        "",
        "## Project overview",
        "",
        f"**Essential question:** {head['Essential question']}",
        "",
        f"**What students do:** {head['Project at a glance']}",
        "",
        f"**Final product:** {head['Final product']}",
        "",
        f"**What good work shows:** {head['What good work shows']}",
        "",
        "## Project data",
        "",
        "Use these exact numbers when building cards, keys and examples.",
        "",
        brief,
        "",
        "## Materials to make",
        "",
        "None of these exist yet; each must be built and answer-checked before teaching. "
        "All project numbers are in **Project data** above"
        + ("; no outside website login or paid reading is required." if no_login else "."),
        "",
        *[p + "\n" for p in materials],
        "## How to run every lesson",
        "",
    ]
    for src, label in ROUTINE_FIELDS:
        if src in routines:
            md += [f"**{label}:** {routines[src]}", ""]

    md += ["## Four-week sequence", "", top["Four-week sequence"], "", "## Lessons", ""]
    for heading in lesson_ids:
        lid, name = heading.split(" - ", 1)
        body = lessons[heading]
        week_line = next((l for l in body.splitlines() if l.startswith("**Week")), "").strip("*. ")
        f = fields(body)
        md += [f'<a id="{lid.lower()}"></a>', f"### {lid} — {name}", "", f"*{week_line}*", ""]
        for src, label in LESSON_FIELDS:
            value = f.get(src)
            if value is None:
                raise SystemExit(f"{source_name} {lid}: missing field '{src}'")
            if src == "Activity design":
                value = numbered_steps(value)
            elif src == "Sequential clock":
                value = timeline(value)
            elif src == "Standards match":
                value = standards_line(value)
            md += [f"**{label}:** {value}", ""]

    md += [
        "## What each standard requires",
        "",
        "Every part listed here must be taught and checked somewhere in the eight lessons.",
        "",
        standards_table(top["Standards component and recurrence routes"], project_id),
        "",
        "## Still to do before teaching",
        "",
        f"- {top['Step 6 handoff']}",
        "- Pacing has not been trialed. The sequence assumes grade-level entry skills; if they are weak, extra class time must be scheduled rather than moved to homework.",
        "- Confirm class size, accommodations and the actual school calendar.",
        "",
    ]

    out = OUTPUT_DIR / project_dir
    out.mkdir(parents=True, exist_ok=True)
    placeholder = out / "README.md"
    if placeholder.exists():
        placeholder.unlink()
    (out / "BUILD_GUIDE.md").write_text("\n".join(md), encoding="utf-8")
    print(f"wrote {out.relative_to(REPO)}/BUILD_GUIDE.md")


if __name__ == "__main__":
    for project_dir, source_name in PROJECTS:
        build(project_dir, source_name)
