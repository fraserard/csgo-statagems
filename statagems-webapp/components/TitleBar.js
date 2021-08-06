import Avatar from "./Avatar"
import { server } from "../config";
import Image from "next/image";
import styles from "./modules/TitleBar.module.sass"
import Link from 'next/link'
import Loader from "./Loader";
import Logo from "./Logo";

const TitleBar = () => {
    return (
    <div className={styles.dad}>
        <div className={styles.inner}>
            <Logo/>
            <div></div>
            <Avatar/>
        </div>
    </div>
    )
}
 
export default TitleBar