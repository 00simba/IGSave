import Head from 'next/head'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
import { useState } from 'react'
import axios from 'axios'
import { useRouter } from 'next/router'
import GoogleAnalytics from "@bradgarropy/next-google-analytics"
import Footer from '../components/footer'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  
  const [url, setUrl] = useState('')
  const router = useRouter()

  const config = {
    headers: {
     'Access-Control-Allow-Origin' : '*',
     'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
     }
 }

  const handleSubmit = (e: { preventDefault: () => void }) => {
    e.preventDefault()
    axios.post('http://127.0.0.1:5000', {url: url}, config).then((res) => {
      router.push({
        pathname: '/media'
      })
    })
  }

  return (
    <>
      <Head>
        <title>Download Instagram Images, Videos, & Reels</title>
        <meta name="description" content="Download any Instagram Image, Video, and Reel in HD using IGSave" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/igsave_logo.png"/>
      </Head> 
      <div className={styles.announcementBar}><span className={inter.className}>🔧 Work in Progress...</span></div>  
      <main className={styles.header}>
        <a href="https://igsave.io"><img className={styles.logo} src='/igsave_logo_full.png'></img></a>
      </main>
      <div className={styles.downloadDiv}>
        <h1 className={inter.className} id='downloadHeading'>
          Instagram Post Downloader
        </h1>
        <form className={styles.form} id='form' action="/" method='POST'>
          <input className={styles.input} type="text" name ='url' placeholder='Paste Instagram Link Here' onChange={(e) => setUrl(e.target.value)}></input>
        </form> 
        <button className={styles.button} onClick={handleSubmit}>Download</button>
      </div> 
      <div className={styles.contentDiv}>

      </div>
      <Footer/>
      <GoogleAnalytics measurementId="G-ZGXMMY4FE3" />
    </>
  )
}
