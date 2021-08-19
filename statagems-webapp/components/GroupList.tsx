
import Link from 'next/link'
import {Group, useGroups} from '../helpers/UseGroup'

const GroupList = () => {
    const { groups, isLoading, isError } = useGroups()
    if (isLoading){
        return (<p>loading</p>)
    } 
    if(isError){
        return (<p>error</p>)
    }
    
    const groupList = groups!.map((g) => 
        <li>
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