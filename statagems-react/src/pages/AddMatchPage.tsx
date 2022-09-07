import { Container, Loader } from "@mantine/core";
import { useQuery } from "urql";
import Error from "~/components/Error";
import AddMatchForm from "~/features/matches/AddMatchForm";
import { AddMatchSelectsDocument, AddMatchSelectsQuery } from "~/graphql";
import Page from "../layouts/Page";

function AddMatchPage() {
  const [result] = useQuery<AddMatchSelectsQuery>({
    query: AddMatchSelectsDocument,
  });

  const { data, fetching, error } = result;

  return (
    <Page title="Add Match">
      {fetching && <Loader />}
      {error && <Error message={error.message} />}

      {!fetching && !error && (
        <Container>
          <AddMatchForm
            mapsList={data!.playableMaps.map((m) => ({ value: m.id, label: m.mapName }))}
            playersList={data!.players.map((m) => ({ value: m.id, label: m.steamUsername }))}
          />
        </Container>
      )}
    </Page>
  );
}

export default AddMatchPage;
