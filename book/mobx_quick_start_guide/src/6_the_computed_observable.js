import { observable } from 'mobx';

console.log('==============================6==============================');

const cart = observable.object({
  items: [],
  modified: new Date(),

  get description() {
    switch (this.items.length) {
      case 0:
        return 'There are no item in the cart';
      case 1:
        return 'There is one item in the cart';
      default:
        return `There are ${this.items.length} items in the cart`;
    }
  },
});

cart.items.push({
  name: 'Shoes',
  quantity: 1,
});

console.log(cart.description);

console.log('==============================6==============================');
