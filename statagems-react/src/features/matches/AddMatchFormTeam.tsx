import { Chip, Group, NumberInput, SelectItem } from '@mantine/core';
import { UseFormReturnType } from '@mantine/form';

import { useEffect, useState } from "react";
import { TeamSide} from '~/graphql';

import AddMatchFormPlayer from "./AddMatchFormPlayer";
import { FormValues } from "./AddMatchFormTypes";



interface Props {
  form: UseFormReturnType<FormValues>;
  formPath: string;
  players: Player[];
  onStartSideChange: Function;
  playersList: SelectItem[];
  setPlayersList: Function;
}

interface Player {
  key: string;
  playerId: string | null;
  kills: number | null;
  deaths: number | null;
  assists: number | null;
  isCaptain: boolean;
}


function AddMatchFormTeam({form, formPath, onStartSideChange, players, playersList, setPlayersList}: Props){
  
  const [captainIndex, setCaptainIndex] = useState(-1);
  
  useEffect(() => {
    if (captainIndex !== -1){
      form.setFieldValue(`${formPath}.players.${captainIndex}.isCaptain`, true)
    }
  }, [captainIndex])

  const setCaptain = (checked: boolean, playerIndex: number) => {
    console.log("is checked: " + checked)
    if (checked){
      if (captainIndex !== -1){
        form.setFieldValue(`${formPath}.players.${captainIndex}.isCaptain`, false)
      }
      setCaptainIndex(playerIndex)
    }else{
      form.setFieldValue(`${formPath}.players.${playerIndex}.isCaptain`, false)
      setCaptainIndex(-1)
    }
  }

 
  const playerRows = players.map((player, index) => (  
    <AddMatchFormPlayer key={player.key} 
      form={form} formPath={`${formPath}.players.${index}`} 
      playerIndex={index} 
      onCaptainChange={setCaptain} 
      playersList={playersList}
      setPlayersList={setPlayersList} />
    ))

  return (
  <>
    <Group mb="sm">
      <NumberInput placeholder="Rounds won" 
          required min={0} 
          {...form.getInputProps(`${formPath}.roundsWon`)} 
        />
      
      <Chip.Group multiple={false} 
        {...form.getInputProps(`${formPath}.startSide`)}
        onChange={(v: TeamSide) => onStartSideChange(v, formPath)}
      >
        <Chip value={TeamSide.Ct} color="blue">CT</Chip>
        <Chip value={TeamSide.T} color="orange">T</Chip>
      </Chip.Group>
    </Group>
    
    <table>
      <thead>
        <tr>
          <th>👑</th>
          <th>Player</th>
          <th>Kills</th>
          <th>Assists</th>
          <th>Deaths</th>
        </tr>
      </thead>
      <tbody>
        {
          playerRows
        } 
      </tbody>
    </table>
  </>
  );
}

export default AddMatchFormTeam;