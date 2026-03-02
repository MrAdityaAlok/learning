from typing import Dict, List
from github_lang_colors import get_lang_color
import math

VIEWBOX_WIDTH = 700

HEADING_FONT_SIZE = 20
FONT_SIZE = 14
LINE_HEIGHT = 1.2
LONGEST_TEXT_LENGTH = 80

BAR_WIDTH = VIEWBOX_WIDTH * 0.5  # 50%
BAR_HEIGHT = 18
BAR_RADIUS = 4

# The inner rectangle where we start drawing.
# There is a padding of 40 from top,bottom and 20 from right,left.
PADDING_X = 20
PADDING_Y = 40

# Gap between each row.
ROW_GAP = 35

_BAR_ROW_GAP = 10  # Gap between bar row elements.
_BAR_ROW_START_X = PADDING_X
_BAR_RECT_START_X = _BAR_ROW_START_X + LONGEST_TEXT_LENGTH + _BAR_ROW_GAP
_BAR_ROW_START_Y = PADDING_Y + HEADING_FONT_SIZE * LINE_HEIGHT + ROW_GAP


def calculate_text_y_position(y: float) -> float:
    return (
        y + BAR_HEIGHT / 2 + FONT_SIZE / 3
    )  # improved version of: y + FONT_SIZE + (BAR_HEIGHT - FONT_SIZE / 2)


def render_bar(label: str, percent: float, color: str, index: int) -> str:
    fill_width = int(percent / 100 * BAR_WIDTH)

    y = _BAR_ROW_START_Y + index * ROW_GAP

    # y+{FONT_SIZE} in text because it starts from baseline.
    return f"""
  <text x="{_BAR_ROW_START_X}" y="{calculate_text_y_position(y)}" class="label">{label} :</text>

  <rect x="{_BAR_RECT_START_X}" y="{y}" width="{BAR_WIDTH}" height="{BAR_HEIGHT}"
        rx="{BAR_RADIUS}" ry="{BAR_RADIUS}" class="bar-bg"/>

  <rect x="{_BAR_RECT_START_X}" y="{y}" width="0" height="{BAR_HEIGHT}"
        rx="{BAR_RADIUS}" ry="{BAR_RADIUS}"
        fill="{color}">
    <animate attributeName="width"
             from="0"
             to="{fill_width}"
             dur="1.5s"
             fill="freeze"
             calcMode="spline"
             keySplines="0.4 0 0.2 1"
             keyTimes="0;1"/>
  </rect>

  <text x="{_BAR_RECT_START_X + BAR_WIDTH + _BAR_ROW_GAP}" y="{calculate_text_y_position(y)}"
        class="progress-text">{percent:.2f}%</text>
"""


def generate_svg(title: str, bars: List[Dict]) -> str:
    """
    bars = [
        {"label": "Python", "percent": 82},
        {"label": "C++", "percent": 65},
        {"label": "Go", "percent": 48}
    ]
    """

    width = math.ceil(
        PADDING_X  # right padding
        + LONGEST_TEXT_LENGTH
        + _BAR_ROW_GAP
        + BAR_WIDTH
        + _BAR_ROW_GAP
        + 60  # This 60 is for max percentage: "100.00%"
        + PADDING_X  # left padding
    )

    height = math.ceil(
        PADDING_Y  # top padding
        + HEADING_FONT_SIZE * LINE_HEIGHT
        + ROW_GAP  # gap after heading
        + len(bars) * ROW_GAP  # each row spaced by ROW_GAP
        + PADDING_Y  # bottom padding
    )

    bars_svg = "".join(
        render_bar(bar["label"], bar["percent"], get_lang_color(bar["label"]), i)
        for i, bar in enumerate(bars)
    )

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">

  <style>
    :root {{
      --bg: #e5e7eb;
      --text: #111827;
      --subtext: #374151;
    }}

    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #2a2f3a;
        --text: #f3f4f6;
        --subtext: #9ca3af;
      }}
    }}

    .heading {{
      font-family: sans-serif;
      font-size: {HEADING_FONT_SIZE}px;
      font-weight: 600;
      fill: var(--text);
    }}

    .label, .progress-text {{
      font-family: sans-serif;
      font-size: {FONT_SIZE}px;
      fill: var(--subtext);
    }}

    .bar-bg {{
      fill: var(--bg);
    }}
  </style>

  <text x="{PADDING_X}" y="{PADDING_Y}" class="heading">{title}</text>

  {bars_svg}

</svg>"""
