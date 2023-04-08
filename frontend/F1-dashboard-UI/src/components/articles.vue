<template>


    
    <img v-if="show && loading" class="img_specific" src="/f1.gif" alt="logo"  />
    <div v-if="show && loading" class="allArticles">
        <h1 class="h1_specific">Latest News</h1>

        <div class="singleArticle"
        v-for="article in articles" :key="article.articleTitle"
        >
        <!-- <ul> -->
            <!-- <li > -->
                <h2>{{ article.articleTitle }}</h2>
                <p v-html="article.articleSummary"></p>
                <p class="published" v-html="article.articlepublished"></p>
                <button>
                    <a :href="article.articleLink" target="_blank">Read More</a>
                </button>
                <!-- </li> -->
                <!-- </ul> -->
        </div>
        </div>


</template>

<script>
import { EventBus } from "@/eventBus.js";


export default {
      name: 'articles',

      created() {

        EventBus.$on("toggle-Articles", () => {
            // EventBus.$emit("select-year-toggled", this.show);
            this.show = !this.show;
            this.getNews()
      });
            // this.show = false;

            // this.show = true;
            // console.log(this.show)
    //   EventBus.$on("toggle-Standings-Components", () => {
    //     this.show = !this.show;
    //     EventBus.$emit("select-year-toggled", this.show);
    //   });
    },
    data() {
    return {
      show: false,
      articles: [],
      loading : false,
    };
  },



      methods: {


        getNews() {
            // this.show = false
            fetch('http://localhost:8888/news', {
                method: 'GET',
                headers: {
                'Content-Type': 'application/json'
                },
            })
                .then(response => response.json())
                .then(data => {
                    this.articles = data
                    // this.show = true;
                    this.loading = true;
                })
                .catch(error => console.error(error));
                }
                 },

//       data() {
//             return {
//                 articles: [],
//             };
//   },

    };
</script>

<style>
.img_specific {
    position: absolute;
    left: 20%;
    width: 420px;
    
}
.h1_specific {
    position: absolute;
    left: 44.5%;
    color: white;
    font-weight: 800;
    font-size: 36px;
}
.allArticles {
    margin:5%;
    overflow: auto;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    text-align: center;
    box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);
    border: 1px solid rgba(0, 0, 0, 0.514);
    transition: all 0.3s ease;
    border-radius: 10px;
    background: rgba(7, 1, 1, 0.589);
    padding: 20px;
    padding-top: 60px;
}

.singleArticle {
            box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);
            border: 1px solid rgba(0, 0, 0, 0.514);
            transition: all 0.3s ease;
            border-radius: 10px;
            background: rgba(7, 1, 1, 0.589);    
    
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    
}


h2 {
    color: aliceblue;
}

a {
    text-decoration: none;
    color: whitesmoke;
    font-size: 20px;
}
p {
    color: gray;
    font-size: 18px;
    /* padding: 5px; */
}
button {
    margin: 10px;
  border: 1px solid black;
  color: white;
  text-decoration: none;
  background-color: black;
  padding: 5px 10px 5px 10px;
  border-radius: 10px;
  transition: transform 0.5s ease;
  box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);


}
/* button:hover {
  transform: scale(1.2);
} */

.published {
    color: white;
    font-size: 15px;
    text-align: right;
    margin-right: 10px;
}
</style>