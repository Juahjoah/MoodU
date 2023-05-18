import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/MovieView.vue'
import CommunityView from '../views/CommunityView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Movie',
    component: MovieView
  },
  {
    path: '/community',
    name: 'Community',
    component: CommunityView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
