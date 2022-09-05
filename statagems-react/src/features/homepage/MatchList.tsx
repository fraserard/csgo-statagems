import { Skeleton, Title } from "@mantine/core";
import { useQuery } from "urql";
import Error from "~/components/Error";
import { GetMatchListDocument, GetMatchListQuery } from "~/graphql";
import NewMatchCard from "./NewMatchCard";

function MatchList() {
  const [result] = useQuery<GetMatchListQuery>({
    query: GetMatchListDocument,
  });

  const { data, fetching, error } = result;
  if (fetching)
    return (
      <>
        <Skeleton height={50} radius="md" width="20%" />
        <Skeleton height={100} mt="sm" radius="md" />
        <Skeleton height={100} mt="sm" radius="md" />
        <Skeleton height={100} mt="sm" radius="md" />
        <Skeleton height={100} mt="sm" radius="md" />
        <Skeleton height={100} mt="sm" radius="md" />
        <Skeleton height={100} mt="sm" radius="md" />

      </>
    );
  if (error) return <Error message={error.message} />;

  return (
    <>
      <Title order={2}>Matches</Title>

      {data!.matches.map((match) => (
        <NewMatchCard key={match.id} match={match} />
      ))}
    </>
  );
}

export default MatchList;
