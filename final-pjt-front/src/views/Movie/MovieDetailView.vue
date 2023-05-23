<template>
  <div class="moviedetail">
    <div>
      <p>{{ movie.title }}</p>
      <p>개봉일: {{ movie.release_date }}</p>
      <img :src="getPoster" />
      <hr />
      <p>{{ movie.overview }}</p>
      <p>인기도: {{ movie.popularity }}</p>
      <p>평균 점수: {{ movie.vote_average }}</p>
      <p>투표 수: {{ movie.vote_count }}</p>
      <div>
        장르 :
        <span v-for="genre in movie.genres" :key="genre.id">
          {{ genre.name }},
        </span>
      </div>
      <hr />
    </div>

    <button @click.self.prevent="likeMovie()">이 영화 맘에 드셨나요?</button>
    <span>{{ count }}</span>

    <MovieComment />
  </div>
</template>

<script>
import axios from "axios";
import MovieComment from "@/components/MovieComment";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieDetailView",
  components: {
    MovieComment,
  },

  data() {
    return {
      movie: Object,

      count: null,
    };
  },

  created() {
    this.getMoviesDetail();
    this.getLikeCount();
  },

  methods: {
    // 영화 상세 정보 가져오기
    getMoviesDetail() {
      axios({
        method: "get",
        url: `${API_URL}/movies/${this.$route.params.id}/`,
      })
      .then((res) => {
        // console.log(response);
        this.movie = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
    },

    // 좋아요 수 가져오기
    getLikeCount() {
      axios({
        method: "get",
        url: `${API_URL}/movies/${this.$route.params.id}/like/count/`,
      })
      .then((res) => {
        // console.log(res);
        this.count = res.data.like_count;
      })
      .catch((err) => {
        console.log(err);
      });
    },

    // 좋아요 누르기
    likeMovie() {
      const token = localStorage.getItem("jwt");

      axios({
        method: "post",
        url: `${API_URL}/movies/${this.$route.params.id}/like/`,
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then(() => {
        // console.log(res);
        this.getLikeCount();
      })
      .catch((err) => {
        console.log(err);
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