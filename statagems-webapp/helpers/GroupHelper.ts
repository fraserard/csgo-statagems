import { server } from "../config";
import {getOptions, postOptions} from './AuthHelper'
import useSWR, { mutate, SWRResponse } from "swr"

// TODO ADD USER ID KEY TO EACH SWR PARAMETER
export function useGroups() {
    const {data, error} : SWRResponse<IGroup[],Error> = useSWR('/api/groups', groupsFetcher)
    
    return {
        groups: data,
        isError: !!error,
        isLoading: !data && !error
    }
}
export const groupsFetcher = async () => {
    const resp: Response = await fetch(`${server}/api/groups`, getOptions())
    if (!resp.ok) throw new Error('Not authorized.')

    const data: IGroup[] = await resp.json()
    return data
}

export function useGroup(gid: number) {
    const {data, error} : SWRResponse<IGroup,Error> = useSWR(['/api/groups/', gid], () => groupFetcher(gid))

    return {
        group: data,
        isError: !!error,
        isLoading: !data && !error
    }
}
export const groupFetcher = async (gid: number) => {
    const resp: Response = await fetch(`${server}/api/groups/${gid}`, getOptions())
    if (!resp.ok) throw new Error('Not authorized.')

    const data: IGroup = await resp.json()
    return data
}
  
export interface IGroup{
    id: number
    creator_id: number
    group_name: string
    description?: string
    members: number[]
    created_at: Date

    // _links: {key: string, uri: string}
}
export interface INewGroup{
    creator_id: number
    group_name: string
    description?: string
}

export const addGroup = async (group: INewGroup) => {
    const resp: Response = await fetch(`${server}/api/groups`, postOptions(group))
    if (!resp.ok) throw new Error('Not authorized.')

    mutate('/api/groups')
}

export interface INewGroupPlayer{
    requester_id: number
    group_id: number
    player_id: number
}
export const addPlayerToGroup = async (groupPlayer: INewGroupPlayer) => {
    const resp: Response = await fetch(`${server}/api/groups/${groupPlayer.group_id}/${groupPlayer.player_id}`, postOptions())
    if (!resp.ok) throw new Error('Not authorized.')

    mutate(['/api/groups/', groupPlayer.group_id])
}

export interface SingleGroupProps{
    gid: number
}
