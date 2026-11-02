import os
import glob
import math
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageEnhance

ARTIFACT_DIR = r"C:\Users\Nexus Computer\.gemini\antigravity\brain\fbd25769-0ccf-41d8-a61e-46f9ca977ef5"
BASE_DIR = r"c:\Users\Nexus Computer\Downloads\obsession-react-vite\obsession-react"
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

for sub in ["products", "hero", "banners", "categories", "blog", "brands", "lifestyle"]:
    os.makedirs(os.path.join(PUBLIC_DIR, "images", sub), exist_ok=True)

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def blend(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def crop_and_resize(img, target_w, target_h):
    w, h = img.size
    target_ratio = target_w / target_h
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
        
    return img.resize((target_w, target_h), Image.Resampling.LANCZOS)

def save_webp(img, path, max_kb=200):
    quality = 90
    while quality >= 35:
        img.save(path, 'WEBP', quality=quality, method=6)
        size_kb = os.path.getsize(path) / 1024
        if size_kb <= max_kb:
            break
        quality -= 5
    size_kb = os.path.getsize(path) / 1024
    print(f"Saved {os.path.relpath(path, BASE_DIR)}: {img.size[0]}x{img.size[1]} ({size_kb:.1f} KB, q={quality})")
    return size_kb

def find_artifact(prefix):
    matches = glob.glob(os.path.join(ARTIFACT_DIR, f"{prefix}*.jpg"))
    if matches:
        return sorted(matches, key=os.path.getmtime)[-1]
    return None

def create_studio_bg(w, h, top_color=(252, 250, 248), bot_color=(235, 230, 224), spot_pos=(0.5, 0.45), spot_intensity=30):
    bg = Image.new('RGB', (w, h), top_color)
    draw = ImageDraw.Draw(bg)
    for y in range(h):
        t = y / h
        c = blend(top_color, bot_color, t * t)
        draw.line([(0, y), (w, y)], fill=c)
    
    spot = Image.new('L', (w, h), 0)
    sdraw = ImageDraw.Draw(spot)
    cx, cy = int(w * spot_pos[0]), int(h * spot_pos[1])
    rx, ry = int(w * 0.45), int(h * 0.4)
    sdraw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=spot_intensity)
    spot = spot.filter(ImageFilter.GaussianBlur(int(min(w, h) * 0.15)))
    
    enhancer = ImageEnhance.Brightness(bg)
    bright = enhancer.enhance(1.15)
    bg.paste(bright, (0, 0), spot)
    return bg

def add_contact_shadow(layer, cx, ground_y, rx, ry, opacity=0.45):
    w, h = layer.size
    shadow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    
    # Outer soft shadow
    sdraw.ellipse([cx - rx, ground_y - ry, cx + rx, ground_y + ry], fill=(20, 16, 12, int(255 * opacity * 0.5)))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=max(3, int(ry * 1.6))))
    
    # Inner contact shadow
    inner = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    idraw = ImageDraw.Draw(inner)
    idraw.ellipse([cx - int(rx * 0.65), ground_y - int(ry * 0.4), cx + int(rx * 0.65), ground_y + int(ry * 0.4)], fill=(10, 8, 6, int(255 * opacity)))
    inner = inner.filter(ImageFilter.GaussianBlur(radius=max(2, int(ry * 0.5))))
    
    layer.alpha_composite(shadow)
    layer.alpha_composite(inner)

def render_cylinder(draw, x1, y1, x2, y2, base_rgb, curve=12, highlight_ratio=0.35, cap_top=True):
    w = max(1, x2 - x1)
    for x in range(x1, x2):
        t = (x - x1) / w
        ambient = 0.62
        diffuse = math.sin(t * math.pi) * 0.38
        h_diff = abs(t - highlight_ratio)
        spec = math.exp(- (h_diff * h_diff) / 0.015) * 0.65
        rim = math.exp(- ((t - 0.95)**2) / 0.02) * 0.25
        
        factor = ambient + diffuse + spec + rim
        pixel_c = tuple(min(255, max(0, int(c * factor))) for c in base_rgb)
        
        if spec > 0.35:
            whiteness = (spec - 0.35) / 0.65
            pixel_c = blend(pixel_c, (255, 255, 255), whiteness * 0.85)
            
        draw.line([(x, y1), (x, y2)], fill=pixel_c)
        
    if cap_top:
        top_c = tuple(min(255, int(c * 1.15)) for c in base_rgb)
        draw.ellipse([x1, y1 - curve, x2, y1 + curve], fill=top_c)
    bot_c = tuple(int(c * 0.72) for c in base_rgb)
    draw.ellipse([x1, y2 - curve, x2, y2 + curve], fill=bot_c)

