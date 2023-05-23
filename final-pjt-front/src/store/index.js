import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [
    ],
    user: null,
  },

  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
      console.log(state.movies)
    },
    USER(state, username) {
      state.user = username
      console.log(state.user)
    },
    LOGOUT(state) {
      state.user = null
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
        .then((response) => {
          console.log(response)
          context.commit('GET_MOVIES', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    signup(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      const last_name = payload.last_name
      const email = payload.email

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2, last_name, email
        }
      })
        .then(() => {
          // console.log(response)
          alert('MoodU와 함께 오늘의 한 페이지를 남겨봐요!')
          router.push({ name: 'LoginView' })

        })
        .catch((error) => {
          if (error.response.status === 400) {
            alert('중복 ID 입니다. ID를 변경해주세요.')
          }
          console.log(error)
        })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((response) => {
          // console.log(response)
          console.log(response.data.user.username)
          localStorage.setItem("jwt", response.data.token.accessToken)
          context.commit("USER", username)
          router.push({ name: 'Movie' })
        })
        .catch((error) => {
          // if (error.response.status === 401) {
          //   alert('확인되지 않은 사용자입니다. 다시 한 번 확인해주세요!')
          // }
          console.log(error)
        })
    },
    logout(context) {
      console.log(context)
      const username = this.state.user

      if (username) {
        localStorage.removeItem('jwt')
        context.commit('LOGOUT')
        router.push({ name: 'Movie' }).catch(() => { });
      }
    }
  },
  modules: {
  }
})
