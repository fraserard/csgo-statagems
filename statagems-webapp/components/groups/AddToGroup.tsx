import { Form } from "@jobber/components/Form";
import { Content } from '@jobber/components/Content'
import { InputText } from "@jobber/components/InputText";
import { Button } from "@jobber/components/Button";
import { useFormState } from "@jobber/hooks";
import { useState } from 'react'
import { addPlayerToGroup, INewGroupPlayer, SingleGroupProps } from "../../helpers/GroupHelper";
import useUser from "../../helpers/UseUser";
const AddToGroup = ({gid}: SingleGroupProps) => {
    const [{ isDirty, isValid }, setFormState] = useFormState()
    const [playerId, setId] = useState(0)
    const { user } = useUser()
    
    const addPlayer = () => {
        const newPlayer: INewGroupPlayer = {
            requester_id: user.id,
            group_id: gid,
            player_id: playerId,
        }
        addPlayerToGroup(newPlayer)
    }
    return (
        <Form
            onSubmit={addPlayer}
            onStateChange={setFormState}>
            <Content>
                <InputText placeholder='Player ID' name='playerId' 
                    value={playerId} 
                    onChange={(_pid:number) => {setId(_pid) }}
                    validations={{
                        required: {
                            value: true,
                            message: 'Id is required',
                        },
                    }}/>
                <Button
                    label="Add Player"
                    submit={true}
                    disabled={!isDirty || !isValid}
                />
            </Content>
        </Form>
      );
}
 
export default AddToGroup;
