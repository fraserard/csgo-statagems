import useSWR, {cache} from "swr"
import { server } from "../config";
import cookieCutter from 'cookie-cutter'

export default function useUser() {
    
    const options = {
        revalidateOnMount: !cache.has("/api/me"), // swr cache
      };
    const {data} = useSWR('/api/me', userFetcher, options)

    return {
        user: data,      
    }
}

export const userFetcher = async () => {
    
    const options = {
        headers: {
        'X-CSRF-TOKEN': cookieCutter.get('csrf_access_token')
        }
    }
    const resp = await fetch(`${server}/api/me`, options)
    
    const data = await resp.json()
    if (resp.status == 200 && data != undefined && data.id != undefined) {

        return data
    }

    // not authorized
    return data
  }