<template>
  <div class="Movie">
    <router-link
      class="mainrecombtn"
      data-text-after="기분에 따라 영화를 추천받을 수 있어요!"
      data-text="오늘도 모듀와 함께해요!"
      :to="{ name: 'RecommendView' }"
    ></router-link>
    <br />
    <input type="text" v-model="searchMovie" @keyup.enter="search()">
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
        this.$router.push({name: 'MovieSearchView', params: {movieTitle : this.searchMovie}}).catch(()=>{})

      } else {
        alert('검색할 단어를 써주고 검색을 눌러주겠어?')
        this.$router.push({name: 'MovieView'})
      }
    }
  },
};
</script>

<style>
.Movie {
  font-family: "Poor Story", cursive;
}

.movielist {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin: 0px 20px;
}

.mainrecombtn {
  position: absolute;
  transform: translate(-50%, -50%);
  width: 35rem;
  height: 3rem;
  line-height: 50px;
  font-size: 20px;
  text-align: center;
  font-family: "Poor Story", cursive;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 5px;
  background: #ccc;
}
.mainrecombtn:before {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  text-align: center;
  background: #fffaf3;
  color: black;
  transition: 0.5s;
  transform-origin: bottom;
  transform: translatey(-100%) rotatex(90deg);
}
.mainrecombtn:hover:before {
  transform: translatey(0) rotatex(0deg);
}

.mainrecombtn:after {
  content: attr(data-text-after);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  text-align: center;
  background: #fffaf3;
  color: black;
  transition: 0.5s;
  transform-origin: top;
  transform: translatey(0) rotatex(0deg);
}
.mainrecombtn:hover:after {
  transform: translatey(100%) rotatex(90deg);
}
</style>