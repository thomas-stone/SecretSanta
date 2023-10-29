import React from 'react'
import Header from '../components/Header'
import Footer from '../components/Footer'

const Groups = () => {
  return (
    <div className="flex flex-col h-screen justify-between">
        <Header></Header>
        <div>Group Content</div>
        <Footer></Footer>
    </div>
  )
}

export default Groups