import {
  action, autorun, makeAutoObservable, observable,
} from 'mobx';

console.log('==============================11==============================');

class Cart {
  @observable modified = new Date();

  @observable.shallow items = [];

  constructor() {
    makeAutoObservable(this);
    autorun(() => {
      console.log(`Items in Cart: ${this.items.length}`);
    });
  }

  @action.bound
  addItem(name, quantity) {
    this.items.push({ name, quantity });
    this.modified = new Date();
  }
}

const cart = new Cart();

cart.addItem('Power Cable', 1);
cart.addItem('Shoes', 1);

console.log('==============================11==============================');
