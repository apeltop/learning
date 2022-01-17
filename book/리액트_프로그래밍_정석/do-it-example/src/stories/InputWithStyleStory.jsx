import React from 'react';
import { storiesOf } from '@storybook/react';
import Input from '../03/Input';
import { action } from '@storybook/addon-actions';
import InputWithStyles from '../04/InputWithStyles';

storiesOf('InputWithStyles', module)
  .addWithJSX('기본 설정', () => <InputWithStyles name='name' />)
  .addWithJSX('label 예제', () => <InputWithStyles name='name' label='이름' />)
  .addWithJSX('errorMessage 예제', () => <InputWithStyles name='name' errorMessage={'에러'}/>)
  .addWithJSX('onChane 예제', () => <InputWithStyles name='name' onChange={action('onChange 이벤트 발생')} />);