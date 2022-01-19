import React from 'react';
import { storiesOf } from '@storybook/react';

import Button from '../04/Button';
import Text from '../04/Text';
import withLoading from '../05/withLoading';
import BranchLoadingButton from '../05/branch';

const TextWithLoading = withLoading('로딩 중 ')(Text);
const ButtonWithLoading = withLoading(<Button disable>로딩중...</Button>)(Button);


storiesOf('Branch', module)
  .addWithJSX('isLoading 예제', () => (
    <BranchLoadingButton isLoading>안녕하세요</BranchLoadingButton>
  ));