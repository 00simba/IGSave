import Head from 'next/head'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
import { useState } from 'react'
import axios from 'axios'
import { useRouter } from 'next/router'

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
    axios.post('https://igsave.onrender.com', {url: url}, config).then((res) => {
      router.push({
        pathname: '/media'
      })
    })
  }

  return (
    <>
      <Head>
        <title>IGSave - Download Instagram Images, Videos, & Reels</title>
        <meta name="description" content="Download any Instagram Image, Video, and Reel using iGramSaver" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/igsave_logo.png"/>
      </Head>
      <main className={styles.header}>
        <img className={styles.logo} src='/igsave_logo_full.png'></img>
      </main>
      <br/>
      <div className={styles.downloadDiv}>
        <h1 className={inter.className} id='downloadHeading'>
          Instagram Post Downloader
        </h1>
        <form className={styles.form} id='form' action="/" method='POST'>
          <input className={styles.input} type="text" name ='url' placeholder='Paste Instagram Link Here' onChange={(e) => setUrl(e.target.value)}></input>
        </form> 
        <button className={styles.button} onClick={handleSubmit}>Download</button>
      </div>
    </>
  )
}
