<template>
  <div class="Movie">
    <h1>Movie</h1>
    <br />
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
  },
};
</script>

<style>

.movielist {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin: 0px 20px;

}
</style>