# -------------------------------------------------------------
# Process Generated Assets from Subagents
# -------------------------------------------------------------
print("--- Processing Generated Hero Assets ---")
hero_files = [
    ("hero_lipcare", "hero-1.webp", (1600, 700), 350),
    ("hero_fragrance", "hero-2.webp", (1600, 700), 350),
    ("hero_giftsets", "hero-3.webp", (1600, 700), 350)
]
for prefix, out_name, (tw, th), max_kb in hero_files:
    art = find_artifact(prefix)
    out_path = os.path.join(PUBLIC_DIR, "images", "hero", out_name)
    if art and os.path.exists(art):
        im = Image.open(art).convert('RGB')
        im = crop_and_resize(im, tw, th)
        save_webp(im, out_path, max_kb=max_kb)
    else:
        print(f"Warning: {prefix} artifact not found, generating fallback")
        bg = create_studio_bg(tw, th, (240, 235, 230), (210, 205, 195))
        save_webp(bg, out_path, max_kb=max_kb)

print("--- Processing Signature Asset ---")
sig_art = find_artifact("midnight_oud_signature")
sig_out = os.path.join(PUBLIC_DIR, "images", "lifestyle", "signature.webp")
if sig_art and os.path.exists(sig_art):
    im = Image.open(sig_art).convert('RGB')
    im = crop_and_resize(im, 900, 1100)
    save_webp(im, sig_out, max_kb=200)
else:
    print("Warning: midnight_oud_signature not found, generating fallback")
    bg = create_studio_bg(900, 1100, (40, 30, 25), (15, 12, 10))
    save_webp(bg, sig_out, max_kb=200)

print("--- Processing Banner Assets ---")
banner_specs = [
    ("banner_happy_glow", "banner-1.webp", (800, 1000)),
    ("banner_juicy_bomb", "banner-2.webp", (800, 1000)),
    ("banner_choco_lot", "banner-3.webp", (800, 1000)),
]
for prefix, out_name, (tw, th) in banner_specs:
    art = find_artifact(prefix)
    out_path = os.path.join(PUBLIC_DIR, "images", "banners", out_name)
    if art and os.path.exists(art):
        im = Image.open(art).convert('RGB')
        im = crop_and_resize(im, tw, th)
        save_webp(im, out_path, max_kb=200)

# Banner 4: Free Delivery (Luxury packaging / gift box / shopping bag)
b4_path = os.path.join(PUBLIC_DIR, "images", "banners", "banner-4.webp")
im = create_studio_bg(800, 1000, (248, 245, 242), (220, 212, 205), spot_pos=(0.5, 0.4))
layer = Image.new('RGBA', (800, 1000), (0, 0, 0, 0))
add_contact_shadow(layer, 400, 830, 280, 50, 0.45)
# Render luxury gift boxes and bag
draw = ImageDraw.Draw(layer)
# Shopping bag body
draw.polygon([(260, 480), (540, 480), (560, 820), (240, 820)], fill=(245, 242, 238, 255))
# Ribbon and shadow side
draw.polygon([(540, 480), (580, 510), (600, 810), (560, 820)], fill=(210, 205, 198, 255))
# Deep burgundy satin ribbon
draw.rectangle([385, 480, 415, 820], fill=(160, 24, 40, 255))
# Silk ribbon bow on bag
draw.ellipse([340, 440, 460, 490], fill=(180, 28, 48, 255))
draw.ellipse([365, 455, 435, 485], fill=(130, 18, 30, 255))
# Handles
draw.arc([350, 380, 450, 520], start=180, end=360, fill=(180, 28, 48, 255), width=8)
# Small luxury gift box beside it
draw.polygon([(160, 680), (320, 650), (320, 830), (160, 840)], fill=(230, 215, 200, 255))
draw.polygon([(320, 650), (360, 680), (360, 820), (320, 830)], fill=(195, 180, 165, 255))
draw.polygon([(160, 680), (200, 650), (360, 680), (320, 710)], fill=(245, 232, 220, 255))
draw.line([(240, 665), (240, 835)], fill=(180, 28, 48, 255), width=10)
im.paste(Image.alpha_composite(im.convert('RGBA'), layer).convert('RGB'))
save_webp(im, b4_path, max_kb=200)

