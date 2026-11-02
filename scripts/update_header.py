import re

# Read main.js
with open('src/main.js', 'r', encoding='utf-8') as f:
    main_code = f.read()

# 1. Update AR dictionary
ar_additions = """  'Find a Store':'ابحث عن متجر','Find A Store':'ابحث عن متجر','Contact Us':'تواصل معنا',
  'FREE Delivery on orders above 25KD!':'توصيل مجاني للطلبات فوق 25 د.ك!',
  'Sign in/ Register':'تسجيل الدخول / التسجيل','Sign In':'تسجيل الدخول','Register':'تسجيل','Create Account':'إنشاء حساب','Create an Account':'إنشاء حساب',
  'Sign in to Obsession':'تسجيل الدخول إلى أوبسيشن','Access your wishlist, order tracking and exclusive perks.':'تمتع بقائمة أمنياتك وتتبع طلباتك والعروض الحصرية.',
  'Full Name':'الاسم الكامل','Password':'كلمة المرور','Signed in successfully!':'تم تسجيل الدخول بنجاح!',
  'Already have an account?':'هل لديك حساب بالفعل؟','New to Obsession?':'جديد في أوبسيشن؟',
  'Exclusive':'حصري','Nail Care':'العناية بالأظافر','Kuwaiti Brands':'علامات كويتية','All Brands':'كل العلامات','All Brands ✦':'كل العلامات ✦',
  'Eau de Parfum':'أو دو بارفان','Body Mists & Room Sprays':'معطرات غرف ورذاذ الجسم','Reed Diffusers':'معطرات القصب','Signature Oud':'مجموعة العود المميزة',
  'Face & Powders':'الوجه والبودرة','Lipsticks & Lip Jams':'أحمر الشفاه وملمعات','Eyes & Brows':'العيون والحواجب','Setting Sprays':'بخاخات التثبيت',
  'The Obsession Blog':'مدونة أوبسيشن','About Obsession':'عن أوبسيشن',"""

main_code = main_code.replace("'OBSESSION':'أوبسيشن',", "'OBSESSION':'أوبسيشن',\n" + ar_additions)

# Check Shop filter
old_filter = "let L=P.filter(p=>(cat=='All'||p.cat==cat)&&(br=='All'||p.brand==br)&&p.price<=mx&&(!a.tag||(a.tag=='new'?p.tag:p.rating>=4.5))&&(!a.q||(p.name+p.brand+p.cat).toLowerCase().includes(a.q.toLowerCase())));"
new_filter = "let L=P.filter(p=>(cat=='All'||p.cat==cat)&&(br=='All'||p.brand==br)&&p.price<=mx&&(!a.tag||(a.tag=='new'?p.tag:a.tag=='exclusive'?(p.price>4||p.id%3==0):a.tag=='kuwaiti'?(p.brand=='Oud & Co'||p.brand=='Obsession Lab'):p.rating>=4.5))&&(!a.q||(p.name+p.brand+p.cat).toLowerCase().includes(a.q.toLowerCase())));"

if old_filter in main_code:
    main_code = main_code.replace(old_filter, new_filter)
else:
    print("Warning: old_filter not found in main.js")

# Let's write the SvgI icon definitions and the updated App component
# Let's find function App() in main.js
app_idx = main_code.find("function App(){")
if app_idx == -1:
    raise Exception("function App() not found")

before_app = main_code[:app_idx]

