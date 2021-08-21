import Layout from "../components/layout/Layout";
import GroupList from "../components/groups/GroupList";
import NewGroup from '../components/groups/NewGroup'

export default function Groups() {
    return(
        <Layout>
            <h1>Groups!</h1>
            <NewGroup/>
            <GroupList/>
        </Layout>
    )
}

