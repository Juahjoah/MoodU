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
      <button class="comebtn" @click.self.prevent="updateCommunity(community)">
        제출하기
      </button>
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
            name: "CommunityDetailView",
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

.comebtn {
  margin: 20px;
  outline: none;
}
.comebtn {
  width: 100px;
  height: 40px;
  padding: 10px 25px;
  border: 2px solid #000;
  font-family: "Lato", sans-serif;
  font-weight: 450;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
}
.comebtn {
  background: #000;
  color: #fff;
  line-height: 42px;
  padding: 0;
  border: none;
}
.comebtn:hover {
  background: transparent;
  color: #000;
  box-shadow: -7px -7px 20px 0px #fff9, -4px -4px 5px 0px #fff9,
    7px 7px 20px 0px #0002, 4px 4px 5px 0px #0001;
}
.comebtn:before,
.comebtn:after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  height: 2px;
  width: 0;
  background: #000;
  transition: 400ms ease all;
}
.comebtn:after {
  right: inherit;
  top: inherit;
  left: 0;
  bottom: 0;
}
.comebtn:hover:before,
.comebtn:hover:after {
  width: 100%;
  transition: 800ms ease all;
}
#createbtncenter {
  display: flex;
  text-align: center;
  width: 10rem;
  margin: 0px auto;
}
</style>