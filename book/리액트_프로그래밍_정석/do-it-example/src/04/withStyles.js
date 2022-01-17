import ThemedStyleSheet from 'react-with-styles/lib/ThemedStyleSheet';
import Theme from './Theme';
import aphroditeInterface from 'react-with-styles-interface-aphrodite/lib/aphroditeInterface';
import { css, withStyles, withStylesPropTypes } from 'react-with-styles';

ThemedStyleSheet.registerTheme(Theme);
ThemedStyleSheet.registerInterface(aphroditeInterface);

export { css, withStyles, withStylesPropTypes, ThemedStyleSheet };
export default withStyles;