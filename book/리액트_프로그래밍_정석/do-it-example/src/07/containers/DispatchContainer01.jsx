import React from 'react';
import { setAge } from '../actions/collectionActions02';
import ActionComponent from '../ActionComponent01';
import { connect } from 'react-redux';

// const mapDispatchToProps = dispatch => {
//   return {
//     setAge: (id, age) => dispatch(setAge(id, age)),
//   };
// };

const mapDispatchToProps = {
  setAge,
};

export default connect(null, mapDispatchToProps)(ActionComponent);