import { useGroup, SingleGroupProps } from '../../helpers/GroupHelper'
import Link from 'next/link'
import { mutate } from 'swr'

const SingleGroup = ({ gid }: SingleGroupProps) => {
    const { group, isLoading, isError } = useGroup(gid)

    if (isLoading){
        return (<p>loading</p>)
    } 
    if(isError){
        return (<p>error</p>)
    }
    const membersList = group!.members.map((m) => 
        <li key={m}>
            <Link href={`/player/${encodeURIComponent(m)}`}><a>Member id: {m}</a></Link>
        </li>
    ) 

    return(  
        <>
            <h2>{group!.group_name}</h2>
            <p>{!!group!.description ? group!.description : <i>No group description. Ask a group moderator to add one!</i>}</p>
            <ul>{membersList}</ul>
        </>
    )
}
export default SingleGroup
function useEffect(arg0: () => void, arg1: any[]) {
    throw new Error('Function not implemented.')
}

