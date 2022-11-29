import router from '@/router'
import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
    // 회원가입 && 로그인
    SAVE_TOKEN(state, data) {
      state.username = data.username
      state.token = data.token
      router.push({ name: 'HomeView' })
    },
  },
  actions: {
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/api/rest-auth/registration/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
      .then((res) => {
        // console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(err => console.log(err))
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/api/rest-auth/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
      .then((res) => {
        const data = { token: res.data.key, username: payload.username }
        context.commit('SAVE_TOKEN', data)
      })
      .catch(() => {
        alert('일치하지 않는 회원 정보입니다.')
      })
    },
  },
  modules: {
  }
})
