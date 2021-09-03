import Document, { Html, Head, Main, NextScript } from 'next/document'

class MyDocument extends Document {

    render() {
      return (
        <Html>
          <Head>
            <style jsx>{`
             
             @import url('https://fonts.googleapis.com/css2?family=Armata&family=Julius+Sans+One&display=swap');
             //font-family: 'Armata', sans-serif; Text n stuff
             //font-family: 'Julius Sans One', sans-serif; Logo font
             `}</style> 
          </Head>
          <body>
            <Main />
            <NextScript />
          </body>
        </Html>
      )
    }
  }
  
  export default MyDocument