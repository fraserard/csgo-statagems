import Link from 'next/link'
import Image from 'next/image'
import { server } from '../config'
import Avatar from './Avatar'
import useUser from '../helpers/UseUser'
import { logout, refresh } from '../helpers/AuthHelper'
import { useRouter } from 'next/router'
import styles from "./modules/Nav.module.sass"

function Nav() {
    const { user } = useUser()
    const router = useRouter()

    if(user == undefined || user.id == undefined){
        return(
            <nav className={styles.dad}>
                <ul>
                    <li>Please sign in with Steam.</li>
                </ul>
            </nav>
        )
    }
    if(user.is_admin = false){
        return(
            <nav className={styles.dad}>
                <ul>
                    <li><Link href='/profile'><a>My Profile</a></Link></li>
                    <li><Link href='/matches'><a>My Matches</a></Link></li>
                    <li><Link href='/friends'><a>My Friends</a></Link></li>
                    <li><Link href='/groups'><a>My Groups</a></Link></li>
                    <li><Link href='/settings'><a>My Settings</a></Link></li>
                    <li><button onClick={() => {
                        logout()
                        router.push("/")
                        }}>
                        Logout
                    </button></li>    
                </ul>
            </nav>
        )
    }
    if(user.is_admin = true){
        return(
            <nav className={styles.dad}>
                <ul>
                    <li><Link href='/profile'><a>My Profile</a></Link></li>
                    <li><Link href='/matches'><a>My Matches</a></Link></li>
                    <li><Link href='/friends'><a>My Friends</a></Link></li>
                    <li><Link href='/groups'><a>My Groups</a></Link></li>
                    <li><Link href='/settings'><a>My Settings</a></Link></li>
                    <li><Link href='/admin'><a>Admin Zone</a></Link></li>
                    <li><button onClick={(e) => {refresh()}}>
                            Refresh
                    </button></li>
                    <li><button onClick={() => {
                        logout()
                        router.push("/")
                        }}>
                        Logout
                    </button></li>    
                </ul>
            </nav>
        )
    }
}

export default Nav