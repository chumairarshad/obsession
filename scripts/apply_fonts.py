import re

with open('src/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add Google fonts import at the very top if not present
import_rule = "@import url('https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,300..900;1,300..900&family=Passion+One:wght@400;700;900&family=Playfair+Display:wght@600;700;800&family=Tajawal:wght@400;500;700;800&display=swap');\n\n"

if "@import url('https://fonts.googleapis.com" not in css:
    css = import_rule + css

# 2. Add font variables to :root
if "--font-title" not in css:
    css = css.replace(
        "--ser:'Playfair Display',Georgia,serif;",
        "--ser:'Playfair Display',Georgia,serif;\n  --font-title:'Passion One', 'Tajawal', system-ui, sans-serif;\n  --font-body:'Figtree', 'Tajawal', system-ui, -apple-system, sans-serif;\n  --font-product:'Figtree', 'Tajawal', system-ui, -apple-system, sans-serif;"
    )

# 3. Update body font
css = re.sub(
    r'body\{font-family:[^;]+;',
    "body{font-family:var(--font-body);",
    css
)

# 4. Update titles:
# .hero-content h1
css = re.sub(
    r'\.hero-content h1\{[^}]+\}',
    ".hero-content h1{font-family:var(--font-title);font-size:clamp(34px,5.5vw,66px);line-height:1.04;font-weight:700;letter-spacing:0.02em;text-transform:uppercase;margin:10px 0 14px}",
    css
)

# .hd h2
css = re.sub(
    r'\.hd h2\{[^}]+\}',
    ".hd h2{font-family:var(--font-title);font-size:28px;font-weight:700;letter-spacing:0.02em;line-height:1.1}",
    css
)

# .trust h2
css = re.sub(
    r'\.trust h2\{[^}]+\}',
    ".trust h2{font-family:var(--font-title);font-size:28px;font-style:normal;font-weight:700;letter-spacing:0.02em;margin-bottom:10px}",
    css
)

# .bn h3
css = re.sub(
    r'\.bn h3\{[^}]+\}',
    ".bn h3{font-family:var(--font-title);font-size:28px;font-weight:700;letter-spacing:0.02em;line-height:1.15}",
    css
)

# .news h2
css = re.sub(
    r'\.news h2\{[^}]+\}',
    ".news h2{font-family:var(--font-title);font-size:30px;font-weight:700;letter-spacing:0.02em}",
    css
)

# .cl h1
css = re.sub(
    r'\.cl h1\{[^}]+\}',
    ".cl h1{font-family:var(--font-title);font-size:32px;font-weight:700;letter-spacing:0.02em}",
    css
)

# .sig h2
css = re.sub(
    r'\.sig h2\{[^}]+\}',
    ".sig h2{font-family:var(--font-title);font-size:clamp(34px,4.5vw,56px);font-weight:700;letter-spacing:0.02em;margin:10px 0}",
    css
)

# .stats b
css = re.sub(
    r'\.stats b\{[^}]+\}',
    ".stats b{font-family:var(--font-title);display:block;font-size:40px;color:var(--gold);font-weight:700;letter-spacing:0.02em}",
    css
)

# .post-body h1
css = css.replace(
    ".post-body{",
    ".post-body h1{font-family:var(--font-title);font-weight:700;letter-spacing:0.02em}\n.post-body{"
)

# 5. Product elements typography with Figtree
product_typography_css = """
/* ==========================================================================
   Product Typography (Figtree, Sans-Serif)
   ========================================================================== */
.pc h3 {
  font-family: var(--font-product) !important;
  font-weight: 600 !important;
  font-size: 14px !important;
  line-height: 1.35 !important;
  margin: 3px 0 6px !important;
  letter-spacing: normal !important;
}
.pc small {
  font-family: var(--font-product) !important;
  font-weight: 500 !important;
  font-size: 10.5px !important;
  letter-spacing: 0.05em !important;
  text-transform: uppercase !important;
}
.pc .pr {
  font-family: var(--font-product) !important;
  font-weight: 700 !important;
  font-size: 15px !important;
}
.pc .qa {
  font-family: var(--font-product) !important;
  font-weight: 600 !important;
}

/* Product Detail Page (Figtree, Sans-Serif) */
.pd h1 {
  font-family: var(--font-product) !important;
  font-size: 26px !important;
  font-weight: 700 !important;
  line-height: 1.25 !important;
  letter-spacing: normal !important;
}
.pd small {
  font-family: var(--font-product) !important;
  font-size: 13px !important;
  font-weight: 500 !important;
}
.pd .p {
  font-family: var(--font-product) !important;
  font-size: 24px !important;
  font-weight: 800 !important;
}
.pd p,
.pd .bx,
.pd .ar,
.acc,
.acc button,
.acc div,
.rv {
  font-family: var(--font-product) !important;
}
.ci b,
.ci small,
.ci .pr,
.dw .pr {
  font-family: var(--font-product) !important;
}
"""

if "Product Typography (Figtree, Sans-Serif)" not in css:
    css += "\n" + product_typography_css

# 6. RTL rules update
old_rtl = "[dir=rtl] body,[dir=rtl] button,[dir=rtl] input,[dir=rtl] select,[dir=rtl] textarea,[dir=rtl] .logo,[dir=rtl] .hd h2,[dir=rtl] .hero-content h1,[dir=rtl] .cl h1,[dir=rtl] .pd h1,[dir=rtl] .trust h2,[dir=rtl] .sig h2,[dir=rtl] .news h2,[dir=rtl] .bn h3,[dir=rtl] .q p,[dir=rtl] .stats b{font-family:Tajawal,Inter,sans-serif}"
new_rtl = """[dir=rtl] body,[dir=rtl] button,[dir=rtl] input,[dir=rtl] select,[dir=rtl] textarea{font-family:'Figtree','Tajawal',sans-serif}
[dir=rtl] .hero-content h1,[dir=rtl] .hd h2,[dir=rtl] .trust h2,[dir=rtl] .bn h3,[dir=rtl] .news h2,[dir=rtl] .cl h1,[dir=rtl] .sig h2,[dir=rtl] .post-body h1,[dir=rtl] .stats b{font-family:'Passion One','Tajawal',sans-serif}
[dir=rtl] .pc h3,[dir=rtl] .pd h1,[dir=rtl] .pc .pr,[dir=rtl] .pd .p,[dir=rtl] .pd p,[dir=rtl] .acc,[dir=rtl] .ci b,[dir=rtl] .ci .pr{font-family:'Figtree','Tajawal',sans-serif!important}"""

if old_rtl in css:
    css = css.replace(old_rtl, new_rtl)

with open('src/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("styles.css updated with Passion One & Figtree successfully!")
