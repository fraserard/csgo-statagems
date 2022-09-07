import { Container } from "@mantine/core";
import { useParams } from "react-router-dom";
import Match from "~/features/matches/Match";
import Page from "~/layouts/Page";

function MatchPage() {
  const { matchId } = useParams();

  return (
    <Page title="Match Details">
      <Container>
        <Match matchId={Number(matchId)} />
      </Container>
    </Page>
  );
}

export default MatchPage;
