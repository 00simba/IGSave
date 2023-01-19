import axios from 'axios';
import { useEffect, useState } from 'react';
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'

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
            <div>
                <h1 className={inter.className}>Media Page</h1>  
                <br/>
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