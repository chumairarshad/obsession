import React,{useState,useEffect,useContext,createContext,useRef} from 'react';
import ReactDOM from 'react-dom/client';
import htm from 'htm';
import './styles.css';

let LANG=(()=>{try{return JSON.parse(localStorage.getItem('obs_lang'))||'en'}catch(e){return'en'}})();
const AR={
  'OBSESSION':'أوبسيشن','Find a Store · Contact Us':'ابحث عن متجر · تواصل معنا','FREE Delivery on orders above 25 KWD!':'توصيل مجاني للطلبات فوق 25 د.ك!','KWD':'د.ك','Home':'الرئيسية','New Arrivals':'وصل حديثاً','Best Sellers':'الأكثر مبيعاً','Makeup':'مكياج','Fragrance':'عطور','Skin Care':'العناية بالبشرة','Hair Care':'العناية بالشعر','Bath & Body':'الاستحمام والجسم','Gift Sets':'مجموعات الهدايا','Blog':'المدونة','/ Blog':'/ المدونة','About':'حول','Contact':'اتصل بنا','What are you looking for?':'عمّ تبحث؟',
  'Juicy Bomb Flavors':'نكهات جوسي بومب','Lip care that tastes as good as it looks.':'عناية بالشفاه بنكهة رائعة ومظهر أجمل.','Scents You’ll Never Forget':'عطور لا تُنسى','Timeless perfumes and modern signatures.':'عطور خالدة وتوقيعات عصرية.','Gifts Made to Impress':'هدايا تبهر الجميع','Curated sets for every occasion.':'مجموعات مختارة لكل مناسبة.','Shop Now':'تسوّق الآن','Quick add':'إضافة سريعة','New':'جديد','View All':'عرض الكل','The latest beauty finds, fresh and exciting.':'أحدث صيحات الجمال، منعشة ومثيرة.',
  'Authentic. Affordable. Always.':'أصلي. بسعر مناسب. دائماً.','Fast Delivery':'توصيل سريع','Free Returns':'إرجاع مجاني','100% Authentic Products':'منتجات أصلية 100%','Easy Checkout':'دفع سهل','Secure Payment':'دفع آمن','Money Guarantee':'ضمان استرداد المال','Easy Returns':'إرجاع سهل','Secure Checkout':'دفع آمن',
  'Shop Fragrances':'تسوّق العطور','Find your signature scent.':'اكتشف عطرك المميز.','Elevate your look with essentials that highlight your natural beauty.':'ارتقِ بإطلالتك بأساسيات تبرز جمالك الطبيعي.','Happy Glow':'إشراقة سعيدة','Skincare that loves you back':'عناية بالبشرة تبادلك الحب','Juicy Bomb':'جوسي بومب','Long-lasting shine, unforgettable look':'لمعان يدوم، وإطلالة لا تُنسى','Love is in the Choco’Lot':'الحب في الشوكولاتة','Limited edition collection':'مجموعة إصدار محدود','Free Delivery':'توصيل مجاني','On orders above 25 KWD':'للطلبات فوق 25 د.ك','Explore':'استكشف','Gifts & Value Sets':'الهدايا والمجموعات الاقتصادية','Share the joy of beauty with curated gift sets.':'شارك فرحة الجمال مع مجموعات هدايا مختارة.','Shop By Brands':'تسوّق حسب العلامة','Shop All Brands':'كل العلامات','Our Blog Posts':'مقالات المدونة','View All Posts':'كل المقالات','Read More':'اقرأ المزيد',
  'Authentic Products':'منتجات أصلية','100% genuine, guaranteed':'أصلية 100% ومضمونة','14-day hassle-free returns':'إرجاع بسهولة خلال 14 يوماً','Gift Ready':'جاهز للإهداء','Beautifully wrapped on request':'تغليف أنيق عند الطلب','Our most loved picks, by category.':'اختياراتنا الأكثر حباً حسب الفئة.','Signature Collection':'المجموعة المميزة','Midnight Oud':'ميدنايت عود','A rich, smoky blend of oud, amber and vanilla — crafted for evenings that linger.':'مزيج غني ودخاني من العود والعنبر والفانيليا، لأمسيات لا تُنسى.','Discover':'اكتشف','Loved by our customers':'محبوبة من عملائنا','Maryam A.':'مريم أ.','The fragrance collection is unmatched. Authentic, beautifully packed and delivered the next day.':'مجموعة العطور لا مثيل لها. أصلية ومغلفة بأناقة وتصل في اليوم التالي.','Fahad R.':'فهد ر.','Great prices and genuine products. The gift sets are perfect for every occasion.':'أسعار رائعة ومنتجات أصلية. مجموعات الهدايا مثالية لكل مناسبة.','Layla H.':'ليلى ح.','My go-to for makeup. The shade range is amazing and customer service is superb.':'وجهتي الأولى للمكياج. تشكيلة الألوان مذهلة وخدمة العملاء ممتازة.','Years of trust':'سنة من الثقة','Happy customers':'عميل سعيد','Authentic products':'منتجات أصلية','Customer support':'دعم العملاء','Follow @obsession':'تابعونا @obsession','Share your look with #ObsessionBeauty':'شاركنا إطلالتك عبر #ObsessionBeauty',
  'Join the Obsession list':'انضم إلى قائمة أوبسيشن','Sign up and receive 10% off your first order using code':'سجّل واحصل على خصم 10% على أول طلب باستخدام الرمز','Sign Up':'اشترك','Enter your email':'أدخل بريدك الإلكتروني','Thank you! Check your inbox for your code.':'شكراً لك! تفقد بريدك للحصول على الرمز.',
  'Learn More':'اعرف المزيد','Obsession is a trusted beauty destination built on authenticity, service and care. Since 2006 we have connected customers with genuine international products at fair prices.':'أوبسيشن وجهة جمال موثوقة قائمة على الأصالة والخدمة والاهتمام. منذ 2006 نربط العملاء بمنتجات عالمية أصلية بأسعار عادلة.','Quick Help':'مساعدة سريعة','About Us':'من نحن','Contact Us':'تواصل معنا','Shop':'المتجر','All products':'كل المنتجات','Bundles':'العروض المجمّعة','Policies':'السياسات','Terms of Service':'شروط الخدمة','Privacy Policy':'سياسة الخصوصية','Refund Policy':'سياسة الاسترجاع','Shipping Policy':'سياسة الشحن','Contact Information':'معلومات التواصل','Tunisia St, Hawally, KW':'شارع تونس، حولي، الكويت','10:00am – 10:00pm, All Week-long':'10:00 ص – 10:00 م، طوال الأسبوع','© 2026 Obsession. All rights reserved.':'© 2026 أوبسيشن. جميع الحقوق محفوظة.','KNET · Visa · Mastercard · Cash on Delivery':'كي نت · فيزا · ماستركارد · الدفع عند الاستلام',
  'Filter':'تصفية','Sort by:':'ترتيب حسب:','Most relevant':'الأكثر صلة','Price: low to high':'السعر: من الأقل للأعلى','Price: high to low':'السعر: من الأعلى للأقل','Name A–Z':'الاسم أ–ي','Category':'الفئة','All':'الكل','Brand':'العلامة','Max price:':'أعلى سعر:','products':'منتج','No products found':'لا توجد منتجات','Try changing your filters.':'جرّب تغيير عوامل التصفية.','Reset':'إعادة ضبط','/ Collection /':'/ المجموعة /','All Products':'كل المنتجات','Results for':'نتائج البحث عن','Browse authentic products at Obsession. Every product is sourced from official distributors.':'تصفح منتجات أصلية في أوبسيشن. جميع منتجاتنا من موزعين رسميين.',
  'Brand:':'العلامة:','· SKU: OBS-':'· الرمز: OBS-','Shade:':'اللون:','Shade 0':'اللون 0','Shade 01':'اللون 01','Shade 02':'اللون 02','Shade 03':'اللون 03','Shade 04':'اللون 04','Add To Cart':'أضف إلى السلة','Buy It Now':'اشترِ الآن','In stock and ready to ship.':'متوفر وجاهز للشحن.','Hurry up, only':'أسرع، متبقي فقط','items left in stock.':'قطع في المخزون.','Payment & Security':'الدفع والأمان','We accept KNET, Visa, Mastercard and Cash on Delivery. Your payment information is processed securely.':'نقبل كي نت وفيزا وماستركارد والدفع عند الاستلام. تتم معالجة بيانات الدفع بأمان.','Description':'الوصف','Shipping & Return':'الشحن والإرجاع','Product Specifications':'مواصفات المنتج','A bestselling essential with a premium finish, designed for everyday wear and long-lasting results.':'منتج أساسي الأكثر مبيعاً بلمسة فاخرة، مصمم للاستخدام اليومي ونتائج تدوم طويلاً.','Free delivery on orders above 25 KWD. Standard delivery takes 1–3 working days. Unopened items can be returned within 14 days.':'توصيل مجاني للطلبات فوق 25 د.ك. التوصيل العادي من 1 إلى 3 أيام عمل. يمكن إرجاع المنتجات غير المفتوحة خلال 14 يوماً.','· Category:':'· الفئة:','· Shades: 4 · Origin: Imported':'· الألوان: 4 · المنشأ: مستورد','is one of the trusted names available exclusively at Obsession.':'من العلامات الموثوقة المتوفرة حصرياً في أوبسيشن.',
  'Customer Reviews':'آراء العملاء','Write a review':'اكتب تقييماً','Your name':'اسمك','stars':'نجوم','Your review':'تقييمك','Submit':'إرسال','reviews)':'تقييم)','Amira K.':'أميرة ك.','Beautiful quality and arrived quickly. Will order again!':'جودة رائعة ووصل بسرعة. سأطلب مجدداً!','Noor S.':'نور س.','Lovely finish and long lasting.':'لمسة جميلة وتدوم طويلاً.','You may also like':'قد يعجبك أيضاً','Discover more in our FAQ':'اكتشف المزيد في الأسئلة الشائعة','Are your products authentic?':'هل منتجاتكم أصلية؟','Yes, all products are 100% authentic and sourced from trusted distributors.':'نعم، جميع المنتجات أصلية 100% ومن موزعين موثوقين.','How long does delivery take?':'كم يستغرق التوصيل؟','Usually 1–3 working days within Kuwait.':'عادةً من 1 إلى 3 أيام عمل داخل الكويت.','Can I return or exchange my order?':'هل يمكنني إرجاع أو استبدال طلبي؟','Yes, unopened items can be returned within 14 days.':'نعم، يمكن إرجاع المنتجات غير المفتوحة خلال 14 يوماً.','What payment methods do you accept?':'ما طرق الدفع المقبولة؟','KNET, Visa, Mastercard and Cash on Delivery.':'كي نت، فيزا، ماستركارد والدفع عند الاستلام.',
  'Your Cart':'سلة التسوق','Add':'أضف','more for free delivery':'للحصول على توصيل مجاني','You’ve unlocked free delivery 🎉':'حصلت على توصيل مجاني 🎉','Your cart is empty.':'سلتك فارغة.','Your cart is empty':'سلتك فارغة','Subtotal':'المجموع الفرعي','Checkout':'إتمام الشراء','Start Shopping':'ابدأ التسوق','added to cart':'أُضيف إلى السلة','Delivery details':'تفاصيل التوصيل','First name':'الاسم الأول','Last name':'اسم العائلة','Email':'البريد الإلكتروني','Phone (+965)':'الهاتف (+965)','Address (Block, Street, House)':'العنوان (القطعة، الشارع، المنزل)','City':'المدينة','Area':'المنطقة','Payment':'الدفع','KNET':'كي نت','Credit / Debit Card':'بطاقة ائتمان / خصم','Cash on Delivery':'الدفع عند الاستلام','Order summary':'ملخص الطلب','Delivery':'التوصيل','Free':'مجاني','Total':'الإجمالي','Place Order':'تأكيد الطلب','Thank you! ✓':'شكراً لك! ✓','Your order':'طلبك','has been placed. A confirmation will be sent to your email.':'تم استلامه. سيصلك تأكيد على بريدك الإلكتروني.','Continue Shopping':'متابعة التسوق',
  'The Obsession Blog':'مدونة أوبسيشن','Beauty guides, product knowledge and stories from our team.':'أدلة جمال ومعلومات عن المنتجات وقصص من فريقنا.','← Back to blog':'→ العودة إلى المدونة','Related products':'منتجات ذات صلة','About Obsession':'عن أوبسيشن','A trusted beauty destination built on authenticity, service and care.':'وجهة جمال موثوقة قائمة على الأصالة والخدمة والاهتمام.','Since 2006 we have connected customers with genuine international products at fair prices. Our team hand-picks every brand, works directly with official distributors and stands behind each order with easy returns and fast delivery.':'منذ 2006 نربط العملاء بمنتجات عالمية أصلية بأسعار عادلة. يختار فريقنا كل علامة بعناية ويتعامل مباشرة مع الموزعين الرسميين ويدعم كل طلب بإرجاع سهل وتوصيل سريع.','From everyday skincare to statement fragrances, Obsession exists to make beauty simple, trustworthy and a little bit addictive.':'من العناية اليومية بالبشرة إلى العطور المميزة، وُجدت أوبسيشن لتجعل الجمال بسيطاً وموثوقاً وجذاباً.','Shop the collection':'تسوّق المجموعة','We usually reply within one working day.':'نرد عادةً خلال يوم عمل واحد.','Name':'الاسم','How can we help?':'كيف نساعدك؟','Send Message':'إرسال الرسالة','Message sent. Thank you for reaching out!':'تم إرسال الرسالة. شكراً لتواصلك!','My Wishlist':'قائمة أمنياتي','Wishlist':'المفضلة','No saved items yet.':'لا توجد عناصر محفوظة.','Browse products':'تصفح المنتجات',
  'Matte Fresh Setting Spray':'بخاخ تثبيت المكياج مات','Pore No More Primer':'برايمر تصغير المسام','Liquid Lipstick Trio':'مجموعة أحمر الشفاه السائل','Face & Under Eye Powder':'بودرة الوجه وتحت العين','2-in-1 Brow Pencil':'قلم حواجب 2 في 1','Jazzy Eyeshadow Palette':'باليت ظلال العيون جازي','Floral Flush Blush Palette':'باليت أحمر الخدود الزهري','Coconut Reed Diffuser':'معطر جو بالقصب وجوز الهند','Midnight Oud Eau de Parfum':'ميدنايت عود أو دو بارفان','Silver Mountain Parfum':'عطر سيلفر ماونتن','Rose Noir Eau de Parfum':'روز نوار أو دو بارفان','Vanilla Room Spray':'معطر غرف الفانيليا','Hydra Jelly Pocket Lip Jam':'جل الشفاه المرطب','Vitamin C Glow Serum':'سيروم فيتامين سي للإشراقة','Hydrating Cream SPF 30':'كريم مرطب SPF 30','Gentle Foaming Cleanser':'غسول رغوي لطيف','Repair Hair Mist':'بخاخ إصلاح الشعر','Argan Hair Oil':'زيت الأرغان للشعر','Lavender Body Butter':'زبدة الجسم باللافندر','Shower Gel Vanilla Bean':'شاور جل الفانيليا','Purple Lavender Gift Set':'مجموعة هدايا اللافندر','Glow Lip Kit':'طقم الشفاه المتوهج','Crystal Noir Parfum Set':'مجموعة كريستال نوار للعطور','Pro Makeup Brush Set':'طقم فرش المكياج الاحترافي','Obsession Lab':'مختبر أوبسيشن','Velvet Muse':'فيلفت ميوز','Aura Noir':'أورا نوار','Maison Rouge':'ميزون روج','Lumière':'لوميير','Oud & Co':'عود آند كو',
  'Two Decades of Trust: The Journey Behind Obsession':'عقدان من الثقة: رحلة أوبسيشن','Oct 29, 2025':'29 أكتوبر 2025','Oct 23, 2025':'23 أكتوبر 2025','Oct 12, 2025':'12 أكتوبر 2025','Educational':'تثقيفي','Obsession began as a small boutique with one promise: authentic beauty at fair prices. Two decades later, that promise still guides every product we choose.':'بدأت أوبسيشن كبوتيك صغير بوعد واحد: جمال أصيل بأسعار عادلة. وبعد عقدين ما زال هذا الوعد يوجّه كل منتج نختاره.','We work only with official distributors and trusted partners, so every item that reaches your door is genuine and carefully stored.':'نتعامل فقط مع الموزعين الرسميين والشركاء الموثوقين، ليصل إليك كل منتج أصلياً ومخزناً بعناية.','Today we serve thousands of customers every month, and we are just getting started.':'نخدم اليوم آلاف العملاء كل شهر، ونحن في بداية الطريق.',
  'Understanding Perfume Concentrations':'فهم تركيزات العطور','Parfum, Eau de Parfum, Eau de Toilette and Eau Fraîche differ mainly in how much fragrance oil they contain.':'تختلف أنواع العطور أساساً في نسبة الزيوت العطرية التي تحتويها.','Higher concentrations last longer and project more softly, while lighter ones feel fresh and are ideal for warm days.':'التركيزات الأعلى تدوم أطول، أما الأخف فتمنح انتعاشاً مثالياً للأيام الدافئة.','Test a scent on skin and give it a few hours to settle before deciding.':'جرّب العطر على بشرتك وامنحه بضع ساعات ليستقر قبل أن تقرر.',
  'How to Spot Authentic Beauty Products Online':'كيف تميّز منتجات التجميل الأصلية عبر الإنترنت','Check the seller, the packaging details, batch codes and the price. Deals that look too good to be true usually are.':'تحقق من البائع وتفاصيل التغليف ورموز الدفعة والسعر. العروض الجيدة أكثر من اللازم غالباً ليست حقيقية.','Buy from stores that source directly from brands and offer clear return policies.':'اشترِ من متاجر تتعامل مباشرة مع العلامات وتوفر سياسة إرجاع واضحة.','When in doubt, contact the store before you order.':'عند الشك، تواصل مع المتجر قبل الطلب.',
  'A Simple Five-Step Evening Skincare Routine':'روتين مسائي بسيط للعناية بالبشرة في خمس خطوات','Cleanse, tone, treat, moisturise and protect. That is all most skin needs at night.':'التنظيف، التونر، العلاج، الترطيب والحماية. هذا كل ما تحتاجه معظم البشرة ليلاً.','Introduce one new active at a time and give it two weeks before judging results.':'أدخل مكوناً فعالاً جديداً واحداً في كل مرة وانتظر أسبوعين قبل الحكم على النتائج.','Consistency beats complicated routines every time.':'الاستمرارية تتفوق على الروتين المعقد دائماً.',
  'Obsession Beauty Lifestyle':'أسلوب حياة أوبسيشن','Image':'صورة'
};

