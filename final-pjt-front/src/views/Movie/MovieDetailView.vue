<template>
  <div class="moviedetail">
    <p>{{ movie.title }}</p>
    <p>개봉일: {{ movie.release_date }}</p>
    <br />
    <img :src="getPoster" />
    <hr />
    <p>{{ movie.overview }}</p>
    <p>인기도: {{ movie.popularity }}</p>
    <p>평균 점수: {{ movie.vote_average }}</p>
    <p>투표 수: {{ movie.vote_count }}</p>
    <p>장르 : {{ movie.genres }}</p>
    <hr />
    <p>좋아요 누른 사용자 : {{ movie.like_users }}</p>
    <section class="user_comment">
      <p class="displaytext">여러분은 영화를 어떻게 보셨나요?</p>
      <p>{{ movie.comment_set }}</p>
    </section>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieDetailView",
  data() {
    return {
      movie: Object,
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
  computed: {
    getPoster() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`;
    },
  },
};
</script>

<style scoped>
img {
  float: right;
  width: 15em;
}
</style>