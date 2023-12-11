import { it, beforeEach, afterEach, describe } from '@jest/globals'
import { expect } from '@storybook/test'
import { render, RenderResult, screen } from '@testing-library/react'
import { Input } from '@/components/Input/index'

describe('Input', () => {
  let renderResult: RenderResult

  beforeEach(() => {
    renderResult = render(<Input label={'Username'} id={'username'} />)
  })

  afterEach(() => {
    renderResult.unmount()
  })

  it('should empty in input on initial render', () => {
    const inputNode = screen.getByLabelText('Username') as HTMLInputElement
    expect(inputNode).toHaveValue('')
  })
})
