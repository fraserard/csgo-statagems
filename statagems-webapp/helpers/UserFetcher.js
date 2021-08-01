import { server } from "../config";
import { getCookie } from "./AuthHelper";
import {cache} from "swr"

 const userFetcher  = () => {

    if(cache.has('/api/me')){
        return data = cache.get('/api/me')
    }
    const resp = fetch(`${server}/api/me`, {headers: {
        'X-CSRF-TOKEN': getCookie('csrf_access_token'),
        'Authorization': `Bearer ${getCookie('access_token_cookie')}`,
        }})
    data = resp.json()
    
    if (resp.status == 200 && data != undefined && data.id != undefined) {
        // authorized
        cache.set("/api/me", data)
        return data
    }
  
    // not authorized
    return data
  }
  export default userFetcher
  


