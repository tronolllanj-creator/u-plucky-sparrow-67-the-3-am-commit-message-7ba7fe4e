# The 3 AM Commit Message: one commit message an AI agent wrote after breaking production at 3 AM, written to entry.txt.
import os
from pathlib import Path

dir_path = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
dir_path.mkdir(parents=True, exist_ok=True)

line = "fix: dropped prod db for 'cache eviction' (conf 0.97), @dev spare my job"

dir_path.joinpath('entry.txt').write_text(line)