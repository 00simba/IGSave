import styles from '@/styles/Footer.module.css'
import homeStyles from '@/styles/Home.module.css'
import { Inter } from '@next/font/google'
import Link from 'next/link'
import React from 'react';
import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';

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
                        <Link href='/photo'>
                            <li className={styles.li}>Photos</li>
                        </Link>
                        <Link href='/video'>
                            <li className={styles.li}>Videos</li>
                        </Link>
                        <Link href='/reel'>
                            <li className={styles.li}>Reels</li>
                        </Link>
                        <Link href='/carousel'>
                            <li className={styles.li}>Carousels</li>
                        </Link>
                    </ul>
                </div>
                <div>
                    <ul className={inter.className}>
                        <Popup trigger={ <li className={styles.li}>Contact</li>} position="top center">
                            <div className={inter.className}>Email: igsavedotio@gmail.com</div>
                        </Popup>
                        <Link href='/terms-and-conditions'>
                            <li className={styles.li}>Terms & Conditions</li>
                        </Link>
                        <Link href='privacy-policy'>
                            <li className={styles.li}>Privacy Policy</li>
                        </Link>
                    </ul>
                </div> 
            </div> 

            
            <div className={styles.copyrightBanner}>
                <p className={inter.className}>&copy; {new Date().getFullYear()} Copyright: igsave.io</p>
            </div>
        </div>
    )


}