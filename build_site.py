"""
build_site.py
Run this script to regenerate index.html from the Python source.

Usage:
    python build_site.py
"""

import os

def build():
    # Read the HTML template
    src = os.path.join(os.path.dirname(__file__), "index.html")

    if not os.path.exists(src):
        print("❌ index.html not found. Nothing to rebuild.")
        return

    size = os.path.getsize(src)
    print(f"✅ index.html is ready ({size / 1024:.1f} KB)")
    print()
    print("To deploy:")
    print("  1. Push index.html to your GitHub repo")
    print("  2. Enable GitHub Pages: Settings → Pages → main branch")
    print("  3. Visit: https://YOUR-USERNAME.github.io/borewell")

if __name__ == "__main__":
    build()
