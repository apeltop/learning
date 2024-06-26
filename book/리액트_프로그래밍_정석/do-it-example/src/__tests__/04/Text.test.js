import React from 'react';
import { mount, shallow } from 'enzyme';

import Text from '../../04/Text';

describe('<Text>', () => {
  it('renders without crashing', () => {
    expect(() => {
      shallow(<Text>테스트</Text>);
    }).not.toThrow();
  });

  it('contains <span>', () => {
    expect(shallow(<Text>테스트</Text>).dive().find('span')).toHaveLength(1);
    expect(mount(<Text>테스트</Text>).find('span')).toHaveLength(1);
  });
});