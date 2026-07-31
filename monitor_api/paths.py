"""Repo-anchored paths.

Every path is derived from this file's location, so the pipeline can be run from
any working directory (the old scripts all used bare relative paths and only
worked when CWD happened to be the repo root).
"""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Stage 1 output (raw scrape cache) — also stage 2 input.
HTML_DIR = REPO_ROOT / "html"
ENDPOINT_INDEX = REPO_ROOT / "endpoint_index.json"

# Generated artifacts. Both are rebuilt from scratch by build.py.
BUILD_DIR = REPO_ROOT / "build"
MODEL_JSON = BUILD_DIR / "model.json"
OKF_DIR = REPO_ROOT / "okf"

# Staging directories. Emitters write here and swap on success, so a crash
# mid-emit leaves the previous good output in place instead of a half-written
# bundle where a complete one used to be.
BUILD_TMP_DIR = REPO_ROOT / "build.tmp"
OKF_TMP_DIR = REPO_ROOT / "okf.tmp"

# Recorded stats floor; validate() fails if a build drops below it.
BASELINE_JSON = REPO_ROOT / "baseline.json"
