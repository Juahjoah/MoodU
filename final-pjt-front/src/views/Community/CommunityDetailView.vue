<template>
  <div class="communitydetail">
    <p>제목 : {{ community.title }}</p>
    <p>내용 : {{ community.content }}</p>
    <p @click="movieOtherProfile()">작성자 : {{ community.username }}</p>
    <hr />
    <button @click.self.prevent="communityUpdate()">[수정하기]</button>
    <button @click.self.prevent="communityDelete()">[삭제하기]</button>

    <router-link :to="{name : 'CommunityView'}">뒤로가기</router-link>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";
const token = localStorage.getItem('jwt')

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
          console.log(response);
          this.community = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    communityUpdate() {
      if (this.$store.state.user == this.community.username) {
        this.$router.push({
          name: "CommunityUpdate",
          params: { id: this.community.id },
        });
      } else {
        alert("본인이 작성한 글만 수정이 가능합니다.");
      }
    },
    communityDelete() {
      if (confirm("정말 삭제하시겠습니까?")) {
        axios({
          method: "delete",
          url: `${API_URL}/community/${this.$route.params.id}/`,
          headers: this.setToken(),
        })
          .then(() => {
            this.$router.push({ name: "Community" });
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    // 다른 사람의 프로필로 이동
    movieOtherProfile() {
      const user = this.community.username
        axios({
          method: 'post',
          url: `${API_URL}/accounts/profile/${user}/`,
          headers: {
            Authorization: `Bearer ${token}`,
          }
        })
        .then((res)=> {
          console.log(res.data)
          if (res.data.username === this.$store.state.user) {
            alert('본인의 아이디를 클릭하셨네요 ! 본인 프로필로 넘어갑니다.')
            this.$router.push({name: 'ProfileView', params: {username: this.$store.state.user}})
          } else {
            this.$router.push({name: 'ProfileView', params: {username : res.data.username}})
          }
        })
        .catch((err)=> {
          console.log(err)
        })
    }
  },
};
</script>

<style scoped>
</style>