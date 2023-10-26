import { Button } from "@mui/joy";
import React, { useState } from "react";
import FormControl from "@mui/joy/FormControl";
import Input from "@mui/joy/Input";
import Modal from "@mui/joy/Modal";
import ModalDialog from "@mui/joy/ModalDialog";
import DialogTitle from "@mui/joy/DialogTitle";
import DialogContent from "@mui/joy/DialogContent";
import Stack from "@mui/joy/Stack";
import Box from "@mui/joy/Box";
import Switch from "@mui/joy/Switch";
import Card from "@mui/joy/Card";
import CardCover from "@mui/joy/CardCover";
import { Navigate } from "react-router-dom";
import strong_santa from "../assets/strong_santa.gif";

const Login = () => {
  const [login, setLogin] = useState(false);

  const [openCreate, setOpenCreate] = useState(false);
  const [openLogin, setOpenLogin] = useState(false);
  const [groupAdmin, setGroupAdmin] = useState(false);

  const handleSubmitLogin = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setOpenLogin(false);
    setLogin(true);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <Card sx={{ minWidth: 500, flexGrow: .3, margin: 5 }}>
        <CardCover>
          <img loading="lazy" src={strong_santa} alt="strong_santa" />
        </CardCover>
      </Card>
      <Button
        className="w-fit bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        onClick={() => {
          setOpenCreate(true);
        }}
        variant="solid"
      >
        <div className="text-xl">Get Started</div>
      </Button>
      <div className="text-sm">Or</div>
      <Button
        color="neutral"
        onClick={() => {
          setOpenLogin(true);
        }}
        size="sm"
        variant="plain"
      >
        Sign In
      </Button>

      {login && <Navigate to="/" />}

      <Modal open={openCreate} onClose={() => setOpenCreate(false)}>
        <ModalDialog>
          <DialogTitle>Create new account</DialogTitle>
          <DialogContent>Fill out the required fields</DialogContent>
          <form
            onSubmit={(event: React.FormEvent<HTMLFormElement>) => {
              event.preventDefault();
              setOpenCreate(false);
            }}
          >
            <Stack spacing={2}>
              <FormControl>
                <Input placeholder="Email*" autoFocus required />
              </FormControl>
              <FormControl>
                <Input type="password" placeholder="Password*" required />
              </FormControl>
              <FormControl>
                <Input
                  type="password"
                  placeholder="Confirm Password*"
                  required
                />
              </FormControl>
              <FormControl>
                <Input placeholder="First Name*" required />
              </FormControl>
              <FormControl>
                <Input placeholder="Last Name*" required />
              </FormControl>
              <FormControl>
                <Input placeholder="Nickname" />
              </FormControl>
              <Box sx={{ display: "flex", gap: 16 }}>
                <p>Group Admin</p>
                <Switch
                  size="lg"
                  variant="outlined"
                  checked={groupAdmin}
                  onChange={(event) => {
                    setGroupAdmin(event.target.checked);
                    console.log(groupAdmin);
                  }}
                />
              </Box>
              {groupAdmin && (
                <FormControl>
                  <Input placeholder="Group Name" />
                </FormControl>
              )}

              <Button type="submit">Submit</Button>
            </Stack>
          </form>
        </ModalDialog>
      </Modal>

      <Modal open={openLogin} onClose={() => setOpenLogin(false)}>
        <ModalDialog>
          <DialogTitle>Sign In</DialogTitle>
          <form
            onSubmit={(event: React.FormEvent<HTMLFormElement>) => {
              handleSubmitLogin(event);
            }}
          >
            <Stack spacing={2}>
              <FormControl>
                <Input placeholder="Email*" autoFocus required />
              </FormControl>
              <FormControl>
                <Input type="password" placeholder="Password*" required />
              </FormControl>

              <Button type="submit">Next</Button>
            </Stack>
          </form>
        </ModalDialog>
      </Modal>
    </div>
  );
};

export default Login;
