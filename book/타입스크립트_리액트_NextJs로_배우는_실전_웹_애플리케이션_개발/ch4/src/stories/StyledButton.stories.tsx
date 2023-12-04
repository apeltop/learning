import {StyledButton} from "@/components/StyledButton";
import {Meta} from "@storybook/react";

export default {
    title: 'StyledButton',
    component: StyledButton,
} as Meta<typeof StyledButton>

export const Primary = (props) => {
    return (
        <StyledButton variant="primary" {...props}>Primary</StyledButton>
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
