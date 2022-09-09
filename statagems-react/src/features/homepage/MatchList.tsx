import { Skeleton, Title } from "@mantine/core";
import { useQuery } from "urql";
import Error from "~/components/Error";
import { GetMatchListDocument, GetMatchListQuery } from "~/graphql";
import MatchCard from "./MatchCard";

function MatchList() {
  const [result] = useQuery<GetMatchListQuery>({
    query: GetMatchListDocument,
  });

  const { data, fetching, error } = result;
  if (fetching)
    return (
      <>
        <Skeleton height={50} radius="md" width="20%" />
        <Skeleton height={80} mt="sm" radius="md" />
        <Skeleton height={80} mt="sm" radius="md" />
        <Skeleton height={80} mt="sm" radius="md" />
        <Skeleton height={80} mt="sm" radius="md" />
        <Skeleton height={80} mt="sm" radius="md" />
        <Skeleton height={80} mt="sm" radius="md" />
        <Skeleton height={80} mt="sm" radius="md" />
      </>
    );
  if (error) return <Error message={"Matches failed to load."} />;
  if (!data?.matches) return <></>;
  const allMatches = data?.matches.slice(1);

  return (
    <>
      <Title order={3}>Matches</Title>

      {allMatches!.map((match) => (
        <MatchCard key={match.id} match={match} />
      ))}
    </>
  );
}

export default MatchList;
