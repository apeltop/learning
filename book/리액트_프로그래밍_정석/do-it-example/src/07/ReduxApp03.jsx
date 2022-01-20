import React, { PureComponent } from 'react';
import { Provider } from 'react-redux';
import configureStore from './configureStore';

const reducer = (state, action) => {
  const { type, payload } = action;

  switch (type) {
    case 'SET_LOADING': {
      return {
        ...state,
        loading: payload,
      };
    }

    case 'RESET_LOADING': {
      return {
        ...state,
        loading: false,
      };
    }

    case 'SET_USER': {
      return {
        ...state,
        user: payload,
      };
    }

    default:
      return state;
  }
};

export class ReduxApp extends PureComponent {
  store = configureStore({ loading: false });

  componentDidMount() {
    this.store.dispatch({
      type: 'SET_LOADING',
      payload: true,
    });

    this.store.dispatch({ type: 'RESET_LOADING' });

    this.store.dispatch({
      type: 'SET_USER',
      payload: {
        name: 'Park',
        age: 20,
      },
    });
  }

  render() {
    return (
      <Provider store={this.store}>
        리덕스 예제
      </Provider>
    );
  }
}