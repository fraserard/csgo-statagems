
import Link from 'next/link'
import { useGroups } from '../helpers/UseGroup'

const GroupList = () => {
    const { groups, isLoading, isError } = useGroups()
    if (isLoading){
        return (<p>loading</p>)
    } 
    if(isError){
        return (<p>error</p>)
    }
    
    const groupList = groups!.map((g) => 
        <li key={g.id}>
            <Link href={`/group/${encodeURIComponent(g.id)}`}>{g.group_name}</Link>
        </li>
    ) 
    return(  
        <ul>
            {groupList}
        </ul> 
    )
}
export default GroupList