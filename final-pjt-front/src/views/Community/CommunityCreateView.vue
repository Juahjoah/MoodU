<template>
  <div class="create">
    <h1>커뮤니티 게시글 작성</h1>
    <form @submit.prevent="createCommunity"></form>
    <label for="title"> 제목: </label>
    <input type="text" id="title" v-model.trim="title" />
    <br />
    <label for="content"> 내용 :</label>
    <input type="text" id="content" v-model.trim="content" />
    <br />
    <input type="submit" value="작성 완료" />
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityCreateView",
  data() {
    return {
      title: null,
      content: null,
    };
  },
  methods: {
    createCommunity() {
      const title = this.title;
      const content = this.content;

      if (!title) {
        alert("제목 입력해주세요");
        return;
      } else if (!content) {
        alert("내용 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/community/create/`,
        data: {
          title,
          content,
        },
        header: {
          Authorization: `Bearer ${"#"}`,
        },
      })
        .then(() => {
          this.$router.push({ name: "CommunityView" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
</style>