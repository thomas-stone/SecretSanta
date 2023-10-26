import Button from './Button'
import axios from 'axios'

interface Props {
    urlPath : string
    buttonText : string
}

const PostButton = ({urlPath, buttonText} : Props) => {

    const sendRequest = () => {
        axios
            .post(urlPath)
            .then(function (response) {
                console.log(response);
        });
    }

  return (
    <div className="m-2">
      <Button onClick={sendRequest} buttonText={buttonText} colorStyle='bg-green-500 hover:bg-green-700'></Button>
    </div>
  );
}

export default PostButton