print("--- Processing Category Assets ---")
cat_specs = [
    ("cat_makeup", "cat-1.webp"),
    ("cat_fragrance", "cat-2.webp"),
    ("cat_skincare", "cat-3.webp"),
]
for prefix, out_name in cat_specs:
    art = find_artifact(prefix)
    out_path = os.path.join(PUBLIC_DIR, "images", "categories", out_name)
    if art and os.path.exists(art):
        im = Image.open(art).convert('RGB')
        im = crop_and_resize(im, 400, 400)
        save_webp(im, out_path, max_kb=200)

# Categories 4, 5, 6
# Cat 4: Hair Care (Amber bottle with golden glow)
im4 = create_studio_bg(400, 400, (245, 240, 235), (220, 215, 205), spot_pos=(0.5, 0.45))
layer = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
add_contact_shadow(layer, 200, 340, 110, 24, 0.4)
draw = ImageDraw.Draw(layer)
render_cylinder(draw, 140, 160, 260, 335, (190, 120, 45), curve=16, highlight_ratio=0.35)
render_cylinder(draw, 175, 120, 225, 160, (25, 25, 25), curve=8, highlight_ratio=0.35)
render_cylinder(draw, 185, 95, 215, 120, (190, 150, 80), curve=6, highlight_ratio=0.35)
im4.paste(Image.alpha_composite(im4.convert('RGBA'), layer).convert('RGB'))
save_webp(im4, os.path.join(PUBLIC_DIR, "images", "categories", "cat-4.webp"), max_kb=200)

# Cat 5: Bath & Body (Frosted cream jar)
im5 = create_studio_bg(400, 400, (248, 246, 244), (225, 222, 218), spot_pos=(0.5, 0.45))
layer = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
add_contact_shadow(layer, 200, 330, 130, 26, 0.4)
draw = ImageDraw.Draw(layer)
render_cylinder(draw, 110, 210, 290, 325, (235, 228, 230), curve=20, highlight_ratio=0.32)
render_cylinder(draw, 105, 160, 295, 215, (215, 190, 160), curve=20, highlight_ratio=0.32)
im5.paste(Image.alpha_composite(im5.convert('RGBA'), layer).convert('RGB'))
save_webp(im5, os.path.join(PUBLIC_DIR, "images", "categories", "cat-5.webp"), max_kb=200)

# Cat 6: Gift Sets (Ribbon tied box)
im6 = create_studio_bg(400, 400, (250, 246, 245), (228, 220, 216), spot_pos=(0.5, 0.45))
layer = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
add_contact_shadow(layer, 200, 335, 140, 28, 0.42)
draw = ImageDraw.Draw(layer)
# Box body
draw.polygon([(100, 200), (300, 200), (290, 330), (110, 330)], fill=(240, 225, 220, 255))
# Ribbon cross
draw.rectangle([185, 200, 215, 330], fill=(170, 30, 50, 255))
draw.rectangle([105, 255, 295, 275], fill=(170, 30, 50, 255))
# Top lid
draw.polygon([(90, 175), (310, 175), (305, 205), (95, 205)], fill=(248, 238, 234, 255))
draw.rectangle([185, 175, 215, 205], fill=(170, 30, 50, 255))
# Bow
draw.ellipse([160, 145, 240, 185], fill=(185, 35, 55, 255))
draw.ellipse([180, 155, 220, 175], fill=(130, 20, 35, 255))
im6.paste(Image.alpha_composite(im6.convert('RGBA'), layer).convert('RGB'))
save_webp(im6, os.path.join(PUBLIC_DIR, "images", "categories", "cat-6.webp"), max_kb=200)

