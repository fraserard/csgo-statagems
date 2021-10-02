import { useRouter } from "next/router";
import useUser from '../helpers/UseUser'
import { useEffect } from "react";
import Loader from '../components/Loader'

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

    
    return <Loader/>
}


  

