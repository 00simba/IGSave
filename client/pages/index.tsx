import Head from 'next/head'
import { Inter } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import { useState } from 'react'
import { useRouter } from 'next/router'
import GoogleAnalytics from "@bradgarropy/next-google-analytics"
import Footer from '../components/footer'
import Faq from "react-faq-component"
import Link from 'next/link'


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
    title: "Frequently Asked Questions",
    rows: [
        {
            title: <p className={styles.pTag}>What is the purpose of IGSave?</p>,
            content: <p className={styles.pTag}>IGSave is an easy and free to use tool that helps Instagram users download Instagram content such as images/photos, videos, and reels in the highest quality possible directly to their device. IGSave also allows for you to view the content you wish without an internet connection and share Instagram posts on other social media or communications platforms.</p>,
        },
        {
          title: <p className={styles.pTag}>Is there a limit for downloading content?</p>,
          content: <p className={styles.pTag}>Nope! Thankfully IGSave was developed in such a way that enables its users to download any amount of content they wish per session. All types of content such as photos, videos, and reels can be downloaded at any amount without any kinds of restrictions!</p>,
        },
        {
          title: <p className={styles.pTag}>Is IGSave free to use?</p>,
          content: <p className={styles.pTag}>Yes! IGSave is completely free to use as IGSave values the convinence of its users. For as long as IGSave exists, it is guaranteed to be free to use!</p>,
        },
        {
            title: <p className={styles.pTag}>Which devices does IGSave support?</p>,
            content:
                <p className={styles.pTag}>IGSave was designed to provide full compatibility with various devices. Thanks to IGSave being a web based tool it is able to run on any platform such as Windows, MacOS, iOS, Android, and Linux with browser support. Additionally browsers such as Google Chrome, Safari, Mozilla Firefox, Microsoft Edge, Opera, Chromium, and more support IGSave!</p>,
        },
        {
            title: <p className={styles.pTag}>Does IGSave download posts from any account?</p>,
            content: <p className={styles.pTag}>In order for IGSave to download a post it is required that the account of interest is a public account. This means that private Instagram accounts are not supported when it comes to downloading content from them due to privacy reasons set by the user of that account.</p>,
        },
        {
          title: <p className={styles.pTag}>What quality are posts downloaded at?</p>,
          content: <p className={styles.pTag}>By default, all posts are downloaded at the maximum quality possible which depends on the dimensions of the post originally uploaded by the user. In most cases the resolution of post that is being downloaded is 1080x1350 as IGSave strives to provide the best results for its users.</p>,
        },
        {
          title: <p className={styles.pTag}>What sort of file formats can I expect?</p>,
          content: <p className={styles.pTag}>IGSave downloads video or reel posts in the .mp4 file format and .jpg file format for pictures. These file formats are expected to provide the most efficiency for an IGSave user as they result in smaller file size while retaining quality, delivering the best outcome.</p>,
        },
        {
          title: <p className={styles.pTag}>Will any of my data be required to use IGSave?</p>,
          content: <p className={styles.pTag}>IGSave does not require any sort of personal data on your end. You do not need to provide any sort of Instagram login information to use IGSave which means your account information will remain completely safe. IGSave only needs the public post link to help you download Instagram content fully anonymously.</p>,
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
          Instagram Post Downloader
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
            <h1 className={inter.className}>Download Instagram Photos and Videos!</h1>
          </div>
          <br/>
          <p className={inter.className}>IGSave helps you download Instagram Photos, Videos, Carousels, and Reels with ease!</p>
          <br/>
          <p className={inter.className}>Thanks to its user and device friendly design you can download Instagram content to any device such a desktop, laptop, mobile, or tablet!</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>3 Easy Steps To Download!</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>1. Copy the link for the post or reel.</p>
          <p className={inter.className}>2. Paste into the textbox above</p>
          <p className={inter.className}>3. Click the `Download` button and save away!</p>
        </div>
      </div>

      <div className={styles.supportHeading}>
        <h1 className={inter.className}>IGSave Helps With</h1>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Photo Download</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>One of the internets most popular ways of sharing photos is done through Instagram. IGSave helps you download pictures from Instagram at a full resolution!</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Video Download</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
            <br/>
            <p className={inter.className}>Instagram does not come with a video download feature, however, using IGSave you can download any kind of Instagram video to your device.</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
            <div className={styles.divHeading}>
              <h1 className={inter.className}>Reel Download</h1>
            </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>Instagram reels are by far the most popular way of sharing videos and IGSave helps you save Reels straight to your device in high definition!</p>
        </div>
      </div>

      <div className={styles.aboutDiv}>
        <div className={styles.aboutLeftDiv}>
          <div className={styles.divHeading}>
            <h1 className={inter.className}>Carousel Download</h1>
          </div> 
        </div>
        <div className={styles.subHeading}>
          <br/>
          <p className={inter.className}>Instagram carousels are a creative way of combining photos and videos into one post. IGSave helps you download content from carousels you wish.</p>
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
