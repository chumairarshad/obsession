with open('src/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Refine logo CSS
old_logo_css = """.logo-stripes {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 38px;
  height: 22px;
  flex-shrink: 0;
}
.logo-stripes span {
  display: block;
  width: 100%;
  height: 2.6px;
  background-color: var(--fg);
  border-radius: 1px;
}
.logo-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1;
}
.logo-en {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-weight: 800;
  font-size: 19px;
  letter-spacing: 0.08em;
  color: var(--fg);
  text-transform: uppercase;
}
.logo-ar {
  font-family: 'Amiri', 'Segoe UI', Tahoma, Arial, sans-serif;
  font-weight: 700;
  font-size: 12.5px;
  letter-spacing: 0.04em;
  color: var(--fg);
  margin-top: 2px;
  direction: rtl;
}"""

new_logo_css = """.logo-stripes {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 44px;
  height: 23px;
  flex-shrink: 0;
}
.logo-stripes span {
  display: block;
  width: 100%;
  height: 2px;
  background-color: var(--fg);
  border-radius: 0.5px;
}
.logo-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1;
  text-align: left;
}
[dir=rtl] .logo-text {
  text-align: right;
}
.logo-en {
  font-family: var(--ser);
  font-weight: 800;
  font-size: 20px;
  letter-spacing: 0.12em;
  color: var(--fg);
  text-transform: uppercase;
  line-height: 1;
}
.logo-ar {
  font-family: 'Amiri', 'Segoe UI', Tahoma, Arial, sans-serif;
  font-weight: 700;
  font-size: 13.5px;
  letter-spacing: 0.08em;
  color: var(--fg);
  margin-top: 3px;
  line-height: 1;
  text-align: left;
}
[dir=rtl] .logo-ar {
  text-align: right;
}"""

if old_logo_css in css:
    css = css.replace(old_logo_css, new_logo_css)
else:
    print("Warning: old_logo_css not found")

# Top left gap
css = css.replace(".top-left {\n  display: flex;\n  align-items: center;\n  gap: 14px;\n}", ".top-left {\n  display: flex;\n  align-items: center;\n  gap: 20px;\n}")

# Cart button styling
old_cart_css = """.hdr-cart-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1.5px solid var(--line);
  background: var(--bg);
  display: grid;
  place-items: center;
  position: relative;
  color: var(--fg);
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, background-color 0.2s;
}"""

new_cart_css = """.hdr-cart-btn {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1.5px solid var(--top-line);
  background: var(--card);
  display: grid;
  place-items: center;
  position: relative;
  color: var(--fg);
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, background-color 0.2s;
}"""

if old_cart_css in css:
    css = css.replace(old_cart_css, new_cart_css)

with open('src/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS refined successfully!")
