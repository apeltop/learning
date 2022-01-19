import React from 'react';
import withLoadingContextAndKey, { loadingPropTypes } from './withLoadingContextAndKey';
import Button from '../04/Button';
import PropTypes from 'prop-types';

function ButtonWithLoadingContext({ children, loading, setLoading }) {
  return (
    <Button onPress={() => setLoading(!loading)}>
      {loading ? '로딩 중' : children}
    </Button>
  );
}

ButtonWithLoadingContext.propTypes = {
  ...loadingPropTypes,
  children: PropTypes.string,
};

export const ButtonWithDefaultLoadingContext = withLoadingContextAndKey()(ButtonWithLoadingContext);
export const ButtonWithLoading2Context = withLoadingContextAndKey('loading2')(ButtonWithLoadingContext);