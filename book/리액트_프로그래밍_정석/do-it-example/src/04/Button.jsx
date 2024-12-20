import React, { PureComponent } from 'react';
import PropTypes from 'prop-types';
import { css, withStyles } from './withStyles';

class Button extends PureComponent {
  render() {
    const {
      children,
      disabled,
      onPress,
      styles,
      large,
      xlarge,
      small,
      xsmall,
      primary,
      secondary,
    } = this.props;

    return (
      <button
        onClick={onPress}
        {...css(styles.default,
          large && styles.large,
          xlarge && styles.xlarge,
          small && styles.small,
          xsmall && styles.xsmall,
          primary && styles.primary,
          secondary && styles.secondary,
        )}>
        {children}
      </button>
    );
  }
}

Button.propTypes = {
  children: PropTypes.node.isRequired,
  onPress: PropTypes.func,

  large: PropTypes.bool,
  xlarge: PropTypes.bool,
  small: PropTypes.bool,
  xsmall: PropTypes.bool,
  primary: PropTypes.bool,
  secondary: PropTypes.bool,
};

Button.defaultProps = {
  onPress: () => {
  },
  large: false,
  xlarge: false,
  small: false,
  xsmall: false,
  primary: false,
  secondary: false,
};

export default withStyles(({ color, size, unit, responsive }) => ({
  default: {
    border: 1,
    borderStyle: 'solid',
    borderColor: color.default,
    borderRadius: 2,
    color: color.default,
    fontSize: size.md,
    padding: unit * 2,
    cursor: 'pointer',
    [responsive.small]: {
      width: '100%',
    },
  },

  large: {
    fontSize: size.xg,
  },
  xlarge: {
    fontSize: size.lg,
  },
  small: {
    fontSize: size.sm,
    padding: unit,
  },
  xsmall: {
    fontSize: size.xs,
    padding: unit,
  },
  primary: {
    borderColor: color.primary,
    color: color.white,
    backgroundColor: color.primary,
  },
  secondary: {
    borderColor: color.secondary,
    color: color.secondary,
  },
}))(Button);