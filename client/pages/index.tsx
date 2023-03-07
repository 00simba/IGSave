import Head from 'next/head'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
import { useState } from 'react'
import { useRouter } from 'next/router'
import GoogleAnalytics from "@bradgarropy/next-google-analytics"
import Footer from '../components/footer'

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

  return (
    <>
      <Head>
        <title>Download Instagram Images, Videos, & Reels</title>
        <meta name='description' content='Download any Instagram Image, Video, and Reel in HD using IGSave' />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/igsave_logo.png'/>
      </Head> 
      {/* <div className={styles.announcementBar}><span className={inter.className}>🔧 Work in Progress...</span></div> */}
      <main className={styles.header}>
        <a href='https://igsave.io'><img className={styles.logo} src='/igsave_logo_full.png'></img></a>
      </main>
      <div className={styles.downloadDiv}>
        <h1 className={inter.className} id='downloadHeading'>
          Instagram Post Downloader
        </h1>
        <form className={styles.form} id='form' action="/" method='POST'>
          <input className={styles.input} id='url' type='text' name ='url' placeholder='Paste Instagram Link Here' value={url} onChange={(e) => setUrl(e.target.value)}></input>
        </form> 
        <button className={styles.button} onClick={handleSubmit}>Download</button>
      </div> 

      <div className={styles.aboutDiv}>
        <img src='/aboutLogo.png'></img>
        <div className={styles.aboutParaDiv}>
          <h1 className={inter.className}>Download Instagram Photos and Videos!</h1>
          <br/>
          <p className={inter.className}>IGSave helps you download Instagram Photos, Videos, Carousels, and Reels with ease!</p>
          <br/>
          <p className={inter.className}>Thanks to its user and device friendly design you can download Instagram content to any device such running Windows, macOS, iPhone, or Android!</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.divHeading}>
          <h1 className={inter.className}>3 Easy Steps To Download!</h1>
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>1. Copy the link for the post or reel.</p>
          <p className={inter.className}>2. Paste into the box above</p>
          <p className={inter.className}>3. Hit the `Download` Button and save to your device!</p>
        </div>
      </div>

      <div className={styles.supportHeading}>
        <h1 className={inter.className}>IGSave Supports</h1>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.divHeading}>
          <h1 className={inter.className}>Photos Download</h1>
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>Instagram photo posts are visual content shared on the social media platform Instagram. These posts can include a variety of images, such as photographs, graphics, illustrations, and memes. Use IGSave to download pictures you desire at full resolution.</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.divHeading}>
          <h1 className={inter.className}>Video Download</h1>
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>Instagram videos are short-form video content shared on the social media platform Instagram. Instagram allows users to record videos directly within the app or upload videos from their devices camera roll. Use IGSave to download any Instagram video.</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.divHeading}>
          <h1 className={inter.className}>Reel Download</h1>
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>Instagram Reels are a feature on the social media platform Instagram that allows users to create and share short-form video content. Reels are typically 15 to 30 seconds in length and are designed to be fun, creative, and engaging. IGSave also enables you to download your favourite reels at high definition straight to your device.</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.divHeading}>
          <h1 className={inter.className}>Carousel Download</h1>
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>Instagram carousel posts are a type of Instagram post that allows users to share up to 10 images or videos in a single post. With carousel posts, users can swipe through the images or videos to view all the content in the post. IGSave helps you download videos and/or images from a carousel.</p>
        </div>
      </div>
      <Footer/>
      <GoogleAnalytics measurementId='G-ZGXMMY4FE3' />
    </>
  )
}
