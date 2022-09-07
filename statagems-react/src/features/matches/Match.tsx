import { Container, Group, Loader, Title } from "@mantine/core";
import { useQuery } from "urql";
import TimeAgo from "~/components/TimeAgo";
import { GetMatchDocument } from "~/graphql";
import MatchTeam from "./MatchTeam";

interface Props {
  matchId: number;
}

function Match({ matchId }: Props) {
  const [result] = useQuery({
    query: GetMatchDocument,
    variables: { matchId: Number(matchId) },
  });

  const { data, fetching, error } = result;
  if (fetching) return <Loader />;
  if (error) return <p>Error! {error.message}</p>;

  const match = data!.match!;

  return (
    <>
      <Container size={"xs"}>
        <Group mb="md" position="apart">
          <Title order={2}>{match.map.mapName}</Title>
          <Title order={2}>{match.score}</Title>
          <Title order={3}>
            <TimeAgo isoDate={match.datePlayed} />
          </Title>
        </Group>
      </Container>
      <MatchTeam key={match.teams[0].teamId} team={match.teams[0]}></MatchTeam>
      <MatchTeam key={match.teams[1].teamId} team={match.teams[1]}></MatchTeam>
    </>
  );
}

export default Match;