print("--- Processing Blog Assets ---")
blog_specs = [
    ("blog_boutique_trust", "blog-1.webp"),
    ("blog_perfume_guide", "blog-2.webp"),
]
for prefix, out_name in blog_specs:
    art = find_artifact(prefix)
    out_path = os.path.join(PUBLIC_DIR, "images", "blog", out_name)
    if art and os.path.exists(art):
        im = Image.open(art).convert('RGB')
        im = crop_and_resize(im, 1200, 800)
        save_webp(im, out_path, max_kb=200)

# Blog 3: How to spot authentic beauty
im_b3 = create_studio_bg(1200, 800, (246, 242, 238), (220, 214, 206), spot_pos=(0.48, 0.45))
layer = Image.new('RGBA', (1200, 800), (0, 0, 0, 0))
add_contact_shadow(layer, 550, 620, 380, 60, 0.35)
draw = ImageDraw.Draw(layer)
# Clean cosmetics packaging flatlay
draw.polygon([(300, 320), (750, 280), (780, 580), (330, 620)], fill=(245, 242, 238, 255))
draw.polygon([(750, 280), (840, 330), (870, 560), (780, 580)], fill=(215, 210, 202, 255))
render_cylinder(draw, 720, 380, 820, 590, (190, 80, 95), curve=14)
im_b3.paste(Image.alpha_composite(im_b3.convert('RGBA'), layer).convert('RGB'))
save_webp(im_b3, os.path.join(PUBLIC_DIR, "images", "blog", "blog-3.webp"), max_kb=200)

# Blog 4: Evening Skincare Routine
im_b4 = create_studio_bg(1200, 800, (238, 235, 230), (205, 200, 192), spot_pos=(0.52, 0.45))
layer = Image.new('RGBA', (1200, 800), (0, 0, 0, 0))
add_contact_shadow(layer, 600, 640, 420, 70, 0.38)
draw = ImageDraw.Draw(layer)
# Serum bottle, cream jar and mist bottle in calm evening tone
render_cylinder(draw, 360, 340, 460, 610, (195, 140, 70), curve=16)
render_cylinder(draw, 490, 430, 670, 620, (230, 225, 220), curve=22)
render_cylinder(draw, 700, 290, 790, 600, (180, 150, 190), curve=15)
im_b4.paste(Image.alpha_composite(im_b4.convert('RGBA'), layer).convert('RGB'))
save_webp(im_b4, os.path.join(PUBLIC_DIR, "images", "blog", "blog-4.webp"), max_kb=200)

print("--- Processing Lifestyle Assets ---")
l1_art = find_artifact("lifestyle_1")
l1_out = os.path.join(PUBLIC_DIR, "images", "lifestyle", "insta-1.webp")
if l1_art and os.path.exists(l1_art):
    im = Image.open(l1_art).convert('RGB')
    im = crop_and_resize(im, 600, 600)
    save_webp(im, l1_out, max_kb=200)

