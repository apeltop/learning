import React from 'react';
import ReactDOM from 'react-dom';
import Input from '../../03/Input';
import { shallow } from 'enzyme';

describe('<Input>', () => {
  it('renders without crashing', () => {
    expect(() => {
      shallow(<Input name='name' />);
    }).not.toThrow();
  });

  it('has one element', () => {
    const wrapper = shallow(<Input name={'test_name'} />);
    expect(wrapper.length).toEqual(1);
    expect(wrapper).toHaveLength(1);
  });

  describe('contains <input>', () => {
    it('renders one input', () => {
      const wrapper = shallow(<Input name='test_name' />);
      expect(wrapper.find('input')).toHaveLength(1);
      expect(wrapper.find('label')).toHaveLength(1);
    });
  });
});