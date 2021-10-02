import { Form } from "@jobber/components/Form";
import { Content } from '@jobber/components/Content'
import { InputText } from "@jobber/components/InputText";
import { Button } from "@jobber/components/Button";
import { useFormState } from "@jobber/hooks";
import { addGroup, INewGroup } from "../../helpers/GroupHelper";
import useUser from '../../helpers/UseUser'
import { useState } from 'react'

const NewGroup = () => {
    const [{ isDirty, isValid }, setFormState] = useFormState()
    const [name, setName] = useState('')
    const [desc, setDesc] = useState('')
    const { user } = useUser()

    const submitGroup = () => {
        const newGroup: INewGroup = {
            creator_id: user.id,
            group_name: name,
            description: desc,
        }
        addGroup(newGroup)
    }

    return(
        <Form
            onSubmit={submitGroup}
            onStateChange={setFormState} >
            <Content>
                <InputText placeholder='Group Name' name='groupName' 
                    value={name} 
                    onChange={(_name:string) => {setName(_name) }}
                    validations={{
                        required: {
                            value: true,
                            message: 'Group name is required',
                        },
                        minLength: {
                            value: 3,
                            message: 'Group name is too short (min 3 characters)',
                        },
                        maxLength: {
                            value: 32,
                            message: 'Group name is too long (max 32 characters)',
                        },
                    }} 
                />
                <InputText placeholder='Group Description' multiline name='groupDescription' 
                    value={desc} 
                    onChange={(_desc:string) => {setDesc(_desc) }}
                    validations={{
                        required: {
                            value: false,
                        },
                        maxLength: {
                            value: 255,
                            message: 'Group description is too long (max 255 characters)',
                        },
                    }} 
                />
                <Button
                    label="Create Group"
                    submit={true}
                    disabled={!isDirty || !isValid}
                />
            </Content>
        </Form>
    )
}


export default NewGroup