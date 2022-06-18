
import styles from "./TitleBar.module.css"
import { Link } from "react-router-dom";
import { Content } from "@jobber/components/Content";


function Titlebar() {
    return (
    <Content>
    <div className={styles.titlebar}>
        <h1 className={styles.logo}><Link to="/">Statagems!</Link></h1>
        {/* Login button OR Avatar */}
    </div>
    </Content>
    )
}
 
export default Titlebar