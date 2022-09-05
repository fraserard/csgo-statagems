import { Container } from "@mantine/core";
import MatchList from "../features/homepage/MatchList";
import Page from "../layouts/Page";

export default function HomePage() {
  return (
    <Page title="Home">
        <MatchList />
    </Page>
  );
}
