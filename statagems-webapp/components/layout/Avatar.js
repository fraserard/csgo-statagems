import useUser from "../../helpers/UseUser"
import getAvatarUrl from '../../helpers/SteamHelper'
import { server } from "../../config"
import Image from "next/dist/client/image"
import Link from 'next/link'
import styles from './Avatar.module.sass'

function Avatar () {
    const { user} = useUser();
    if (user == undefined || user.id == undefined){
        return (
        <div className={styles.logged_out}>
            <a href={`${server}/auth/login`}>
            <Image src='/login_steam_large.png' alt='Login With Steam' width='114'height='43'/>
            </a> 
        </div>
        )
        
    }
    
    if(user){ 
        return(
        <div className={styles.logged_in}>
            <Link href={`/player/${user.id}`}><a>
                <Image className={styles.image} src={getAvatarUrl(user.avatar_hash, "medium")} width="60" height="60" quality="100" />   
                </a>
            </Link>
        </div>
        )
    } 
       
            
    return null      
  }
  export default Avatar