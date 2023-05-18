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
    token: null,
  },
  getters: {
    isLogin(state) {
      // 로그인 상태를 확인해서 작업 가능 권한 부여
      return state.token ? true : false
    },
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'MovieView.vue' })
    }
  },
  actions: {
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
        .then((response) => {
          // console.log(response)
          context.commit('SAVE_TOKEN', response.data.key)
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
          context.commit('SAVE_TOKEN', response.data.key)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  modules: {
  }
})