const T=s=>{if(LANG!='ar'||typeof s!='string')return s;const k=s.trim();return AR[k]?s.replace(k,AR[k]):s};
const h=function(t,p,...c){this[0]=3;if(p&&typeof t=='string'){if(p.class){p={...p,className:p.class};delete p.class}for(const k of ['placeholder','aria-label','alt'])if(p[k])p={...p,[k]:T(p[k])}}return React.createElement(t,p,...c.map(x=>T(x)))};
const html=htm.bind(h);const X=createContext();
const ld=(k,d)=>{try{return JSON.parse(localStorage.getItem(k))||d}catch(e){return d}},sv=(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
const money=n=>n.toFixed(3)+' '+T('KWD'),CATS=['Makeup','Fragrance','Skin Care','Hair Care','Bath & Body','Gift Sets'],SH=['#e9a1a8','#b5535f','#d9a27c','#8a4b3c','#f2c9b8','#7a3b5e'];
const BR=['Obsession Lab','Velvet Muse','Aura Noir','Maison Rouge','Lumière','Oud & Co'];

const CAT_IMGS=[
  '/images/categories/cat-1.webp',
  '/images/categories/cat-2.webp',
  '/images/categories/cat-3.webp',
  '/images/categories/cat-4.webp',
  '/images/categories/cat-5.webp',
  '/images/categories/cat-6.webp'
];

const BANS=[
  ['Happy Glow','Skincare that loves you back','/images/banners/banner-1.webp','Skin Care'],
  ['Juicy Bomb','Long-lasting shine, unforgettable look','/images/banners/banner-2.webp','Makeup'],
  ['Love is in the Choco’Lot','Limited edition collection','/images/banners/banner-3.webp','Makeup'],
  ['Free Delivery','On orders above 25 KWD','/images/banners/banner-4.webp','Gift Sets']
];

const HERO_SLIDES=[
  ['New Arrivals','Juicy Bomb Flavors','Lip care that tastes as good as it looks.','/images/hero/hero-1.webp',{tag:'new'}],
  ['Fragrance','Scents You’ll Never Forget','Timeless perfumes and modern signatures.','/images/hero/hero-2.webp',{cat:'Fragrance'}],
  ['Gift Sets','Gifts Made to Impress','Curated sets for every occasion.','/images/hero/hero-3.webp',{cat:'Gift Sets'}]
];

const INSTA_P=[0,7,12,20,5,9];
const INSTA_IMGS=[
  '/images/lifestyle/insta-1.webp',
  '/images/lifestyle/insta-2.webp',
  '/images/lifestyle/insta-3.webp',
  '/images/lifestyle/insta-4.webp',
  '/images/lifestyle/insta-5.webp',
  '/images/lifestyle/insta-6.webp'
];

const P=[
  ['Matte Fresh Setting Spray','Obsession Lab','Makeup',2.25,'#f4d35e'],
  ['Pore No More Primer','Velvet Muse','Makeup',2.5,'#7fd1c7'],
  ['Liquid Lipstick Trio','Velvet Muse','Makeup',3,'#b5535f'],
  ['Face & Under Eye Powder','Lumière','Makeup',2.75,'#f2b8c6'],
  ['2-in-1 Brow Pencil','Obsession Lab','Makeup',1.5,'#c9a66b'],
  ['Jazzy Eyeshadow Palette','Aura Noir','Makeup',3,'#a0643c'],
  ['Floral Flush Blush Palette','Velvet Muse','Makeup',3.25,'#e8788f'],
  ['Coconut Reed Diffuser','Maison Rouge','Fragrance',3,'#e8d57a'],
  ['Midnight Oud Eau de Parfum','Oud & Co','Fragrance',5.75,'#3a2a22'],
  ['Silver Mountain Parfum','Aura Noir','Fragrance',5.75,'#9bb7d4'],
  ['Rose Noir Eau de Parfum','Maison Rouge','Fragrance',6.5,'#b5304a'],
  ['Vanilla Room Spray','Lumière','Fragrance',3.5,'#f1d9a7'],
  ['Hydra Jelly Pocket Lip Jam','Velvet Muse','Makeup',2,'#e87a8f'],
  ['Vitamin C Glow Serum','Lumière','Skin Care',4.5,'#f4a73b'],
  ['Hydrating Cream SPF 30','Obsession Lab','Skin Care',3.9,'#bfe3f2'],
  ['Gentle Foaming Cleanser','Lumière','Skin Care',2.8,'#a8d8b9'],
  ['Repair Hair Mist','Aura Noir','Hair Care',3.2,'#c9a3e0'],
  ['Argan Hair Oil','Oud & Co','Hair Care',4.25,'#d4943a'],
  ['Lavender Body Butter','Maison Rouge','Bath & Body',3.75,'#b9a3e3'],
  ['Shower Gel Vanilla Bean','Obsession Lab','Bath & Body',2.25,'#f1d9a7'],
  ['Purple Lavender Gift Set','Maison Rouge','Gift Sets',5.75,'#a58bd6'],
  ['Glow Lip Kit','Velvet Muse','Gift Sets',3.75,'#e87a8f'],
  ['Crystal Noir Parfum Set','Aura Noir','Gift Sets',12.5,'#3b3b4f'],
  ['Pro Makeup Brush Set','Lumière','Makeup',8.75,'#d9a27c']
].map((r,i)=>({
  id:i,
  name:r[0],
  brand:r[1],
  cat:r[2],
  price:r[3],
  images:[1,2,3,4].map(k=>`/images/products/p${String(i+1).padStart(2,'0')}-${k}.webp`),
  tag:i%5==0?'New':'',
  rating:i%3?4.5:4,
  stock:2+i%8,
  shades:[r[4],SH[i%6],SH[(i+2)%6],SH[(i+4)%6]]
}));

const B=[
  ['Two Decades of Trust: The Journey Behind Obsession','About Obsession','Oct 29, 2025',['Obsession began as a small boutique with one promise: authentic beauty at fair prices. Two decades later, that promise still guides every product we choose.','We work only with official distributors and trusted partners, so every item that reaches your door is genuine and carefully stored.','Today we serve thousands of customers every month, and we are just getting started.'],'/images/blog/blog-1.webp'],
  ['Understanding Perfume Concentrations','Educational','Oct 29, 2025',['Parfum, Eau de Parfum, Eau de Toilette and Eau Fraîche differ mainly in how much fragrance oil they contain.','Higher concentrations last longer and project more softly, while lighter ones feel fresh and are ideal for warm days.','Test a scent on skin and give it a few hours to settle before deciding.'],'/images/blog/blog-2.webp'],
  ['How to Spot Authentic Beauty Products Online','Educational','Oct 23, 2025',['Check the seller, the packaging details, batch codes and the price. Deals that look too good to be true usually are.','Buy from stores that source directly from brands and offer clear return policies.','When in doubt, contact the store before you order.'],'/images/blog/blog-3.webp'],
  ['A Simple Five-Step Evening Skincare Routine','Skin Care','Oct 12, 2025',['Cleanse, tone, treat, moisturise and protect. That is all most skin needs at night.','Introduce one new active at a time and give it two weeks before judging results.','Consistency beats complicated routines every time.'],'/images/blog/blog-4.webp']
];

function Img({src, alt='', ratio, fit='cover', priority=false, className='', style={}, ...rest}){
  const[err,setErr]=useState(false);
  const[loaded,setLoaded]=useState(false);
  const s={
    aspectRatio:ratio||undefined,
    objectFit:fit,
    ...style
  };
  if(err){
    return html`<div className=${`img-fb ${className}`} style=${{...s,display:'grid',placeItems:'center'}} role="img" aria-label=${T(alt||'Image')}/>`;
  }
  return html`<img
    src=${src}
    alt=${T(alt)}
    loading=${priority?'eager':'lazy'}
    fetchpriority=${priority?'high':'auto'}
    decoding="async"
    className=${`img-c ${loaded?'loaded':'loading'} ${className}`}
    style=${s}
    onError=${()=>setErr(true)}
    onLoad=${()=>setLoaded(true)}
    ...${rest}
  />`;
}

const Stars=({r})=>html`<span className="st" aria-label=${r+' stars'}>${'★★★★★'.slice(0,Math.round(r))}${'☆☆☆☆☆'.slice(0,5-Math.round(r))}</span>`;
const Acc=({t,children})=>{const[o,s]=useState(false);return html`<div className="acc"><button onClick=${()=>s(!o)}>${t}<span>${o?'−':'+'}</span></button>${o&&html`<div>${children}</div>`}</div>`};

function Card({p}){
  const{go,wish,tw,add}=useContext(X);
  const on=wish.includes(p.id);
  return html`<div className="pc" onClick=${()=>go('product',p.id)}>
    ${p.tag&&html`<span className="tag">${p.tag}</span>`}
    <button className=${'hrt'+(on?' on':'')} aria-label="Wishlist" onClick=${e=>{e.stopPropagation();tw(p.id)}}>${on?'♥':'♡'}</button>
    <div className="pc-img">
      <${Img} src=${p.images[0]} alt=${p.name} ratio="4/5" fit="contain" className="pc-main"/>
      <${Img} src=${p.images[1]||p.images[0]} alt=${p.name} ratio="4/5" fit="contain" className="pc-hover"/>
    </div>
    <small>${p.brand}</small>
    <h3>${p.name}</h3>
    <div className="sw">${p.shades.map((c,i)=>html`<i key=${i} style=${{background:c}}/>`)}</div>
    <span className="pr">${money(p.price)}</span>
    <button className="qa" onClick=${e=>{e.stopPropagation();add(p,0)}}>Quick add</button>
  </div>`;
}

function Row({items}){
  const r=useRef();
  return html`<div>
    <div className="row" ref=${r}>${items.map(p=>html`<${Card} key=${p.id} p=${p}/>`)}</div>
    <div className="arrs" style=${{marginTop:12}}>
      <button aria-label="Previous" onClick=${()=>r.current.scrollBy({left:-420,behavior:'smooth'})}>‹</button>
      <button aria-label="Next" onClick=${()=>r.current.scrollBy({left:420,behavior:'smooth'})}>›</button>
    </div>
  </div>`;
}

const Hd=({t,s,l,a})=>{const{go}=useContext(X);return html`<div className="hd"><div><h2>${t}</h2>${s&&html`<p>${s}</p>`}</div>${l&&html`<a onClick=${()=>go(...a)}>${l}</a>`}</div>`};

function News(){
  const[e,s]=useState(''),[d,sd]=useState(false);
  return html`<div className="news w">
    <h2>Join the Obsession list</h2>
    <p style=${{color:'var(--mut)'}}>Sign up and receive 10% off your first order using code <b>OBS10</b></p>
    ${d?html`<p style=${{marginTop:14,color:'#0a8a4c',fontWeight:600}}>Thank you! Check your inbox for your code.</p>`:html`<form onSubmit=${x=>{x.preventDefault();if(/\S+@\S+\.\S+/.test(e))sd(true)}}><input type="email" required placeholder="Enter your email" value=${e} onChange=${x=>s(x.target.value)} aria-label="Email"/><button className="btn">Sign Up</button></form>`}
  </div>`;
}

const IC=['M3 7h11v9H3zM14 10h4l3 3v3h-7M7 19a2 2 0 100-4 2 2 0 000 4M17 19a2 2 0 100-4 2 2 0 000 4','M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z','M4 12a8 8 0 108-8H7M7 1L4 4l3 3','M4 10h16v10H4zM2 7h20v3H2zM12 7v13M12 7c-3-4-6-1-4 0M12 7c3-4 6-1 4 0'];
function Perks(){
  return html`<div className="perks">${[['Free Delivery','On orders above 25 KWD'],['Authentic Products','100% genuine, guaranteed'],['Easy Returns','14-day hassle-free returns'],['Gift Ready','Beautifully wrapped on request']].map((x,i)=>html`<div className="pk" key=${i}><svg viewBox="0 0 24 24" aria-hidden="true"><path d=${IC[i]} strokeLinecap="round" strokeLinejoin="round"/></svg><div><b>${x[0]}</b><span>${x[1]}</span></div></div>`)}</div>`;
}

function Tabs(){
  const[c,sc]=useState('Makeup');
  return html`<div className="sec"><${Hd} t="Best Sellers" s="Our most loved picks, by category."/><div className="tabs">${CATS.slice(0,5).map(x=>html`<button key=${x} className=${c==x?'on':''} onClick=${()=>sc(x)}>${x}</button>`)}</div><${Row} items=${P.filter(p=>p.cat==c)}/></div>`;
}

function Sig(){
  const{go}=useContext(X);
  const p=P[8];
  return html`<div className="sig">
    <div>
      <small>Signature Collection</small>
      <h2>Midnight Oud</h2>
      <p>A rich, smoky blend of oud, amber and vanilla — crafted for evenings that linger.</p>
      <div className="pr2">${money(p.price)}</div>
      <a className="btn l" onClick=${()=>go('product',8)}>Discover</a>
    </div>
    <div className="sig-media">
      <${Img} src="/images/lifestyle/signature.webp" alt="Midnight Oud Eau de Parfum" ratio="9/11" fit="cover" className="sig-img"/>
    </div>
  </div>`;
}

function Quotes(){
  return html`<div className="sec"><${Hd} t="Loved by our customers"/><div className="qs">${[['Maryam A.','The fragrance collection is unmatched. Authentic, beautifully packed and delivered the next day.'],['Fahad R.','Great prices and genuine products. The gift sets are perfect for every occasion.'],['Layla H.','My go-to for makeup. The shade range is amazing and customer service is superb.']].map((q,i)=>html`<div className="q" key=${i}><span className="st">★★★★★</span><p>“${q[1]}”</p><small>${q[0]}</small></div>`)}</div></div>`;
}

function Stats(){
  return html`<div className="stats">${[['20+','Years of trust'],['50K+','Happy customers'],['100%','Authentic products'],['24/7','Customer support']].map(s=>html`<div key=${s[1]}><b>${s[0]}</b><span>${s[1]}</span></div>`)}</div>`;
}

function Insta(){
  const{go}=useContext(X);
  return html`<div className="sec" style=${{paddingTop:0}}>
    <${Hd} t="Follow @obsession" s="Share your look with #ObsessionBeauty"/>
    <div className="ig">
      ${INSTA_IMGS.map((src,i)=>html`<div key=${i} onClick=${()=>go('product',INSTA_P[i])}>
        <${Img} src=${src} alt=${'Obsession Beauty Lifestyle '+(i+1)} ratio="1/1" fit="cover"/>
      </div>`)}
    </div>
  </div>`;
}

function Home(){
  const{go}=useContext(X);
  const[i,si]=useState(0);
  useEffect(()=>{const t=setInterval(()=>si(x=>(x+1)%3),5000);return()=>clearInterval(t)},[]);
  const H=HERO_SLIDES[i];
  return html`<div>
    <section className="hero">
      <${Img} src=${H[3]} alt=${H[1]} priority=${i==0} fit="cover" className="hero-bg"/>
      <div className="hero-ov"/>
      <div className="w hero-content">
        <div>
          <small style=${{letterSpacing:'.2em',textTransform:'uppercase'}}>${H[0]}</small>
          <h1>${H[1]}</h1>
          <p>${H[2]}</p>
          <a className="btn l" onClick=${()=>go('shop',H[4])}>Shop Now</a>
        </div>
      </div>
      <div className="dots">${[0,1,2].map(k=>html`<button key=${k} className=${k==i?'on':''} aria-label=${'Slide '+(k+1)} onClick=${()=>si(k)}/>`)}</div>
    </section>
    <div className="w">
      <${Perks}/>
      <div className="cats">
        ${CATS.map((c,k)=>html`<a className="cat" key=${c} onClick=${()=>go('shop',{cat:c})}>
          <div className="cat-img"><${Img} src=${CAT_IMGS[k]} alt=${c} ratio="1/1" fit="cover"/></div>
          <span>${c}</span>
        </a>`)}
      </div>
      <div className="sec">
        <${Hd} t="New Arrivals" s="The latest beauty finds, fresh and exciting." l="View All" a=${['shop',{tag:'new'}]}/>
        <${Row} items=${P.filter(p=>p.tag).concat(P.filter(p=>!p.tag).slice(0,4))}/>
      </div>
    </div>
    <div className="trust">
      <h2>Authentic. Affordable. Always.</h2>
      <div>${['Fast Delivery','Free Returns','100% Authentic Products','Easy Checkout','Secure Payment','Money Guarantee'].map(t=>html`<span key=${t}>✓ ${t}</span>`)}</div>
    </div>
    <div className="w">
      <${Tabs}/>
      <div className="sec">
        <${Hd} t="Shop Fragrances" s="Find your signature scent." l="View All" a=${['shop',{cat:'Fragrance'}]}/>
        <${Row} items=${P.filter(p=>p.cat=='Fragrance')}/>
      </div>
      <div className="sec" style=${{paddingTop:0}}>
        <${Hd} t="Makeup" s="Elevate your look with essentials that highlight your natural beauty." l="View All" a=${['shop',{cat:'Makeup'}]}/>
        <${Row} items=${P.filter(p=>p.cat=='Makeup')}/>
      </div>
      <${Sig}/>
      <div className="ban">
        ${BANS.map(b=>html`<div key=${b[0]} className="bn" onClick=${()=>go('shop',{cat:b[3]})}>
          <${Img} src=${b[2]} alt=${b[0]} fit="cover" className="bn-bg"/>
          <div className="bn-ov"/>
          <div className="bn-ct">
            <h3>${b[0]}</h3>
            <p style=${{margin:'6px 0 14px',opacity:.9}}>${b[1]}</p>
            <span className="btn l" style=${{alignSelf:'flex-start'}}>Explore</span>
          </div>
        </div>`)}
      </div>
      <div className="sec">
        <${Hd} t="Gifts & Value Sets" s="Share the joy of beauty with curated gift sets." l="View All" a=${['shop',{cat:'Gift Sets'}]}/>
        <${Row} items=${P.filter(p=>p.cat=='Gift Sets'||p.price<2.5)}/>
      </div>
      <${Quotes}/>
      <${Stats}/>
      <div className="sec" style=${{paddingTop:0}}>
        <${Hd} t="Shop By Brands" l="Shop All Brands" a=${['shop',{}]}/>
        <div className="brands">${BR.map(b=>html`<a key=${b} onClick=${()=>go('shop',{brand:b})}>${T(b).toUpperCase()}</a>`)}</div>
      </div>
      <${Insta}/>
      <div className="sec" style=${{paddingTop:0}}>
        <${Hd} t="Our Blog Posts" l="View All Posts" a=${['blog']}/>
        <${Posts} n=${3}/>
      </div>
    </div>
    <${News}/>
  </div>`;
}

function Posts({n}){
  const{go}=useContext(X);
  return html`<div className="posts">
    ${B.slice(0,n).map((b,i)=>html`<div className="post" key=${i} onClick=${()=>go('post',i)}>
      <div className="post-img"><${Img} src=${b[4]} alt=${b[0]} ratio="16/9" fit="cover"/></div>
      <small>${b[1]} · ${b[2]}</small>
      <h3>${b[0]}</h3>
      <p>${T(b[3][0]).slice(0,110)}…</p>
      <b style=${{fontSize:12,textDecoration:'underline'}}>Read More</b>
    </div>`)}
  </div>`;
}

function Shop(){
  const{go,route}=useContext(X);
  const a=route.a||{};
  const[cat,sc]=useState(a.cat||'All');
  const[br,sb]=useState(a.brand||'All');
  const[mx,sm]=useState(15);
  const[so,ss]=useState('rel');
  const[pg,sp]=useState(1);
  const[fo,sf]=useState(false);
  useEffect(()=>{sc(a.cat||'All');sb(a.brand||'All');sp(1)},[route]);
  let L=P.filter(p=>(cat=='All'||p.cat==cat)&&(br=='All'||p.brand==br)&&p.price<=mx&&(!a.tag||(a.tag=='new'?p.tag:p.rating>=4.5))&&(!a.q||(p.name+p.brand+p.cat).toLowerCase().includes(a.q.toLowerCase())));
  if(so=='lo')L=[...L].sort((x,y)=>x.price-y.price);
  if(so=='hi')L=[...L].sort((x,y)=>y.price-x.price);
  if(so=='az')L=[...L].sort((x,y)=>x.name.localeCompare(y.name));
  const n=Math.ceil(L.length/12)||1,pgc=Math.min(pg,n),V=L.slice((pgc-1)*12,pgc*12);
  const title=a.q?T('Results for')+' “'+a.q+'”':a.tag=='new'?'New Arrivals':a.tag=='best'?'Best Sellers':a.brand||a.cat||'All Products';
  return html`<div className="w">
    <div className="bc"><a onClick=${()=>go('home')}>Home</a> / Collection / ${title}</div>
    <div className="cl"><h1>${title}</h1><p>Browse authentic products at Obsession. Every product is sourced from official distributors.</p></div>
    <div className="tb"><button className="btn o fbtn" onClick=${()=>sf(!fo)}>Filter</button><span style=${{color:'var(--mut)'}}>${L.length} products</span><label>Sort by: <select value=${so} onChange=${e=>ss(e.target.value)}><option value="rel">Most relevant</option><option value="lo">Price: low to high</option><option value="hi">Price: high to low</option><option value="az">Name A–Z</option></select></label></div>
    <div className="shop"><aside className=${'fl'+(fo?' show':'')}><h4 style=${{marginTop:0}}>Category</h4>${['All',...CATS].map(c=>html`<label key=${c}><input type="radio" name="c" checked=${cat==c} onChange=${()=>{sc(c);sp(1)}}/> ${c}</label>`)}<h4>Brand</h4><select value=${br} onChange=${e=>{sb(e.target.value);sp(1)}}><option>All</option>${BR.map(b=>html`<option key=${b}>${b}</option>`)}</select><h4>Max price: ${mx} KWD</h4><input type="range" min="1" max="15" step=".5" value=${mx} onChange=${e=>{sm(+e.target.value);sp(1)}} style=${{width:'100%'}}/></aside>
    <div>${V.length?html`<div className="grid">${V.map(p=>html`<${Card} key=${p.id} p=${p}/>`)}</div>`:html`<div className="ctr"><h3>No products found</h3><p style=${{color:'var(--mut)',margin:'8px 0 16px'}}>Try changing your filters.</p><a className="btn" onClick=${()=>{sc('All');sb('All');sm(15);go('shop',{})}}>Reset</a></div>`}
    ${n>1&&html`<div className="pg">${Array.from({length:n},(_,k)=>html`<button key=${k} className=${pgc==k+1?'on':''} onClick=${()=>{sp(k+1);window.scrollTo(0,0)}}>${k+1}</button>`)}</div>`}</div></div></div>`;
}

function Product(){
  const{go,route,add,wish,tw}=useContext(X);
  const p=P[route.a];
  const[s,ss]=useState(0);
  const[q,sq]=useState(1);
  const[rv,sr]=useState([['Amira K.',5,'Beautiful quality and arrived quickly. Will order again!'],['Noor S.',4,'Lovely finish and long lasting.']]);
  const[wr,sw]=useState(false);
  const[f,sf]=useState({n:'',r:5,t:''});
  useEffect(()=>{ss(0);sq(1)},[route]);
  return html`<div className="w">
    <div className="bc"><a onClick=${()=>go('home')}>Home</a> / <a onClick=${()=>go('shop',{cat:p.cat})}>${p.cat}</a> / ${p.name}</div>
    <div className="pd">
      <div className="gal">
        <div className="th">
          ${p.images.map((imgSrc,k)=>html`<button key=${k} className=${s==k?'on':''} aria-label=${'Shade '+(k+1)} onClick=${()=>ss(k)}>
            <${Img} src=${imgSrc} alt=${p.name+' '+(k+1)} ratio="4/5" fit="contain"/>
          </button>`)}
        </div>
        <div className="mn">
          <${Img} src=${p.images[s]} alt=${p.name} ratio="4/5" fit="contain" priority=${true} className="mn-img"/>
        </div>
      </div>
      <div>
        <small style=${{color:'var(--mut)'}}>Brand: <a style=${{color:'var(--acc)'}} onClick=${()=>go('shop',{brand:p.brand})}>${p.brand}</a> · SKU: OBS-${1000+p.id}</small>
        <h1>${p.name}</h1>
        <div><${Stars} r=${p.rating}/> <small>(${rv.length} reviews)</small></div>
        <div className="p">${money(p.price)}</div>
        <p>Shade: <b>0${s+1}</b></p>
        <div className="sh">
          ${p.shades.map((x,k)=>html`<button key=${k} className=${s==k?'on':''} style=${{background:x}} aria-label=${'Shade '+(k+1)} onClick=${()=>ss(k)}/>`)}
        </div>
        <p style=${{color:'#0a8a4c',fontSize:13}}>${p.stock<5?T('Hurry up, only')+' '+p.stock+' '+T('items left in stock.'):'In stock and ready to ship.'}</p>
        <div className="bar2"><i style=${{width:Math.min(100,p.stock*12)+'%'}}/></div>
        <div className="ar">
          <div className="qt"><button aria-label="Decrease" onClick=${()=>sq(Math.max(1,q-1))}>−</button><span>${q}</span><button aria-label="Increase" onClick=${()=>sq(Math.min(p.stock,q+1))}>+</button></div>
          <a className="btn o" onClick=${()=>add(p,s,q)}>Add To Cart</a>
          <button className="ic" style=${{border:'1px solid var(--line)',color:wish.includes(p.id)?'var(--acc)':''}} aria-label="Wishlist" onClick=${()=>tw(p.id)}>${wish.includes(p.id)?'♥':'♡'}</button>
        </div>
        <a className="btn f" onClick=${()=>{add(p,s,q,true);go('checkout')}}>Buy It Now</a>
        <div className="bx"><b style=${{color:'var(--fg)'}}>Payment & Security</b><p style=${{margin:'6px 0'}}>We accept KNET, Visa, Mastercard and Cash on Delivery. Your payment information is processed securely.</p></div>
        <p style=${{fontSize:13}}>${['100% Authentic Products','Easy Returns','Secure Checkout'].map(x=>html`<span key=${x} style=${{marginInlineEnd:16}}>✓ ${x}</span>`)}</p>
        <div style=${{marginTop:20}}>
          <${Acc} t="Description">${p.name}<br/>A bestselling essential with a premium finish, designed for everyday wear and long-lasting results.<//>
          <${Acc} t="Shipping & Return">Free delivery on orders above 25 KWD. Standard delivery takes 1–3 working days. Unopened items can be returned within 14 days.<//>
          <${Acc} t="Product Specifications">Brand: ${p.brand} · Category: ${p.cat} · Shades: 4 · Origin: Imported<//>
          <${Acc} t=${T('About')+' '+T(p.brand)}>${p.brand} is one of the trusted names available exclusively at Obsession.<//>
        </div>
      </div>
    </div>
    <div style=${{borderTop:'1px solid var(--line)',padding:'30px 0'}}><div className="hd"><h2>Customer Reviews</h2><a className="btn r" onClick=${()=>sw(!wr)}>Write a review</a></div>
    ${wr&&html`<div className="bx"><input className="in" placeholder="Your name" value=${f.n} onChange=${e=>sf({...f,n:e.target.value})}/><select className="in" style=${{margin:'8px 0'}} value=${f.r} onChange=${e=>sf({...f,r:+e.target.value})}>${[5,4,3,2,1].map(x=>html`<option key=${x} value=${x}>${x} stars</option>`)}</select><textarea className="in" rows="3" placeholder="Your review" value=${f.t} onChange=${e=>sf({...f,t:e.target.value})}/><a className="btn" style=${{marginTop:10}} onClick=${()=>{if(f.n&&f.t){sr([[f.n,f.r,f.t],...rv]);sf({n:'',r:5,t:''});sw(false)}}}>Submit</a></div>`}
    ${rv.map((r,k)=>html`<div className="rv" key=${k}><b>${r[0]}</b> <${Stars} r=${r[1]}/><p style=${{color:'var(--mut)'}}>${r[2]}</p></div>`)}</div>
    <div className="sec"><${Hd} t="You may also like"/><${Row} items=${P.filter(x=>x.cat==p.cat&&x.id!=p.id).concat(P.filter(x=>x.cat!=p.cat)).slice(0,8)}/></div>
    <div style=${{maxWidth:700,margin:'0 auto 30px'}}><div className="hd"><h2 style=${{margin:'auto'}}>Discover more in our FAQ</h2></div><${Acc} t="Are your products authentic?">Yes, all products are 100% authentic and sourced from trusted distributors.<//><${Acc} t="How long does delivery take?">Usually 1–3 working days within Kuwait.<//><${Acc} t="Can I return or exchange my order?">Yes, unopened items can be returned within 14 days.<//><${Acc} t="What payment methods do you accept?">KNET, Visa, Mastercard and Cash on Delivery.<//></div>
  </div>`;
}

function Checkout(){
  const{cart,go,clear}=useContext(X);
  const[o,so]=useState(null);
  const sub=cart.reduce((s,i)=>s+P[i.id].price*i.q,0),sh=sub>=25||!sub?0:1.5;
  if(o)return html`<div className="ctr"><h1 style=${{fontSize:32}}>Thank you! ✓</h1><p style=${{margin:'10px 0 20px',color:'var(--mut)'}}>Your order <b>${o}</b> has been placed. A confirmation will be sent to your email.</p><a className="btn" onClick=${()=>go('home')}>Continue Shopping</a></div>`;
  if(!cart.length)return html`<div className="ctr"><h2>Your cart is empty</h2><br/><a className="btn" onClick=${()=>go('shop',{})}>Start Shopping</a></div>`;
  return html`<div className="w"><div className="bc">Checkout</div><form className="ck" onSubmit=${e=>{e.preventDefault();so('OBS-'+Math.floor(100000+Math.random()*900000));clear()}}><div><h2 style=${{marginBottom:14}}>Delivery details</h2><div className="fm"><input className="in" required placeholder="First name"/><input className="in" required placeholder="Last name"/><input className="in full" type="email" required placeholder="Email"/><input className="in full" required placeholder="Phone (+965)"/><input className="in full" required placeholder="Address (Block, Street, House)"/><input className="in" required placeholder="City"/><input className="in" placeholder="Area"/></div><h3 style=${{margin:'22px 0 8px'}}>Payment</h3>${['KNET','Credit / Debit Card','Cash on Delivery'].map((m,k)=>html`<label key=${m} style=${{display:'block',padding:'10px 14px',border:'1px solid var(--line)',borderRadius:10,margin:'6px 0'}}><input type="radio" name="pay" defaultChecked=${k==0}/> ${m}</label>`)}</div>
  <div className="sm">
    <h3>Order summary</h3>
    ${cart.map(i=>{
      const p=P[i.id];
      return html`<div key=${i.k} style=${{display:'flex',alignItems:'center',gap:12,margin:'10px 0'}}>
        <${Img} src=${p.images[i.shade]} alt=${p.name} ratio="1/1" fit="contain" style=${{width:46,height:46,borderRadius:8,background:'var(--bg)',padding:3,flex:'none'}}/>
        <div style=${{flex:1,fontSize:13}}>
          <div><b>${p.name}</b></div>
          <small style=${{color:'var(--mut)'}}>Shade 0${i.shade+1} × ${i.q}</small>
        </div>
        <span style=${{fontWeight:600}}>${money(p.price*i.q)}</span>
      </div>`;
    })}
    <hr style=${{border:0,borderTop:'1px solid var(--line)',margin:'10px 0'}}/>
    <p><span>Subtotal</span><span>${money(sub)}</span></p>
    <p><span>Delivery</span><span>${sh?money(sh):'Free'}</span></p>
    <p><b>Total</b><b>${money(sub+sh)}</b></p>
    <button className="btn r f">Place Order</button>
  </div></form></div>`;
}

function Blog(){
  const{go}=useContext(X);
  return html`<div className="w"><div className="bc"><a onClick=${()=>go('home')}>Home</a> / Blog</div><div className="cl"><h1>The Obsession Blog</h1><p>Beauty guides, product knowledge and stories from our team.</p></div><div style=${{paddingBottom:40}}><${Posts} n=${4}/></div></div>`;
}

function PostPg(){
  const{go,route}=useContext(X);
  const b=B[route.a];
  return html`<div className="w">
    <div className="bc"><a onClick=${()=>go('home')}>Home</a> / <a onClick=${()=>go('blog')}>Blog</a> / ${b[0]}</div>
    <div className="post-body">
      <small style=${{color:'var(--mut)',textTransform:'uppercase'}}>${b[1]} · ${b[2]}</small>
      <h1 style=${{fontSize:32,margin:'8px 0 18px',lineHeight:1.2}}>${b[0]}</h1>
      <div className="post-header-img"><${Img} src=${b[4]} alt=${b[0]} ratio="16/9" fit="cover" priority=${true}/></div>
      ${b[3].map((t,i)=>html`<p key=${i}>${t}</p>`)}
      <a className="btn o" onClick=${()=>go('blog')}>← Back to blog</a>
    </div>
    <div className="sec"><${Hd} t="Related products"/><${Row} items=${P.slice(route.a*3,route.a*3+6)}/></div>
  </div>`;
}

function About(){
  const{go}=useContext(X);
  return html`<div className="w"><div className="bc">About</div><div className="cl"><h1>About Obsession</h1><p>A trusted beauty destination built on authenticity, service and care.</p></div><div className="post-body" style=${{paddingBottom:40}}><p>Since 2006 we have connected customers with genuine international products at fair prices. Our team hand-picks every brand, works directly with official distributors and stands behind each order with easy returns and fast delivery.</p><p>From everyday skincare to statement fragrances, Obsession exists to make beauty simple, trustworthy and a little bit addictive.</p><a className="btn" onClick=${()=>go('shop',{})}>Shop the collection</a></div></div>`;
}

function Contact(){
  const[d,sd]=useState(false);
  return html`<div className="w"><div className="bc">Contact Us</div><div className="cl"><h1>Contact Us</h1><p>We usually reply within one working day.</p></div><div style=${{maxWidth:600,paddingBottom:40}}>${d?html`<p style=${{color:'#0a8a4c',fontWeight:600}}>Message sent. Thank you for reaching out!</p>`:html`<form className="fm" onSubmit=${e=>{e.preventDefault();sd(true)}}><input className="in" required placeholder="Name"/><input className="in" type="email" required placeholder="Email"/><textarea className="in full" rows="5" required placeholder="How can we help?" style=${{borderRadius:14}}/><button className="btn full" style=${{gridColumn:'1/-1'}}>Send Message</button></form>`}</div></div>`;
}

function Wish(){
  const{wish,go}=useContext(X);
  const L=P.filter(p=>wish.includes(p.id));
  return html`<div className="w"><div className="bc">Wishlist</div><div className="cl"><h1>My Wishlist</h1></div>${L.length?html`<div className="grid" style=${{paddingBottom:40}}>${L.map(p=>html`<${Card} key=${p.id} p=${p}/>`)}</div>`:html`<div className="ctr"><p>No saved items yet.</p><br/><a className="btn" onClick=${()=>go('shop',{})}>Browse products</a></div>`}</div>`;
}

function Drawer(){
  const{cart,setCart,setOpen,go}=useContext(X);
  const sub=cart.reduce((s,i)=>s+P[i.id].price*i.q,0),left=Math.max(0,25-sub);
  const up=(k,d)=>setCart(c=>c.map(i=>i.k==k?{...i,q:i.q+d}:i).filter(i=>i.q>0));
  return html`<div className="dr" onClick=${()=>setOpen(false)}><div className="dw" onClick=${e=>e.stopPropagation()}><div className="hd"><h2>Your Cart</h2><button className="ic" aria-label="Close" onClick=${()=>setOpen(false)}>✕</button></div><p style=${{fontSize:12,marginBottom:6}}>${left?T('Add')+' '+money(left)+' '+T('more for free delivery'):'You’ve unlocked free delivery 🎉'}</p><div className="bar2"><i style=${{width:Math.min(100,sub/25*100)+'%'}}/></div>
  <div className="li">${cart.length?cart.map(i=>{
    const p=P[i.id];
    return html`<div className="ci" key=${i.k}>
      <${Img} src=${p.images[i.shade]} alt=${p.name} ratio="1/1" fit="contain" className="ci-img"/>
      <div><b>${p.name}</b><br/><small>Shade 0${i.shade+1}</small><br/><span className="pr">${money(p.price)}</span></div>
      <div className="qt"><button aria-label="Less" onClick=${()=>up(i.k,-1)}>−</button><span>${i.q}</span><button aria-label="More" onClick=${()=>up(i.k,1)}>+</button></div>
    </div>`;
  }):html`<p className="ctr" style=${{color:'var(--mut)'}}>Your cart is empty.</p>`}</div>
  <p style=${{display:'flex',justifyContent:'space-between',margin:'14px 0'}}><b>Subtotal</b><b>${money(sub)}</b></p><a className="btn f" onClick=${()=>go('checkout')}>Checkout</a></div></div>`;
}

function App(){
  const[route,setR]=useState({p:'home',a:null}),[cart,setCart]=useState(()=>ld('obs_cart',[])),[wish,setW]=useState(()=>ld('obs_wish',[])),[open,setOpen]=useState(false),[menu,setMenu]=useState(false),[toast,setT]=useState(''),[q,sq]=useState(''),[lang,sl]=useState(LANG);
  LANG=lang;
  useEffect(()=>sv('obs_cart',cart),[cart]);
  useEffect(()=>{sv('obs_lang',lang);document.documentElement.lang=lang;document.documentElement.dir=lang=='ar'?'rtl':'ltr'},[lang]);
  useEffect(()=>sv('obs_wish',wish),[wish]);
  useEffect(()=>{if(toast){const t=setTimeout(()=>setT(''),2200);return()=>clearTimeout(t)}},[toast]);
  const go=(p,a=null)=>{setR({p,a});setMenu(false);setOpen(false);window.scrollTo(0,0)};
  const add=(p,shade,n=1,silent)=>{setCart(c=>{const k=p.id+'-'+shade,f=c.find(x=>x.k==k);return f?c.map(x=>x.k==k?{...x,q:x.q+n}:x):[...c,{k,id:p.id,shade,q:n}]});if(!silent)setT(T(p.name)+' — '+T('added to cart'))};
  const tw=id=>setW(w=>w.includes(id)?w.filter(x=>x!=id):[...w,id]);
  const n=cart.reduce((s,i)=>s+i.q,0);
  const V={home:Home,shop:Shop,product:Product,checkout:Checkout,blog:Blog,post:PostPg,about:About,contact:Contact,wish:Wish}[route.p];
  const NAV=[['Home',['home']],['New Arrivals',['shop',{tag:'new'}]],['Best Sellers',['shop',{tag:'best'}]],...CATS.map(c=>[c,['shop',{cat:c}]]),['Blog',['blog']],['About',['about']],['Contact',['contact']]];
  return html`<${X.Provider} value=${{go,route,cart,setCart,wish,tw,add,open,setOpen,clear:()=>setCart([])}}>
  <div className="top"><div className="w"><span className="announcement">FREE Delivery on orders above 25 KWD!</span><button className="lang" aria-label="Language" onClick=${()=>sl(lang=='ar'?'en':'ar')}>${lang=='ar'?'English':'العربية'}</button></div></div>
  <header><div className="bar"><button className="ic burger" aria-label="Menu" onClick=${()=>setMenu(!menu)}>${menu?'✕':'☰'}</button><a className="logo" onClick=${()=>go('home')}><i/>OBSESSION</a>
  <form className="srch" onSubmit=${e=>{e.preventDefault();go('shop',{q})}}><input placeholder="What are you looking for?" value=${q} onChange=${e=>sq(e.target.value)} aria-label="Search"/><button className="ic" aria-label="Search">⌕</button></form>
  <button className="ic" aria-label="Wishlist" onClick=${()=>go('wish')}>♡${wish.length>0&&html`<b>${wish.length}</b>`}</button><button className="ic" aria-label="Cart" onClick=${()=>setOpen(true)}>🛍${n>0&&html`<b>${n}</b>`}</button></div>
  <div className="mobile-srch"><form className="srch" onSubmit=${e=>{e.preventDefault();go('shop',{q})}}><input placeholder="What are you looking for?" value=${q} onChange=${e=>sq(e.target.value)} aria-label="Search"/><button className="ic" aria-label="Search">⌕</button></form></div>
  <nav className=${menu?'menu-open':''}>${NAV.map(x=>html`<a key=${x[0]} className=${route.p==x[1][0]&&(!x[1][1]||x[1][1]==route.a)?'on':''} onClick=${()=>go(...x[1])}>${x[0]}</a>`)}</nav></header>
  <main><${V}/></main>
  <footer><div className="w"><div className="fg"><div className="ab"><b>About</b><p style=${{margin:'8px 0 12px',fontSize:13}}>Obsession is a trusted beauty destination built on authenticity, service and care. Since 2006 we have connected customers with genuine international products at fair prices.</p><a style=${{color:'#fff',textDecoration:'underline'}} onClick=${()=>go('about')}>Learn More</a></div>
  <div><h4>Quick Help</h4><a onClick=${()=>go('about')}>About Us</a><a onClick=${()=>go('contact')}>Contact Us</a><a onClick=${()=>go('blog')}>Blog</a></div><div><h4>Shop</h4><a onClick=${()=>go('shop',{})}>All products</a><a onClick=${()=>go('shop',{tag:'new'})}>New Arrivals</a><a onClick=${()=>go('shop',{cat:'Gift Sets'})}>Bundles</a></div><div><h4>Policies</h4><a>Terms of Service</a><a>Privacy Policy</a><a>Refund Policy</a><a>Shipping Policy</a></div><div><h4>Contact Information</h4><a>Tunisia St, Hawally, KW</a><a>hello@obsession.example</a><a>+965 0000 0000</a><a>10:00am – 10:00pm, All Week-long</a></div></div>
  <div className="cp"><span>© 2026 Obsession. All rights reserved.</span><span>KNET · Visa · Mastercard · Cash on Delivery</span></div></div></footer>
  ${open&&html`<${Drawer}/>`}${toast&&html`<div className="toast" role="status">${toast}</div>`}<//>`;
}

ReactDOM.createRoot(document.getElementById('root')).render(html`<${App}/>`);
