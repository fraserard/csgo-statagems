import { Heading } from "@jobber/components/Heading";
import { Content } from "@jobber/components/Content";
import MatchTeam from "./MatchTeam";
import { useQuery } from 'urql';
import { GetMatchQuery, GetMatch, GetMatchQueryVariables } from '~/gql/generated';


interface Props {
  matchId: Number;
}

function Match({ matchId }: Props){
  const [result] = useQuery<GetMatchQuery, GetMatchQueryVariables>({ 
    query: GetMatch, 
    variables: {matchId: Number(matchId)},
  })

  const { data, fetching, error } = result;
  if (fetching) return <p>Loading...</p>
  if (error) return <p>Error! {error.message}</p>

  const match = data!.match;

  return (
    <>
      <Content>
        <Heading level={3}>{match.datePlayed}</Heading>
        <Heading level={2}>{match.map.mapName}</Heading>
        <Heading level={2}>{match.score}</Heading>
        <MatchTeam key={match.teams[0].teamId} team={match.teams[0]}></MatchTeam>
        <MatchTeam key={match.teams[1].teamId} team={match.teams[1]}></MatchTeam>
      </Content>
    </>
  );
}

export default Match;