import { mutate, cache } from 'swr';
import { server } from '../config'

export async function logout(){
    await fetch(`${server}/auth/logout`).catch(() => {})
    //cache.delete('/api/me')
    await mutate('/api/me')
}

export async function refresh(){
    cache.delete('/api/me')
    await mutate('/api/me')
}

export function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
} 