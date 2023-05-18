import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
// import router from '../router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    signup(context, payload) {
      const userid = payload.userid
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          userid, password1, password2
        }
      })
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
    }


  },
  modules: {
  }
})
