import React from 'react'
import axios from 'axios'

const GetButton = ({urlPath, name}) => {

    const sendRequest = () => {
        axios
            .get(urlPath)
            .then(function (response) {
                console.log(response);
        });
    }

  return (
    <button onClick={sendRequest}>{name}</button>
  )
}

export default GetButton