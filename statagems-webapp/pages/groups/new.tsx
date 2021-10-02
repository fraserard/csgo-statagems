import Layout from "../../components/layout/Layout";
import GroupList from "../../components/groups/GroupList";
import NewGroup from '../../components/groups/NewGroup'

export default function AddGroup() {
    return(
        <Layout>
            <h1>Create a new group!</h1>
            <NewGroup/>
        </Layout>
    )
}

