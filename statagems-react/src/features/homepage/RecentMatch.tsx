import { Button, Grid, Group, Skeleton, Stack, Text, Title } from "@mantine/core";
import { Link } from "react-router-dom";
import { useQuery } from "urql";
import Error from "~/components/Error";
import TimeAgo from "~/components/TimeAgo";
import { GetRecentMatchDocument, GetRecentMatchQuery } from "~/graphql";
import RecentMatchTeam from "./RecentMatchTeam";

export default function RecentMatch() {
  const [result] = useQuery<GetRecentMatchQuery>({
    query: GetRecentMatchDocument,
  });

  const { data, fetching, error } = result;

  if (fetching)
    return (
      <>
        <Skeleton height={50} radius="md" width="20%" />
        <Group position="center">
          <Skeleton height={300} mt="sm" radius="md" width="40%" />
          <Skeleton height={80} mt="sm" radius="md" width="15%" />
          <Skeleton height={300} mt="sm" radius="md" width="40%" />
        </Group>
      </>
    );

  if (error) return <Error message={"Recent match failed to load."} />;
  if (!data?.recentMatch) return <Text>No matches!</Text>;
  return (
    <>
      <Title order={3} mb={"sm"}>
        Latest Match
      </Title>
      <Grid
        mx="xs"
        sx={(theme) => ({ backgroundColor: theme.colors.dark[4], borderRadius: theme.radius.md })}
      >
        <Grid.Col md={5.5}>
          <RecentMatchTeam team={data!.recentMatch!.teams[0]} />
        </Grid.Col>
        <Grid.Col md={1}>
          <Stack align={"center"} justify={"center"} sx={() => ({ height: "100%" })}>
            <Text>{data!.recentMatch!.map.mapName}</Text>
            <Text weight={"bolder"} size="xl">
              {data!.recentMatch!.score}
            </Text>
            <Text align="center">
              <TimeAgo isoDate={data!.recentMatch!.datePlayed} />
            </Text>
            <Button component={Link} to={`/match/${data!.recentMatch!.id}`} variant="subtle">
              VIEW
            </Button>
          </Stack>
        </Grid.Col>
        <Grid.Col md={5.5}>
          <RecentMatchTeam team={data!.recentMatch!.teams[1]} />
        </Grid.Col>
      </Grid>
    </>
  );
}
