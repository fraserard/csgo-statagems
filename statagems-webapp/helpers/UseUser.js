import useSWR, {cache} from "swr"
import {userFetcher} from "./UserFetcher"
  
export default function useUser() {
    
    const options = {
        revalidateOnMount: !cache.has("/api/me"), // swr cache
      };
    const {data} = useSWR('/api/me', userFetcher, options)

    return {
        user: data,      
    }
}
