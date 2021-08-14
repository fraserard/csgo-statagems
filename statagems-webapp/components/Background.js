import styles from './modules/Background.module.sass'
import Image from 'next/image'
const Background = () => {
    return ( 
    <div className={styles.bgWrap}>
        
      <Image
        alt="Background image. Outer space."
        src="/bg.jpg"
        layout="fill"
        objectFit="cover"
        quality={100}/>
    </div>
    )
}
 
export default Background;