import React, { PureComponent } from 'react';
import { Provider } from 'react-redux';
import configureStore from './configureStore';

export class ReduxApp extends PureComponent {
  store = configureStore({ loading: false });

  render() {
    return (
      <Provider store={this.store}>
        리덕스 예제
      </Provider>
    );
  }
}