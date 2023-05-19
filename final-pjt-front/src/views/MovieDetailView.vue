<template>
  <div class="moviedetail">
    <p>{{ movie.title }}</p>
    <p>{{ movie.overview }}</p>
    <p>{{ movie.release_date }}</p>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieDetailView",
  data() {
    return {
      movie: null,
    };
  },
  created() {
    this.getMoviesDetail();
  },
  methods: {
    getMoviesDetail() {
      axios({
        method: "get",
        url: `${API_URL}/movies/${this.$route.params.id}/`,
      })
        .then((response) => {
          console.log(response);
          this.movie = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
</style>