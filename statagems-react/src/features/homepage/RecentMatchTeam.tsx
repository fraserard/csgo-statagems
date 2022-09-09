import { Avatar, Paper, Table, Text } from "@mantine/core";
import { Outcome, RecentMatchTeamFragment } from "~/graphql";

interface RecentMatchTeamProps {
  team: RecentMatchTeamFragment;
}

export default function RecentMatchTeam({ team }: RecentMatchTeamProps) {
  const tableHeaders = (
    <tr>
      <th></th>
      <th>
        <Text color={"black"}>Player</Text>
      </th>
      <th>
        <Text color={"black"}>K</Text>
      </th>
      <th>
        <Text color={"black"}>A</Text>
      </th>
      <th>
        <Text color={"black"}>D</Text>
      </th>
    </tr>
  );
  const tableRows = team.matchPlayers.map((player) => (
    <tr key={player.playerId}>
      {player.playerId == team.captainId ? <td>👑</td> : <td></td>}
      <td>
        <Text lineClamp={1} size="md">
          <Avatar
            mr="xs"
            src={player.avatar.smallAvatarUrl}
            alt={`Avatar of ${player.steamUsername}`}
            sx={() => ({
              display: "inline-block",
            })}
          />
          {player.steamUsername}
        </Text>
      </td>
      <td>
        {player.kills}
      </td>
      <td>{player.assists}</td>
      <td>{player.deaths}</td>
    </tr>
  ));
  return (
    <>
      <Paper
        shadow="sm"
        p="sm"
        radius="md"
        withBorder
        sx={(theme) => ({
          backgroundColor:
            team.outcome == Outcome.Won
              ? theme.colors.green[5]
              : team.outcome == Outcome.Lost
              ? theme.colors.red[5]
              : theme.colors.yellow[5],
        })}
      >
        <Table
          sx={(theme) => ({
            color: theme.black,
          })}
        >
          <thead>{tableHeaders}</thead>
          <tbody>{tableRows}</tbody>
        </Table>
      </Paper>
    </>
  );
}
