import puppeteer from 'puppeteer-core';
import fs from 'fs';
import path from 'path';

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const ARTIFACT_DIR = 'C:\\Users\\Nexus Computer\\.gemini\\antigravity\\brain\\fbd25769-0ccf-41d8-a61e-46f9ca977ef5';

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

  // 1. Desktop English (1440px)
  console.log('Testing Desktop 1440px English...');
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://127.0.0.1:5173/', { waitUntil: 'networkidle0' });
  await page.evaluate(() => {
    localStorage.setItem('obs_lang', JSON.stringify('en'));
    location.reload();
  });
  await new Promise(r => setTimeout(r, 1200));

  // Screenshot header area
  const desktopHeaderEn = path.join(ARTIFACT_DIR, 'header_desktop_en.png');
  await page.screenshot({
    path: desktopHeaderEn,
    clip: { x: 0, y: 0, width: 1440, height: 180 }
  });
  console.log('Saved:', desktopHeaderEn);

  // 2. Desktop Arabic (1440px)
  console.log('Testing Desktop 1440px Arabic...');
  await page.evaluate(() => {
    localStorage.setItem('obs_lang', JSON.stringify('ar'));
    location.reload();
  });
  await new Promise(r => setTimeout(r, 1200));

  const desktopHeaderAr = path.join(ARTIFACT_DIR, 'header_desktop_ar.png');
  await page.screenshot({
    path: desktopHeaderAr,
    clip: { x: 0, y: 0, width: 1440, height: 180 }
  });
  console.log('Saved:', desktopHeaderAr);

  // 3. Mobile English (375px)
  console.log('Testing Mobile 375px English...');
  await page.setViewport({ width: 375, height: 812, isMobile: true, hasTouch: true });
  await page.evaluate(() => {
    localStorage.setItem('obs_lang', JSON.stringify('en'));
    location.reload();
  });
  await new Promise(r => setTimeout(r, 1200));

  const mobileHeaderEn = path.join(ARTIFACT_DIR, 'header_mobile_en.png');
  await page.screenshot({
    path: mobileHeaderEn,
    clip: { x: 0, y: 0, width: 375, height: 260 }
  });
  console.log('Saved:', mobileHeaderEn);

  // 4. Test Mobile Hamburger Menu Open
  await page.click('.burger-btn');
  await new Promise(r => setTimeout(r, 500));
  const mobileMenuOpen = path.join(ARTIFACT_DIR, 'header_mobile_menu_open.png');
  await page.screenshot({
    path: mobileMenuOpen,
    clip: { x: 0, y: 0, width: 375, height: 500 }
  });
  console.log('Saved:', mobileMenuOpen);

  console.log('\nConsole errors detected:', consoleErrors.length);
  if (consoleErrors.length > 0) {
    console.log(consoleErrors);
  }

  await browser.close();
  console.log('Verification completed successfully!');
}

run().catch(err => {
  console.error('Test run failed:', err);
  process.exit(1);
});

