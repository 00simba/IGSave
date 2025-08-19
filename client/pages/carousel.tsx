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
    title: "Carousel Downloader FAQ",
    rows: [
        {
          title: <p className={styles.pTag}>Can I downloaded an unlimited number of carousel?</p>,
          content: <p className={styles.pTag}>Yes as long as your device battery does not run out, you can continue to download Instagram carousels using IGSave Carousel Downloader.</p>,
        },
        {
          title: <p className={styles.pTag}>What file extension are carousels downloaded in?</p>,
          content: <p className={styles.pTag}>IGSave Carousel Downloader downloads a mixture of photos and videos which results in .jpg and .mp4 files. The .jpg and .mp4 formats provide great quality, file size, and compatibility with numerous devices which is why IGSave Carousel Downloader prefers them.</p>,
        },
        {
          title: <p className={styles.pTag}>How much does IGSave Carousel Downloader cost?</p>,
          content: <p className={styles.pTag}>Cost start at $0 and go up to $0. That is right, IGSave Carousel Downloader is free to use for as long as it is providing service so download as much as you wish!</p>,
        },
        {
          title: <p className={styles.pTag}>Are carousel expected to be high quality?</p>,
          content: <p className={styles.pTag}>Instagram carousel are not expected to be high quality but rather the highest quality possible! IGSave Carousel Downloader makes sure that you get the most valuble content from a carousel post.</p>,
        },
        {
          title: <p className={styles.pTag}>Which devices are compatible with IGSave Carousel Downloader?</p>,
          content: <p className={styles.pTag}>As long as the device can run Instagram is it guaranteed it can also support IGSave Carousel Downloader. This includes all modern day desktops, laptops, phones, and tablets!</p>,
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
          Instagram Carousel Downloader
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
            <h1 className={inter.className}>Download Instagram Carousels!</h1>
          </div>
          <br/>
          <p className={inter.className}>Instagram features posts that contain a mixture of pictures and videos. These posts are referred to as carousels and contain up to 10 photos and/or videos.</p>
          <br/>
          <p className={inter.className}>IGSave enables you to pick and choose content from a carousel post you wish to download at high resolution and directly to your device!</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Carousel Download Steps!</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>1. Copy the link for the carousel post</p>
          <p className={inter.className}>2. Paste the carousel link into the textbox above</p>
          <p className={inter.className}>3. Click `Download` and choose your downloads!</p>
        </div>
      </div>

      <div className={styles.supportHeading}>
        <h1 className={inter.className}>Carousel Downloader</h1>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Carousel Download</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>Instagram carousels allow users to post a combination of pictures and videos into a single post. This makes it convinient for users posting and for users viewing the post. To add to the convience IGSave takes it a step further by allowing you to seamlessly download carousels and without any hassles.</p>
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
