<template>
  <div class="Movie">
    <div class="searchbox">
      <i class="bi bi-search">
        <input type="text" v-model="searchMovie" @keyup.enter="search()" />
      </i>
    </div>
    <br /><br /><br /><br />

    <section class="moviepic" v-for="(back, index) in backGround" :key="index">
      <img :src="back" alt="">
    </section>

    <br /><br /><br /><br />

    <div id="banner">
      <router-link :to="{ name: 'RecommendView' }">
        <p class="ch">모듀 여기를 주목해주세요!</p>
        <p class="focus">오늘 어떤 영화볼지 고민되시는 분들!</p>
        <i class="handfocus bi bi-hand-index-fill"></i>
        <p class="txt">오늘의 기분을 고르시면,</p>
        <p class="txt2">모듀가 직접 영화를 골라드려요!</p>
        <p class="logo">
          <!-- 아래에서 날라옴 -->
        </p>
        <p class="device">
          <!-- 제자리에서 사라지기 -->
          <i class="bi bi-film"></i>
        </p>
        <img
          class="bannerfooter"
          src="@/assets/logo_black_width.png"
          alt="moodU_logo"
        />
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
// import axios from 'axios';

export default {
  name: "MovieView",
  data() {
    return {
      movies: null,
      backGround : []
    };
  },
  components: {
    MovieCard,
  },
  created() {
    this.getMovies();
    this.getBackGround()
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
        alert("검색할 단어를 써주고 검색을 눌러주세요!");
        this.$router.push({ name: "MovieView" });
      }
    },
    getBackGround() {
      const movies = this.$store.state.movies
      for (let i=0; i<movies.length; i++){
        this.backGround[i] = `https://image.tmdb.org/t/p/original${movies[i].backdrop_path}`
      }
      console.log(this.backGround)
    }
  },
};
</script>

<style scoped>
* {
  font-family: "TheJamsil5Bold";
}
.Movie {
  font-family: "TheJamsil5Bold";
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
  width: 46.25rem;
  height: 10rem;
  border: 1px solid #ccc;
  background: hsl(20, 100%, 98%);
}

.focus {
  font-size: 30px;
  position: absolute;
  left: 70px;
  top: 15px;
  transition: all 0.5s 0.2s;
}
#banner:hover .focus {
  top: 800px;
}
.handfocus {
  font-size: 30px;
  position: absolute;
  left: 530px;
  top: 45px;
  transition: all 0.5s 0.2s;
}
#banner:hover .handfocus {
  top: 800px;
}
.ch {
  position: absolute;
  left: 70px;
  top: 70px;
  transition: all 0.5s;
}

#banner:hover .ch {
  top: 800px;
}

.txt {
  display: block;
  position: absolute;
  left: 70px;
  top: 15px;
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
  left: -400px;
  bottom: 20px;
  font-size: 30px;
  font-weight: bold;
  color: #555;
  transition: all 0.5s 0.3s;
}

#banner:hover .txt2 {
  left: 70px;
}

.logo {
  display: block;
  position: absolute;
  left: 70px;
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
  left: 500px;
  /* top: 15px; */
  bottom: 10px;
  font-size: 70px;
  /* color: #007aae; */
  color: black;
  opacity: 0;
  transition: opacity 0.5s linear 0.2s;
}

#banner:hover .device {
  opacity: 1;
}
.bannerfooter {
  display: block;
  position: absolute;
  bottom: 1px;
  right: 1px;
  width: 4rem;
  height: auto;
}
</style>