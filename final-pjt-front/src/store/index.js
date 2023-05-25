import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
import VueCarousel from 'vue-carousel'

Vue.use(Vuex)
Vue.use(VueCarousel)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [
    ],
    token: null,
    user: null,
  },

  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
      // console.log(state.movies)
    },
    USER(state, userData) {
      state.user = userData.username
      state.token = userData.token
      console.log(state.user)
    },
    LOGOUT(state) {
      state.user = null
      state.token = null
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
        .then((response) => {
          // console.log(response)
          context.commit('GET_MOVIES', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    signup(context, payload) {
      const username = payload.username
      const password = payload.password1
      const password1 = payload.password2
      // const last_name = payload.last_name
      const email = payload.email

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password, password1, email
        }
      })
        .then(() => {
          // console.log(response)
          alert('MoodU와 함께 오늘의 한 페이지를 남겨봐요!')
          router.push({ name: 'LoginView' })

        })
        .catch((err) => {
          if (err.response.status === 401) {
            alert('비밀번호가 달라요...')
          }
          else if (err.response.status === 405) {
            alert('비밀번호를 작성해 주세요!')
          }
          else if (err.response.status === 400) {
            alert('이미 존재하는 아이디예요...')
          }
          console.log(err)
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
          console.log(response.data.user)
          localStorage.setItem("jwt", response.data.token.accessToken)
          const userData = {
            username: username,
            token: response.data.token.accessToken
          }
          context.commit("USER", userData)

          router.go(0)
          router.push({ name: 'MovieView' })
        })
        .catch((error) => {
          console.log(error)
          if (error.response.status === 500) {
            alert('아이디가 없어요! 제대로 된 아이디를 입력하거나 회원가입 먼저 진행해 주세요 :)')
          } else if (error.response.status === 400) {
            alert('비밀번호가 틀렸어요. 다시 확인해주세요 :)')
          }
        })
    },
    logout(context) {
      console.log(context)
      const username = this.state.user

      if (username) {
        localStorage.removeItem('jwt')
        context.commit('LOGOUT')
        router.go(0)
        router.push({ name: 'MovieView' }).catch(() => { });
      } else {
        alert('이미 로그아웃된 상태예요!')
        router.push({ name: 'LoginView' })
      }
    },

  },
  modules: {
  }
})
