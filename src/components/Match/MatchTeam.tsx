import {
  Table,
  Header,
  Body,
  Row,
  Cell,
  CellNumeric,
} from "@jobber/components/Table";
import { Card } from "@jobber/components/Card";
import { Content } from "@jobber/components/Content";
import { Tooltip } from "@jobber/components/Tooltip";
import { Heading } from "@jobber/components/Heading";
import { GetMatchQuery, Outcome } from '~/gql/generated';


interface Props {
  team: GetMatchQuery['match']['teams'][0];
}

function MatchTeam({team}: Props){
  return(
    
    <Card title={
      team.outcome === Outcome.Won ? `Winner :  ${team.roundsWon} Rounds Won` : 
      team.outcome === Outcome.Lost ? `Loser :  ${team.roundsWon} Rounds Won` : "TIED"
      }
      // @ts-ignore (accent colour typing error)
      accent={team.outcome === Outcome.Won ? "green" : team.outcome === Outcome.Lost ? "red" : "yellow"} 
    > 
      <Content spacing="small">
        <Heading level={4}>{team.startSide + " Side Start"}</Heading>
        <Table>
          <Header>
            <Cell></Cell>
            <Cell>Player</Cell>
            <Cell align="right">K</Cell>
            <Cell align="right">A</Cell>
            <Cell align="right">D</Cell>
          </Header>
          <Body>
            {team.matchPlayers.map(player => {
              return (
                <Row key={player.playerId}>
                  {player.playerId == team.captainId 
                    ? <Cell align="center"><Tooltip message="Team Captain"><p>👑</p></Tooltip></Cell> 
                    : <Cell></Cell>
                  }
                  <Cell><img src={player.avatar.smallAvatarUrl}></img>{player.steamUsername}</Cell>
                  <CellNumeric value={player.kills}></CellNumeric>
                  <CellNumeric value={player.assists}></CellNumeric>
                  <CellNumeric value={player.deaths}></CellNumeric>
                </Row>
              );
            })}
          </Body>
        </Table>
      </Content>
    </Card>
  );
}

export default MatchTeam;