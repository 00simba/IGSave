import axios, { AxiosInterceptorManager } from 'axios';
import { useEffect, useState } from 'react';
import { Inter } from '@next/font/google';
import styles from '@/styles/Home.module.css';
import mediaStyles from '@/styles/Media.module.css';
import GoogleAnalytics from "@bradgarropy/next-google-analytics"
import Footer from '@/components/footer';
import '@/styles/Media.module.css'

const inter = Inter({ subsets: ['latin'] })

export default function Media(){

    const [media, setMedia] = useState<Media[]>([])

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

    useEffect(() => {
        const getLinks = async () => {   
            const urlSearchParams = new URLSearchParams(window.location.search);
            const params = Object.fromEntries(urlSearchParams.entries());
            const data = await axios.post('http://127.0.0.1:5000', { url: params.url}, config)   

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
        getLinks()
    }, [])  

    function downloadURI(uri: string , name: string) {
         var link = document.createElement("a");
         link.download = name;
         link.href = uri;
         link.click();
    }

    return(
        <>
            <main className={styles.header}>
                <a href='http://igsave.io'><img className={styles.logo} src='/igsave_logo_full.png'></img></a>
            </main>
            <div>
                <div className={styles.downloadDiv}>
                    <h1 className={inter.className}>Post Media</h1>  
                </div>
            </div>
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
                                    <a className={inter.className} href={item.url} target='_blank' rel='noreferrer' onClick={(e) => {e.preventDefault(); downloadURI(item.base64, `${fileName}${fileExtension}`)}}>Download</a> : 
                                    <a className={inter.className} href={item.url} target='_blank' rel='noreferrer' onClick={(e) => {e.preventDefault(); downloadURI(item?.base64Vid, `${fileName}${fileExtension}`)}}>Download</a>
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