# Lifestyle 2..6: Instagram aesthetics
insta_configs = [
    ("insta-2.webp", (248, 240, 230), (220, 205, 190), (190, 110, 45), "bottle"),
    ("insta-3.webp", (245, 235, 238), (218, 195, 205), (205, 85, 110), "jar"),
    ("insta-4.webp", (235, 242, 245), (195, 210, 220), (70, 150, 180), "spray"),
    ("insta-5.webp", (242, 238, 245), (210, 200, 220), (150, 120, 185), "palette"),
    ("insta-6.webp", (248, 245, 238), (225, 215, 198), (180, 140, 70), "stick")
]
for fname, bg_top, bg_bot, prod_rgb, ptype in insta_configs:
    im = create_studio_bg(600, 600, bg_top, bg_bot, spot_pos=(0.5, 0.45))
    layer = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    add_contact_shadow(layer, 300, 480, 180, 38, 0.4)
    draw = ImageDraw.Draw(layer)
    if ptype == "bottle":
        render_cylinder(draw, 220, 200, 380, 470, prod_rgb, curve=20)
        render_cylinder(draw, 265, 140, 335, 200, (30, 30, 30), curve=10)
    elif ptype == "jar":
        render_cylinder(draw, 180, 290, 420, 470, prod_rgb, curve=28)
        render_cylinder(draw, 170, 230, 430, 295, (220, 210, 200), curve=28)
    elif ptype == "spray":
        render_cylinder(draw, 230, 170, 370, 470, prod_rgb, curve=18)
        render_cylinder(draw, 260, 110, 340, 170, (40, 40, 40), curve=10)
    elif ptype == "palette":
        draw.polygon([(180, 220), (420, 200), (440, 460), (160, 480)], fill=tuple(list(prod_rgb) + [255]))
        draw.ellipse([220, 270, 280, 330], fill=(240, 200, 190, 255))
        draw.ellipse([320, 260, 380, 320], fill=(180, 100, 80, 255))
        draw.ellipse([210, 370, 270, 430], fill=(220, 160, 140, 255))
        draw.ellipse([310, 360, 370, 420], fill=(130, 60, 50, 255))
    elif ptype == "stick":
        render_cylinder(draw, 250, 260, 350, 470, (30, 30, 30), curve=14)
        render_cylinder(draw, 262, 160, 338, 260, (210, 170, 90), curve=10)
        # Bullet
        draw.polygon([(265, 160), (335, 160), (325, 90), (280, 120)], fill=tuple(list(prod_rgb) + [255]))
    im.paste(Image.alpha_composite(im.convert('RGBA'), layer).convert('RGB'))
    save_webp(im, os.path.join(PUBLIC_DIR, "images", "lifestyle", fname), max_kb=200)

# -------------------------------------------------------------
# Generate 24 Products x 4 Images (p01-1.webp .. p24-4.webp)
# -------------------------------------------------------------
print("--- Generating 24 Products x 4 Angles/Shades ---")
SH = ['#e9a1a8', '#b5535f', '#d9a27c', '#8a4b3c', '#f2c9b8', '#7a3b5e']

PRODUCTS_META = [
    # [name, brand, cat, price, type, color]
    ['Matte Fresh Setting Spray', 'Obsession Lab', 'Makeup', 2.25, 'spray', '#f4d35e'],
    ['Pore No More Primer', 'Velvet Muse', 'Makeup', 2.5, 'tube', '#7fd1c7'],
    ['Liquid Lipstick Trio', 'Velvet Muse', 'Makeup', 3, 'stick', '#b5535f'],
    ['Face & Under Eye Powder', 'Lumière', 'Makeup', 2.75, 'jar', '#f2b8c6'],
    ['2-in-1 Brow Pencil', 'Obsession Lab', 'Makeup', 1.5, 'pencil', '#c9a66b'],
    ['Jazzy Eyeshadow Palette', 'Aura Noir', 'Makeup', 3, 'palette', '#a0643c'],
    ['Floral Flush Blush Palette', 'Velvet Muse', 'Makeup', 3.25, 'palette', '#e8788f'],
    ['Coconut Reed Diffuser', 'Maison Rouge', 'Fragrance', 3, 'bottle', '#e8d57a'],
    ['Midnight Oud Eau de Parfum', 'Oud & Co', 'Fragrance', 5.75, 'bottle', '#3a2a22'],
    ['Silver Mountain Parfum', 'Aura Noir', 'Fragrance', 5.75, 'bottle', '#9bb7d4'],
    ['Rose Noir Eau de Parfum', 'Maison Rouge', 'Fragrance', 6.5, 'bottle', '#b5304a'],
    ['Vanilla Room Spray', 'Lumière', 'Fragrance', 3.5, 'spray', '#f1d9a7'],
    ['Hydra Jelly Pocket Lip Jam', 'Velvet Muse', 'Makeup', 2, 'jar', '#e87a8f'],
    ['Vitamin C Glow Serum', 'Lumière', 'Skin Care', 4.5, 'spray', '#f4a73b'],
    ['Hydrating Cream SPF 30', 'Obsession Lab', 'Skin Care', 3.9, 'jar', '#bfe3f2'],
    ['Gentle Foaming Cleanser', 'Lumière', 'Skin Care', 2.8, 'tube', '#a8d8b9'],
    ['Repair Hair Mist', 'Aura Noir', 'Hair Care', 3.2, 'spray', '#c9a3e0'],
    ['Argan Hair Oil', 'Oud & Co', 'Hair Care', 4.25, 'bottle', '#d4943a'],
    ['Lavender Body Butter', 'Maison Rouge', 'Bath & Body', 3.75, 'jar', '#b9a3e3'],
    ['Shower Gel Vanilla Bean', 'Obsession Lab', 'Bath & Body', 2.25, 'tube', '#f1d9a7'],
    ['Purple Lavender Gift Set', 'Maison Rouge', 'Gift Sets', 5.75, 'set', '#a58bd6'],
    ['Glow Lip Kit', 'Velvet Muse', 'Gift Sets', 3.75, 'set', '#e87a8f'],
    ['Crystal Noir Parfum Set', 'Aura Noir', 'Gift Sets', 12.5, 'set', '#3b3b4f'],
    ['Pro Makeup Brush Set', 'Lumière', 'Makeup', 8.75, 'set', '#d9a27c']
]

