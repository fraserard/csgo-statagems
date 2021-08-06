import Head from "next/head";
import Layout from "../components/Layout";
import { useRouter } from "next/router";
import useUser from '../helpers/UseUser'
import { useEffect } from "react";
import {cache} from 'swr'

export default function Profile() {

    const { user } = useUser()
    const router = useRouter()

    useEffect(() => {
        if (user == undefined || user.id == undefined) {
          router.push('/')
        }
        else{
            router.push(`/player/${user.id}`) 
        }
      }, [user])

    
    return <p>redirecting</p>
}


  

