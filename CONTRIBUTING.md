# getting started

## Setup

### Tools needed

- [Python 3.11](https://www.python.org/downloads/)
- [hatch](https://hatch.pypa.io/latest/)
- _(Optional) [mise](https://mise.jdx.dev/)_

### Installation

1. Install [hatch](https://hatch.pypa.io/latest/)
2. _(Optional)_ Install [mise](https://mise.jdx.dev/)

## Workflow

### While working

- Periodically run `hatch run lint:all` to lint all code and check for errors.
- Fix the issues which ruff or basedpyright report.

### Pre-Commit

1. Run `hatch run lint:fmt` to auto format all files.
2. Fix the issues which ruff or basedpyright report.
3. Run `hatch build --clean` to check if it builds correctly.
4. Commit changes.
