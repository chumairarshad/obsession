import puppeteer from 'puppeteer-core';
import path from 'path';

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const ARTIFACT_DIR = 'C:\\Users\\Nexus Computer\\.gemini\\antigravity\\brain\\fbd25769-0ccf-41d8-a61e-46f9ca977ef5';

async function run() {
  console.log('Launching Chrome to verify fonts...');
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });

  const page = await browser.newPage();

  // 1. Desktop English (1440x900)
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://127.0.0.1:5173/', { waitUntil: 'networkidle0' });
  await page.evaluate(() => {
    localStorage.setItem('obs_lang', JSON.stringify('en'));
    location.reload();
  });
  await new Promise(r => setTimeout(r, 1500));

  // Verify computed fonts
  const fonts = await page.evaluate(() => {
    const heroH1 = document.querySelector('.hero-content h1');
    const secH2 = document.querySelector('.hd h2');
    const prodTitle = document.querySelector('.pc h3');
    const prodPrice = document.querySelector('.pc .pr');
    const body = document.body;

    return {
      heroH1Font: heroH1 ? window.getComputedStyle(heroH1).fontFamily : null,
      secH2Font: secH2 ? window.getComputedStyle(secH2).fontFamily : null,
      prodTitleFont: prodTitle ? window.getComputedStyle(prodTitle).fontFamily : null,
      prodPriceFont: prodPrice ? window.getComputedStyle(prodPrice).fontFamily : null,
      bodyFont: window.getComputedStyle(body).fontFamily
    };
  });

  console.log('Computed Font Families in English:');
  console.log(fonts);

  // Screenshot 1: Home page English
  const homeShot = path.join(ARTIFACT_DIR, 'font_home_en.png');
  await page.screenshot({ path: homeShot, clip: { x: 0, y: 0, width: 1440, height: 1100 } });
  console.log('Saved:', homeShot);

  // Navigate to product page
  await page.evaluate(() => {
    const firstProduct = document.querySelector('.pc');
    if (firstProduct) firstProduct.click();
  });
  await new Promise(r => setTimeout(r, 1200));

  const prodFonts = await page.evaluate(() => {
    const pdTitle = document.querySelector('.pd h1');
    const pdPrice = document.querySelector('.pd .p');
    const pdDesc = document.querySelector('.pd p');
    return {
      pdTitleFont: pdTitle ? window.getComputedStyle(pdTitle).fontFamily : null,
      pdPriceFont: pdPrice ? window.getComputedStyle(pdPrice).fontFamily : null,
      pdDescFont: pdDesc ? window.getComputedStyle(pdDesc).fontFamily : null
    };
  });

  console.log('\nComputed Product Page Fonts:');
  console.log(prodFonts);

  // Screenshot 2: Product page English
  const prodShot = path.join(ARTIFACT_DIR, 'font_product_en.png');
  await page.screenshot({ path: prodShot, clip: { x: 0, y: 0, width: 1440, height: 950 } });
  console.log('Saved:', prodShot);

  // 2. Arabic Mode
  await page.evaluate(() => {
    localStorage.setItem('obs_lang', JSON.stringify('ar'));
    location.reload();
  });
  await new Promise(r => setTimeout(r, 1500));

  const prodShotAr = path.join(ARTIFACT_DIR, 'font_product_ar.png');
  await page.screenshot({ path: prodShotAr, clip: { x: 0, y: 0, width: 1440, height: 950 } });
  console.log('Saved:', prodShotAr);

  // Home Arabic
  await page.evaluate(() => {
    const homeLink = document.querySelector('.nav-link');
    if (homeLink) homeLink.click();
  });
  await new Promise(r => setTimeout(r, 1200));

  const homeShotAr = path.join(ARTIFACT_DIR, 'font_home_ar.png');
  await page.screenshot({ path: homeShotAr, clip: { x: 0, y: 0, width: 1440, height: 1100 } });
  console.log('Saved:', homeShotAr);

  await browser.close();
  console.log('\nFont verification completed successfully!');
}

run().catch(err => {
  console.error('Test run failed:', err);
  process.exit(1);
});
