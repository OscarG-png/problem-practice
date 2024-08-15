function lemonadeChange(bills: number[]): boolean {
  let moneyMap = {
    5: 0,
    10: 0,
  };

  for (let i = 0; i < bills.length; i++) {
    const currentBill = bills[i];

    switch (currentBill) {
      case 5:
        moneyMap[5]++;
        break;
      case 10:
        if (moneyMap[5] === 0) {
          return false;
        }
        moneyMap[5]--;
        moneyMap[10]++;
        break;
      case 20:
        if (moneyMap[10] > 0 && moneyMap[5] > 0) {
          moneyMap[10]--;
          moneyMap[5]--;
        } else if (moneyMap[5] >= 3) {
          moneyMap[5] -= 3;
        } else {
          return false;
        }
        break;
    }
  }
  return true;
}
