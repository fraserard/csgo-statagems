import useUser from "../helpers/UseUser"
import getAvatarUrl from '../helpers/SteamHelper'
import { server } from "../config";
import Image from "next/dist/client/image";

function Avatar () {
    const { user, isValidating, mutate} = useUser();
    if (isValidating || user == undefined || user.id == undefined){
        return <a href={`${server}/auth/login`}>
        <Image src='/login_steam.png' alt='Login With Steam' width='154'height='23'></Image></a> 
    }
    
    if(user) 
        return <a href={`${server}/player/${user.id}`}>
            Hi, {user.username}!<Image src={getAvatarUrl(user.avatar_hash)} width='100' height='100' objectFit='contain'>
                </Image></a> 
    return null      
  }
  export default Avatar