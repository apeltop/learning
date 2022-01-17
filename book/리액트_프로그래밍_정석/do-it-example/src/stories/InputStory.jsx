import React from 'react';
import { storiesOf } from '@storybook/react';
import Input from '../03/Input';
import { action } from '@storybook/addon-actions';

storiesOf('Input', module)
  .addWithJSX('기본 설정', () => <Input name='name' />)
  .addWithJSX('label 예제', () => <Input name='name' label='이름' />)
  .addWithJSX('onChane 예제', () => <Input name='name' onChange={action('onChange 이벤트 발생')} />);