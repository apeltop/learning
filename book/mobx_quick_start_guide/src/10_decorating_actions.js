import { action, observable } from 'mobx';

console.log('==============================10==============================');

class Cart {
  @observable modified = new Date();

  @observable.shallow items = [];

  @action
  addItem(name, quantity) {
    this.items.push({ name, quantity });
    this.modified = new Date();
  }

  @action.bound
  removeItem(name) {
    const item = this.items.find((x) => x.name === name);

    if (item) {
      item.quantity -= 1;

      if (item.quantity <= 0) {
        this.items.remove(item);
      }
    }
  }
/* arrow-functions
  @action removeItem = (name) => {
    const item = this.items.find((x) => x.name === name);

    if (item) {
      item.quantity -= 1;

      if (item.quantity <= 0) {
        this.items.remove(item);
      }
    }
  }
  */
}

console.log('==============================10==============================');
