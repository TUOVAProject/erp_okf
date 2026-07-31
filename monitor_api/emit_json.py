"""
This is the programmatic view — everything the pipeline knows, in one file, for
code that wants to query the model rather than read prose.
"""

import json
import shutil

from .paths import BUILD_DIR, BUILD_TMP_DIR, MODEL_JSON


def emit(model: dict) -> None:
    """Write via a staging directory and swap, so a failed write cannot leave a
    truncated model.json where a valid one used to be."""
    if BUILD_TMP_DIR.exists():
        shutil.rmtree(BUILD_TMP_DIR)

    BUILD_TMP_DIR.mkdir(parents=True)
    (BUILD_TMP_DIR / MODEL_JSON.name).write_text(
        json.dumps(model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)

    BUILD_TMP_DIR.rename(BUILD_DIR)
