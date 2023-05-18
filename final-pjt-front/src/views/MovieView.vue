<template>
  <div class="Movie">
    <h1>Movie</h1>
    <p>{{ movie }}</p>
    <br />
    <MovieCard :movie="movie" />
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard.vue";

export default {
  name: "MovieView",
  data() {
    return {
      movie: null,
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
      this.movie = this.$store.state.movies;
    },
  },
};
</script>

<style>
</style>