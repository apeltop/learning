import React, { PureComponent } from 'react';
import Button from '../04/Button';

class ActionComponent extends PureComponent {
  render() {
    const { setAge } = this.props;

    return (
      <React.Fragment>
        <Button onPress={() => setAge(2, 19)}>고유번호 2번 나이 19세로 변경</Button>
      </React.Fragment>
    );
  }
}

export default ActionComponent;