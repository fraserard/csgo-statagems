import { Avatar, Card, Grid, Group, Stack, Text } from "@mantine/core";
import { Link } from "react-router-dom";
import TimeAgo from "~/components/TimeAgo";
import { GetMatchListQuery } from "~/graphql";

interface MatchCardProps {
  match: GetMatchListQuery["matches"][0];
}

export default function MatchCard({ match }: MatchCardProps) {
  return (
    <Card
      sx={(theme) => ({
        backgroundColor: theme.colors.blue[8],
        "&:hover": { backgroundColor: theme.colors.orange[7], color: theme.colors.dark[9] },
      })}
      withBorder
      shadow={"md"}
      component={Link}
      to={`match/${match.id}`}
      m="xs"
      p="xs"
    >
      <Grid align="center">
        <Grid.Col lg={5}>
          <Group position="center">
            {match.teams[0].matchPlayers.map((player) => (
              <Avatar key={player.playerId} src={player.avatar.mediumAvatarUrl} />
            ))}
          </Group>
        </Grid.Col>
        <Grid.Col lg={2}>
          <Stack align="center" spacing="xs" my={"-xs"}>
            <Text>{match.map.mapName}</Text>
            <Text weight="bold" size="xl" mt="-xs" mb="-xs">
              {match.score}
            </Text>
            <Text align="center">
              <TimeAgo isoDate={match.datePlayed} />
            </Text>
          </Stack>
        </Grid.Col>
        <Grid.Col lg={5}>
          <Group position="center">
            {match.teams[1].matchPlayers.map((player) => (
              <Avatar key={player.playerId} src={player.avatar.mediumAvatarUrl} />
            ))}
          </Group>
        </Grid.Col>
      </Grid>
    </Card>
  );
}
