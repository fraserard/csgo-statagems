import Avatar from "./Avatar"
import styles from "./TitleBar.module.sass"
import Logo from "./Logo";

const TitleBar = () => {
    return (
    <div className={styles.hug}>
        <div className={styles.inner}>
            <Logo/>
            <div></div>
            <Avatar/>
        </div>
    </div>
    )
}
 
export default TitleBar