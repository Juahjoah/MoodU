<template>
  <div class="create">
    <h1>커뮤니티 게시글 작성</h1>
    <div class="createbox">
      <form @submit.prevent="createCommunity">
        <div class="createinfo">
          <label for="title"></label>
          <input
            type="text"
            id="title"
            v-model.trim="title"
            class="createinput"
            placeholder="제목을 작성해주세요."
          />
          <br />
          <label class="arealabel" for="content"></label>
          <textarea
            type="text"
            id="content"
            v-model.trim="content"
            class="areainput"
            wrap="hard"
            required
            maxlength="1000"
            placeholder="1000자 이내로 작성해주세요."
            @keyup.enter.self.prevent="createCommunity()"
          />
        </div>
        <br />
        <div id="createbtncenter">
          <input
            type="submit"
            class="comebtn createbbtn"
            @click.self.prevent="createCommunity()"
            value="제출하기"
          />
        </div>
      </form>
    </div>
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
          this.$router.push({ name: "CommunityView" }).catch(() => {});
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
@import url("https://fonts.googleapis.com/css2?family=Gamja+Flower&family=Pangolin&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Poor+Story&display=swap");
</style>
<style scoped>
.create {
  margin-top: 100px;
}

.createbox {
  font-family: "Poor Story", cursive;
  /* background-color: floralwhite; */
  width: 50rem;
  height: 20rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 5rem auto;
}

.createinfo {
  width: 50rem;
  margin: 0px auto;
  position: relative;
}

.createinput {
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

.createinput:focus {
  outline: none;
}

.areainput {
  width: 70%;
  height: 20rem;
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