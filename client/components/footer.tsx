import styles from '@/styles/Footer.module.css'
import homeStyles from '@/styles/Home.module.css'
import { Inter } from '@next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function Footer(){
    return(
        <div className={styles.footerContainer}>
            <div className={styles.footerDiv}>
                <div className={styles.logoContainer}>
                    <img className={homeStyles.logo} src='./igsave_logo_full.png'></img>
                </div>
                <div>
                    <ul className={inter.className}>
                        <li className={styles.li}>Image</li>
                        <li className={styles.li}>Carousel</li>
                        <li className={styles.li}>Reel</li>
                    </ul>
                </div>
                <div>
                    <ul className={inter.className}>
                        <li className={styles.li}>Contact</li>
                        <li className={styles.li}>Terms & Conditions</li>
                        <li className={styles.li}>Privacy Policy</li>
                    </ul>
                </div> 
            </div> 
            <div className={styles.copyrightBanner}>
                <p className={inter.className}>&copy; {new Date().getFullYear()} Copyright: igsave.io</p>
            </div>
        </div>
    )


}