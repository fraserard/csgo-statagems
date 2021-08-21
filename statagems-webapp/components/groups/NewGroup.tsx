import { Form } from "@jobber/components/Form";
import { Content } from '@jobber/components/Content'
import { InputText } from "@jobber/components/InputText";
import { Button } from "@jobber/components/Button";
import { useFormState } from "@jobber/hooks";
import { addGroup, iNewGroup } from "../../helpers/UseGroup";
import useUser from '../../helpers/UseUser'
import { useState } from 'react'

const NewGroup = () => {
    const [{ isDirty, isValid }, setFormState] = useFormState()
    const [name, setName] = useState('')
    const [desc, setDesc] = useState('')
    const { user } = useUser()

    const submitGroup = () => {
        const newGroup: iNewGroup = {
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
                    onChange={newValue =>{
                        if (typeof newValue == "string") setName(newValue) }
                    }
                    validations={{
                        required: {
                            value: true,
                            message: 'Group name is required',
                        },
                        minLength: {
                            value: 3,
                            message: 'Group name is too short',
                        },
                        maxLength: {
                            value: 32,
                            message: 'Group name is too long',
                        },
                    }} 
                />
                <InputText placeholder='Group Description' multiline name='groupDescription' 
                    value={desc} 
                    onChange={newValue =>{
                        if (typeof newValue == "string") setDesc(newValue) }
                    }
                    validations={{
                        required: {
                            value: false,
                            message: 'Group name is required',
                        },
                        maxLength: {
                            value: 255,
                            message: 'Description is too long',
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