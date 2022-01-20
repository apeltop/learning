import React, { PureComponent } from 'react';
import configureStore from './configureStore';
import { setCollection } from './actions/collectionActions01';
import { Provider } from 'react-redux';

class AdvReduxApp extends PureComponent {
  store = configureStore({ loading: false });

  componentDidMount() {
    this.store.dispatch(
      setCollection([
        { id: 1, name: 'John', age: 20 },
        { id: 2, name: 'Park', age: 35 },
      ]),
    );
  }

  render() {
    return (
      <Provider store={this.store}>리덕스 예제</Provider>
    );
  }
}

export default AdvReduxApp;