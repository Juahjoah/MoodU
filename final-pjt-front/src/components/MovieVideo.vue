<template>
  <div class="movievideo">
    <button class="btn-3d clickbtn" @click="getVideo()">유튜브 영상보기</button>
    <div>
      <p v-if="videoMsg">{{ videoMsg }}</p>
      <p v-else>
        <iframe v-if="look"
          class="youtubemovie"
          :width="720"
          :height="480"
          :src="videoURL"
          frameborder="0"
        ></iframe>
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    movieId: Number,
  },
  components: {},
  data() {
    return {
      videoKey: null,
      videoMsg: null,
      videoURL:null,
      look: false,
    };
  },
  methods: {
    getVideo() {
      // const movieId = this.movieId;
      // console.log(movieId)
      this.look = true

      axios({
        method: "get",
        url: `https://api.themoviedb.org/3/movie/${this.movieId}/videos`,
        params: {
          language: "ko-KR",
          api_key: `${API_KEY}`,
        },
      })
        .then((res) => {
          console.log(res.data.results);
          const list = res.data.results.length;
          if (res.data.results.length === 0) {
            this.videoMsg = "유튜브 영상이 없어요 ㅠㅠ.";
          } else {
            this.videoKey = res.data.results[list - 1].key;
            this.videoURL = `https://www.youtube.com/embed/${this.videoKey}`
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },

  
};
</script>

<style scoped>
.movievideo {
  margin-top: 4rem;
  right: 50%;
  left: 50%;
  /* content-visibility: ; */
  /* display: flex;
  flex-direction: column;
  justify-content: center; */
  width: 40rem;
}

.youtubemovie {
  margin: 0 auto;
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
  width: 13rem;
  height: 2.3rem;
  position: relative;
  display: inline-block;
  font-size: 13px;
  margin: 20px 10px 10px;
  border-radius: 6px;
  transition: top 0.01s linear;
  text-shadow: 0 2px 0 rgba(0, 0, 0, 0.15);
}
.btn-3d.clickbtn:hover {
  background-color: #f51f1f;
}

.btn-3d:active {
  top: 9px;
}
/* 3D button colors */
.btn-3d.clickbtn {
  background-color: #f56e6e;
  box-shadow: 0 0 0 1px #f51f1f inset, 0 0 0 2px rgba(255, 255, 255, 0.15) inset,
    0 8px 0 0 #A30808, 0 8px 0 1px rgba(0, 0, 0, 0.4),
    0 8px 8px 1px rgba(0, 0, 0, 0.5);
}
.btn-3d.clickbtn:active {
  box-shadow: 0 0 0 1px #f51f1f inset, 0 0 0 2px rgba(255, 255, 255, 0.15) inset,
    0 0 0 1px rgba(0, 0, 0, 0.4);
}


</style>
