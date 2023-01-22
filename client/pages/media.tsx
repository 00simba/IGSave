import axios from 'axios';
import { useEffect, useState } from 'react';
import { Inter } from '@next/font/google';
import styles from '@/styles/Home.module.css';
import mediaStyles from '@/styles/Media.module.css';
import GoogleAnalytics from "@bradgarropy/next-google-analytics"
import Footer from '@/components/footer';
import '@/styles/Media.module.css'

const inter = Inter({ subsets: ['latin'] })

export default function Media(){

    const [links, setLinks] = useState<any[]>([])

    useEffect(() => {
        const getLinks = async () => {      
            const data = await axios.get('http://127.0.0.1:5000')
            setLinks(data.data.links)
        }
        getLinks()
    }, [])    

    return(
        <>
            <main className={styles.header}>
                <a href="https://igsave.io"><img className={styles.logo} src='/igsave_logo_full.png'></img></a>
            </main>
            <div>
                <div className={styles.downloadDiv}>
                    <h1 className={inter.className}>Post Media</h1>  
                </div>
            </div>
            <div id='cardContainer' className={styles.linkDiv}>
                {links.map((item) => {         
                    return(
                    <div className={mediaStyles.mediaCard} key={item.url}>
                        <img className={mediaStyles.thumbNail} src={item.base64}/>
                        <div className={mediaStyles.downloadButton}>
                            <div className={mediaStyles.aTagDiv}>
                                <a className={inter.className} href={item.url} target="_blank" rel="noreferrer">Download</a>
                            </div>
                        </div>
                    </div>
                    )
                })} 
            </div>
            <div className={styles.contentDiv}>

            </div>
            <Footer/>
            <GoogleAnalytics measurementId="G-ZGXMMY4FE3" />
        </>
    )   
}