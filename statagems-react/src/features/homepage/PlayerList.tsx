import { Avatar, Container, Group, Paper, Skeleton, Stack, Text, Title } from "@mantine/core";
import { Link } from "react-router-dom";
import { useQuery } from "urql";
import Error from "~/components/Error";
import TimeAgo from "~/components/TimeAgo";
import { GetPlayerListDocument, GetPlayerListQuery } from "~/graphql";

export default function PlayerList() {
  const [result] = useQuery<GetPlayerListQuery>({ query: GetPlayerListDocument });
  const { data, fetching, error } = result;
  if (fetching) {
    const skeleton = [<Skeleton height={50} m="xs" radius="md" width="30%" />];
    skeleton.push(<Skeleton height={"100%"} m="xs" radius="md" />);
    return <>{skeleton}</>;
  }

  if (error) return <Error message={"Players failed to load."} />;

  const players = data?.players.map((p) => (
    <Paper
      component={Link}
      to={`/player/${p.id}`}
      m="xs"
      p="xs"
      withBorder
      shadow={"md"}
      sx={(theme) => ({
        backgroundColor: theme.colors.orange[8],
        "&:hover": { backgroundColor: theme.colors.red[3], color: theme.colors.dark[9] },
      })}
    >
      <Group spacing={"xs"}>
        <Avatar src={p.avatar.mediumAvatarUrl} />
        <Stack justify={"center"} align="flex-start">
          <Text weight={"bold"} mb="-xs">
            {p.username}
          </Text>

          <Text mt="-xs" size="sm">
            last seen: &nbsp;
            <TimeAgo isoDate={p.lastSeen} />
          </Text>
        </Stack>
      </Group>
    </Paper>
  ));

  return (
    <>
      <Title order={2}>Players</Title>
      <Container
        mt="xs"
        pt={1}
        pb={1}
        px={0}
        sx={(theme) => ({ backgroundColor: theme.colors.dark[4], borderRadius: theme.radius.md })}
      >
        {players}
      </Container>
    </>
  );
}
