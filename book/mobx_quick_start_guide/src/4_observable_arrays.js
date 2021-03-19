import { observable, toJS } from 'mobx';

console.log('==============================4==============================');

const items = observable.array();

console.log(items.length);

items.push({
  name: 'hats',
  quantity: 40,
});

items.unshift({
  name: 'Ribbons',
  quantity: 2,
});

items.push({
  name: 'balloons',
  quantity: 1,
});

const plainArray = toJS(items);
console.log(plainArray);

console.log('==============================4==============================');
