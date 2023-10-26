import GetButton from "./GetButton";
import PostButton from "./PostButton";
import InputField from "./InputField";
import { useState } from "react";

const TestMainPage = () => {
  const [state, setState] = useState({
    name: "",
    email: "",
  })

  return (
    <div className="grid grid-cols-3 justify-items-center ">
      <div className={""}>
        <h1 className="border-b-2 border-b-slate-400 mb-5">Testing GET Requests</h1>
        <GetButton
          buttonText="GET /user/thomas"
          urlPath="/user/thomas"
        />
        <GetButton buttonText="GET /" urlPath="/"/>
      </div>
      <div className={""}>
        <h1 className="border-b-2 border-b-slate-400 mb-5">Testing POST Requests</h1>
        <PostButton
          buttonText="POST /user/thomas"
          urlPath="/user/thomas"
        />
        <PostButton buttonText="POST /" urlPath="/"/>
      </div>
      <div className={""}>
        <h1 className="border-b-2 border-b-slate-400 mb-5">Testing Input</h1>
        <InputField state={state} setState={setState}></InputField>
        {state.name != "" &&  <h1>Hello {state.name}</h1>}
      </div>
    </div>
  );
}

export default TestMainPage