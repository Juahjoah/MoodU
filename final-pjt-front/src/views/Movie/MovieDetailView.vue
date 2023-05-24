<template>
  <div class="moviedetail">
    <div>
      <p id="titlep">{{ movie.title }}</p>
      <p id="contentp">개봉일: {{ movie.release_date }}</p>
      <hr />
      <img align="right" :src="getPoster" />

      <p>인기도: {{ movie.popularity }}</p>
      <p>평균 점수: {{ movie.vote_average }}</p>
      <p>투표 수: {{ movie.vote_count }}</p>
      <div>
        장르 :
        <span v-for="genre in movie.genres" :key="genre.id">
          {{ genre.name }},
        </span>
        <p v-if="movie.overview" id="overviewp">{{ movie.overview }}</p>
        <p v-else>해당 영화는 줄거리가 제공되지 않습니다.</p>
      </div>
      <hr />
    </div>
    <span>{{ count }} 명의 모듀러가 해당 영화를 좋아합니다. </span>
    <br />
    <MovieVideo :movieId="movie.ids"/>
    <button class="heart" @click.self.prevent="likeMovie()">❤</button>

    <MovieComment />

  </div>
</template>

<script>
import axios from "axios";
import MovieComment from "@/components/MovieComment";
import MovieVideo from "@/components/MovieVideo";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieDetailView",
  components: {
    MovieComment,
    MovieVideo,
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
          confirm("로그인을 해야 좋아요를 누를 수 있어요!");
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
.moviedetail {
  width: 60rem;
  margin: 5rem auto;
  text-align: left;
  padding: 0px 1.5rem;
}

img {
  width: 18em;
  padding: 0.7rem;
}

#titlep {
  font-size: 30px;
  text-align: left;
  margin: 0px 1rem;
}

#contentp {
  font-size: 15px;
  text-align: left;
  margin: 0px 1rem;
}

#overviewp {
  font-size: 14px;
}

.heart {
  font-size: 20px;
}
</style>