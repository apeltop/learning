import React from 'react'
import IntrinsicElements = JSX.IntrinsicElements

type InputProps = IntrinsicElements['input'] & {
  label: string
}

export const Input = (props: InputProps) => {
  const { label, ...rest } = props

  const [text, setText] = React.useState('')

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setText(e.target.value)
  }

  const resetInputField = () => {
    setText('')
  }

  return (
    <div>
      <label htmlFor={props.id}>{label}</label>

      <input {...rest} type={'text'} value={text} onChange={onChange} />

      <button onClick={resetInputField}>Reset</button>
    </div>
  )
}
