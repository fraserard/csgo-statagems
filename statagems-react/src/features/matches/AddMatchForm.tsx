import { Button, Divider, Select, SelectItem, Title } from "@mantine/core";
import { useForm } from "@mantine/form";
import { randomId } from "@mantine/hooks";
import { showNotification } from "@mantine/notifications";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useMutation } from "urql";
import Error from "~/components/Error";
import ValidationErrors from "~/components/ValidationErrors";
import { FormValues } from "~/features/matches/AddMatchFormTypes";
import { AddMatchDocument, AddMatchMutationVariables, TeamSide } from "~/graphql";
import AddMatchFormTeam from "./AddMatchFormTeam";

interface Props {
  mapsList: SelectItem[];
  playersList: SelectItem[];
}

const playerDefaults = {
  isCaptain: false,
  playerId: null,
  kills: null,
  assists: null,
  deaths: null,
};

function AddMatchForm({ mapsList, playersList }: Props) {
  const navigate = useNavigate();
  const form = useForm<FormValues>({
    initialValues: {
      map: "",

      teams: [
        {
          startSide: TeamSide.Ct,
          roundsWon: null,

          players: [
            { ...playerDefaults, key: randomId() },
            { ...playerDefaults, key: randomId() },
            { ...playerDefaults, key: randomId() },
            { ...playerDefaults, key: randomId() },
            { ...playerDefaults, key: randomId() },
          ],
        },
        {
          startSide: TeamSide.T,
          roundsWon: null,

          players: [
            { ...playerDefaults, key: randomId() },
            { ...playerDefaults, key: randomId() },
            { ...playerDefaults, key: randomId() },
            { ...playerDefaults, key: randomId() },
            { ...playerDefaults, key: randomId() },
          ],
        },
      ],
    },
  });

  const [addMatchResult, addMatch] = useMutation(AddMatchDocument);
  const submitForm = async (values: FormValues) => {
    const variables: AddMatchMutationVariables = {
      matchData: {
        mapId: parseInt(values.map),
        team1: {
          startSide: values.teams[0].startSide,
          roundsWon: values.teams[0].roundsWon!,
          captainId: parseInt(values.teams[0].players.find((p) => p.isCaptain)?.playerId!),
          player1: {
            playerId: parseInt(values.teams[0].players[0].playerId!),
            kills: values.teams[0].players[0].kills!,
            assists: values.teams[0].players[0].assists!,
            deaths: values.teams[0].players[0].deaths!,
          },
          player2: {
            playerId: parseInt(values.teams[0].players[1].playerId!),
            kills: values.teams[0].players[1].kills!,
            assists: values.teams[0].players[1].assists!,
            deaths: values.teams[0].players[1].deaths!,
          },
          player3: {
            playerId: parseInt(values.teams[0].players[2].playerId!),
            kills: values.teams[0].players[2].kills!,
            assists: values.teams[0].players[2].assists!,
            deaths: values.teams[0].players[2].deaths!,
          },
          player4: {
            playerId: parseInt(values.teams[0].players[3].playerId!),
            kills: values.teams[0].players[3].kills!,
            assists: values.teams[0].players[3].assists!,
            deaths: values.teams[0].players[3].deaths!,
          },
          player5: {
            playerId: parseInt(values.teams[0].players[4].playerId!),
            kills: values.teams[0].players[4].kills!,
            assists: values.teams[0].players[4].assists!,
            deaths: values.teams[0].players[4].deaths!,
          },
        },
        team2: {
          startSide: values.teams[1].startSide,
          roundsWon: values.teams[1].roundsWon!,
          captainId: parseInt(values.teams[1].players.find((p) => p.isCaptain)?.playerId!),
          player1: {
            playerId: parseInt(values.teams[1].players[0].playerId!),
            kills: values.teams[1].players[0].kills!,
            assists: values.teams[1].players[0].assists!,
            deaths: values.teams[1].players[0].deaths!,
          },
          player2: {
            playerId: parseInt(values.teams[1].players[1].playerId!),
            kills: values.teams[1].players[1].kills!,
            assists: values.teams[1].players[1].assists!,
            deaths: values.teams[1].players[1].deaths!,
          },
          player3: {
            playerId: parseInt(values.teams[1].players[2].playerId!),
            kills: values.teams[1].players[2].kills!,
            assists: values.teams[1].players[2].assists!,
            deaths: values.teams[1].players[2].deaths!,
          },
          player4: {
            playerId: parseInt(values.teams[1].players[3].playerId!),
            kills: values.teams[1].players[3].kills!,
            assists: values.teams[1].players[3].assists!,
            deaths: values.teams[1].players[3].deaths!,
          },
          player5: {
            playerId: parseInt(values.teams[1].players[4].playerId!),
            kills: values.teams[1].players[4].kills!,
            assists: values.teams[1].players[4].assists!,
            deaths: values.teams[1].players[4].deaths!,
          },
        },
      },
    };

    addMatch(variables).then((result) => {
      if (result.data?.addMatch.match) {
        navigate(`/match/${result.data.addMatch.match.id}`);
        showNotification({
          message: `Match Added`,
          color: "green",
        });
      }
    });
  };

  const setStartSides = (side: string, teamPath: string) => {
    const TEAM_ZERO = "teams.0";
    const TEAM_ONE = "teams.1";

    if (side === TeamSide.Ct && teamPath === TEAM_ZERO) {
      form.setFieldValue(`${TEAM_ZERO}.startSide`, TeamSide.Ct);
      form.setFieldValue(`${TEAM_ONE}.startSide`, TeamSide.T);
    } else if (side === TeamSide.T && teamPath === TEAM_ZERO) {
      form.setFieldValue(`${TEAM_ZERO}.startSide`, TeamSide.T);
      form.setFieldValue(`${TEAM_ONE}.startSide`, TeamSide.Ct);
    } else if (side === TeamSide.Ct && teamPath === TEAM_ONE) {
      form.setFieldValue(`${TEAM_ONE}.startSide`, TeamSide.Ct);
      form.setFieldValue(`${TEAM_ZERO}.startSide`, TeamSide.T);
    } else if (side === TeamSide.T && teamPath === TEAM_ONE) {
      form.setFieldValue(`${TEAM_ONE}.startSide`, TeamSide.T);
      form.setFieldValue(`${TEAM_ZERO}.startSide`, TeamSide.Ct);
    }
  };

  const [players, setPlayersList] = useState(playersList);

  return (
    <>
      {addMatchResult.error && <Error message={addMatchResult.error.message} />}
      {addMatchResult.data?.addMatch.errors && (
        <ValidationErrors errors={addMatchResult.data!.addMatch.errors} />
      )}

      <form onSubmit={form.onSubmit((values: FormValues) => submitForm(values))}>
        <Select
          label="Map played"
          placeholder="Choose map"
          data={mapsList}
          required
          {...form.getInputProps("map")}
        ></Select>

        <Divider my="sm" />

        <Title order={2} mb="xs">
          Team 1
        </Title>

        <AddMatchFormTeam
          formPath="teams.0"
          form={form}
          onStartSideChange={setStartSides}
          players={form.values.teams[0].players}
          playersList={players}
          setPlayersList={setPlayersList}
        />

        <Divider my="sm" />

        <Title order={2} mb="xs">
          Team 2
        </Title>

        <AddMatchFormTeam
          formPath="teams.1"
          form={form}
          onStartSideChange={setStartSides}
          players={form.values.teams[1].players}
          playersList={players}
          setPlayersList={setPlayersList}
        />

        <Divider my="sm" />

        <Button type="submit" mr="xl">
          Add Match
        </Button>
        <Button type="reset" variant="outline" onClick={() => form.reset()}>
          Reset
        </Button>
      </form>
    </>
  );
}

export default AddMatchForm;
