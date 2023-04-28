import Head from 'next/head'
import { Inter } from '@next/font/google'
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
    title: "Video Downloader FAQ",
    rows: [
        {
          title: <p className={styles.pTag}>Does the Instagram Video Downloader have a download limit?</p>,
          content: <p className={styles.pTag}>There is absolutely no limit when it comes to downloading Instagram video using the IGSave Video Downloader. The IGSave Video Downloader was engineered with scalability in mind such as downloading lots of Instagram videos in one session.</p>,
        },
        {
          title: <p className={styles.pTag}>What will be the file extension of the downloaded videos?</p>,
          content: <p className={styles.pTag}>Every Instagram video downloaded through IGSave Video Downloader is saved in the .mp4 format. The resons being that it is widely used, supports high compression resulting in smaller file size and quicker downloads.</p>,
        },
        {
          title: <p className={styles.pTag}>Is IGSave Video Downloader free to use?</p>,
          content: <p className={styles.pTag}>Yes the IGSave Video Downloader is fully free to use. IGSave wants its users to have the best experience possible and paying for video downloads is definitely not one of them!</p>,
        },
        {
          title: <p className={styles.pTag}>Does IGSave Video Downloader ensure high resolution download?</p>,
          content: <p className={styles.pTag}>Yes, IGSave ensures that all video files being downloaded by the user are of the highest quality possible. This ensures that IGSave users are completely satisfied with the results as IGSave values its users` needs.</p>,
        },
        {
          title: <p className={styles.pTag}>Can IGSave Video Downloader work on all devices?</p>,
          content: <p className={styles.pTag}>Yes, IGSave Video Downloader works on all devices that can run a browser. In the world of modern technology, almost every Instagram user has access to this making the IGSave Video Downloader a viable option to download Instagram videos.</p>,
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
          Instagram Video Downloader
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
            <h1 className={inter.className}>Download Instagram Videos!</h1>
          </div>
          <br/>
          <p className={inter.className}>Another common use for Instagram is to upload videos to the internet that are up to 60 seconds long. IGSave comes handy when it comes to downloading a video as the app does not support direct video download to your device.</p>
          <br/>
          <p className={inter.className}>Get started today by using IGSave to download your favourite Instagram videos to your device with ease!</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Video Download Steps!</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>1. Copy the link of the Instagram video.</p>
          <p className={inter.className}>2. Paste the video link into the textbox above</p>
          <p className={inter.className}>3. Hit the `Download` button and save the video!</p>
        </div>
      </div>

      <div className={styles.supportHeading}>
        <h1 className={inter.className}>Video Downloader</h1>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Video Download</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>Instagram features video sharing which is a way for content creators to share videos that can be up to 60 seconds long. In many cases videos go viral with people wanting to be save them to their device to be shared or access later. Thankfully, IGSave was built with that purpose in mind allowing you to do so!</p>
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
