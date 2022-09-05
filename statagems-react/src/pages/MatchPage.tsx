import { useParams } from "react-router-dom";
import Page from "~/layouts/Page";
import Match from "~/features/matches/Match";

function MatchPage() {
  const { matchId } = useParams();

  return (
    <Page title="Match Details">
      <Match matchId={Number(matchId)} />
    </Page>
  );
}

export default MatchPage;
