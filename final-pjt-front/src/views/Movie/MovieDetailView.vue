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

    <button @click="likeMovie()">이 영화 맘에 드셨나요?</button>
    <span>{{count}}</span>

    <section class="user_comment">
      <p class="displaytext">여러분은 영화를 어떻게 보셨나요?</p>
      <input type="text" v-model.trim="comment" @keyup.enter="createComment">
      <button @click="createComment">!</button>
      <MovieComment />
    </section>

  </div>
</template>

<script>
import axios from "axios";
import MovieComment from '@/components/MovieComment'

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieDetailView",
  components: {
    MovieComment
  },
  data() {
    return {
      movie: Object,
      comment: null,
      count: null,
    };
  },
  created() {
    this.getMoviesDetail();

    this.getLikeCount()
    
  },
  methods: {
    getMoviesDetail() {
      axios({
        method: "get",
        url: `${API_URL}/movies/${this.$route.params.id}/`,
      })
        .then((response) => {
          // console.log(response);
          this.movie = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getLikeCount() {

      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/like/count/`,
      })
      .then((res)=> {
        console.log(res)
        this.count = res.data.like_count
      })
      .catch((err)=> {
        console.log(err)
      })
    },

    likeMovie() {
      const token = localStorage.getItem('jwt')

      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.id}/like/`,
        headers: {
          Authorization: `Bearer ${token}`,
        }
      })
      .then((res)=> {
        console.log(res)
        this.getLikeCount()
      })
      .catch((err)=> {
        console.log(err)
      })
      
    },

    createComment() {
      const comment = this.comment
      const token = localStorage.getItem('jwt')

      if (!comment) {
        alert('댓글을 달고 엔터를 눌러라')
      } else {
        axios({
          method: 'post',
          url: `${API_URL}/movies/${this.$route.params.id}/comments/create/`,
          headers: {
            Authorization: `Bearer ${token}`,
          },
          data: {
            content : comment
          }
        }).then((res)=> {
          console.log(res)
        }).catch((err)=> {
          console.log(err)
        })
      }


    }
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