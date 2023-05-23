<template>
  <div>
    <h3>모듀님의 기분에 따른 영화를 추천해 드릴게요!</h3>
    <div>
      <span @click.self.prevent="emotionSelect('happy')">행복해요</span> |
      <span @click.self.prevent="emotionSelect('sad')">슬퍼요</span> |
      <span @click.self.prevent="emotionSelect('soso')">그저 그래요</span> |
      <span @click.self.prevent="emotionSelect('joy')">신나요</span> |
      <span @click.self.prevent="emotionSelect('angry')">화나요</span> |
    </div>
    <h5>{{ emo }} 모듀님을 위한 영화</h5>
    <RecommendMovie
      v-for="(movie, index) in emotionMovie"
      :key="index"
      :movie="movie"
    />
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
  methods: {
    emotionSelect(e) {
      // console.log(e);
      this.emo = e;
      const emo = this.emo;
      // console.log(emo);

      const token = localStorage.getItem("jwt");

      axios({
        method: "get",
        url: `${API_URL}/movies/recommended/${emo}/`,
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then((res) => {
        // console.log(res);
        this.emotionMovie = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
    },
    
  },

  components: {
    RecommendMovie,
  },
};
</script>

<style>
</style>