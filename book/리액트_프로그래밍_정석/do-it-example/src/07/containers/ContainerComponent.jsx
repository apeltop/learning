import React from 'react';
import PresentationComponent from '../PresentationComponent';
import { connect } from 'react-redux';

const mapStateToProps = (state, props) => {
  return {
    userName: state.user.name,
    entity: state.collection.entities[props.id],
  };
};

export default connect(mapStateToProps)(PresentationComponent);