import { useRouter } from 'next/router'
import Layout from '../../components/layout/Layout';
import { server } from '../../config';
import Loader from '../../components/Loader';

export default function Player({player}){
    const router = useRouter()
    if (router.isFallback) {
      return <Loader/>
    }

    return <Layout><h1>Player: {player.username}</h1></Layout>
}

export async function getStaticProps({params}){
    const resp = await fetch(`${server}/api/players/${params.id}`).catch(() => {})
    if(resp.status == 404)
        return {notFound: true}
                    
    const data = await resp.json()

    return {
        props: {
            player: data,
        },
        revalidate: 10,
    }
}

export async function getStaticPaths(){
    const resp = await fetch(`${server}/api/players`)
    const data = await resp.json()
    
    // only grab 100 last online players
    const paths = data.map(player => ({ params: {id: player.id.toString()} } ))

    return {
        paths: paths,
        fallback: true
    }
}