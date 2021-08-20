import Layout from "../components/Layout";
import GroupList from "../components/GroupList";
import NewGroup from '../components/NewGroup'

export default function Groups() {
    return(
        <Layout>
            <h1>Groups!</h1>
            <NewGroup/>
            <GroupList/>
        </Layout>
    )
}

