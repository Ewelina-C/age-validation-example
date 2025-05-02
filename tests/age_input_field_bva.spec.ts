import { test, expect } from '@playwright/test';

const testCases = [
  { age: 17, valid: false },
  { age: 18, valid: true },
  { age: 98, valid: true },
  { age: 99, valid: false },
];

for (const { age, valid } of testCases) {
  test(`Age ${age} should ${valid ? 'pass' : 'fail'}`, async ({ page }) => {
    await page.goto('https://ewelina-c.github.io/age-validation-example');
    await page.fill('#age', age.toString());
    await page.click('#submit');

    if (valid) {
      await expect(page.locator('#result')).toHaveText('Success');
    } else {
      await expect(page.locator('#error')).toContainText('Invalid age');
    }
  });
}
