import Link from 'next/link'
import Image from 'next/image'
import { server } from '../config'
import Avatar from './Avatar'
import useUser from '../helpers/UseUser'
import { logout, refresh } from '../helpers/AuthHelper'
import { useRouter } from 'next/router'
function Nav() {
    const { user } = useUser()
    const router = useRouter()

    if(user == undefined || user.id == undefined){
        return(
            <nav>
                <ul>
                    <li><Link href='/'><a>Statagems!</a></Link></li>
                    <li><Avatar></Avatar></li>
                    <li><button onClick={() => {refresh()}}>
                            Refresh
                    </button></li>
                </ul>
            </nav>
        )
    }
    if(user){
        return(
            <nav>
                <ul>
                    <li><Link href='/'><a>Statagems!</a></Link></li>
                    <li><Link href='/matches'><a>My Matches!</a></Link></li>
                    <li><Link href='/friends'><a>My Friends!</a></Link></li>
                    <li><button onClick={() => {refresh()}}>
                            Refresh
                    </button></li>
                    <li><button onClick={() => {
                        logout()
                        router.push("/")
                        }}>
                        Logout
                    </button></li>    
                    <li><Avatar></Avatar></li>
                </ul>
            </nav>
        )
    }
}

export default Nav