<template>
  <div class="Movie">
    <h1>Movie</h1>
    <p>{{ movie }}</p>
    <br />
    <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
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
</style>