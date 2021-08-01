import Nav from './Nav'
import Head from 'next/head'

const Layout = ({ children }) => {
    return(
        <>
            <Head>
                <title>Statagems!</title>
            </Head>
            <Nav/>
            {children}
        </>
    )
}

export default Layout