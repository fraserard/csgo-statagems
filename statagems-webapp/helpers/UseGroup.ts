import { server } from "../config";
import {getOptions, postOptions} from './AuthHelper'
import useSWR, { SWRResponse } from "swr"

export function useGroups() {
    
    const {data, error} : SWRResponse<iGroup[],Error> = useSWR('/api/groups', groupFetcher)
    let isLoading = false, isError = false
    if(error) isError = true
    if(!data && !isError) isLoading = true
    
    return {
        groups: data,
        isError,
        isLoading
    }
}

export const groupFetcher = async () => {
    
    const resp: Response = await fetch(`${server}/api/groups`, getOptions())
    if (!resp.ok) throw new Error('Not authorized.')

    const data: iGroup[] = await resp.json()
    return data
}
  
export interface iGroup{
    id: number
    creator_id: number
    group_name: string
    description?: string
    members: number[]
    created_at: Date

    // _links: {key: string, uri: string}
}
export interface iNewGroup{
    creator_id: number
    group_name: string
    description?: string
}

export const addGroup = async (group: iNewGroup) => {
    const resp: Response = await fetch(`${server}/api/groups`, postOptions(group))
    if (!resp.ok) throw new Error('Not authorized.')
}
