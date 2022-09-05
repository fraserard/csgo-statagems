import { Avatar, Badge, Group, Paper, Table, Text } from "@mantine/core";
import { GetMatchQuery, Outcome, TeamSide, MatchTeamFragment } from "~/graphql";

interface Props {
  team: MatchTeamFragment;
}

function MatchTeam({ team }: Props) {
  const tableHeaders = (
    <tr>
      <th></th>
      <th>Player</th>
      <th>K</th>
      <th>A</th>
      <th>D</th>
    </tr>
  );
  const tableRows = team.matchPlayers.map((player) => (
    <tr key={player.playerId}>
      {player.playerId == team.captainId ? <td>👑</td> : <td></td>}
      <td>
        <Group>
          <Avatar src={player.avatar.smallAvatarUrl} alt={`Avatar of ${player.steamUsername}`} />
          {player.steamUsername}
        </Group>
      </td>
      <td>{player.kills}</td>
      <td>{player.assists}</td>
      <td>{player.deaths}</td>
    </tr>
  ));
  return (
    <>
      <Paper shadow="sm" p="lg" radius="xs" withBorder mb="md">
        <Table highlightOnHover>
          <caption>
            <Group position="center">
              <Badge
                color={
                  team.outcome === Outcome.Won ? "green" : team.outcome === Outcome.Lost ? "red" : "yellow"
                }
                size="xl"
                variant="filled"
              >
                {team.outcome === Outcome.Won
                  ? "W I N N E R"
                  : team.outcome === Outcome.Lost
                  ? "L O S E R"
                  : "T I E D"}
              </Badge>

              <Badge color={team.startSide === TeamSide.Ct ? "blue" : "orange"} size="lg" variant="outline">
                Started {team.startSide}
              </Badge>

              <Text>{"Rounds Won: " + team.roundsWon}</Text>
            </Group>
          </caption>
          <thead>{tableHeaders}</thead>
          <tbody>{tableRows}</tbody>
        </Table>
      </Paper>
    </>
  );
}

export default MatchTeam;
