import Layout from "../../components/layout/Layout";
import GroupList from "../../components/groups/GroupList";
import NewGroup from '../../components/groups/NewGroup'
import Link from 'next/link'
import { useRouter} from 'next/router'


export default function Groups() {
    const router = useRouter()
    return(
        <Layout>
            <h1>Groups!</h1>
            <Link href='/groups/add'><a>New Group!</a></Link>
            <GroupList/>
        </Layout>
    )
}

