import { mutate, cache } from 'swr';
import { server } from '../config'
import cookieCutter from 'cookie-cutter'


export async function logout(){
    const options = {
        headers: {
        'X-CSRF-TOKEN': cookieCutter.get('csrf_access_token')
        }
    }
    
    await fetch(`${server}/auth/logout`, options).catch(() => {})
    
    mutate('/api/me')
}

export async function refresh(){
    mutate('/api/me')
}
