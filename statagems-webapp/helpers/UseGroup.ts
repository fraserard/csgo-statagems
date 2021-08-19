import { server } from "../config";
import {getOptions} from './AuthHelper'
import useSWR, { SWRResponse } from "swr"

export const groupFetcher = async () => {
    
    const resp: Response = await fetch(`${server}/api/groups`, getOptions())
    if (!resp.ok) throw new Error('Not authorized.')

    const data: Group[] = await resp.json()
    return data
}
  
export function useGroups() {
    
    const {data, error} : SWRResponse<Group[],Error> = useSWR('/api/groups', groupFetcher)
    let isLoading = false, isError = false
    if(error) isError = true
    if(!data && !isError) isLoading = true
    
    return {
        groups: data,
        isError,
        isLoading
    }
}

export interface Group{
    id: number
    creator_id: number
    group_name: string
    description: string
    members: number[]
    created_at: Date

    // _links: {key: string, uri: string}
}

