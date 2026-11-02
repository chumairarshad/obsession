css_code = """/* ==========================================================================
   Obsession 3-Tier Header System (Ref. Screenshot Match)
   ========================================================================== */

/* Tier 1: Top Announcement Bar */
.top-bar {
  background: var(--top-bg);
  color: var(--top-fg);
  font-size: 12px;
  line-height: 1;
  border-bottom: 1px solid var(--top-line);
}
.top-bar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 32px;
  gap: 16px;
}
.top-left {
  display: flex;
  align-items: center;
  gap: 14px;
}
.top-left a {
  color: var(--mut);
  text-decoration: none;
  font-size: 12px;
  font-weight: 400;
  cursor: pointer;
  transition: color 0.15s;
}
.top-left a:hover {
  color: var(--acc);
}
.top-sep {
  display: inline-block;
  width: 1px;
  height: 10px;
  background: var(--top-line);
}
.top-center {
  font-size: 12px;
  font-weight: 600;
  color: var(--fg);
  letter-spacing: 0.02em;
  text-align: center;
  white-space: nowrap;
}
.top-right {
  display: flex;
  align-items: center;
  gap: 18px;
}
.top-lang-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  background: none;
  border: none;
  color: var(--top-fg);
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  padding: 0;
  transition: color 0.15s;
}
.top-lang-btn:hover {
  color: var(--acc);
}
.top-chev {
  display: flex;
  align-items: center;
  color: var(--mut);
}
.top-socials {
  display: flex;
  align-items: center;
  gap: 10px;
}
.top-socials a {
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--fg);
  transition: color 0.15s, transform 0.15s;
  padding: 2px;
}
.top-socials a:hover {
  color: var(--acc);
  transform: translateY(-1px);
}

/* Tier 2: Main Brand Header */
.hdr-master {
  position: sticky;
  top: env(safe-area-inset-top, 0px);
  background: var(--bg);
  z-index: 40;
  border-bottom: 1px solid var(--line);
}
.main-header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 12px 20px;
}
.burger-btn {
  display: none;
  width: 36px;
  height: 36px;
  border-radius: 8px;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  color: var(--fg);
  background: none;
  border: none;
  cursor: pointer;
}
.burger-btn:hover {
  background: var(--card);
}

/* Brand Logo (5 horizontal stripes + bold text + Arabic) */
.brand-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  cursor: pointer;
  flex-shrink: 0;
  user-select: none;
}
.logo-stripes {
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
}
.logo-acc {
  color: var(--acc);
}

/* Extended Pill Search Bar */
.pill-search {
  flex: 1;
  max-width: 580px;
  height: 42px;
  background: var(--search-bg);
  border-radius: 9999px;
  display: flex;
  align-items: center;
  padding: 0 8px 0 20px;
  border: 1px solid transparent;
  transition: border-color 0.2s, background-color 0.2s;
  margin: 0 auto;
}
.pill-search:focus-within {
  border-color: var(--line);
  background: var(--bg);
  box-shadow: 0 0 0 3px rgba(193, 18, 31, 0.08);
}
.pill-search input {
  flex: 1;
  border: none;
  background: transparent;
  outline: none;
  font-size: 13.5px;
  color: var(--fg);
  min-width: 0;
  padding: 0;
}
.pill-search input::placeholder {
  color: var(--mut);
  font-size: 13.5px;
}
.pill-search-btn {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  color: var(--mut);
  background: none;
  border: none;
  cursor: pointer;
  transition: color 0.15s;
  flex-shrink: 0;
}
.pill-search-btn:hover {
  color: var(--acc);
}

/* Header Action Items (Find a store, Sign in, Wishlist, Cart) */
.hdr-actions {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-shrink: 0;
}
.hdr-action-link {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 13px;
  font-weight: 500;
  color: var(--fg);
  text-decoration: none;
  cursor: pointer;
  transition: color 0.15s;
  white-space: nowrap;
}
.hdr-action-link:hover {
  color: var(--acc);
}
.hdr-action-link svg {
  flex-shrink: 0;
}

.hdr-icon-btn {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  position: relative;
  color: var(--fg);
  cursor: pointer;
  transition: color 0.15s, background-color 0.15s;
}
.hdr-icon-btn:hover {
  background: var(--card);
  color: var(--acc);
}

/* Cart Button (Circular Outline Container) */
.hdr-cart-btn {
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
}
.hdr-cart-btn:hover {
  border-color: var(--acc);
  color: var(--acc);
  background: var(--card);
}

.hdr-badge {
  position: absolute;
  top: -2px;
  right: -2px;
  background: var(--acc);
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  min-width: 17px;
  height: 17px;
  border-radius: 9px;
  display: grid;
  place-items: center;
  padding: 0 3px;
  box-shadow: 0 0 0 2px var(--bg);
}

/* Mobile search row container */
.mobile-search-row {
  display: none;
  padding: 0 14px 10px;
}

/* Tier 3: Category Navigation Bar */
.nav-tier {
  background: var(--bg);
  border-top: 1px solid var(--line);
}
.nav-inner {
  display: flex;
  align-items: center;
  gap: 22px;
  padding: 9px 20px 10px;
  max-width: 1240px;
  margin: 0 auto;
  overflow-x: auto;
  white-space: nowrap;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}
.nav-inner::-webkit-scrollbar {
  display: none;
}
.nav-link {
  font-size: 12.5px;
  font-weight: 500;
  color: var(--fg);
  text-decoration: none;
  cursor: pointer;
  transition: color 0.15s;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.nav-link:hover {
  color: var(--acc);
}
.nav-red {
  color: var(--acc) !important;
  font-weight: 600 !important;
}
.nav-sparkle {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 3px;
}
.sparkle-ic {
  color: var(--acc);
  margin-bottom: 5px;
  flex-shrink: 0;
}

/* Navigation Dropdowns */
.nav-dropdown-wrap {
  position: relative;
  display: inline-flex;
  align-items: center;
}
.nav-drop-ic {
  display: inline-flex;
  align-items: center;
  color: var(--mut);
  margin-top: 1px;
}
.nav-dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  min-width: 210px;
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 8px 0;
  box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.06);
  display: none;
  flex-direction: column;
  z-index: 100;
}
.nav-dropdown-wrap:hover .nav-dropdown-menu {
  display: flex;
}
.nav-dropdown-menu a {
  padding: 8px 18px;
  font-size: 13px;
  font-weight: 500;
  color: var(--fg);
  text-decoration: none;
  transition: background-color 0.15s, color 0.15s;
}
.nav-dropdown-menu a:hover {
  background: var(--card);
  color: var(--acc);
}

.mobile-menu-extras {
  display: none;
}

/* RTL Specific Overrides */
[dir=rtl] .top-left {
  direction: rtl;
}
[dir=rtl] .pill-search {
  padding: 0 20px 0 8px;
}
[dir=rtl] .hdr-badge {
  right: auto;
  left: -2px;
}
[dir=rtl] .nav-dropdown-menu {
  left: auto;
  right: 0;
}
[dir=rtl] .sparkle-ic {
  margin-right: 2px;
  margin-left: 0;
}

/* Mobile & Tablet Responsive Behavior */
@media(max-width: 960px) {
  .top-left {
    display: none;
  }
  .top-socials {
    display: none;
  }
  .top-bar-inner {
    justify-content: space-between;
    padding: 0 14px;
    height: 30px;
  }
  .top-center {
    font-size: 11px;
    flex: 1;
    text-align: center;
  }

  .main-header-inner {
    padding: 10px 14px;
    gap: 10px;
  }
  .burger-btn {
    display: grid;
  }
  .pill-search {
    display: none;
  }
  .hdr-action-link {
    display: none;
  }
  .hdr-actions {
    gap: 8px;
  }

  .mobile-search-row {
    display: block;
  }
  .mobile-search-row .pill-search {
    display: flex;
    max-width: none;
    width: 100%;
  }

  .nav-tier {
    display: none;
  }
  .nav-tier.menu-open {
    display: block !important;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: var(--bg);
    border-bottom: 1px solid var(--line);
    box-shadow: 0 20px 25px -5px rgba(0,0,0,0.15);
    max-height: calc(100vh - 120px);
    overflow-y: auto;
    z-index: 50;
  }
  .nav-tier.menu-open .nav-inner {
    flex-direction: column;
    align-items: stretch;
    gap: 4px;
    padding: 14px 14px 24px;
    overflow-x: visible;
    white-space: normal;
  }
  .nav-tier.menu-open .nav-link {
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
  }
  .nav-tier.menu-open .nav-link:hover {
    background: var(--card);
  }
  .nav-tier.menu-open .nav-dropdown-wrap {
    flex-direction: column;
    align-items: stretch;
  }
  .nav-tier.menu-open .nav-dropdown-menu {
    position: static;
    display: flex;
    box-shadow: none;
    border: none;
    background: transparent;
    padding: 0 0 4px 20px;
  }
  [dir=rtl] .nav-tier.menu-open .nav-dropdown-menu {
    padding: 0 20px 4px 0;
  }
  .nav-tier.menu-open .nav-dropdown-menu a {
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 13px;
  }
  .mobile-menu-extras {
    display: flex;
    flex-direction: column;
    border-top: 1px solid var(--line);
    margin-top: 12px;
    padding-top: 12px;
    gap: 4px;
  }
  .mobile-socials {
    display: flex;
    gap: 16px;
    padding: 12px 14px 4px;
    color: var(--fg);
  }
  .mobile-socials a {
    color: var(--fg);
    display: flex;
    align-items: center;
    justify-content: center;
  }
}

/* Auth Modal Styles */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  z-index: 1000;
  display: grid;
  place-items: center;
  padding: 20px;
}
.auth-modal {
  background: var(--bg);
  color: var(--fg);
  border-radius: 16px;
  padding: 28px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
  border: 1px solid var(--line);
  animation: modalIn 0.2s ease-out;
}
@keyframes modalIn {
  from { opacity: 0; transform: scale(0.96) translateY(8px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}
.auth-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.auth-header h3 {
  font-size: 18px;
  font-weight: 700;
  margin: 0;
}
.auth-close {
  font-size: 18px;
  background: none;
  border: none;
  color: var(--mut);
  cursor: pointer;
  padding: 4px;
  line-height: 1;
}
.auth-close:hover {
  color: var(--fg);
}
"""

with open('src/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update variables in :root, dark media, and dark theme
var_light = """  --top-bg:#f3f4f6;
  --top-fg:#374151;
  --top-line:#e5e7eb;
  --search-bg:#f3f4f6;"""

var_dark = """    --top-bg:#18181b;
    --top-fg:#d1d5db;
    --top-line:#27272a;
    --search-bg:#1f1f23;"""

# Add variables to :root
if '--top-bg' not in css:
    css = css.replace("--gold:#b8935a;", "--gold:#b8935a;\n" + var_light)
    css = css.replace("--acc:#ef4452;", "--acc:#ef4452;\n" + var_dark)

s_marker = '/* =========================================================================='
e_marker = '/* Base Image & Shimmer */'

s_idx = css.find(s_marker)
e_idx = css.find(e_marker)

if s_idx == -1 or e_idx == -1:
    raise Exception("Markers not found in styles.css")

updated_css = css[:s_idx] + css_code + "\n" + css[e_idx:]

with open('src/styles.css', 'w', encoding='utf-8') as f:
    f.write(updated_css)

print("styles.css cleaned and updated!")
