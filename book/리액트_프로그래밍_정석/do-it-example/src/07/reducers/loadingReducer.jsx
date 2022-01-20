import React from 'react';

const initState = false;

export default function reducer(state = initState, action) {
  const { type, payload } = action;

  switch (type) {
    case 'SET_LOADING': {
      return payload;
    }

    case 'RESET_LOADING': {
      return false;
    }

    default:
      return state;
  }
}