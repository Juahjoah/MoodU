<template>
  <div class="communitydetail">
    <p>{{ community }}</p>
    <p>제목 : {{ community.title }}</p>
    <p>내용 : {{ community.content }}</p>
    <p>작성자 : {{ community.user }}</p>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityDetailView",
  data() {
    return {
      community: Object,
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
</style>