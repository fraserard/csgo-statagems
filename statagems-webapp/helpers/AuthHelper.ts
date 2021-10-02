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

export const getOptions = () => {
    const csrf: string = cookieCutter.get('csrf_access_token')
    const opt: RequestInit = { method: 'GET',
                headers: { 
                    'X-CSRF-TOKEN': csrf,
                }
    }
    return opt
}

export const postOptions = (data:any=null) => {
    const csrf: string = cookieCutter.get('csrf_access_token')
    const opt: RequestInit = { 
                method: 'POST',
                headers: { 
                    'X-CSRF-TOKEN': csrf,
                    'Content-Type': 'application/json',
                },
                body: data==null ? null : JSON.stringify(data)
    }
    return opt
}

