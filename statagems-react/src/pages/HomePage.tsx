import { Divider, Grid } from "@mantine/core";
import PlayerList from "~/features/homepage/PlayerList";
import RecentMatch from "~/features/homepage/RecentMatch";
import MatchList from "../features/homepage/MatchList";
import Page from "../layouts/Page";

export default function HomePage() {
  return (
    <Page title="Home">
      <RecentMatch />
      <Divider mt="xl" mb="xs" />
      <Grid>
        <Grid.Col sm={8} xs={8}>
          <MatchList />
        </Grid.Col>
        <Grid.Col sm={4} xs={4}>
          <PlayerList />
        </Grid.Col>
      </Grid>
    </Page>
  );
}
