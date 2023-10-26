import { MouseEventHandler } from "react"

interface Props {
    colorStyle : string
    buttonText: string
    onClick : MouseEventHandler
}

const Button = ({colorStyle, buttonText, onClick}: Props) => {
  return (
    <button onClick={onClick} className={`text-white font-bold py-2 px-4 rounded-full ${colorStyle}`}>{buttonText}</button>
  )
}

export default Button