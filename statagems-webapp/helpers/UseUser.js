import useSWR, {cache} from "swr"
import {userFetcher} from "./UserFetcher"

  
  
export default function useUser() {
  
    //cache.delete("/api/me")
    
    // const options = {
    //     revalidateOnMount: !cache.has("/api/me"), //here we refer to the SWR cache
    //   };
    const {data} = useSWR('/api/me', userFetcher)

    return {
        user: data,      
    }
}
