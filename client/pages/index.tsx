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
        <title>iGramSaver</title>
        <meta name="description" content="Download any Instagram Image, Video, and Reel using iGramSaver" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
            <h1 className={inter.className}>
              iGramSaver
            </h1>
            <br/>
            <p className={inter.className}>
              Download any Instagram Image, Video, or Reel by pasting its link below and clicking submit.
            </p>
            <br/>
            <p className={inter.className}>Enter Link</p>
  
            <form id='form' action="/" method='POST'>
              <input type="text" name ='url' onChange={(e) => setUrl(e.target.value)}></input>
            </form> 
            <button onClick={handleSubmit}>Submit</button>
      </main>
    </>
  )
}
