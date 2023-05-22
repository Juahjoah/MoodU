<template>
  <div class="communityupdateview">
    <h1>커뮤니티 게시글 수정</h1>
    <form>
      <label for="title"> 제목: </label>
      <input type="text" id="title" v-model.trim="community.title" />
      <br />
      <label for="content"> 내용 :</label>
      <textarea type="text" id="content" v-model.trim="community.content" />
      <br />
      <button @click.self.prevent="updateCommunity(community)">제출</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityUpdateView",
  data() {
    return {
      community: Object,
      // title: "",
      // content: "",
    };
  },
  methods: {
    setToken() {
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `Bearer ${token}`,
      };
      return config;
    },
    getCommunityDetail() {
      axios({
        method: "get",
        url: `${API_URL}/community/${this.$route.params.id}/`,
      })
        .then((response) => {
          this.community = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateCommunity(community) {
      const title = community.title;
      const content = community.content;

      axios({
        method: "put",
        url: `${API_URL}/community/${this.$route.params.id}/update/`,
        data: {
          title,
          content,
        },
        headers: this.setToken(),
      })
        .then((response) => {
          console.log(response);
          this.$router.push({
            name: "CommunityDetail",
            params: { id: this.community.id },
          }).catch(() => { });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getCommunityDetail();
  },
};
</script>

<style>
</style>