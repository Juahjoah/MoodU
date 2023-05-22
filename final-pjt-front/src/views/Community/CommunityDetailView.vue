<template>
  <div class="communitydetail">
    <p>{{ movie.title }}</p>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityDetailView",
  data() {
    return {
      communities: Object,
    };
  },
  created() {
    this.getCommunityDetail();
  },
  methods: {
    getCommunityDetail() {
      axios({
        method: "get",
        url: `${API_URL}/community/${this.$route.params.id}/`,
      })
        .then((response) => {
          console.log(response);
          this.community = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  computed: {},
};
</script>

<style scoped>
img {
  float: right;
  width: 15em;
}
</style>