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
  getters: {
    isLogin(state) {
      // 로그인 상태를 확인해서 작업 가능 권한 부여
      return state.token ? true : false
    },
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
      console.log(state.movies)
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'MovieView.vue' })
    },
    USER(state, username) {
      state.user = username
      console.log(state.user)
    },
    LOGOUT(state){
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
          // console.log(response, context)
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

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then(() => {
        // console.log(response)
        alert('회원가입 성공')
        router.push({name: 'LoginView'})

      })
      .catch((error) => {
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
          localStorage.setItem("jwt", response.data.accessToken)
          context.commit("USER", username)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    logout(context) {
      console.log(context)
      
      if (this.state.user) {
        localStorage.removeItem('jwt')
        context.commit("LOGOUT")
      }
      
    }
  },
  modules: {
  }
})
