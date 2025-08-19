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
    title: "Photo Downloader FAQ",
    rows: [
        {
          title: <p className={styles.pTag}>Is there an Instagram Photo Downloader limit?</p>,
          content: <p className={styles.pTag}>No, there is absolutely no limit to how many photos, images, or pictures you can download using IGSave during your session. Feel free to download as many photo posts are you require with complete convinence!</p>,
        },
        {
          title: <p className={styles.pTag}>What file extension will my photos be downloaded in?</p>,
          content: <p className={styles.pTag}>All Instagram photos downloaded through the Photo Downaloder will be saved in .jpg format as it is widely used, has a quick loading time, and is highly compatible.</p>,
        },
        {
          title: <p className={styles.pTag}>Is IGSave Photo Downloader free to use?</p>,
          content: <p className={styles.pTag}>IGSave Photo Downloader is completely free to use as it understands the significance of convinience. Use IGSave Photo Downloader and download as many photo posts you desire for free!</p>,
        },
        {
          title: <p className={styles.pTag}>Does IGSave Photo Downloader save in high resolution?</p>,
          content: <p className={styles.pTag}>Yes, every photo is processed on our end to deliver the highest quality possible to you. Normally the resolution is 1350x1080, however, it varies with each post as not every image uploaded by a user is the same resolution.</p>,
        },
        {
          title: <p className={styles.pTag}>Does the Photo Downloader work on all devices?</p>,
          content: <p className={styles.pTag}>Yes, IGSave Photo Downloader does work on all devices that can run a browser. The IGSave Photo Downloader was designed with inclusivity as it strives to support all devices and provide everyone with an equal experience.</p>,
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
          Instagram Photo Downloader
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
            <h1 className={inter.className}>Download Instagram Photos!</h1>
          </div>
          <br/>
          <p className={inter.className}>As Instagram does not support downloading posts directly to your device it maybe frustrating. Luckily, IGSave solves this problem by helping you do so in an instant!</p>
          <br/>
          <p className={inter.className}>Use IGSave to help you download any Instagram photo in high resolution. You can download a single image or multiple images from a caroursel post!</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Photo Download Steps!</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>1. Copy the link for the Instagram photo post</p>
          <p className={inter.className}>2. Paste the photo link into the textbox above</p>
          <p className={inter.className}>3. Click the `Download` button and save your photo!</p>
        </div>
      </div>

      <div className={styles.supportHeading}>
        <h1 className={inter.className}>Photo Downloader</h1>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Photo Download</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>Instagram is by far one of the most popular platforms for the internet to share their images. As one scrolls through Instagram and not be able to download a picture to their device it could be disappointing! That is why IGSave helps you download photos from Instagram posts with great convinience!</p>
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
