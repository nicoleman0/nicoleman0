"""Refresh all public, merged upstream PRs using GitHub's paginated API."""

import html
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
QUERY = """
query($login: String!, $endCursor: String) {
  user(login: $login) {
    pullRequests(states: MERGED, first: 100, after: $endCursor,
                 orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes {
        number title url mergedAt
        repository { nameWithOwner url isPrivate owner { login } }
      }
      pageInfo { hasNextPage endCursor }
    }
  }
}
"""


def fetch(login):
    result = subprocess.run(
        ["gh", "api", "graphql", "--paginate", "--slurp", "-f", f"query={QUERY}",
         "-f", f"login={login}"],
        check=True, capture_output=True, text=True,
    )
    pulls = []
    for page in json.loads(result.stdout):
        if page.get("errors"):
            raise RuntimeError(f"GitHub query failed: {page['errors']}")
        pulls.extend(page["data"]["user"]["pullRequests"]["nodes"])
    return [pr for pr in pulls if not pr["repository"]["isPrivate"]
            and pr["repository"]["owner"]["login"].casefold() != login.casefold()]


def render(pulls):
    groups = {}
    for pr in sorted(pulls, key=lambda pr: (pr["mergedAt"], pr["url"]), reverse=True):
        groups.setdefault(pr["repository"]["nameWithOwner"], []).append(pr)
    lines = [f"**{len(pulls)} merged PRs across {len(groups)} community projects.**",
             "", "All public merged PRs to repositories outside my account.", ""]
    for name, entries in groups.items():
        lines.extend([f"#### [{name}]({entries[0]['repository']['url']})", ""])
        for pr in entries:
            title = html.escape(pr["title"].replace("\n", " "))
            for character in "\\`*_[]|":
                title = title.replace(character, "\\" + character)
            lines.append(f"- [#{pr['number']}]({pr['url']}) {title}")
        lines.append("")
    return "\n".join(lines).rstrip()


def replace_section(text, name, content):
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"README must contain exactly one {name} marker pair")
    before, remaining = text.split(start)
    _, after = remaining.split(end)
    return f"{before}{start}\n{content}\n{end}{after}"


def main():
    readme = ROOT / "README.md"
    text = replace_section(readme.read_text(), "contributions", render(fetch("nicoleman0")))
    metrics = "![GitHub stats and notable contributions](github-metrics.svg)" if (ROOT / "github-metrics.svg").exists() else ""
    text = replace_section(text, "metrics", metrics)
    readme.write_text(text)


if __name__ == "__main__":
    main()
