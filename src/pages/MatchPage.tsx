import Match from "../components/Match/Match";
import { Heading } from "@jobber/components/Heading";
import { Content } from "@jobber/components/Content";
import { Page } from "../components/Page/Page";
import { useParams } from 'react-router-dom';



function MatchPage() {
  const { matchId } = useParams();
  
  return (
    <Page>
    <Content>
      <Heading level={1}>Match Details</Heading>
      <Match matchId={Number(matchId)}/>
    </Content>
    </Page>

  );
}

export default MatchPage;