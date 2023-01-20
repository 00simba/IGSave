import axios from 'axios';
import { useEffect, useState } from 'react';
import { Inter } from '@next/font/google';
import styles from '@/styles/Home.module.css';

const inter = Inter({ subsets: ['latin'] })

export default function Media(){

    const [links, setLinks] = useState([])

    useEffect(() => {
        const getLinks = async () => {      
            const data = await axios.get('https://igsave.onrender.com')
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
            <div className={styles.linkDiv}>
    
                {links.map((link) => {           
                    return(
                    <div className={styles.mediaCard} key={link}>
                        <button className={styles.downloadButton} onClick={() => {window.open(link)}}>Download</button>
                    </div>
                    )
                })} 
            </div>
        </>
    )   
}