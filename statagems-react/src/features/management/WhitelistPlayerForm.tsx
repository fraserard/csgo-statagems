import { Button, Group, Input, Title } from "@mantine/core";
import { useForm } from "@mantine/form";
import { showNotification } from "@mantine/notifications";
import { useMutation } from "urql";
import Error from "~/components/Error";
import { WhitelistPlayerDocument, WhitelistPlayerMutation } from "~/graphql";

interface WhitelistPlayerFormProps {
  addUser: Function;
}

export default function WhitelistPlayerForm({ addUser }: WhitelistPlayerFormProps) {
  const form = useForm({
    initialValues: {
      steamId: "",
    },
  });

  const [whitelistPlayerResult, whitelistPlayer] =
    useMutation<WhitelistPlayerMutation>(WhitelistPlayerDocument);

  const submitForm = async (values: { steamId: string }) => {
    await whitelistPlayer({ steamId: values.steamId }).then((result) => {
      if (result.data?.addPlayer) {
        form.reset();
        addUser(result.data!.addPlayer);
        showNotification({
          title: `Whitelisted ${result.data?.addPlayer.username}`,
          message: `Successfully added ${result.data?.addPlayer.username} to the whitelist.`,
          color: "green",
        });
      }
    });
  };

  return (
    <>
      <Title order={3} mb="xs">
        Whitelist new player
      </Title>
      {whitelistPlayerResult.error && <Error message={"Unexpected error. Please try again."} />}
      {/* {whitelistPlayerResult.data?.addPlayer.errors && <ValidationErrors errors={whitelistPlayerResult.data!.addPlayer.errors} /> } */}

      <form onSubmit={form.onSubmit((values) => submitForm(values))}>
        <Group>
          <Input placeholder="Steam ID" required {...form.getInputProps("steamId")} />
          <Button type="submit" mr="xl">
            Add
          </Button>
        </Group>
      </form>
    </>
  );
}
