import Box from "@mui/joy/Box";
import Switch from "@mui/joy/Switch";
import Stack from "@mui/joy/Stack";
import FormControl from  "@mui/joy/FormControl";
import Input from  "@mui/joy/Input";

interface Props {
    onSubmit : (event: React.FormEvent<HTMLFormElement>) => void
}

const CreateAccountForm = ({onSubmit}: Props) => {
  return (
    <form onSubmit={onSubmit}>
      <Stack spacing={2}>
        <FormControl>
          <Input placeholder="Email" autoFocus required />
        </FormControl>
        <FormControl>
          <Input type="password" placeholder="Password" required />
        </FormControl>
        <FormControl>
          <Input type="password" placeholder="Confirm Password" required />
        </FormControl>
        <FormControl>
          <Input placeholder="First Name" required />
        </FormControl>
        <FormControl>
          <Input placeholder="Last Name" required />
        </FormControl>
        <FormControl>
          <Input placeholder="Nickname (Optional)" />
        </FormControl>
        {/* <Box sx={{ display: "flex", gap: 16 }}>
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
        )} */}
        <button type="submit">Create Account</button>
      </Stack>
    </form>
  );
}

export default CreateAccountForm