import React from 'react';
import { storiesOf } from '@storybook/react';
import Input from '../03/Input';
import { action } from '@storybook/addon-actions';
import CheckBox from '../04/CheckBox';
import Text from '../04/Text';

storiesOf('CheckBox', module)
  .addWithJSX('기본 설정', () => <CheckBox name='agree' />)
  .addWithJSX('children 예제', () => <CheckBox name='agree'><Text>동의합니다</Text></CheckBox>)
  .addWithJSX('onChange 예제', () => <CheckBox name='agree'
                                             onChange={action('onChange 이벤트 발생 ')}><Text>동의합니다</Text></CheckBox>)
  .addWithJSX('errorMessage 예제', () => <CheckBox name='agree'
                                             onChange={action('onChange 이벤트 발생 ')} errorMessage={'동의가 필요합니다 '}><Text>동의합니다</Text></CheckBox>);