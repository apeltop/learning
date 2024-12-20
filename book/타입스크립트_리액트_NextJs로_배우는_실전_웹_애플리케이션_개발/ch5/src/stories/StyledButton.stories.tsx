import { action } from '@storybook/addon-actions'
import { Meta } from '@storybook/react'
import { StyledButton } from '@/components/StyledButton'

export default {
  title: 'StyledButton',
  component: StyledButton,
  argTypes: {
    onClick: { action: 'clicked' },
    variant: {
      control: {
        type: 'radio',
      },
      options: ['primary', 'success', 'transparent'],
    },
    children: {
      control: {
        type: 'text',
      },
    },
  },
} as Meta<typeof StyledButton>

const incrementAction = action('increment')
export const Primary = (props) => {
  const [count, setCount] = React.useState(0)
  const onClick = (e: React.MouseEvent) => {
    setCount(count + 1)
    incrementAction()
  }

  return (
    <StyledButton variant="primary" {...props} onClick={onClick}>
      Count {count}
    </StyledButton>
  )
}

export const Success = (props) => {
  return (
    <StyledButton variant="success" {...props}>
      Success
    </StyledButton>
  )
}

export const Transparent = (props) => {
  return (
    <StyledButton variant="transparent" {...props}>
      Transparent
    </StyledButton>
  )
}
