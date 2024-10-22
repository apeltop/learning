import styled, { css } from 'styled-components'

const variants = {
  primary: {
    color: '#fff',
    backgroundColor: '#1D9BF0',
    border: 'none',
  },
  success: {
    color: '#fff',
    backgroundColor: '#5cb85c',
    border: 'none',
  },
  transparent: {
    color: '#111',
    backgroundColor: 'transparent',
    border: '1px solid black',
  },
} as const

type StyleButtonProps = {
  variant: keyof typeof variants
}

export const StyledButton = styled.button<StyleButtonProps>`
  ${({ variant }) => {
    const style = variants[variant]

    return css`
      color: ${style.color};
      background-color: ${style.backgroundColor};
      border: ${style.border};
    `
  }}

  border-radius: 12px;
  font-size: 14px;
  height: 38px;
  line-height: 22px;
  letter-spacing: -0.02em;
  cursor: pointer;

  &:focus {
    outline: none;
  }
`
