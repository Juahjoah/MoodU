<template>
  <div class="MovieCard">
    <!-- <h1>MovieCard</h1> -->
    <div>
      <img class="movie-poster-img" :src="getPoster" alt="Movie Img">
      <p>{{movie.title}}</p>
      <p>{{movie.overview}}</p>

    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
  computed: {
    getPoster() { 
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    }
  },
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
