<template>
    <div class="profile">
      <h1>My profile</h1>
      {{userData.username}}의 프로필
      <div>
        <p>
          닉네임 : {{userData.last_name}}
        </p>
        <p>
        이메일 : {{userData.email}}

        </p>
        <p>
          팔로잉 : {{userData.followings}}
          팔로워 : {{userData.followers}}
        </p>
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
        const user = this.$store.state.user
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
      }
    },
    created() {
      this.getUserData()
    }
  };
  </script>
  
  <style>
  </style>