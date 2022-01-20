import React from 'react';
import { storiesOf } from '@storybook/react';
import { ReduxApp } from '../07/ReduxApp01';
import { ReduxApp as ReduxApp2 } from '../07/ReduxApp02';
import { ReduxApp as ReduxApp3 } from '../07/ReduxApp03';
import AdvReduxApp from '../07/AdvReduxApp03';
import AdvReduxApp4 from '../07/AdvReduxApp04';

storiesOf('Redux', module)
  .addWithJSX('기본 설정', () => <ReduxApp>안녕하세요</ReduxApp>)
  .addWithJSX('dispatch 예제', () => <ReduxApp2 />)
  .addWithJSX('reducer 예제', () => <ReduxApp3 />)
  .addWithJSX('그래프 데이터베이스 기본 예제', () => <AdvReduxApp />)
  .addWithJSX('그래프 데이터베이스 데이터 읽기 예제', () => <AdvReduxApp4 />);