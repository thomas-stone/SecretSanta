import Stack from "@mui/joy/Stack";
import FormControl from  "@mui/joy/FormControl";
import Input from  "@mui/joy/Input";

interface Props {
    onSubmit : (event: React.FormEvent<HTMLFormElement>) => void
}

const LoginForm = ({onSubmit}: Props) => {
  return (
    <form onSubmit={onSubmit}>
      <Stack spacing={2}>
        <FormControl>
          <Input placeholder="Email" autoFocus required />
        </FormControl>
        <FormControl>
          <Input type="password" placeholder="Password" required />
        </FormControl>

        <button type="submit">Next</button>
      </Stack>
    </form>
  );
}

export default LoginForm