import { mutate, cache } from 'swr';
import { server } from '../config'
import cookieCutter from 'cookie-cutter'


export async function logout(){
    await fetch(`${server}/auth/logout`, getOptions()).catch(() => {})
    mutate('/api/me')
}

export async function refresh(){
    mutate('/api/me')
}

export const getOpt = () =>  {
    let csrf:string = cookieCutter.get('csrf_access_token')
    
    let opt: RequestInit = { method: 'GET',
                headers: { 
                    'X-CSRF-TOKEN': csrf,
                }
    }
    return opt

}

export function getOptions(): RequestInit{
    const csrf: string = cookieCutter.get('csrf_access_token')
    const opt: RequestInit = { method: 'GET',
                headers: { 
                    'X-CSRF-TOKEN': csrf,
                }
    }
    return opt

}

