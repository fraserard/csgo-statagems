import { Grid } from "@mantine/core";
import PlayerList from "~/features/homepage/PlayerList";
import MatchList from "../features/homepage/MatchList";
import Page from "../layouts/Page";

export default function HomePage() {
  return (
    <Page title="Home">
      <Grid>
        <Grid.Col xl={8} sm={8} xs={8}>
          <MatchList />
        </Grid.Col>
        <Grid.Col xl={3} sm={4} xs={4}>
          <PlayerList />
        </Grid.Col>
      </Grid>
    </Page>
  );
}
