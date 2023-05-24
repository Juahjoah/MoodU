<template>
  <div >
    <div class="recommendview">
      <h3>모듀러님의 기분에 따른 영화를 추천해 드릴게요!</h3>
      <h5>현재 기분을 골라주세요!</h5>
      <div class="emobtn">
        <span
          class="btn-3d clickbtn happy"
          @click.self.prevent="emotionSelect('happy')"
          >😀<br />
          행복해요</span
        >
  
        <span
          class="btn-3d clickbtn sad"
          @click.self.prevent="emotionSelect('sad')"
          >😥<br />
          슬퍼요</span
        >
  
        <span
          class="btn-3d clickbtn soso"
          @click.self.prevent="emotionSelect('soso')"
          >😗<br />그저 그래요</span
        >
  
        <span
          class="btn-3d clickbtn joy"
          @click.self.prevent="emotionSelect('joy')"
          >😎<br />신나요</span
        >
        <span
          class="btn-3d clickbtn angry"
          @click.self.prevent="emotionSelect('angry')"
          >😤<br />화나요</span
        >
        <span
          class="btn-3d clickbtn depressed"
          @click.self.prevent="emotionSelect('depressed')"
          >🥴<br />속상해요</span
        >
      </div>
      <h5>{{ emo }}한 기분인 모듀러를 위한 영화</h5>
      <div class="recommendmovielist">
        <RecommendMovie
          v-for="(movie, index) in emotionMovie"
          :key="index"
          :movie="movie"
        />
      </div>

    </div>
  </div>
</template>

<script>
import RecommendMovie from "@/components/RecommendMovie";
const API_URL = "http://127.0.0.1:8000";
import axios from "axios";

export default {
  name: "RecommendView",
  data() {
    return {
      emo: null,
      emotionMovie: [],
    };
  },
  components: {
    RecommendMovie,
  },
  methods: {
    setToken() {
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `Bearer ${token}`,
      };
      return config;
    },
    emotionSelect(e) {
      // console.log(e);
      this.emo = e;
      const emo = this.emo;
      // console.log(emo);
      axios({
        method: "get",
        url: `${API_URL}/movies/recommended/${emo}/`,
        headers: this.setToken(),
      })
        .then((res) => {
          // console.log(res);
          this.emotionMovie = res.data;
        })
        .catch((err) => {
          confirm("로그인한 콩알님들만 볼 수 있어요😣!");
          this.$router.push({ name: "LoginView" });
          console.log(err);
        });
    },
  },
  created() {
    this.loginuseronly();
  },
};
</script>

<style>
.recommendview {

  padding-top: 50px;
}



.emobtn {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin: 0px auto;
  width: 70rem;
}
.clickbtn {
  margin: 0.7rem;
  /* display: flex; */
}

.btn-3d {
  width: 9rem;
  position: relative;
  display: inline-block;
  font-size: 17px;
  padding: 10px 20px;
  color: black;
  margin: 20px 10px 10px;
  border-radius: 6px;
  text-align: center;
  transition: top 0.01s linear;
  text-shadow: 0 4px 0 rgba(0, 0, 0, 0.15);
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

.recommendmovielist {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 80rem;
  margin: 0px auto;
}
</style>