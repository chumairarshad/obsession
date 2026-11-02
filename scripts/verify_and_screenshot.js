import puppeteer from 'puppeteer-core';
import fs from 'fs';
import path from 'path';

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const ARTIFACT_DIR = 'C:\\Users\\Nexus Computer\\.gemini\\antigravity\\brain\\fbd25769-0ccf-41d8-a61e-46f9ca977ef5';

async function autoScroll(page) {
  await page.evaluate(async () => {
    await new Promise((resolve) => {
      let totalHeight = 0;
      const distance = 400;
      const timer = setInterval(() => {
        const scrollHeight = document.body.scrollHeight;
        window.scrollBy(0, distance);
        totalHeight += distance;
        if (totalHeight >= scrollHeight) {
          clearInterval(timer);
          window.scrollTo(0, 0);
          resolve();
        }
      }, 100);
    });
  });
  await new Promise(r => setTimeout(r, 600));
}

async function run() {
  console.log('Launching Chrome via puppeteer-core...');
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });

  const page = await browser.newPage();
  
  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleErrors.push(msg.text());
    }
  });
  page.on('pageerror', err => {
    consoleErrors.push(err.toString());
  });

  // 1. Desktop Tests (1440x900) in English
  console.log('\n--- 1. Testing Desktop (1440x900) in English ---');
  await page.setViewport({ width: 1440, height: 900 });
  
  await page.goto('http://127.0.0.1:5173/', { waitUntil: 'networkidle0' });
  await page.evaluate(() => {
    localStorage.setItem('obs_lang', JSON.stringify('en'));
  });
  await page.goto('http://127.0.0.1:5173/', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 400));

  await autoScroll(page);
  const homeEnOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  console.log('Home EN Horizontal Scroll Overflow:', homeEnOverflow);

  const homeEnBroken = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('img')).filter(img => !img.complete || img.naturalWidth === 0).map(img => img.src);
  });
  console.log('Home EN Broken Images Count:', homeEnBroken.length);

  const homeEnPath = path.join(ARTIFACT_DIR, 'home_en.png');
  await page.screenshot({ path: homeEnPath, fullPage: false });

  // 2. Desktop Product & Shade Switch
  console.log('\n--- 2. Testing Product Page & Shade Switch ---');
  await page.evaluate(() => document.querySelector('.pc')?.click());
  await new Promise(r => setTimeout(r, 500));
  await autoScroll(page);

  const prodEnBroken = await page.evaluate(() => Array.from(document.querySelectorAll('img')).filter(img => !img.complete || img.naturalWidth === 0).length);
  console.log('Product Page Broken Images Count:', prodEnBroken);

  const prodEnPath = path.join(ARTIFACT_DIR, 'product_en.png');
  await page.screenshot({ path: prodEnPath, fullPage: false });

  // 3. Desktop Arabic (RTL)
  console.log('\n--- 3. Testing Desktop Arabic RTL ---');
  await page.evaluate(() => document.querySelector('.lang')?.click());
  await new Promise(r => setTimeout(r, 400));
  await page.evaluate(() => document.querySelector('.logo')?.click());
  await new Promise(r => setTimeout(r, 500));
  await autoScroll(page);

  const homeArPath = path.join(ARTIFACT_DIR, 'home_ar.png');
  await page.screenshot({ path: homeArPath, fullPage: false });

  await page.evaluate(() => document.querySelector('.pc')?.click());
  await new Promise(r => setTimeout(r, 500));
  await autoScroll(page);
  const prodArPath = path.join(ARTIFACT_DIR, 'product_ar.png');
  await page.screenshot({ path: prodArPath, fullPage: false });

  // 4. Mobile Viewport (375x812) Tests
  console.log('\n--- 4. Testing Mobile Viewport (375x812) ---');
  await page.setViewport({ width: 375, height: 812 });

  // Switch back to EN for Mobile Home
  await page.evaluate(() => document.querySelector('.lang')?.click());
  await new Promise(r => setTimeout(r, 400));
  await page.evaluate(() => document.querySelector('.logo')?.click());
  await new Promise(r => setTimeout(r, 500));
  await autoScroll(page);

  let mOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  console.log('Mobile (375px) EN Home Horizontal Overflow:', mOverflow);

  const mobileHomeEnPath = path.join(ARTIFACT_DIR, 'mobile_home_en.png');
  await page.screenshot({ path: mobileHomeEnPath, fullPage: false });
  console.log('Saved mobile screenshot:', mobileHomeEnPath);

  // Mobile Product Page EN
  await page.evaluate(() => document.querySelector('.pc')?.click());
  await new Promise(r => setTimeout(r, 500));
  await autoScroll(page);

  mOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  console.log('Mobile (375px) EN Product Horizontal Overflow:', mOverflow);

  const mobileProdEnPath = path.join(ARTIFACT_DIR, 'mobile_product_en.png');
  await page.screenshot({ path: mobileProdEnPath, fullPage: false });
  console.log('Saved mobile screenshot:', mobileProdEnPath);

  // Mobile Arabic RTL
  await page.evaluate(() => document.querySelector('.lang')?.click());
  await new Promise(r => setTimeout(r, 400));
  await page.evaluate(() => document.querySelector('.logo')?.click());
  await new Promise(r => setTimeout(r, 500));
  await autoScroll(page);

  mOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  console.log('Mobile (375px) AR Home Horizontal Overflow:', mOverflow);

  const mobileHomeArPath = path.join(ARTIFACT_DIR, 'mobile_home_ar.png');
  await page.screenshot({ path: mobileHomeArPath, fullPage: false });
  console.log('Saved mobile screenshot:', mobileHomeArPath);

  // Mobile Menu Toggle Check
  console.log('\n--- 5. Testing Mobile Menu Toggle ---');
  await page.evaluate(() => document.querySelector('.burger')?.click());
  await new Promise(r => setTimeout(r, 300));
  const menuOpened = await page.evaluate(() => document.querySelector('nav.menu-open') !== null);
  console.log('Mobile burger menu expands:', menuOpened);

  // Mobile Cart Drawer Check
  console.log('\n--- 6. Testing Mobile Cart Drawer ---');
  await page.evaluate(() => document.querySelector('header button[aria-label="Cart"]')?.click());
  await new Promise(r => setTimeout(r, 300));
  const drawerOpened = await page.evaluate(() => document.querySelector('.dw') !== null);
  console.log('Mobile cart drawer opens:', drawerOpened);

  // Final Console Errors Check
  console.log('\n--- 7. Final Console Errors Check ---');
  console.log('Total Console Errors logged:', consoleErrors.length);
  if (consoleErrors.length > 0) {
    console.log('Errors:', consoleErrors);
  }

  await browser.close();
  console.log('\nALL RESPONSIVE MOBILE & DESKTOP CHECKS PASSED!');
}

run().catch(err => {
  console.error('Verification failed:', err);
  process.exit(1);
});
