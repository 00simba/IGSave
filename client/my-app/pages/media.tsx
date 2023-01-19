import axios from 'axios';
import { useEffect, useState } from 'react';


export default function Media(){

    const [links, setLinks] = useState([])

    useEffect(() => {
        const getLinks = async () => {      
            const data = await axios.get('http://ec2-3-99-182-77.ca-central-1.compute.amazonaws.com/')
            setLinks(data.data.links)
      }
      getLinks()
    }, [])    

    return(
        <>
            <div>
                <h1>Media Page</h1>  
                <br/>
            </div>
            {links.map((link) => {
                return(
                <div>
                    <a href={link}>Download<br/></a>
                </div>
                )
            })} 
        </>
    )   
}