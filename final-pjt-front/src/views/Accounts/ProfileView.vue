<template>
  <div>
    <div v-if="this.$store.state.user === this.$route.params.username">
      <h1>나의 프로필</h1>
        <p>
          아이디 : {{userData.username}}
        </p>
        <p>
          이메일 : {{userData.email}}
        </p>
        <p>
          팔로잉 : {{userData.followings.length}}
        </p>
        <li v-for="(following, index) in userData.followings" :key="index">
          {{following.username}}
        </li>
        <p>
          팔로워 : {{userData.followers.length}}
        </p>
        <li v-for="(follower, index) in userData.followers" :key="index">
          {{follower.username}}
        </li>
        <p>
          내가 좋아요 한 영화 개수 : {{userData.like_movies.length}}
        </p>
        <li v-for="(like, index) in userData.like_movies" :key="index">
          {{like.title}}
        </li>
    </div>
    <div v-else>
        <h1>{{userData.username}}님의 프로필</h1>
        <p>
          아이디 : {{userData.username}}
        </p>
        <p>
          이메일 : {{userData.email}}
        </p>
        <p>
          팔로잉 : {{userData.followings.length}}
        </p>
        <li v-for="(following, index) in userData.followings" :key="index">
          {{following.username}}
        </li>
        <p>
          팔로워 : {{userData.followers.length}}
        </p>
        <li v-for="(follower, index) in userData.followers" :key="index">
          {{follower.username}}
        </li>
        <p>
          {{userData.username}}님이 좋아요 한 영화 개수 : {{userData.like_movies.length}}
        </p>
        <li v-for="(like, index) in userData.like_movies" :key="index">
          {{like.title}}
        </li>

        <button @click="followingUser()">
          팔로잉하기
        </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
const token = localStorage.getItem('jwt')

export default {
  name: "ProfileView",
  data() {
    return {
      userData: [],
    }
  },
  methods: {
    getUserData() {
      const user = this.$route.params.username
      axios({
        method: 'post',
        url: `${API_URL}/accounts/profile/${user}/`,
        headers: {
          Authorization: `Bearer ${token}`,
        }
      })
      .then((res)=> {
        console.log(res.data)
        this.userData = res.data
      })
      .catch((err)=> {
        console.log(err)
      })
    },
    followingUser() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/${this.userData.id}/follow/`,
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      .then((res)=> {
        console.log(res)
        this.getUserData()
      })
    }
  },
  created() {
    this.$route.params.username
    this.getUserData()
  }
};
</script>

<style>
</style>