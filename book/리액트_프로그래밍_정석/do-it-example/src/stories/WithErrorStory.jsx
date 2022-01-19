import React from 'react';
import { storiesOf } from '@storybook/react';
import withError from '../05/withError';
import Input from '../04/InputWithStyles';

const InputWithError = withError('올바르지 못한 값입니다.')(Input);

storiesOf('WithError', module)
  .addWithJSX('기본 설정', () => <InputWithError name='name' hasError />)
  .addWithJSX('errorMessage 예제', () => <InputWithError name='name' hasError errorMessage={'필수 항목입니다.'} />)