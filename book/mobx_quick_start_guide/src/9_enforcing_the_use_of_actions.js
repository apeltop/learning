import { configure, observable } from 'mobx';

console.log('==============================9==============================');

configure({
  enforceActions: 'always',
});

const cart = observable({
  items: [],
  modified: new Date(),
});

// Modifying outside of an action
cart.items.push({ name: 'test', quantity: 1 });
cart.modified = new Date();

console.log('==============================9==============================');
