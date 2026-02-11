#!/usr/bin/env python3
"""Generate icon for Dirty Git Finder - GitHub style"""

from PIL import Image, ImageDraw, ImageFont
import os
import math

def create_icon():
    # Create a 256x256 image with dark background (GitHub style)
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw circular background - dark like GitHub
    margin = 10
    bg_color = '#24292e'  # GitHub dark color
    draw.ellipse([margin, margin, size - margin, size - margin], fill=bg_color)

    # Draw a Git branch icon in the center (simplified)
    center_x, center_y = size // 2, size // 2

    # Draw git branches (white, GitHub style)
    branch_color = '#ffffff'

    # Main vertical line (trunk)
    trunk_x = center_x - 20
    draw.ellipse([trunk_x - 12, center_y - 60 - 12, trunk_x + 12, center_y - 60 + 12],
                 fill=branch_color)
    draw.rectangle([trunk_x - 6, center_y - 60, trunk_x + 6, center_y + 50],
                   fill=branch_color)
    draw.ellipse([trunk_x - 12, center_y + 50 - 12, trunk_x + 12, center_y + 50 + 12],
                 fill=branch_color)

    # Branch to the right
    branch_x = center_x + 35
    branch_y = center_y - 15

    # Draw branch line
    draw.line([trunk_x, center_y - 10, branch_x, branch_y],
              fill=branch_color, width=12)

    # Draw branch node
    draw.ellipse([branch_x - 12, branch_y - 12, branch_x + 12, branch_y + 12],
                 fill=branch_color)

    # Add flame indicator (orange/red for "dirty") - similar to notification badge
    flame_color = '#ff6b35'
    flame_x = size - 50
    flame_y = 50

    # Draw flame as a badge
    draw.ellipse([flame_x - 25, flame_y - 25, flame_x + 25, flame_y + 25],
                 fill=flame_color)

    # Add exclamation mark or fire symbol
    try:
        font_size = 35
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", font_size)
            except:
                font = ImageFont.load_default()

        # Draw "!" in white on the badge
        text = "!"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        text_x = flame_x - text_width // 2 - bbox[0]
        text_y = flame_y - text_height // 2 - bbox[1]

        draw.text((text_x, text_y), text, fill='white', font=font)
    except Exception as e:
        print(f"Font error: {e}")

    # Save as PNG
    icon_path = os.path.join(os.path.dirname(__file__), 'app_icon.png')
    img.save(icon_path, 'PNG')
    print(f"Icon created: {icon_path}")

    # Also create smaller versions
    for size_small in [128, 64, 32, 16]:
        img_small = img.resize((size_small, size_small), Image.Resampling.LANCZOS)
        icon_small_path = os.path.join(os.path.dirname(__file__), f'app_icon_{size_small}.png')
        img_small.save(icon_small_path, 'PNG')

    return icon_path

if __name__ == '__main__':
    create_icon()
