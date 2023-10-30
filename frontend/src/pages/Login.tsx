import { Button } from "@mui/joy";
import React, { useState } from "react";
import FormControl from "@mui/joy/FormControl";
import Input from "@mui/joy/Input";
import Modal from "@mui/joy/Modal";
import ModalDialog from "@mui/joy/ModalDialog";
import DialogTitle from "@mui/joy/DialogTitle";
import DialogContent from "@mui/joy/DialogContent";
import Stack from "@mui/joy/Stack";
import Card from "@mui/joy/Card";
import CardCover from "@mui/joy/CardCover";
import { Navigate } from "react-router-dom";
import strong_santa from "../assets/strong_santa.gif";
import Header from "../components/Header";
import Footer from "../components/Footer";
import SolidButton from "../components/SolidButton";
import NeutralButton from "../components/NeutralButton";
import CreateAccountForm from "../components/CreateAccountForm"
import LoginForm from "../components/LoginForm";
import StrongSataCard from "../components/StrongSataCard";
import { authApi } from "../api"

const Login = () => {
  const [login, setLogin] = useState(false);
  const [openCreate, setOpenCreate] = useState(false);
  const [openLogin, setOpenLogin] = useState(false);

  const handleSubmitLogin = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    //call authApi.login here() with username, password from form
    setOpenLogin(false);
    setLogin(true);
  };

  return (
    <div className="flex flex-col h-screen justify-between">
      <Header></Header>

      <div className="flex flex-col items-center justify-center">
        <h1 className="font-festive text-xl mb-3">
          The Ultimate Secret Santa App
        </h1>
        <StrongSataCard className="m-3"></StrongSataCard>

        <SolidButton
          onClick={() => {
            setOpenCreate(true);
          }}
          className="mb-3"
        >
          <div className="text-xl">Create Account</div>
        </SolidButton>

        <NeutralButton
          onClick={() => {
            setOpenLogin(true);
          }}
        >
          <div>Sign In</div>
        </NeutralButton>

        {login && <Navigate to="/" />}

        <Modal open={openCreate} onClose={() => setOpenCreate(false)}>
          <ModalDialog>
            <DialogTitle>Create new account</DialogTitle>
            <DialogContent>Fill out the required fields</DialogContent>
            <CreateAccountForm
              onSubmit={(event: React.FormEvent<HTMLFormElement>) => {
                event.preventDefault();
                setOpenCreate(false);
              }}
            ></CreateAccountForm>
          </ModalDialog>
        </Modal>

        <Modal open={openLogin} onClose={() => setOpenLogin(false)}>
          <ModalDialog>
            <DialogTitle>Sign In</DialogTitle>
            <LoginForm
              onSubmit={(event: React.FormEvent<HTMLFormElement>) => {
                handleSubmitLogin(event);
              }}
            ></LoginForm>
          </ModalDialog>
        </Modal>
      </div>

      <Footer></Footer>
    </div>
  );
};

export default Login;
