const puppeteer = require('puppeteer');
const argv = require('yargs')
  .option('i', {
    alias: 'input',
    describe: 'Input URL',
    demandOption: true
  })
  .option('o', {
    alias: 'output',
    describe: 'Output file name',
    demandOption: true
  })
  .help()
  .argv;

const inputUrl = argv.i;
const outputFile = argv.o;

console.log('Input URL:', inputUrl);
console.log('Output PDF name:', outputFile);

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(inputUrl, { waitUntil: 'networkidle2' });
  await page.pdf({ path: outputFile, format: 'A4', printBackground: true });

  await browser.close();
})();