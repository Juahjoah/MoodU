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
          />
        </div>
        <div id="createbtncenter">
          <input
            type="submit"
            class="create_btn createbbtn"
            @click.self.prevent="createCommunity()"
            value="Submit"
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
@import url("https://fonts.googleapis.com/css2?family=Gamja+Flower&family=Pangolin&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Poor+Story&display=swap");
</style>
<style scoped>
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

form {
  display: inline-block;
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

.create_btn {
  font-family: "Pangolin", cursive;
  flex: 1 1 auto;
  margin: 10px;
  padding: 5px;
  text-align: center;
  text-transform: uppercase;
  transition: 0.5s;
  background-size: 200% auto;
  color: black;
  text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 20px #eee;
  border-radius: 5px;
}

.create_btn:hover {
  background-position: right center; /* change the direction of the change here */
}
.createbbtn {
  background-image: linear-gradient(
    to right,
    #b2b0eb 0%,
    #fefefe 51%,
    #6e6bd7 100%
  );
}
#createbtncenter {
  display: flex;
  text-align: center;
  width: 10rem;
  margin: 0px auto;
}
.arealabel {
  display: inline-block;
}
</style>