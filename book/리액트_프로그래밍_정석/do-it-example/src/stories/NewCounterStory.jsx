import React from 'react';
import { storiesOf } from '@storybook/react';
import Input from '../03/Input';
import NewCounter from '../03/NewCounter';

storiesOf('NewCounter', module)
  .add('기본 설정', () => <NewCounter count={0} />);