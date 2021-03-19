import { observable, autorun } from 'mobx';

console.log('==============================1==============================');
const cart = observable({
  itemCount: 0,
  modified: new Date(),
});

autorun(() => {
  console.log(`The Cart contains ${cart.itemCount} item(s).`);
});

cart.itemCount++;
console.log('==============================1==============================');
