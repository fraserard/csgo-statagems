import { Avatar, Card, Group, Stack, Text } from "@mantine/core";
import { Link } from "react-router-dom";
import TimeAgo from "~/components/TimeAgo";
import { GetMatchListQuery } from "~/graphql";

interface NewMatchCardProps {
  match: GetMatchListQuery["matches"][0];
}

export default function NewMatchCard({ match }: NewMatchCardProps) {
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
      <Group grow>
        <Group position="center">
          {match.teams[0].matchPlayers.map((player) => (
            <Avatar key={player.playerId} src={player.avatar.smallAvatarUrl} />
          ))}
        </Group>

        <Stack align="center" spacing="xs">
          <Text>{match.map.mapName}</Text>
          <Text weight="bold" size="xl" mt="-xs" mb="-xs">
            {match.score}
          </Text>
          <Text>
            <TimeAgo isoDate={match.datePlayed} />
          </Text>
        </Stack>

        <Group position="center">
          {match.teams[1].matchPlayers.map((player) => (
            <Avatar key={player.playerId} src={player.avatar.smallAvatarUrl} />
          ))}
        </Group>
      </Group>
    </Card>
  );
}
