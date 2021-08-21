import styles from './Logo.module.sass'
import Link from 'next/link';

const Logo = () => {
    return (  
        <h1 className={styles.logo}><Link href='/'><a>Statagems!</a></Link></h1>
    )
}
 
export default Logo;