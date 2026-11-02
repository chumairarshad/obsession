import re

with open('src/main.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace language display string
code = code.replace(
    "<span>${lang=='ar'?'English':'العربية'}</span>",
    "<span>${lang=='ar'?'العربية':'English'}</span>"
)

# Remove top-sep from top-left
old_top_left = """        <div className="top-left">
          <a onClick=${()=>go('contact')}>Find a Store</a>
          <span className="top-sep"></span>
          <a onClick=${()=>go('contact')}>Contact Us</a>
        </div>"""

new_top_left = """        <div className="top-left">
          <a onClick=${()=>go('contact')}>Find a Store</a>
          <a onClick=${()=>go('contact')}>Contact Us</a>
        </div>"""
code = code.replace(old_top_left, new_top_left)

# Update Bag icon in SvgI to exact tote bag shape
old_bag = 'bag: html`<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>`'
new_bag = 'bag: html`<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M5 9h14l-1.5 11h-11L5 9z"/><path d="M9 9V6a3 3 0 0 1 6 0v3"/></svg>`'
code = code.replace(old_bag, new_bag)

# Update logo stripes to 6 stripes and letter O / و red
old_logo = """        <a className="brand-logo" onClick=${()=>go('home')}>
          <div className="logo-stripes">
            <span></span><span></span><span></span><span></span><span></span>
          </div>
          <div className="logo-text">
            <div className="logo-en">OB<span className="logo-acc">S</span>ESSION</div>
            <div className="logo-ar">أوبـ<span className="logo-acc">سـ</span>ـيشن</div>
          </div>
        </a>"""

new_logo = """        <a className="brand-logo" onClick=${()=>go('home')}>
          <div className="logo-stripes">
            <span></span><span></span><span></span><span></span><span></span><span></span>
          </div>
          <div className="logo-text">
            <div className="logo-en"><span className="logo-acc">O</span>BSESSION</div>
            <div className="logo-ar">أ<span className="logo-acc">و</span>بسيشن</div>
          </div>
        </a>"""
code = code.replace(old_logo, new_logo)

# In Tier 2 desktop actions: exactly Find a store, Sign in/ Register, and Cart button
# (Wishlist is accessible in mobile view and auth modal/drawer)
old_actions = """        <div className="hdr-actions">
          <a className="hdr-action-link" onClick=${()=>go('contact')}>
            ${SvgI.pinLoc}
            <span>Find A Store</span>
          </a>

          <a className="hdr-action-link" onClick=${()=>setAuthModal(true)}>
            ${SvgI.user}
            <span>Sign in/ Register</span>
          </a>

          <a className="hdr-icon-btn hdr-wish-btn" onClick=${()=>go('wish')} aria-label="Wishlist">
            ${SvgI.heart}
            ${wish.length > 0 && html`<span className="hdr-badge">${wish.length}</span>`}
          </a>

          <button className="hdr-cart-btn" onClick=${()=>setOpen(true)} aria-label="Cart">
            ${SvgI.bag}
            ${n > 0 && html`<span className="hdr-badge">${n}</span>`}
          </button>
        </div>"""

new_actions = """        <div className="hdr-actions">
          <a className="hdr-action-link" onClick=${()=>go('contact')}>
            ${SvgI.pinLoc}
            <span>Find A Store</span>
          </a>

          <a className="hdr-action-link" onClick=${()=>setAuthModal(true)}>
            ${SvgI.user}
            <span>Sign in/ Register</span>
          </a>

          <button className="hdr-cart-btn" onClick=${()=>setOpen(true)} aria-label="Cart">
            ${SvgI.bag}
            ${n > 0 && html`<span className="hdr-badge">${n}</span>`}
          </button>
        </div>"""
code = code.replace(old_actions, new_actions)

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Refined main.js successfully!")

