import pic1 from "./picSrc/protest.jpg"; 
import pic2 from "./picSrc/plant.jpg"; 
import pic3 from "./picSrc/smoothie.jpg"; 
import axios from 'axios';

// {"articles": blueprintData}
// make the api call here and set blueprintData = the api call

// const axios = require('axios')

const getAgnes = async () => {
  try {
    return await axios.get('http://ethic-blueprint.herokuapp.com/articles')
  } catch (error) {
    console.error(error)
  }
}

const countBreeds = async () => {
  const breeds = await getAgnes()

  console.log(breeds.data['articles'])
}

countBreeds()

const blueprintData = [
    {
        id: 0,
        title: "15 Best Blogs To Follow About Web Design",
        img: "https://media.treehugger.com/assets/images/2020/02/vinegar.jpg.859x0_q70_crop-center.jpg",
        context: "Tenetur quidem quidem autem quaerat tempora cupiditate. Et consequatur eaque. Quidem et labore adipisci dolorum et eum expedita praesentium. Aliquid atque itaque accusantium maiores. Quasi architecto eum sequi dolores exercitationem incidunt molestiae. Quidem dolorem autem laborum vel voluptatem ut.",
        url: "https://google.com",
        author: "your mom"
    },
    {
        id: 1,
        title: "15 Best Blogs To Follow About Web Design",
        img: pic2,
        context: "Tenetur quidem quidem autem quaerat tempora cupiditate. Et consequatur eaque. Quidem et labore adipisci dolorum et eum expedita praesentium. Aliquid atque itaque accusantium maiores. Quasi architecto eum sequi dolores exercitationem incidunt molestiae. Quidem dolorem autem laborum vel voluptatem ut.",
        url: "https://google.com",
        author: "your mom"
    },
    {
        id: 2,
        title: "15 Best Blogs To Follow About Web Design",
        img: pic3,
        context: "Tenetur quidem quidem autem quaerat tempora cupiditate. Et consequatur eaque. Quidem et labore adipisci dolorum et eum expedita praesentium. Aliquid atque itaque accusantium maiores. Quasi architecto eum sequi dolores exercitationem incidunt molestiae. Quidem dolorem autem laborum vel voluptatem ut.",
        url: "https://google.com",
        author: "your mom"
    },
]

export default blueprintData

//  URL, title, author, image_url, content, publish_date