import { observable, autorun, action } from 'mobx';

console.log('==============================2==============================');
const cart = observable({
  itemCount: 0,
  modified: new Date(),
});

autorun(() => {
  console.log(`The Cart contains ${cart.itemCount} item(s).`);
});

const incrementCount = action(() => {
  cart.itemCount++;
});

incrementCount();
console.log('==============================2==============================');
