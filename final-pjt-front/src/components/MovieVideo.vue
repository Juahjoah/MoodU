<template>
  <div class="movievideo">
    <button @click="getVideo()">유튜브 영상보기</button>
    <div>
      <p v-if="videoMsg">{{ videoMsg }}</p>
      <p v-else>
        <iframe
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
    };
  },
  methods: {
    getVideo() {
      const movieId = this.movieId;
      // console.log(movieId)

      axios({
        method: "get",
        url: `https://api.themoviedb.org/3/movie/${movieId}/videos`,
        params: {
          language: "ko-KR",
          api_key: "***REMOVED***",
        },
      })
        .then((res) => {
          console.log(res.data.results);
          const list = res.data.results.length;
          if (res.data.results.length === 0) {
            this.videoMsg = "유튜브 영상이 없어요 ㅠㅠ.";
          } else {
            this.videoKey = res.data.results[list - 1].key;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    videoURL() {
      return `https://www.youtube.com/embed/${this.videoKey}`;
    },
  },
  created() {
    this.getVideo();
    this.videoURL;
  },
};
</script>

<style>
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
</style>