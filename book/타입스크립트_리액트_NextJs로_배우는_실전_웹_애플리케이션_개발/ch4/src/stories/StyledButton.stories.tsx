import {StyledButton} from "@/components/StyledButton";
import {Meta} from "@storybook/react";
import {action} from "@storybook/addon-actions";

export default {
    title: 'StyledButton',
    component: StyledButton,
    argTypes: {
        onClick: {action: 'clicked'},
    }
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
        <StyledButton variant="success" {...props}>Success</StyledButton>
    )
}

export const Transparent = (props) => {
    return (
        <StyledButton variant="transparent" {...props}>Transparent</StyledButton>
    )
}
