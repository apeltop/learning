import React, { PureComponent } from 'react';
import Button from '../04/Button';
import ButtonWithLoadingContext from './ButtonWithLoadingContext';
import LoadingProvider from './LoadingProvider';

function RowBComponent() {
  return <Button>버튼</Button>;
}

function RowCComponent() {
  return <ButtonWithLoadingContext>버튼</ButtonWithLoadingContext>;
}

function TableComponent() {
  return (
    <table>
      <RowBComponent />
      <RowCComponent />
    </table>
  );
}

export default class HomePageComponent extends PureComponent {
  render() {
    return (
      <LoadingProvider>
        <TableComponent />
        <ButtonWithLoadingContext label={'상태 변경'} />
      </LoadingProvider>
    );
  }
}