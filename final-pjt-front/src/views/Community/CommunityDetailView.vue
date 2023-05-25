<template>
  <div class="communitydetail">
    <p>제목 : {{ community.title }}</p>
    <p>내용 : {{ community.content }}</p>
    <p @click.self.prevent="movieOtherProfile()" class="namep"> 작성자 : {{ community.username }}</p>
    <hr />
    <button @click.self.prevent="communityUpdate()" class="comebtn">수정하기</button>
    <button @click.self.prevent="communityDelete()" class="comebtn">삭제하기</button>

    <router-link :to="{name : 'CommunityView'}" class="comebtn">뒤로가기</router-link>
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
            this.$router.push({ name: "CommunityView" });
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
            this.$router.push({name: 'OtherProfileView', params: {username : res.data.username}})
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
.communitydetail {
  margin-top: 100px ;
}

.namep {
  cursor: pointer;
}
a {
  text-decoration: none;
  font-family: 'Lato', sans-serif;
  font-size: 14px;
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
  font-family: 'Lato', sans-serif;
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
   box-shadow:
   -7px -7px 20px 0px #fff9,
   -4px -4px 5px 0px #fff9,
   7px 7px 20px 0px #0002,
   4px 4px 5px 0px #0001;
}
.comebtn:before,
.comebtn:after{
  content:'';
  position:absolute;
  top:0;
  right:0;
  height:2px;
  width:0;
  background: #000;
  transition:400ms ease all;
}
.comebtn:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
}
.comebtn:hover:before,
.comebtn:hover:after{
  width:100%;
  transition:800ms ease all;
}


</style>