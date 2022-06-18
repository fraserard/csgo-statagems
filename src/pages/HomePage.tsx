import { Page } from "../components/Page/Page";
import { Heading } from "@jobber/components/Heading";
import MatchList from "../components/Match/MatchList";


function HomePage() {
  return (
    <Page>
      <Heading level={1}>Matches</Heading>
      <MatchList />
    </Page>
  );
}

export default HomePage;