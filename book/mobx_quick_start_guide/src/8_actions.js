import { action, observable } from 'mobx';

console.log('==============================8==============================');

const cart = observable({
  items: [],
  modified: new Date(),
});

const addItem = action((name, quantity) => {
  const item = cart.items.find((x) => x.name === name);

  if (item) {
    item.quantity += 1;
  } else {
    cart.items.push({ name, quantity });
  }

  cart.modified = new Date();
});

const removeItem = action((name) => {
  const item = cart.items.find((x) => x.name === name);

  if (item) {
    item.quantity -= 1;

    if (item.quantity <= 0) {
      cart.items.remove(item);
    }

    cart.modified = new Date();
  }
});

addItem('balloons', 2);
addItem('paint', 2);
removeItem('paint');

console.log('==============================8==============================');