new_app_code = """const SvgI={
  fb: html`<svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95C18.05 21.45 22 17.19 22 12z"/></svg>`,
  x: html`<svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>`,
  ig: html`<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.5" fill="currentColor"/></svg>`,
  tiktok: html`<svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64c.298-.002.595.042.88.13V9.4a6.33 6.33 0 0 0-1-.08A6.34 6.34 0 0 0 3 15.66a6.34 6.34 0 0 0 10.82 4.5 6.3 6.3 0 0 0 1.86-4.49V8.75a8.2 8.2 0 0 0 4.91 1.62V6.9a4.82 4.82 0 0 1-1-.21z"/></svg>`,
  pin: html`<svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12c0 4.24 2.64 7.86 6.39 9.3-.09-.78-.17-1.98.04-2.83.19-.77 1.25-5.3 1.25-5.3s-.32-.64-.32-1.58c0-1.48.86-2.59 1.93-2.59.91 0 1.35.68 1.35 1.5 0 .92-.58 2.29-.89 3.56-.25 1.07.54 1.94 1.59 1.94 1.91 0 3.38-2.02 3.38-4.93 0-2.58-1.85-4.38-4.5-4.38-3.07 0-4.87 2.3-4.87 4.68 0 .93.36 1.92.8 2.46.09.11.1.2.07.32-.08.33-.26 1.05-.29 1.19-.05.21-.17.25-.38.16-1.42-.66-2.31-2.73-2.31-4.4 0-3.58 2.6-6.87 7.5-6.87 3.94 0 7 2.81 7 6.56 0 3.91-2.47 7.07-5.9 7.07-1.15 0-2.24-.6-2.61-1.31l-.71 2.71c-.26 1-.96 2.26-1.43 3.03.95.29 1.95.45 2.99.45 5.52 0 10-4.48 10-10S17.52 2 12 2z"/></svg>`,
  snap: html`<svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M12 2.5c-3.1 0-5.5 2.3-5.5 5.3 0 .7.1 1.4.3 2-.7.2-1.4.6-1.7 1.1-.3.5-.2 1.1.2 1.5.3.3.7.4 1.1.5.1.7.5 1.4 1 1.9-.3.2-.8.5-1.5.8-.9.4-1.3.8-1.3 1.4 0 .7.7 1.2 1.9 1.4 1.2.2 2.6-.1 3.5-.5.7.4 1.4.6 2 .6s1.3-.2 2-.6c.9.4 2.3.7 3.5.5 1.2-.2 1.9-.7 1.9-1.4 0-.6-.4-1-1.3-1.4-.7-.3-1.2-.6-1.5-.8.5-.5.9-1.2 1-1.9.4-.1.8-.2 1.1-.5.4-.4.5-1 .2-1.5-.3-.5-1-.9-1.7-1.1.2-.6.3-1.3.3-2 0-3-2.4-5.3-5.5-5.3z"/></svg>`,
  yt: html`<svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M21.58 7.19a2.5 2.5 0 0 0-1.76-1.77C18.26 5 12 5 12 5s-6.26 0-7.82.42A2.5 2.5 0 0 0 2.42 7.19 26.3 26.3 0 0 0 2 12a26.3 26.3 0 0 0 .42 4.81 2.5 2.5 0 0 0 1.76 1.77C5.74 19 12 19 12 19s6.26 0 7.82-.42a2.5 2.5 0 0 0 1.76-1.77A26.3 26.3 0 0 0 22 12a26.3 26.3 0 0 0-.42-4.81zM9.75 15.02V8.98L15 12l-5.25 3.02z"/></svg>`,
  pinLoc: html`<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M12 21s-7-6.2-7-11a7 7 0 1 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>`,
  user: html`<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>`,
  heart: html`<svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>`,
  bag: html`<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>`,
  srch: html`<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>`,
  chev: html`<svg viewBox="0 0 10 6" width="8" height="5" fill="none"><path d="M1 1L5 5L9 1" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/></svg>`,
  sparkle: html`<svg viewBox="0 0 24 24" width="9" height="9" fill="currentColor" className="sparkle-ic"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>`
};

function App(){
  const[route,setR]=useState({p:'home',a:null});
  const[cart,setCart]=useState(()=>ld('obs_cart',[]));
  const[wish,setW]=useState(()=>ld('obs_wish',[]));
  const[open,setOpen]=useState(false);
  const[menu,setMenu]=useState(false);
  const[toast,setT]=useState('');
  const[q,sq]=useState('');
  const[lang,sl]=useState(LANG);
  const[authModal,setAuthModal]=useState(false);
  const[isRegister,setIsRegister]=useState(false);

  LANG=lang;
  useEffect(()=>sv('obs_cart',cart),[cart]);
  useEffect(()=>{
    sv('obs_lang',lang);
    document.documentElement.lang=lang;
    document.documentElement.dir=lang=='ar'?'rtl':'ltr';
  },[lang]);
  useEffect(()=>sv('obs_wish',wish),[wish]);
  useEffect(()=>{
    if(toast){
      const t=setTimeout(()=>setT(''),2200);
      return()=>clearInterval(t);
    }
  },[toast]);

  const go=(p,a=null)=>{
    setR({p,a});
    setMenu(false);
    setOpen(false);
    window.scrollTo(0,0);
  };

  const add=(p,shade,n=1,silent)=>{
    setCart(c=>{
      const k=p.id+'-'+shade,f=c.find(x=>x.k==k);
      return f?c.map(x=>x.k==k?{...x,q:x.q+n}:x):[...c,{k,id:p.id,shade,q:n}];
    });
    if(!silent)setT(T(p.name)+' — '+T('added to cart'));
  };

  const tw=id=>setW(w=>w.includes(id)?w.filter(x=>x!=id):[...w,id]);
  const n=cart.reduce((s,i)=>s+i.q,0);
  const V={home:Home,shop:Shop,product:Product,checkout:Checkout,blog:Blog,post:PostPg,about:About,contact:Contact,wish:Wish}[route.p];

  return html`<${X.Provider} value=${{go,route,cart,setCart,wish,tw,add,open,setOpen,clear:()=>setCart([])}}>
    <!-- TIER 1: Top Bar -->
    <div className="top-bar">
      <div className="w top-bar-inner">
        <div className="top-left">
          <a onClick=${()=>go('contact')}>Find a Store</a>
          <span className="top-sep"></span>
          <a onClick=${()=>go('contact')}>Contact Us</a>
        </div>
        <div className="top-center">
          <span>FREE Delivery on orders above 25KD!</span>
        </div>
        <div className="top-right">
          <button className="top-lang-btn" onClick=${()=>sl(lang=='ar'?'en':'ar')} aria-label="Toggle Language">
            <span>${lang=='ar'?'English':'العربية'}</span>
            <span className="top-chev">${SvgI.chev}</span>
          </button>
          <div className="top-socials">
            <a href="https://facebook.com" target="_blank" rel="noreferrer" aria-label="Facebook">${SvgI.fb}</a>
            <a href="https://twitter.com" target="_blank" rel="noreferrer" aria-label="X">${SvgI.x}</a>
            <a href="https://instagram.com" target="_blank" rel="noreferrer" aria-label="Instagram">${SvgI.ig}</a>
            <a href="https://tiktok.com" target="_blank" rel="noreferrer" aria-label="TikTok">${SvgI.tiktok}</a>
            <a href="https://pinterest.com" target="_blank" rel="noreferrer" aria-label="Pinterest">${SvgI.pin}</a>
            <a href="https://snapchat.com" target="_blank" rel="noreferrer" aria-label="Snapchat">${SvgI.snap}</a>
            <a href="https://youtube.com" target="_blank" rel="noreferrer" aria-label="YouTube">${SvgI.yt}</a>
          </div>
        </div>
      </div>
    </div>

    <!-- TIER 2: Main Brand Header -->
    <header className="hdr-master">
      <div className="w main-header-inner">
        <button className="burger-btn" aria-label="Menu" onClick=${()=>setMenu(!menu)}>
          ${menu?'✕':'☰'}
        </button>

        <a className="brand-logo" onClick=${()=>go('home')}>
          <div className="logo-stripes">
            <span></span><span></span><span></span><span></span><span></span>
          </div>
          <div className="logo-text">
            <div className="logo-en">OB<span className="logo-acc">S</span>ESSION</div>
            <div className="logo-ar">أوبـ<span className="logo-acc">سـ</span>ـيشن</div>
          </div>
        </a>

        <form className="pill-search" onSubmit=${e=>{e.preventDefault();go('shop',{q})}}>
          <input
            type="search"
            placeholder="What are you looking for?"
            value=${q}
            onChange=${e=>sq(e.target.value)}
            aria-label="Search"
          />
          <button type="submit" className="pill-search-btn" aria-label="Search">
            ${SvgI.srch}
          </button>
        </form>

        <div className="hdr-actions">
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
        </div>
      </div>

      <!-- Mobile Search Bar (under main header on smaller screens) -->
      <div className="mobile-search-row">
        <form className="pill-search" onSubmit=${e=>{e.preventDefault();go('shop',{q})}}>
          <input
            type="search"
            placeholder="What are you looking for?"
            value=${q}
            onChange=${e=>sq(e.target.value)}
            aria-label="Search"
          />
          <button type="submit" className="pill-search-btn" aria-label="Search">
            ${SvgI.srch}
          </button>
        </form>
      </div>

      <!-- TIER 3: Navigation Menu Bar -->
      <nav className=${`nav-tier ${menu?'menu-open':''}`}>
        <div className="w nav-inner">
          <a className="nav-link" onClick=${()=>go('home')}>Home</a>
          <a className="nav-link nav-red" onClick=${()=>go('shop',{tag:'exclusive'})}>Exclusive</a>
          <a className="nav-link" onClick=${()=>go('shop',{tag:'new'})}>New Arrivals</a>
          <a className="nav-link" onClick=${()=>go('shop',{tag:'best'})}>Best Sellers</a>

          <!-- Fragrance dropdown -->
          <div className="nav-dropdown-wrap">
            <a className="nav-link nav-has-drop" onClick=${()=>go('shop',{cat:'Fragrance'})}>
              <span>Fragrance</span>
              <span className="nav-drop-ic">${SvgI.chev}</span>
            </a>
            <div className="nav-dropdown-menu">
              <a onClick=${()=>go('shop',{cat:'Fragrance'})}>Eau de Parfum</a>
              <a onClick=${()=>go('shop',{cat:'Fragrance'})}>Body Mists & Room Sprays</a>
              <a onClick=${()=>go('shop',{cat:'Fragrance'})}>Reed Diffusers</a>
              <a onClick=${()=>go('shop',{cat:'Fragrance',brand:'Oud & Co'})}>Signature Oud</a>
            </div>
          </div>

          <!-- Makeup dropdown -->
          <div className="nav-dropdown-wrap">
            <a className="nav-link nav-has-drop" onClick=${()=>go('shop',{cat:'Makeup'})}>
              <span>Makeup</span>
              <span className="nav-drop-ic">${SvgI.chev}</span>
            </a>
            <div className="nav-dropdown-menu">
              <a onClick=${()=>go('shop',{cat:'Makeup'})}>Face & Powders</a>
              <a onClick=${()=>go('shop',{cat:'Makeup'})}>Lipsticks & Lip Jams</a>
              <a onClick=${()=>go('shop',{cat:'Makeup'})}>Eyes & Brows</a>
              <a onClick=${()=>go('shop',{cat:'Makeup'})}>Setting Sprays</a>
            </div>
          </div>

          <a className="nav-link" onClick=${()=>go('shop',{cat:'Makeup'})}>Nail Care</a>
          <a className="nav-link" onClick=${()=>go('shop',{cat:'Hair Care'})}>Hair Care</a>
          <a className="nav-link" onClick=${()=>go('shop',{cat:'Skin Care'})}>Skin Care</a>
          <a className="nav-link" onClick=${()=>go('shop',{cat:'Bath & Body'})}>Bath & Body</a>
          <a className="nav-link" onClick=${()=>go('shop',{brand:'Obsession Lab'})}>Kuwaiti Brands</a>

          <!-- All Brands with red sparkle -->
          <a className="nav-link nav-red nav-sparkle" onClick=${()=>go('shop',{})}>
            <span>All Brands</span>
            ${SvgI.sparkle}
          </a>

          <!-- About dropdown -->
          <div className="nav-dropdown-wrap">
            <a className="nav-link nav-has-drop" onClick=${()=>go('about')}>
              <span>About</span>
              <span className="nav-drop-ic">${SvgI.chev}</span>
            </a>
            <div className="nav-dropdown-menu">
              <a onClick=${()=>go('about')}>About Obsession</a>
              <a onClick=${()=>go('contact')}>Contact Us</a>
              <a onClick=${()=>go('blog')}>The Obsession Blog</a>
            </div>
          </div>

          <!-- Mobile Only Extra Links inside Drawer -->
          <div className="mobile-menu-extras">
            <a className="nav-link" onClick=${()=>go('contact')}>Find a Store</a>
            <a className="nav-link" onClick=${()=>go('contact')}>Contact Us</a>
            <a className="nav-link" onClick=${()=>setAuthModal(true)}>Sign in/ Register</a>
            <div className="mobile-socials">
              <a href="https://facebook.com" target="_blank" rel="noreferrer">${SvgI.fb}</a>
              <a href="https://twitter.com" target="_blank" rel="noreferrer">${SvgI.x}</a>
              <a href="https://instagram.com" target="_blank" rel="noreferrer">${SvgI.ig}</a>
              <a href="https://tiktok.com" target="_blank" rel="noreferrer">${SvgI.tiktok}</a>
              <a href="https://youtube.com" target="_blank" rel="noreferrer">${SvgI.yt}</a>
            </div>
          </div>
        </div>
      </nav>
    </header>

    <main><${V}/></main>

    <footer>
      <div className="w">
        <div className="fg">
          <div className="ab">
            <b>About</b>
            <p style=${{margin:'8px 0 12px',fontSize:13}}>Obsession is a trusted beauty destination built on authenticity, service and care. Since 2006 we have connected customers with genuine international products at fair prices.</p>
            <a style=${{color:'#fff',textDecoration:'underline'}} onClick=${()=>go('about')}>Learn More</a>
          </div>
          <div><h4>Quick Help</h4><a onClick=${()=>go('about')}>About Us</a><a onClick=${()=>go('contact')}>Contact Us</a><a onClick=${()=>go('blog')}>Blog</a></div>
          <div><h4>Shop</h4><a onClick=${()=>go('shop',{})}>All products</a><a onClick=${()=>go('shop',{tag:'new'})}>New Arrivals</a><a onClick=${()=>go('shop',{cat:'Gift Sets'})}>Bundles</a></div>
          <div><h4>Policies</h4><a>Terms of Service</a><a>Privacy Policy</a><a>Refund Policy</a><a>Shipping Policy</a></div>
          <div><h4>Contact Information</h4><a>Tunisia St, Hawally, KW</a><a>hello@obsession.example</a><a>+965 0000 0000</a><a>10:00am – 10:00pm, All Week-long</a></div>
        </div>
        <div className="cp"><span>© 2026 Obsession. All rights reserved.</span><span>KNET · Visa · Mastercard · Cash on Delivery</span></div>
      </div>
    </footer>

    ${open&&html`<${Drawer}/>`}
    ${toast&&html`<div className="toast" role="status">${toast}</div>`}

    <!-- Auth Modal -->
    ${authModal && html`
      <div className="modal-overlay" onClick=${()=>setAuthModal(false)}>
        <div className="auth-modal" onClick=${e=>e.stopPropagation()}>
          <div className="auth-header">
            <h3>${isRegister ? T('Create an Account') : T('Sign in to Obsession')}</h3>
            <button className="auth-close" onClick=${()=>setAuthModal(false)}>✕</button>
          </div>
          <p style=${{color:'var(--mut)',fontSize:13,margin:'6px 0 16px'}}>
            ${T('Access your wishlist, order tracking and exclusive perks.')}
          </p>
          <form onSubmit=${e=>{e.preventDefault();setAuthModal(false);setT(T('Signed in successfully!'))}}>
            ${isRegister && html`<input className="in full" style=${{marginBottom:10}} placeholder="Full Name" required/>`}
            <input className="in full" style=${{marginBottom:10}} type="email" placeholder="Email" required/>
            <input className="in full" style=${{marginBottom:14}} type="password" placeholder="Password" required/>
            <button className="btn full" style=${{width:'100%',borderRadius:8}}>
              ${isRegister ? T('Register') : T('Sign In')}
            </button>
          </form>
          <div style=${{marginTop:14,textAlign:'center',fontSize:13}}>
            ${isRegister
              ? html`<span>Already have an account? </span><a style=${{color:'var(--acc)',fontWeight:600}} onClick=${()=>setIsRegister(false)}>Sign In</a>`
              : html`<span>New to Obsession? </span><a style=${{color:'var(--acc)',fontWeight:600}} onClick=${()=>setIsRegister(true)}>Create Account</a>`
            }
          </div>
        </div>
      </div>
    `}
  <//>`;
}

ReactDOM.createRoot(document.getElementById('root')).render(html`<${App}/>`);
"""

full_updated_main = before_app + new_app_code

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(full_updated_main)

print("src/main.js updated successfully!")
