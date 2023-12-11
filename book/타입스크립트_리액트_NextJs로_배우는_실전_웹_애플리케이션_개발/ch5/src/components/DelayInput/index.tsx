import React, { useCallback, useEffect, useRef } from 'react'

type DelayInputProps = {
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void
}

export const DelayInput = (props: DelayInputProps) => {
  const { onChange } = props

  const [isTyping, setIsTyping] = React.useState(false)
  const [inputValue, setInputValue] = React.useState('')
  const [viewValue, setViewValue] = React.useState('')

  const timeRef = useRef<ReturnType<typeof setTimeout>>(null)

  const handleChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setIsTyping(true)

      setInputValue(e.target.value)

      if (timeRef.current !== null) {
        clearTimeout(timeRef.current)
      }

      timeRef.current = setTimeout(() => {
        timeRef.current = null

        setIsTyping(false)

        setViewValue(e.target.value)
        onChange(e)
      }, 1000)
    },
    [onChange],
  )

  const text = isTyping ? '입력 중...' : `입력 값: ${viewValue}`

  return (
    <div>
      <input
        data-testid={'input-text'}
        value={inputValue}
        onChange={handleChange}
      />
      <span data-testid={'display-text'}>{text}</span>
    </div>
  )
}
