import Nav from './Nav'
import Head from './MyHead'
import TitleBar from './TitleBar'
import Footer from './Footer'
import Background from './Background'
import styles from './Layout.module.sass'

const Layout = ({ children }) => {
    return(
        <>
            <Background/>
            <Head/>
            <TitleBar/>
            <Nav/>
            <main className={styles.content}>
                    {children}
            </main>
            <Footer/>
            
        </>
    )
}

export default Layout

