import Button from './Button'
import axios from 'axios'

interface Props {
    urlPath : string
    buttonText : string
}

const GetButton = ({urlPath, buttonText} : Props) => {

    const sendRequest = () => {
        axios
            .get(urlPath)
            .then(function (response) {
                console.log(response);
        });
    }

  return (
    <div className="m-2">
      <Button onClick={sendRequest} buttonText={buttonText} colorStyle='bg-blue-500 hover:bg-blue-700'></Button>
    </div>
  );
}

export default GetButton