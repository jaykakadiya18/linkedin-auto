const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');

puppeteer.use(StealthPlugin());

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
async function inviteConnectionsToEvent(eventUrl) {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  // Sign in to LinkedIn
  await page.goto('https://www.linkedin.com/login');
  await page.waitForSelector('#username');
  await page.type('#username', '***********'); 
  await sleep(5000);
  await page.type('#password', '**********');
  await sleep(5000);
  await page.click('button[type="submit"]');
  await page.waitForNavigation();

  await sleep(5000);
  // Navigate to the event page
  await page.goto(eventUrl);
  await page.waitForSelector('.event-top-card');

  // Click the "Invite" button
  await page.click('button[data-control-name="invite_single"]');
  await page.waitForSelector('.send-invite__header');

  // Select and invite the top 10 members
  const inviteeSelectors = await page.$$eval(
    '.invite-modal .invitee .entity-result__title-text',
    (elements) => elements.slice(0, 10).map((el) => el.innerText.trim())
  );

  for (const inviteeSelector of inviteeSelectors) {
    const inviteeElement = await page.$x(
      `//span[@class="entity-result__title-text" and contains(text(), "${inviteeSelector}")]`
    );

    if (inviteeElement.length > 0) {
      const inviteeContainer = await inviteeElement[0].$x(
        'ancestor::div[contains(@class, "invite-modal__profile-container")]'
      );

      if (inviteeContainer.length > 0) {
        const inviteeCheckbox = await inviteeContainer[0].$('input[type="checkbox"]');
        if (inviteeCheckbox)
          await inviteeCheckbox.click();
      }
    }
  }

  // Close the invite dialog
  await sleep(5000);
  await page.click('.artdeco-modal .artdeco-modal__dismiss');

  // Keep the browser open (comment out the next line if you want to close the browser)
  await page.waitForNavigation();

  // Close the browser
  await browser.close();
}

// Usage example
const eventUrl = 'https://www.linkedin.com/events/gibsonreports-virtualrssevent-p6756991161354784768/';
inviteConnectionsToEvent(eventUrl);
