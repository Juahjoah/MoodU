<template>
  <div class="Movie">
    <div class="searchbox">
      <i class="bi bi-search"> 
        <input type="text" v-model="searchMovie" @keyup.enter="search()" /> </i>
    </div>
    <br><br><br><br>

    <section class="moviepic">

    </section>
    
    <br><br><br><br>

    <div id="banner">
    <router-link      
    :to="{ name: 'RecommendView' }"
    > 
          <p class="ch"> 오늘 어떤 영화볼지 고민인가요?</p>
          <!-- <img class="tistory" src="images/ch_logo.png"> -->
          <p class="txt">오늘의 기분을 고르시면,</p>
          <p class="txt2">모듀가 직접 영화를 골라드려요!</p>
          <p class="logo"><i class="fab fa-chrome"></i><i class="fab fa-internet-explorer"></i><i class="fab fa-firefox"></i><i class="fab fa-opera"></i><i class="fab fa-safari"></i></p>
          <p class="device"><i class="fas fa-desktop"></i><i class="fas fa-mobile-alt"></i></p>
        </router-link>
      </div>
  

    <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
    <h1>Movie</h1>
    <section class="movielist">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
    </section>
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard.vue";

export default {
  name: "MovieView",
  data() {
    return {
      movies: null,
    };
  },
  components: {
    MovieCard,
  },
  created() {
    this.getMovies();
  },
  methods: {
    getMovies() {
      this.$store.dispatch("getMovies");
      this.movies = this.$store.state.movies;
    },
    search() {
      if (this.searchMovie) {
        this.$router
          .push({
            name: "MovieSearchView",
            params: { movieTitle: this.searchMovie },
          })
          .catch(() => {});
      } else {
        alert("검색할 단어를 써주고 검색을 눌러주겠어?");
        this.$router.push({ name: "MovieView" });
      }
    },
  },
};
</script>

<style scoped>
* {
  font-family: 'TheJamsil5Bold';
}
.Movie {

  font-family: 'TheJamsil5Bold';
}
input {
  width: 20rem;
  height: 1.7rem;
  border-radius: 3px;
  margin-left: 0.5rem;
}
i {
  font-size: 0.9rem;
}
.searchbox {
  float: right;
  margin-right: 10rem;
}

.moviepic {
  height: 20rem;
  background-color: #555;
  border-bottom: 2px solid yellow;
}

.movielist {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin: 40px auto 0;
  width: 80%;
}



a {

text-decoration: none;

color: black;

}



#banner {
display: inline-flex;
position: relative;

overflow: hidden;

width: 700px;

height: 250px;

border: 1px solid #ccc;

background: #E3DAD5 

}



.ch {

position: absolute;

left: 290px;

top: 10px;

transition: all 0.5s;

}



#banner:hover .ch {

left: 520px;

}



.tistory {

position: absolute;

left: 15px;

top: -90px;

transition: all 0.5s 0.2s;

}



#banner:hover .tistory {

top: 15px;

}



.txt {

display: block;

position: absolute;

left: 20px;

top: 110px;

font-size: 30px;

font-weight: bold;

opacity: 0;

transform: scale(2, 2);

transition: all 0.25s linear 0.2s;

}



#banner:hover .txt {

opacity: 1;

transform: scale(1, 1);

}



.txt2 {

display: block;

position: absolute;

left: -300px;

bottom: 20px;

font-size: 30px;

font-weight: bold;

color: #555;

transition: all 0.5s 0.3s;

}



#banner:hover .txt2 {

left: 18px;

}



.logo {

display: block;

position: absolute;

left: 270px;

bottom: -50px;

font-size: 20px;

color: #888;

transition: all 0.5s 0.3s;

}



#banner:hover .logo {

bottom: 20px;

}



.device {

display: block;

position: absolute;

right: 180px;

bottom: 10px;

font-size: 55px;

color: #007AAE;

opacity: 0;

transition: opacity 0.5s linear 0.2s;

}



#banner:hover .device {

opacity: 1;

}
</style>