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
    """
    Generate an SVG badge showing security status with color-coded severity levels.

    Args:
        critical_count: Number of critical issues
        critical_trend: Trend direction ("up", "down", or "stable")
        high_count: Number of high severity issues
        high_trend: Trend direction
        medium_count: Number of medium severity issues
        medium_trend: Trend direction
        low_count: Number of low severity issues
        low_trend: Trend direction

    Returns:
        SVG string representing the security status badge
    """

    # Color definitions
    colors = {
        "critical": "#e05d44",  # Red
        "high": "#fe7d37",  # Orange
        "medium": "#dfb317",  # Yellow
        "low": "#97ca00",  # Green
        "label": "#555555",  # Gray for label
    }

    # Arrow symbols
    arrows = {"up": "↑", "down": "↓", "stable": "→"}

    # Prepare data for each severity level
    levels = [
        ("C", critical_count, critical_trend, colors["critical"]),
        ("H", high_count, high_trend, colors["high"]),
        ("M", medium_count, medium_trend, colors["medium"]),
        ("L", low_count, low_trend, colors["low"]),
    ]

    # Calculate dimensions
    label_width = 110
    box_width = 60
    total_width = label_width + (box_width * len(levels))
    height = 20

    # Start building SVG
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="{height}">
    <linearGradient id="smooth" x2="0" y2="100%">
        <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
        <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    
    <clipPath id="round">
        <rect width="{total_width}" height="{height}" rx="3" fill="#fff"/>
    </clipPath>
    
    <g clip-path="url(#round)">
        <!-- Label section -->
        <rect width="{label_width}" height="{height}" fill="{colors['label']}"/>
        <rect x="{label_width}" width="{box_width * len(levels)}" height="{height}" fill="{colors['critical']}"/>
        <rect width="{total_width}" height="{height}" fill="url(#smooth)"/>
    </g>
    
    <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">
        <!-- Label text -->
        <text x="{label_width / 2}" y="14" fill="#fff">Security Status</text>
"""

    # Add each severity level box
    x_position = label_width
    for i, (label, count, trend, color) in enumerate(levels):
        # Add colored rectangle for this level
        if i > 0:
            svg += f'        <rect x="{x_position}" width="{box_width}" height="{height}" fill="{color}"/>\n'

        # Add text with count and trend arrow
        arrow = arrows.get(trend.lower(), "→")
        text_x = x_position + (box_width / 2)
        svg += f'        <text x="{text_x}" y="14" fill="#fff">{label}: {count} {arrow}</text>\n'

        x_position += box_width

    svg += """    </g>
</svg>"""

    return svg


if __name__ == "__main__":
    print("Starting badge generation...")

    try:
        svg_output = generate_security_badge_svg(
            critical_count=10,
            critical_trend="up",
            high_count=20,
            high_trend="down",
            medium_count=30,
            medium_trend="stable",
            low_count=5,
            low_trend="down",
        )

        print("SVG content generated successfully!")
        print(f"SVG length: {len(svg_output)} characters")

        # Save to file
        with open("security_badge.svg", "w", encoding="utf-8") as f:
            f.write(svg_output)

        print("✓ SVG badge saved to security_badge.svg")
        print("\nFirst 200 characters of SVG:")
        print(svg_output[:200])

    except Exception as e:
        print(f"ERROR: {e}")
        import traceback

        traceback.print_exc()
