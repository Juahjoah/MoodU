<template>
  <div class="profile">
    <div v-if="this.$store.state.user === this.$route.params.username">
      <h1>나의 프로필</h1>
      <div class="myinfo">
        <div class="basicinfo">
          <i class="bi bi-person-circle"></i>
          <div class="idemail">
            <p>아이디 : {{ userData.username }}</p>
            <p>이메일 : {{ userData.email }}</p>
          </div>
        </div>
        <div class="followbox">
          <p>팔로잉 {{ userData.followings.length }}명</p>
          <div
            class="followingsbox"
            v-for="(following, index) in userData.followings"
            :key="index"
          >
            <div class="followings">
              <i class="biuser bi-person-hearts"></i>
              {{ following.username }}
            </div>
          </div>
          <p>팔로워 {{ userData.followers.length }}명</p>
          <div
            class="followersbox"
            v-for="(follower, index) in userData.followers"
            :key="index"
          >
            <div class="followers">
              <i class="biuser bi-person-heart"></i>
              {{ follower.username }}
            </div>
          </div>
        </div>
        <div class="likemovie">
          <p>내가 좋아요 한 영화 개수 : {{ userData.like_movies.length }}</p>
          <section class="movielist">
            <ProfileMovie v-for="(like, index) in userData.like_movies" :key="index" :like="like" />
          </section>
          </div>
        </div>
      </div>
    
  <div v-else>
      <h1>{{ userData.username }}님의 프로필</h1>
      <div class="userinfo">
        <div class="basicinfo">
          <div class="userfollow">
            <i class="bi bi-person-circle"></i>
            <button
              type="button"
              class="followbtn"
              @click.self.prevent="followingUser()"
              data-text="팔로우"
            >
              {{ followMsg }}
            </button>
          </div>
          <div class="idemail">
            <p>아이디 : {{ userData.username }}</p>
            <p>이메일 : {{ userData.email }}</p>
          </div>
        </div>
        <div class="followbox">
          <p>팔로잉 {{ userData.followings.length }}명</p>

          <div
            class="followingsbox"
            v-for="(following, index) in userData.followings"
            :key="index"
          >
            <div class="followings">
              <i class="biuser bi-person-hearts"></i>
              {{ following.username }}
            </div>
          </div>
          <p>팔로워 {{ userData.followers.length }}명</p>
          <div
            class="followersbox"
            v-for="(follower, index) in userData.followers"
            :key="index"
          >
            <div class="followers">
              <i class="biuser bi-person-heart"></i>
              {{ follower.username }}
            </div>
          </div>
        </div>
        <div class="likemovie">
          <p> {{ userData.username }}님이 좋아요 한 영화
            {{ userData.like_movies.length }} 개 </p>
          <section class="movielist">
            <ProfileMovie v-for="(like, index) in userData.like_movies" :key="index" :like="like" />
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProfileMovie from "@/components/ProfileMovie.vue";

const API_URL = "http://127.0.0.1:8000";
const token = localStorage.getItem("jwt");

export default {
  name: "ProfileView",
  data() {
    return {
      userData: [],
      followMsg: null,
    };
  },
  components: {
    ProfileMovie
  },
  computed: {

  },
  methods: {
    getUserData() {
      const user = this.$route.params.username;
      axios({
        method: "post",
        url: `${API_URL}/accounts/profile/${user}/`,
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then((res) => {
          console.log(res.data);
          this.userData = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    followingUser() {
      axios({
        method: "post",
        url: `${API_URL}/accounts/${this.userData.id}/follow/`,
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then((res) => {
          console.log(res);
          if (res.data.is_followed) {
            this.followMsg = "팔로우 취소";
          } else {
            this.followMsg = "팔로우";
          }
          this.getUserData();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },

  created() {
    this.getUserData();
    this.followingUser();
  },
};
</script>

<style>
.profile {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 80rem;
} 


.myinfo {
  display: flex;
  flex-direction: column;
  width: 50rem;
  height: 80rem;
  margin: 0px auto;
}
.userinfo {
  display: flex;
  flex-direction: column;
  width: 50rem;
  height: 80rem;
  margin: 0px auto;
}
.userfollow {
  display: flex;
  flex-direction: column;
}
.followbtn {
  width: 15rem;
}
.followbtn::after {
  content: attr(data-text);
}

.basicinfo {
  display: flex;
  justify-content: center;
  align-items: center;
}
.bi {
  font-size: 15rem;
  margin-right: 10rem;
}

.followbox {
  text-align: left;
}
.followersbox {
  display: inline-block;
}
.followers {
  width: 7rem;
  display: flex;
  flex-direction: column;
  align-content: center;
  text-align: center;
}
.followingsbox {
  display: inline-block;
}
.followings {
  width: 7rem;
  display: flex;
  flex-direction: column;
  align-content: center;
  text-align: center;
}
.biuser {
  margin-top: 1rem;
  font-size: 3rem;
}

</style>