
import { GetMatchList, GetMatchListQuery } from '~/gql/generated';
import { useQuery } from "urql";
import MatchCard from "~/components/Match/MatchCard"

function MatchList(){
  
  const [result] = useQuery<GetMatchListQuery>({ 
    query: GetMatchList, 
  })

  const { data, fetching, error } = result;
  if (fetching) return <p>Loading...</p>
  if (error) return <p>Error! {error.message}</p>

  return (
      <ul>
        {data!.matches.map(match => 
          <MatchCard key={match.id} match={match} />
        )}
      </ul>
  );
}

export default MatchList;