def render_product_image(p_idx, shade_idx, shade_hex, p_type, p_name):
    w, h = 800, 1000 # 4:5 ratio
    rgb = hex_to_rgb(shade_hex)
    
    # Soft neutral studio background
    im = create_studio_bg(w, h, (252, 250, 248), (232, 228, 222), spot_pos=(0.5, 0.42), spot_intensity=35)
    layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    
    # Angle variation offsets
    # angle 0: front
    # angle 1: slight 3/4 turn (for card hover)
    # angle 2: close elevated view
    # angle 3: texture / open detail shot
    angle = shade_idx
    
    ground_y = 820
    cx = 400
    
    if p_type == 'spray':
        # Setting spray / mist bottle
        add_contact_shadow(layer, cx, ground_y, 190, 42, 0.45)
        bw = 180 if angle != 2 else 210
        bh = 460 if angle != 2 else 490
        bx1, bx2 = cx - bw//2, cx + bw//2
        by1, by2 = ground_y - bh, ground_y - 20
        # Translucent glass / tinted body
        render_cylinder(draw, bx1, by1, bx2, by2, rgb, curve=24, highlight_ratio=0.33)
        # Collar
        render_cylinder(draw, cx - 45, by1 - 50, cx + 45, by1, (20, 20, 20) if p_idx%2 else (210, 180, 110), curve=10)
        # Actuator / Nozzle
        render_cylinder(draw, cx - 35, by1 - 100, cx + 35, by1 - 50, (30, 30, 30) if p_idx%2 else (225, 195, 125), curve=8)
        # Cap: if angle == 3 (open view), cap resting beside
        if angle == 3:
            render_cylinder(draw, cx + 130, ground_y - 180, cx + 230, ground_y - 20, (240, 240, 245), curve=18)
        else:
            # Translucent cap on top
            cap_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
            cdraw = ImageDraw.Draw(cap_layer)
            render_cylinder(cdraw, cx - 48, by1 - 120, cx + 48, by1, (245, 245, 250), curve=12)
            layer.paste(cap_layer, (0, 0), cap_layer)

    elif p_type == 'tube':
        # Squeeze tube
        add_contact_shadow(layer, cx, ground_y, 170, 38, 0.42)
        tw = 210
        th = 480
        # Cap at bottom
        render_cylinder(draw, cx - 55, ground_y - 80, cx + 55, ground_y - 15, (230, 225, 220), curve=14)
        # Tube body tapering down to cap
        tx1, tx2 = cx - tw//2, cx + tw//2
        ty_top = ground_y - th
        ty_bot = ground_y - 80
        # draw crimp on top
        draw.rectangle([tx1 - 10, ty_top - 20, tx2 + 10, ty_top], fill=(int(rgb[0]*0.85), int(rgb[1]*0.85), int(rgb[2]*0.85), 255))
        # Tube body gradient
        for y in range(ty_top, ty_bot):
            prog = (y - ty_top) / (ty_bot - ty_top)
            cur_w = int(tw * (1.0 - 0.48 * prog * prog))
            x_l = cx - cur_w // 2
            x_r = cx + cur_w // 2
            for x in range(x_l, x_r):
                t = (x - x_l) / max(1, (x_r - x_l))
                factor = 0.65 + math.sin(t * math.pi) * 0.35 + math.exp(-((t - 0.35)**2)/0.02) * 0.5
                c = tuple(min(255, int(v * factor)) for v in rgb)
                draw.point((x, y), fill=c)

    elif p_type == 'stick':
        # Luxury lipstick / gloss
        add_contact_shadow(layer, cx, ground_y, 140, 32, 0.45)
        # Heavy metallic casing
        render_cylinder(draw, cx - 70, ground_y - 280, cx + 70, ground_y - 20, (25, 25, 25), curve=18)
        # Inner collar
        render_cylinder(draw, cx - 58, ground_y - 410, cx + 58, ground_y - 280, (215, 185, 110), curve=14)
        # Bullet
        bx1, bx2 = cx - 50, cx + 50
        by_base = ground_y - 410
        by_tip = ground_y - 560
        render_cylinder(draw, bx1, by_tip + 50, bx2, by_base, rgb, curve=12)
        # Angled tear-drop tip
        draw.polygon([(bx1, by_tip + 50), (bx2, by_tip + 50), (bx2 - 20, by_tip), (bx1 + 10, by_tip + 20)], fill=tuple(list(rgb) + [255]))
        # If angle 3: add swatch smear on base
        if angle == 3:
            draw.ellipse([cx - 180, ground_y - 70, cx - 40, ground_y - 30], fill=tuple(list(rgb) + [230]))

    elif p_type == 'jar':
        # Frosted glass luxury cosmetic jar
        add_contact_shadow(layer, cx, ground_y, 220, 48, 0.46)
        jw = 340
        jh = 240
        jx1, jx2 = cx - jw//2, cx + jw//2
        jy1, jy2 = ground_y - jh, ground_y - 20
        # Frosted glass body with inner cream
        render_cylinder(draw, jx1, jy1, jx2, jy2, rgb, curve=36, highlight_ratio=0.32)
        # Screw lid
        render_cylinder(draw, jx1 - 10, jy1 - 85, jx2 + 10, jy1 + 5, (230, 220, 210) if p_idx%2 else (30, 30, 30), curve=38, highlight_ratio=0.32)

    elif p_type == 'pencil':
        # Dual-ended brow pencil
        add_contact_shadow(layer, cx, ground_y, 160, 26, 0.35)
        # Diagonal / standing sleek body
        render_cylinder(draw, cx - 18, ground_y - 600, cx + 18, ground_y - 60, (28, 28, 28), curve=6)
        # Gold ferrules
        render_cylinder(draw, cx - 20, ground_y - 120, cx + 20, ground_y - 60, (215, 185, 105), curve=6)
        render_cylinder(draw, cx - 20, ground_y - 560, cx + 20, ground_y - 500, (215, 185, 105), curve=6)
        # Colored precision tip
        draw.polygon([(cx - 14, ground_y - 600), (cx + 14, ground_y - 600), (cx, ground_y - 660)], fill=tuple(list(rgb) + [255]))

    elif p_type == 'palette':
        # Multi-pan compact palette
        add_contact_shadow(layer, cx, ground_y, 240, 50, 0.42)
        # Perspective angled compact
        draw.polygon([(cx - 220, ground_y - 340), (cx + 220, ground_y - 360), (cx + 260, ground_y - 50), (cx - 180, ground_y - 30)], fill=(32, 28, 26, 255))
        # Inner tray
        draw.polygon([(cx - 195, ground_y - 320), (cx + 200, ground_y - 338), (cx + 238, ground_y - 68), (cx - 158, ground_y - 50)], fill=(45, 40, 38, 255))
        # 6 powder pans inside
        pan_coords = [
            (-120, -260), (0, -270), (120, -280),
            (-95, -160), (25, -170), (145, -180)
        ]
        for k, (px, py) in enumerate(pan_coords):
            cur_c = rgb if k == angle else hex_to_rgb(SH[(k + p_idx) % 6])
            draw.ellipse([cx + px - 38, ground_y + py - 24, cx + px + 38, ground_y + py + 24], fill=tuple(list(cur_c) + [255]))

    elif p_type == 'bottle':
        # Perfume / Diffuser / Hair Oil flacon
        add_contact_shadow(layer, cx, ground_y, 200, 44, 0.46)
        bw = 250
        bh = 380
        bx1, bx2 = cx - bw//2, cx + bw//2
        by1, by2 = ground_y - bh, ground_y - 20
        # Heavy crystal base & flacon
        render_cylinder(draw, bx1, by1, bx2, by2, rgb, curve=30, highlight_ratio=0.3)
        # Metallic neck
        render_cylinder(draw, cx - 45, by1 - 50, cx + 45, by1, (215, 185, 110), curve=12)
        # Cap
        render_cylinder(draw, cx - 65, by1 - 160, cx + 65, by1 - 50, (25, 25, 25) if p_idx%2 else (230, 200, 120), curve=16)
        # If reed diffuser (Coconut Reed Diffuser)
        if 'Diffuser' in p_name:
            for angle_offset in [-25, -15, -5, 8, 18, 28]:
                rad = math.radians(angle_offset)
                x_end = cx + int(math.sin(rad) * 450)
                y_end = by1 - int(math.cos(rad) * 450)
                draw.line([(cx, by1 - 50), (x_end, y_end)], fill=(210, 185, 145, 255), width=7)

    elif p_type == 'set':
        # Gift Set / Brush Set
        add_contact_shadow(layer, cx, ground_y, 260, 52, 0.44)
        if 'Brush' in p_name:
            # Luxury makeup brushes
            for bi, bx_off in enumerate([-120, -60, 0, 60, 120]):
                bcx = cx + bx_off
                cur_rgb = rgb if bi == angle else hex_to_rgb(SH[bi%6])
                render_cylinder(draw, bcx - 14, ground_y - 420, bcx + 14, ground_y - 30, (24, 24, 24), curve=6)
                render_cylinder(draw, bcx - 16, ground_y - 520, bcx + 16, ground_y - 420, (215, 185, 110), curve=6)
                # Bristles
                draw.polygon([(bcx - 22, ground_y - 520), (bcx + 22, ground_y - 520), (bcx + 15, ground_y - 640), (bcx - 15, ground_y - 640)], fill=tuple(list(cur_rgb) + [255]))
        else:
            # Luxury rigid gift box with satin ribbon
            draw.polygon([(cx - 240, ground_y - 380), (cx + 240, ground_y - 380), (cx + 220, ground_y - 30), (cx - 220, ground_y - 30)], fill=tuple(list(rgb) + [255]))
            # Ribbon
            draw.rectangle([cx - 30, ground_y - 380, cx + 30, ground_y - 30], fill=(245, 240, 235, 255))
            draw.rectangle([cx - 230, ground_y - 220, cx + 230, ground_y - 180], fill=(245, 240, 235, 255))
            # Bow
            draw.ellipse([cx - 70, ground_y - 440, cx + 70, ground_y - 370], fill=(255, 250, 245, 255))
            draw.ellipse([cx - 40, ground_y - 425, cx + 40, ground_y - 385], fill=(210, 205, 200, 255))

    im.paste(Image.alpha_composite(im.convert('RGBA'), layer).convert('RGB'))
    return im

