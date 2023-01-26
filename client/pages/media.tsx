import axios from 'axios';
import { useEffect, useState } from 'react';
import { Inter } from '@next/font/google';
import styles from '@/styles/Home.module.css';
import mediaStyles from '@/styles/Media.module.css';
import GoogleAnalytics from "@bradgarropy/next-google-analytics"
import Footer from '@/components/footer';
import '@/styles/Media.module.css'
import { useRouter } from 'next/router';
import LoadingIcons from 'react-loading-icons'

const inter = Inter({ subsets: ['latin'] })

export default function Media(){

    const [media, setMedia] = useState<Media[]>([])
    const [url, setUrl] = useState('')
    const router = useRouter()

    const config = {
        headers: {
         'Access-Control-Allow-Origin' : '*',
         'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
         }
    }

    type Media = {
        url: string;
        base64: string;
        base64Vid: string;
    };

    const getLinks = async () => { 
        setMedia([])
        const urlSearchParams = new URLSearchParams(window.location.search);
        const params = Object.fromEntries(urlSearchParams.entries());

        const data = await axios.post('https://igsave.onrender.com', { url: params.url}, config)   

        var dataArr = new Array<Media>
        data.data.links.map((item: Media) => {
            var tempObj: Media = {
                url: item.url,
                base64: item.base64,
                base64Vid: item?.base64Vid,
            }
            dataArr.push(tempObj)
        })
        setMedia(dataArr)       
    }


    useEffect(() => {
        getLinks()
    }, [router.query.url])  


    function downloadURI(url: string, uri: string , name: string) {
        var link = document.createElement("a");
        link.download = name;
        link.href = uri;
        link.target = '_self'
        link.click();
    }

    const handleSubmit = (e: { preventDefault: () => void; }) => {
        e.preventDefault();
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

    return(
        <>
            <main className={styles.header}>
                <a href='http://igsave.io'><img className={styles.logo} src='/igsave_logo_full.png'></img></a>
            </main>
            <div>
                <div className={styles.downloadDiv}>
                    <h1 className={inter.className}>Post Media Download</h1>  

                    <form className={styles.form} id='form' action="/" method='POST'>
                        <input className={styles.input} id='url' type='text' name ='url' placeholder='Paste Instagram Link Here' value={url} onChange={(e) => setUrl(e.target.value)}></input>
                    </form> 
                    <button className={styles.button} onClick={handleSubmit}>Download</button>
                </div>
            </div>

            {!media.length && 
            <div className={mediaStyles.loading}>
                <LoadingIcons.ThreeDots fill="#8f0af8"/>
            </div>}
            
            <div id='cardContainer' className={styles.linkDiv}>
  
                {media.map((item) => {  

                    var fileExtension: string;
                    if(item?.base64Vid){
                        fileExtension = '.mp4'
                    }
                    else{
                        fileExtension = '.jpg'
                    }

                    var fileName: string;
                    fileName = item.url.split('/')[5].split('.')[0]

                    return(
                    <div className={mediaStyles.mediaCard} key={item.url}>
                        <img className={mediaStyles.thumbNail} src={item.base64}/>
                        <div className={mediaStyles.downloadButton}>
                            <div className={mediaStyles.aTagDiv}>
                                {!item.base64Vid ? 
                                    <a className={inter.className} target="_blank" rel="noreferrer" href={item.url} onClick={() =>{downloadURI(item.url, item.base64, `${fileName}${fileExtension}`)}}>Download</a> : 
                                    <a className={inter.className}  target="_blank" rel="noreferrer" href={item.url} onClick={() => {downloadURI(item.url, item?.base64Vid, `${fileName}${fileExtension}`)}}>Download</a>
                                }
                            </div>
                        </div>
                    </div>
                    )
                })}
            </div>
            <div className={styles.contentDiv}>

            </div>
            <Footer/>
            <GoogleAnalytics measurementId='G-ZGXMMY4FE3'/>
        </>
    )   
}