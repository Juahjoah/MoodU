<template>
  <div class="communityupdateview">
    <h1>커뮤니티 게시글 수정</h1>
    <br />
    <form class="updateinfo">
      <label for="title"> 제목: </label>
      <input
        type="text"
        id="title"
        class="updateinput"
        v-model.trim="community.title"
      />
      <br />
      <label class="arealabel" for="content"> 내용 :</label>
      <textarea
        class="areainput"
        required
        type="text"
        id="content"
        v-model.trim="community.content"
        @keyup.enter.self.prevent="updateCommunity(community)"
      />
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
          this.$router
            .push({
              name: "CommunityDetail",
              params: { id: this.community.id },
            })
            .catch(() => {});
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
.communityupdateview {
  margin-top: 100px;
}

.updateinfo {
  width: 50rem;
  margin: 0px auto;
  position: relative;
}

.updateinput {
  border-left-width: 0;
  border-right-width: 0;
  border-top-width: 0;
  border-bottom-width: 1;
  font-family: "Poor Story", cursive;
  width: 70%;
  height: 1.5rem;
  margin: 5px auto;
  font-size: 20px;
  letter-spacing: 2px;
}
.updateinput:focus {
  outline: none;
}

.areainput {
  width: 70%;
  height: auto;
  resize: none;
  border: 2px solid grey;
  font-family: "Poor Story", cursive;
  font-size: 20px;
  border-radius: 5px;
}
.areainput:focus {
  outline: none;
}
</style>