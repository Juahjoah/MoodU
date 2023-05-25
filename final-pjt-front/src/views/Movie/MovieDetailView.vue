<template>
  <div class="moviedetail">
    <div>
      <div class="namecontent">
        <div>
          <p id="titlep">{{ movie.title }}</p>
          <br />
          <p id="contentp">개봉일: {{ movie.release_date }}</p>

          <div class="like">
            <button
              class="heart btn-3d clickbtn"
              @click.self.prevent="likeMovie()"
              data-text="💖 좋아요"
            ></button>
            <h6 class="h6style">
              {{ count }} 명의 모듀러가 해당 영화를 좋아합니다.
            </h6>
          </div>
        </div>
      </div>
      <hr class="dotted" />
      <img align="right" :src="getPoster" />
      <div class="detailcontent">
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
      </div>
      <hr />
      <MovieVideo :movieId="movie.ids" />
    </div>

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
  mounted() {

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
.like {
  display: flex;
  justify-content: space-between;
}
.dotted {
  border-bottom: 1px dotted black;
}
.detailcontent {
  padding: 1rem;
}
.namecontent {
  padding: 1rem;
}

.clickbtn {
  margin: 0.7rem;
  /* display: flex; */
}

.btn-3d::after {
  content: attr(data-text);
}
.btn-3d {
  font-family: "TheJamsil5Bold";
  width: 8rem;
  height: 3rem;
  position: relative;
  display: inline-block;
  font-size: 13px;
  margin: 20px 10px 10px;
  border-radius: 6px;
  transition: top 0.01s linear;
  text-shadow: 0 2px 0 rgba(0, 0, 0, 0.15);
}
.btn-3d.clickbtn:hover {
  background-color: #e6d3ed;
}

.btn-3d:active {
  top: 9px;
}
/* 3D button colors */
.btn-3d.clickbtn {
  background-color: #e6d3ed;
  box-shadow: 0 0 0 1px #f8eded inset, 0 0 0 2px rgba(255, 255, 255, 0.15) inset,
    0 8px 0 0 #b2b0eb, 0 8px 0 1px rgba(0, 0, 0, 0.4),
    0 8px 8px 1px rgba(0, 0, 0, 0.5);
}
.btn-3d.clickbtn:active {
  box-shadow: 0 0 0 1px #f8eded inset, 0 0 0 2px rgba(255, 255, 255, 0.15) inset,
    0 0 0 1px rgba(0, 0, 0, 0.4);
}
</style>