import {
  action, makeAutoObservable, observable, when,
} from 'mobx';

console.log('==============================14==============================');

class Inventory {
  @observable items = [];

  cancelTracker = null;

  constructor() {
    makeAutoObservable(this);
  }

  trackAvailability(name) {
    this.cancelTracker = when(
      () => {
        const item = this.items.find((x) => x.name === name);
        return item ? item.quantity > 0 : false;
      },
      () => {
        console.log(`${name} is now available`);
      },
    );
  }

  @action
  addItem(name, quantity) {
    const item = this.items.find((x) => x.name === name);

    if (item) {
      item.quantity += quantity;
    } else {
      this.items.push({ name, quantity });
    }
  }
}

const inventory = new Inventory();

inventory.addItem('Shoes', 0);
inventory.trackAvailability('Shoes');

inventory.addItem('Shoes', 2);
inventory.addItem('Shoes', 1);

console.log('==============================14==============================');
