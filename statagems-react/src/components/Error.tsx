import { Alert } from "@mantine/core"

interface Props {
  message: string
}

export default function Error({ message }: Props ) {
  return (
    <Alert title="Error!" color="red" variant="filled">{message}</Alert>
  );
}