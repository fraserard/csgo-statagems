import { Loader } from "@mantine/core";
import { useQuery } from "urql";
import Error from "~/components/Error";
import MapsTable from "~/features/management/MapsTable";
import { GetAllMapsDocument, GetAllMapsQuery } from "~/graphql";
import Page from "~/layouts/Page";

export default function ManageMapsPage() {
  const [{ data, fetching, error }] = useQuery<GetAllMapsQuery>({
    query: GetAllMapsDocument,
  });

  return (
    <Page title="Manage Maps">
      {fetching && <Loader />}
      {error && <Error message={error.message} />}
      {data?.maps! && <MapsTable mapsFragment={data?.maps!} />}
    </Page>
  );
}
