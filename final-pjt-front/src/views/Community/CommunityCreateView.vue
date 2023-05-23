<template>
  <div class="create">
    <h1>커뮤니티 게시글 작성</h1>
    <form>
      <label for="title"> 제목: </label>
      <input type="text" id="title" v-model.trim="title" />
      <br />
      <label for="content"> 내용 :</label>
      <textarea type="text" id="content" v-model.trim="content" />
      <br />
      <button @click.self.prevent="createCommunity()">제출</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommunityCreateView",
  data() {
    return {
      title: "",
      content: "",
    };
  },
  methods: {
    createCommunity() {
      const title = this.title;
      const content = this.content;

      if (!title) {
        confirm("제목 입력해주세요");
        return;
      } else if (!content) {
        confirm("내용 입력해주세요");
        return;
      }
      const token = localStorage.getItem("jwt");
      axios({
        method: "post",
        url: `${API_URL}/community/create/`,
        data: {
          title,
          content,
        },
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then((response) => {
          this.$router.push({ name: "Community" }).catch(() => {});
          console.log(response);
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