total_prod_images = 0
for idx, r in enumerate(PRODUCTS_META):
    p_num = f"{idx+1:02d}"
    shades = [r[5], SH[idx%6], SH[(idx+2)%6], SH[(idx+4)%6]]
    for s_idx, shade in enumerate(shades):
        out_name = f"p{p_num}-{s_idx+1}.webp"
        out_path = os.path.join(PUBLIC_DIR, "images", "products", out_name)
        prod_im = render_product_image(idx, s_idx, shade, r[4], r[0])
        save_webp(prod_im, out_path, max_kb=200)
        total_prod_images += 1

print(f"--- Completed generating {total_prod_images} product images ---")

# Summary check
all_webps = glob.glob(os.path.join(PUBLIC_DIR, "images", "**", "*.webp"), recursive=True)
print(f"Total webp images in public/images: {len(all_webps)}")
total_bytes = sum(os.path.getsize(p) for p in all_webps)
print(f"Total size of public/images: {total_bytes / (1024*1024):.2f} MB")
oversized = [p for p in all_webps if os.path.getsize(p) > (350*1024 if "hero" in p else 200*1024)]
if oversized:
    print(f"WARNING: Found {len(oversized)} oversized images: {oversized}")
else:
    print("ALL images strictly meet the <=200KB (hero <=350KB) size limit!")
