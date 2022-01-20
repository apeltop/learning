import React from 'react';
import { storiesOf } from '@storybook/react';
import { ReduxApp } from '../07/ReduxApp01';
import { ReduxApp as ReduxApp2 } from '../07/ReduxApp02';

storiesOf('Redux', module)
  .addWithJSX('기본 설정', () => <ReduxApp>안녕하세요</ReduxApp>)
  .addWithJSX('dispatch 예제', () => <ReduxApp2 />);