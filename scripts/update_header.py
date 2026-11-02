with open('src/main.js', 'r', encoding='utf-8') as f:
    c = f.read()

target = """  <div className="top"><div className="w"><span>Find a Store · Contact Us</span><span>FREE Delivery on orders above 25 KWD!</span><button className="lang" aria-label="Language" onClick=${()=>sl(lang=='ar'?'en':'ar')}>${lang=='ar'?'English':'العربية'}</button></div></div>
  <header><div className="bar"><button className="ic burger" aria-label="Menu" onClick=${()=>setMenu(!menu)}>☰</button><a className="logo" onClick=${()=>go('home')}><i/>OBSESSION</a>
  <form className="srch" onSubmit=${e=>{e.preventDefault();go('shop',{q})}}><input placeholder="What are you looking for?" value=${q} onChange=${e=>sq(e.target.value)} aria-label="Search"/><button className="ic" aria-label="Search">⌕</button></form>
  <button className="ic" aria-label="Wishlist" onClick=${()=>go('wish')}>♡${wish.length>0&&html`<b>${wish.length}</b>`}</button><button className="ic" aria-label="Cart" onClick=${()=>setOpen(true)}>🛍${n>0&&html`<b>${n}</b>`}</button></div>
  <nav style=${menu?{flexDirection:'column',gap:10,paddingBottom:16}:{}}>${NAV.map(x=>html`<a key=${x[0]} className=${route.p==x[1][0]&&(!x[1][1]||x[1][1]==route.a)?'on':''} onClick=${()=>go(...x[1])}>${x[0]}</a>`)}</nav></header>"""

replacement = """  <div className="top"><div className="w"><span className="announcement">FREE Delivery on orders above 25 KWD!</span><button className="lang" aria-label="Language" onClick=${()=>sl(lang=='ar'?'en':'ar')}>${lang=='ar'?'English':'العربية'}</button></div></div>
  <header><div className="bar"><button className="ic burger" aria-label="Menu" onClick=${()=>setMenu(!menu)}>${menu?'✕':'☰'}</button><a className="logo" onClick=${()=>go('home')}><i/>OBSESSION</a>
  <form className="srch" onSubmit=${e=>{e.preventDefault();go('shop',{q})}}><input placeholder="What are you looking for?" value=${q} onChange=${e=>sq(e.target.value)} aria-label="Search"/><button className="ic" aria-label="Search">⌕</button></form>
  <button className="ic" aria-label="Wishlist" onClick=${()=>go('wish')}>♡${wish.length>0&&html`<b>${wish.length}</b>`}</button><button className="ic" aria-label="Cart" onClick=${()=>setOpen(true)}>🛍${n>0&&html`<b>${n}</b>`}</button></div>
  <div className="mobile-srch"><form className="srch" onSubmit=${e=>{e.preventDefault();go('shop',{q})}}><input placeholder="What are you looking for?" value=${q} onChange=${e=>sq(e.target.value)} aria-label="Search"/><button className="ic" aria-label="Search">⌕</button></form></div>
  <nav className=${menu?'menu-open':''}>${NAV.map(x=>html`<a key=${x[0]} className=${route.p==x[1][0]&&(!x[1][1]||x[1][1]==route.a)?'on':''} onClick=${()=>go(...x[1])}>${x[0]}</a>`)}</nav></header>"""

if target in c:
    c = c.replace(target, replacement)
    with open('src/main.js', 'w', encoding='utf-8') as f:
        f.write(c)
    print("SUCCESS: Header updated cleanly")
else:
    print("TARGET NOT FOUND")
    idx = c.find("FREE Delivery on orders above 25 KWD!")
    print(repr(c[idx-50:idx+350]))

