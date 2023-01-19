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
                <h1 className={inter.className}>Post Media</h1>  
            </div>
            {links.map((link) => {
                return(
                <div key={link}>
                    <a href={link}>Download<br/></a>
                </div>
                )
            })} 
        </>
    )   
}