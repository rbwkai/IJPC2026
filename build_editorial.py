import csv
import json
import re
from pathlib import Path

PROBLEMS_CSV = Path("problems.csv")
CONTEST_JSON = Path("contest.json")
TUTORIALS_DIR = Path("Tutorials")
OUTPUT_FILE = Path("Editorial.md")

LINK_PATTERN = re.compile(r'(!?\[[^\]]*\]\()([^)]+)(\))')



def load_contest():
    with CONTEST_JSON.open(encoding="utf-8") as f:
        return json.load(f)


def load_problems():
    with PROBLEMS_CSV.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))



def fix_links(content: str, source_file: Path) -> str:
    source_dir = source_file.parent.resolve()
    root_dir = Path.cwd().resolve()

    def replace(match):
        prefix, target, suffix = match.group(1), match.group(2), match.group(3)

        if (
            target.startswith("http://")
            or target.startswith("https://")
            or target.startswith("#")
            or target.startswith("/")
        ):
            return match.group(0)

        resolved = (source_dir / target).resolve()

        try:
            relative = resolved.relative_to(root_dir)
        except ValueError:
            return match.group(0)

        return f"{prefix}{relative.as_posix()}{suffix}"

    return LINK_PATTERN.sub(replace, content)



def write_header(out, contest):
    out.write("<!-- AUTO-GENERATED FILE. DO NOT EDIT. -->\n\n")

    out.write(f"# Editorial for {contest.get('name', 'Unknown Contest')}\n\n")

    if contest.get("date"):
        out.write(f"**Date:** {contest['date']}\n\n")

    if contest.get("contest_link"):
        out.write(f"**Contest:** {contest['contest_link']}\n\n")

    contributors = contest.get("contributors", [])
    if contributors:
        out.write("## Contributors\n\n")
        out.write("| Name | Role |\n")
        out.write("|------|------|\n")

        for c in contributors:
            name = c.get("name", "Unknown")
            roles = c.get("roles", [])
            role = ", ".join(roles) if roles else c.get("role", "")

            if c.get("link"):
                name = f"[{name}]({c['link']})"

            out.write(f"| {name} | {role} |\n")

        out.write("\n")

def problem_anchor(pid: str) -> str:
    return f"problem-{pid.lower()}"

def write_toc(out, problems):
    out.write("## Problems\n\n")
    out.write("| Problem ID | Problem Title |\n")
    out.write("|------------|---------------|\n")

    for p in problems:
        pid = p["id"].strip()
        name = p["name"].strip()

        anchor = problem_anchor(pid)
        out.write(f"| {pid} | [{name}](#{anchor}) |\n")

    out.write("\n---\n\n")


def write_tutorials_header(out):
    out.write("# Tutorials\n\n")

def write_tutorial_item(out, problem_id, problem_name, content):
    anchor = problem_anchor(problem_id)

    out.write(f'<a id="{anchor}"></a>\n\n')

    out.write("<details>\n")
    out.write(f"<summary><strong>{problem_id}. {problem_name}</strong></summary>\n\n")
    out.write(content.rstrip())
    out.write("\n\n</details>\n\n")

def write_tutorials(out, problems, tutorials_dir):
    write_tutorials_header(out)

    for p in problems:
        pid = p["id"].strip()
        name = p["name"].strip()

        tutorial_file = tutorials_dir / f"{pid}.md"

        if tutorial_file.exists():
            content = tutorial_file.read_text(encoding="utf-8")
            content = fix_links(content, tutorial_file)
        else:
            content = "_Tutorial not available._"

        write_tutorial_item(out, pid, name, content)



def main():
    contest = load_contest()
    problems = load_problems()

    with OUTPUT_FILE.open("w", encoding="utf-8") as out:
        write_header(out, contest)
        write_toc(out, problems)
        write_tutorials(out, problems, TUTORIALS_DIR)

    print(f"Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    main()