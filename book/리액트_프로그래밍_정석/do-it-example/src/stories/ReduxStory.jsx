import React from 'react';
import { storiesOf } from '@storybook/react';
import { ReduxApp } from '../07/ReduxApp01';

storiesOf('Redux', module)
  .addWithJSX('기본 설정', () => <ReduxApp>안녕하세요</ReduxApp>);