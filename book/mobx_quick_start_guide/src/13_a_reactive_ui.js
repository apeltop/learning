import { observable } from 'mobx';
import { observer } from 'mobx-react';

const item = observable.box(30);

const ItemComponent = observer(() => <h1>Current Item Value = {item.get()}</h1>);

setTimeout(() => item.set(50), 2000);

export default ItemComponent;
