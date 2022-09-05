import { Select, Checkbox, NumberInput, SelectItem } from "@mantine/core"
import { UseFormReturnType } from '@mantine/form';
import { useState } from "react";

import { FormValues } from "./AddMatchFormTypes";


interface Props {
  form: UseFormReturnType<FormValues>;
  formPath: string;
  playerIndex: number;
  onCaptainChange: Function;
  playersList: SelectItem[];
  setPlayersList: Function;
}

function AddMatchFormPlayer({form, formPath, playerIndex, onCaptainChange, playersList, setPlayersList}: Props){
  
  const [selectedPlayerId, setSelectedPlayerId] = useState('');
  const updatePlayersList = (playerId: string, previousPlayerId: string) => {
    const updatedPlayersList = playersList.map(player => (
      player.value === playerId ? {...player, disabled: true} :
      player.value === previousPlayerId ? {...player, disabled: false} : 
      player
    ));
    form.setFieldValue(`${formPath}.playerId`, playerId);
    setPlayersList(updatedPlayersList);
    setSelectedPlayerId(playerId);
  };

  return (    
  <tr>
    <td><Checkbox {...form.getInputProps(`${formPath}.isCaptain`, { type: 'checkbox' })} onChange={(e) => onCaptainChange(e.target.checked, playerIndex)}/></td>
    <td><Select {...form.getInputProps(`${formPath}.playerId`)}
          placeholder="Choose Player" 
          data={playersList} searchable required
          onChange={(v) => updatePlayersList(v!, selectedPlayerId)}
        />
    </td>
    <td>      
      <NumberInput {...form.getInputProps(`${formPath}.kills`)} required />
    </td>
    <td>      
      <NumberInput {...form.getInputProps(`${formPath}.assists`)} required />
    </td>
    <td>      
      <NumberInput {...form.getInputProps(`${formPath}.deaths`)} required />
    </td>
  </tr> );
}

export default AddMatchFormPlayer;