import { observable } from 'mobx';

console.log('==============================5==============================');

const twitterUserMap = observable.map();

console.log(twitterUserMap.size);

twitterUserMap.set('pavanpodila', 'Pavan Podila');
twitterUserMap.set('mweststrate', 'Michel Weststrate');

console.log(twitterUserMap.get('pavanpodila'));
console.log(twitterUserMap.get('mweststrate'));

twitterUserMap.forEach((value, key) => console.log(`${key}: ${value}`));

console.log('==============================5==============================');
