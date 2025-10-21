# Security Status SVG Badge Generator
This Python program, `badgecreation.py`, generates a dynamic **Security Status** badge in SVG format. It's designed to visually represent the current count and trend (up, down, or stable) for different severity levels of security issues (Critical, High, Medium, Low).

This badge is ideal for use in project READMEs, dashboards, or any other web content where a quick, visual security summary is needed.

## ✨ Features

* **Color-Coded Severity:** Uses distinct colors for Critical (Red), High (Orange), Medium (Yellow), and Low (Green) issues.
* **Trend Indicators:** Displays an arrow symbol (`↑`, `↓`, `→`) next to the count to show the current trend.
* **Scalable Vector Graphics (SVG):** Generates high-quality, resolution-independent badges.
* **Simple Function Interface:** Easy to integrate into other Python-based reporting or build systems.

The generated badge will look something like this (though you'll need to embed the SVG content to view it):

| Label | Critical | High | Medium | Low |
| :---: | :---: | :---: | :---: | :---: |
| **Security Status** | **C: 10 ↑** | **H: 20 ↓** | **M: 30 →** | **L: 5 ↓** |

---

## 💻 API - `generate_security_badge_svg`

The core functionality is encapsulated in a single, self-contained function.

```python
def generate_security_badge_svg(
    critical_count: int,
    critical_trend: str,
    high_count: int,
    high_trend: str,
    medium_count: int,
    medium_trend: str,
    low_count: int,
    low_trend: str,
) -> str:
    # ... function implementation ...
