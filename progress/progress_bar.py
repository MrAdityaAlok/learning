from typing import Dict, List
import progress
from svg import generate_svg


def generate_progress_bars_mapping() -> List[Dict]:
    bars = []
    for lang, progress_percentage in progress.get_progress():
        bars.append({"label": lang, "percent": progress_percentage})
    return bars


if __name__ == "__main__":
    with open("../assets/exercism_progress.svg", "w") as f:
        f.write(generate_svg("Exercism Progress", generate_progress_bars_mapping()))
