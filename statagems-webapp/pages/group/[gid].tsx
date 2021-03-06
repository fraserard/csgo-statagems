import Layout from '../../components/layout/Layout'
import SingleGroup from '../../components/groups/SingleGroup'
import { useRouter } from 'next/router'
import AddToGroup from '../../components/groups/AddToGroup'

export default function Group(){
    const router = useRouter()
    const gid = Number(router.query['gid'])

    return (
        <Layout>
            <SingleGroup gid={gid}/>
            <AddToGroup gid={gid}/>
        </Layout>

    )
}
