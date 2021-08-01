import { useRouter } from 'next/router'
import { useEffect } from 'react';
import Layout from '../../components/Layout';
import { server } from '../../config';

export default function Player({player}){
    const router = useRouter()
    if (router.isFallback) {
      return <div>Loading...</div>
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
        revalidate: 1,
    }
}

export async function getStaticPaths(){
    const resp = await fetch(`${server}/api/players`)
    const data = await resp.json()
    
    const paths = data.map(player => ({ params: {id: player.id.toString()} } ))

    return {
        paths: paths,
        fallback: true
    }
}