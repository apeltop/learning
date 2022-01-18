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

  it('assings the prop value and type', () => {
    const expectedValue = '123';
    const wrapper = shallow(<Input name='test_name' value={expectedValue} />);
    expect(wrapper.find('input').prop('value')).toBe(expectedValue);

    const { type, value } = wrapper.find('input').props();
    expect(value).toBe(expectedValue);
    expect(type).toBe('text');
  });

  it('renders errorMessage', () => {
    const wrapper = shallow(<Input name='test_name' />);
    expect(wrapper.find('.eeror')).toHaveLength(0);

    const expectedErrorMessage = '옳지 못한 값이 입력되었습니다.';
    wrapper.setProps({
      errorMessage: expectedErrorMessage,
    });

    expect(wrapper.find('span').prop('className')).toBe('error');
    expect(wrapper.find('.error')).toHaveLength(1);
    expect(wrapper.html()).toContain(expectedErrorMessage);
  });

  describe('contains <input>', () => {
    it('renders one input', () => {
      const wrapper = shallow(<Input name='test_name' />);
      expect(wrapper.find('input')).toHaveLength(1);
      expect(wrapper.find('label')).toHaveLength(1);
    });
  });
});