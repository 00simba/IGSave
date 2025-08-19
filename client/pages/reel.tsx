import Head from 'next/head'
import { Inter } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import { useState } from 'react'
import { useRouter } from 'next/router'
import GoogleAnalytics from "@bradgarropy/next-google-analytics"
import Footer from '../components/footer'
import Link from 'next/link'
import Faq from "react-faq-component"

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  
  const [url, setUrl] = useState('')
  const router = useRouter()

  const handleSubmit = (e: { preventDefault: () => void }) => {
    e.preventDefault()
    var reUrl = /https?:\/\/(?:www\.)?instagram\.com(?:\/[^\/]+)?\/(?:p|reel)\/([^\/?#&]+){10}\//gm
    if(url.match(reUrl)){
      router.push({
        pathname: '/media',
        query: {url: url}, 
      })
    }
    else{
      var inputVal = (document.getElementById('url') as HTMLInputElement)  
      inputVal.value = ''
      setUrl('')
    }
  }

  const data = {
    title: "Reel Downloader FAQ",
    rows: [
        {
          title: <p className={styles.pTag}>How many reels can I download with IGSave Reel Downloader?</p>,
          content: <p className={styles.pTag}>As many Instagram reels as you want! IGSave runs without any download limits be it photos, videos, and reels making your experience awesome! Download as many reels as you want starting now.</p>,
        },
        {
          title: <p className={styles.pTag}>What is the format are Instagram reels downloaded in?</p>,
          content: <p className={styles.pTag}>Instagram reels are downloaded in the .mp4 format as it is accepted as the webs standard, provides high quality, and compatibility with nearly every device.</p>,
        },
        {
          title: <p className={styles.pTag}>Do I need to pay to use IGSave Reel Downloader?</p>,
          content: <p className={styles.pTag}>No, you do not need to pay a single penny to use IGSave Reel Downloader as it is designed to be a totally free to use service.</p>,
        },
        {
          title: <p className={styles.pTag}>What quality does IGSave Reel Downloader provide?</p>,
          content: <p className={styles.pTag}>IGSave Reel Downloader ensures that the reel of interest is downloaded at the highest resolution possible. IGSave Reel Downloader processes all video data for you and picks out the full resolution version of the reel to be downloaded on to your device.</p>,
        },
        {
          title: <p className={styles.pTag}>Does IGSave Reel Downloader work on every device?</p>,
          content: <p className={styles.pTag}>Yes, IGSave Reel Downloader was created with the purpose of serving as many people as possible. This means that users from Windows, MacOS, iOS, Android, Linux, or any operating system that supports a browser is able to use IGSave Reel Downloader.</p>,
        },
    ],
  };

  const style = {
    bgColor: 'white',
    titleTextColor: "black",
    rowTitleColor: "black",
    rowContentColor: 'purple',
    arrowColor: "purple",
  };

  const config = {
      animate: true,
      tabFocus: true,
      expandIcon: "+",
      collapseIcon: "-",
  };

  return (
    <>
      <Head>
        <title>Download Instagram Images, Videos, & Reels</title>
        <meta name='description' content='Download any Instagram Image, Video, and Reel in HD using IGSave' />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/igsave_logo.png'/>
      </Head> 
      <main className={styles.header}>
        <Link href='/'><img className={styles.logo} src='/igsave_logo_full.png'></img></Link>
      </main>
      <div className={styles.downloadDiv}>
        <h1 className={inter.className} id='downloadHeading'>
          Instagram Reel Downloader
        </h1>
        <form className={styles.form} id='form' action="/" method='POST'>
          <input className={styles.input} id='url' type='text' name ='url' placeholder='Paste Instagram Link Here' value={url} onChange={(e) => setUrl(e.target.value)}></input>
        </form> 
        <button className={styles.button} onClick={handleSubmit}>Download</button>
      </div> 

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <img src='/aboutLogo.png'></img>
        </div>
        <div className={styles.aboutParaDiv}>
          <div className={styles.downloadHeading}>
            <h1 className={inter.className}>Download Instagram Reels!</h1>
          </div>
          <br/>
          <p className={inter.className}>Reels are a unique and fun way of creating videos that span the entire screen and are up to 90 seconds long. The interaction of scrolling through reels can become addicting making users come across various reels they wish to download.</p>
          <br/>
          <p className={inter.className}>Use IGSave Reel Downloader to download Instagram Reels quickly to your device in the highest resolution!</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Reel Download Steps!</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>1. Copy the link of the reel post</p>
          <p className={inter.className}>2. Paste the reel link into the textbox above</p>
          <p className={inter.className}>3. Press the `Download` button and save your reel!</p>
        </div>
      </div>

      <div className={styles.supportHeading}>
        <h1 className={inter.className}>Reel Downloader</h1>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Reel Download</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>Instagram reels were inspired by TikTok and quickly became the platforms most viral way of sharing videos. Reels have surpassed Instagram videos and will continue to do so as they provide users a better viewing experience. To share this experince IGSave allows users to download Reels directly to their device!</p>
        </div>
      </div>

      <div className={styles.FAQContainer}>
        <div className={inter.className}>
          <Faq
            data={data}
            styles={style}
            config={config}
          />
        </div>
      </div>

      <Footer/>
      <GoogleAnalytics measurementId='G-ZGXMMY4FE3' />
    </>
  )
}
