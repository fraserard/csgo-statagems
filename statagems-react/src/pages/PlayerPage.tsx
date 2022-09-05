import { useParams } from "react-router-dom";
import Page from "~/layouts/Page";

export default function PlayerPage() {
  const { playerId } = useParams();

  return <Page title={`Player ${playerId}`}>Work in progress! :]</Page>;
}
