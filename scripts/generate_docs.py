#!/usr/bin/env python3
"""Generate docs/arn-list.md and docs/index.html from aws_arn_data."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from aws_arn import generate_markdown_table  # noqa: E402
from aws_arn.data import aws_arn_data  # noqa: E402

DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AWS ARN Reference</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, -apple-system, sans-serif; background: #f8f9fa; color: #212529; }

    header { background: #232f3e; color: #fff; padding: 1.5rem 2rem; }
    header h1 { font-size: 1.4rem; margin-bottom: 0.25rem; }
    .stats { font-size: 0.82rem; opacity: 0.65; margin-bottom: 1rem; }

    #search {
      width: 100%; max-width: 640px; padding: 0.6rem 1rem;
      font-size: 0.95rem; border: none; border-radius: 4px; outline: none;
    }

    .container { padding: 1rem 2rem 3rem; overflow-x: auto; }
    .meta { font-size: 0.82rem; color: #6c757d; margin-bottom: 0.6rem; }

    table {
      border-collapse: collapse; width: 100%; font-size: 0.78rem;
      background: #fff; border-radius: 6px; overflow: hidden;
      box-shadow: 0 1px 6px rgba(0,0,0,.08);
    }
    thead tr { background: #232f3e; color: #fff; }
    th { padding: 0.6rem 0.8rem; text-align: left; white-space: nowrap; font-weight: 600; }
    td { padding: 0.45rem 0.8rem; border-bottom: 1px solid #e9ecef; vertical-align: top; }
    tr:last-child td { border-bottom: none; }
    tr:hover td { background: #f1f3f5; }
    code {
      background: #e9ecef; padding: 0.1em 0.35em; border-radius: 3px;
      font-size: 0.72rem; word-break: break-all; font-family: monospace;
    }
    .hidden { display: none; }
    .badge {
      display: inline-block; padding: 0.15em 0.5em; border-radius: 3px;
      font-size: 0.7rem; white-space: nowrap; font-family: monospace;
    }
    .badge-tf   { background: #ede0f7; color: #6929a5; }
    .badge-cf   { background: #daedf7; color: #1a6fa0; }
    .badge-asff { background: #d5f5e3; color: #1a7a3c; }

    footer { text-align: center; font-size: 0.78rem; color: #aaa; padding: 1rem; }
    a { color: #0066cc; }
  </style>
</head>
<body>

<header>
  <h1>AWS ARN Reference</h1>
  <p class="stats">__SERVICES__ services &nbsp;·&nbsp; __TOTAL__ resources</p>
  <input id="search" type="search" placeholder="Filter by service, Terraform, CloudFormation, ASFF…" autofocus />
</header>

<div class="container">
  <p class="meta" id="count">Showing __TOTAL__ of __TOTAL__ resources</p>
  <table id="tbl">
    <thead>
      <tr>
        <th>Service</th>
        <th>Resource</th>
        <th>ARN Format</th>
        <th>ID Name</th>
        <th>ID Regexp</th>
        <th>ASFF Name</th>
        <th>CloudFormation</th>
        <th>Terraform</th>
      </tr>
    </thead>
    <tbody id="tbody"></tbody>
  </table>
</div>

<footer>
  Generated from <a href="https://github.com/gabrielsoltz/aws-arn">aws-arn</a>
  &nbsp;·&nbsp; <a href="arn-list.md">Download as Markdown</a>
</footer>

<script>
const DATA  = __DATA_JSON__;
const TOTAL = __TOTAL__;
const tbody  = document.getElementById('tbody');
const countEl = document.getElementById('count');

function esc(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function row(r) {
  return '<tr>'
    + '<td><strong>' + esc(r.service) + '</strong></td>'
    + '<td>' + esc(r.sub_service) + '</td>'
    + '<td><code>' + esc(r.arn_format) + '</code></td>'
    + '<td>' + esc(r.id_name) + '</td>'
    + '<td>' + (r.id_regexp ? '<code>' + esc(r.id_regexp) + '</code>' : '') + '</td>'
    + '<td>' + (r.asff_name ? '<span class="badge badge-asff">' + esc(r.asff_name) + '</span>' : '') + '</td>'
    + '<td>' + (r.cloudformation ? '<span class="badge badge-cf">' + esc(r.cloudformation) + '</span>' : '') + '</td>'
    + '<td>' + (r.terraform ? '<span class="badge badge-tf">' + esc(r.terraform) + '</span>' : '') + '</td>'
    + '</tr>';
}

function filter(q) {
  q = q.toLowerCase().trim();
  let shown = 0;
  tbody.innerHTML = DATA.map(r => {
    const hit = !q || Object.values(r).some(v => v.toLowerCase().includes(q));
    if (hit) shown++;
    return hit ? row(r) : '';
  }).join('');
  countEl.textContent = 'Showing ' + shown + ' of ' + TOTAL + ' resources';
}

document.getElementById('search').addEventListener('input', e => filter(e.target.value));
filter('');
</script>

</body>
</html>
"""


def generate_markdown() -> None:
    md = generate_markdown_table()
    path = DOCS / "arn-list.md"
    path.write_text(md, encoding="utf-8")
    print(f"Written {path}")


def generate_html() -> None:
    records = [
        {
            "service": service,
            "sub_service": sub_service,
            "arn_format": attrs.get("arn_format", ""),
            "id_name": attrs.get("id_name", ""),
            "id_regexp": attrs.get("id_regexp", ""),
            "asff_name": attrs.get("asff_name", ""),
            "cloudformation": attrs.get("cloudformation", ""),
            "terraform": attrs.get("terraform", ""),
        }
        for service, resources in aws_arn_data.items()
        for sub_service, attrs in resources.items()
    ]

    total = len(records)
    services = len(aws_arn_data)
    data_json = json.dumps(records, ensure_ascii=False)

    html = (
        HTML_TEMPLATE.replace("__DATA_JSON__", data_json)
        .replace("__TOTAL__", str(total))
        .replace("__SERVICES__", str(services))
    )

    path = DOCS / "index.html"
    path.write_text(html, encoding="utf-8")
    print(f"Written {path}")


if __name__ == "__main__":
    generate_markdown()
    generate_html()
    print("Done.")
