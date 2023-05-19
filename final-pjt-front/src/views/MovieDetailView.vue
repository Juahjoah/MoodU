<template>
  <div class="moviedetail"></div>
</template>

<script>
export default {
  name: "MovieDetailView",
  data() {
    return {
      movies: null,
    };
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