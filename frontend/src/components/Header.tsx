
const Header = () => {
  return (
    <div className="flex flex-row items-center justify-between h-28 bg-slate-300 border-b-2 border-b-black">
      
      <div className="pl-7 lg:ml-10 h-28 flex justify-center items-center mb-1">
        <img src="/santa.svg" alt="logo" className="h-2/3 w-2/3"/>
      </div>

      <h1 className="text text-4xl font-festive">Secret Santa Picker</h1>

      <div className="flex justify-around w-2/5 mr-12 lg:visible sm:invisible">
          <a href="#home" className="text-lg font-semibold text-blue-800 transition-all hover:text-red-400">Home</a>
          <a href="#product" className="text-lg font-semibold text-blue-800 transition-all hover:text-red-400">Groups</a>
          <a href="#faq" className="text-lg font-semibold text-blue-800 transition-all hover:text-red-400">Create</a>
      </div>

  </div>
  )
}

export default Header