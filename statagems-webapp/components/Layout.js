import Nav from './Nav'
import Head from './MyHead'
import TitleBar from './TitleBar'
import Footer from './Footer'
import Background from './Background'
import styles from './modules/Layout.module.sass'

const Layout = ({ children }) => {
    return(
        <>
            <Background/>
            <Head/>
            <TitleBar/>
            <Nav/>
            <div className={styles.content}>
                    {children}
            </div>
            <Footer/>
            
        </>
    )
}

export default Layout

