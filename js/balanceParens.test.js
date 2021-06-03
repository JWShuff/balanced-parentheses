const bp = require('./balanceParens');
const { expect, test } = require('@jest/globals');

test('does it return a string?', () => {
  expect(typeof(bp.balanceParens("[]"))).toBe("string")
})