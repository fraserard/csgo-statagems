import { Alert, Stack } from "@mantine/core"

interface Props {
  errors: {__typename: string, message: string}[]
}

export default function ValidationErrors({ errors }: Props ) {
  const alerts = errors.map((e, index) => (  
      <Alert key={index} title={e.__typename} color="red" variant="outline">{e.message}</Alert>   
    ))
  return (
    <Stack>
      {alerts}
    </Stack>
  );
}