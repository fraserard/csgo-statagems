import { Grid } from "@mantine/core";
import PlayerList from "~/features/homepage/PlayerList";
import MatchList from "../features/homepage/MatchList";
import Page from "../layouts/Page";

export default function HomePage() {
  return (
    <Page title="Home">
      <Grid justify={"space-evenly"}>
        <Grid.Col sm={8}>
          <MatchList />
        </Grid.Col>
        <Grid.Col sm={4}>
          <PlayerList />
        </Grid.Col>
      </Grid>
    </Page>
  );
}
