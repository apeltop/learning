import { afterEach, beforeEach, describe, it, jest } from '@jest/globals'
import { expect, fireEvent } from '@storybook/test'
import { render, RenderResult, screen } from '@testing-library/react'
import { act } from 'react-dom/test-utils'
import { DelayInput } from '@/components/DelayInput/index'

describe('DelayInput', () => {
  let renderResult: RenderResult
  let handleChange

  beforeEach(() => {
    handleChange = jest.fn()

    renderResult = render(<DelayInput onChange={handleChange} />)

    jest.useFakeTimers()
  })

  afterEach(() => {
    renderResult.unmount()

    jest.useFakeTimers()
  })

  it('should display empty in span on initial render', () => {
    const spanNode = screen.getByTestId('display-text') as HTMLSpanElement

    expect(spanNode).toHaveTextContent('입력 값:')
  })

  it('should display "입력 중..." immediately after onChange event occurs', () => {
    const inputText = 'Test Input Text'
    const inputNode = screen.getByTestId('input-text') as HTMLInputElement

    fireEvent.change(inputNode, { target: { value: inputText } })

    const spanNode = screen.getByTestId('display-text') as HTMLSpanElement

    expect(spanNode).toHaveTextContent('입력 중...')
  })

  it('should display "입력 값: Test Input Text" after 1 second', () => {
    const inputText = 'Test Input Text'
    const inputNode = screen.getByTestId('input-text') as HTMLInputElement

    fireEvent.change(inputNode, { target: { value: inputText } })

    act(() => {
      jest.runAllTimers()
    })

    const spanNode = screen.getByTestId('display-text') as HTMLSpanElement

    expect(spanNode).toHaveTextContent(`입력 값: ${inputText}`)
  })
})
