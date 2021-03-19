import { computed, observable } from 'mobx';

console.log('==============================7==============================');

class Cart {
  @observable.shallow items = [];

  @observable modified = new Date();

  @computed get description() {
    switch (this.items.length) {
      case 0:
        return 'There are no item in the cart';
      case 1:
        return 'There is one item in the cart';
      default:
        return `There are ${this.items.length} items in the cart`;
    }
  }
}

console.log('==============================7==============================');
