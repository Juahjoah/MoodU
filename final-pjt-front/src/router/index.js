import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/Movie/MovieView.vue'
import CommunityView from '../views/Community/CommunityView.vue'
import SignupView from '../views/Accounts/SignupView.vue'
import LoginView from '../views/Accounts/LoginView.vue'
import MovieDetailView from '../views/Movie/MovieDetailView.vue'
import CommunityCreateView from '../views/Community/CommunityCreateView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Movie',
    component: MovieView
  },
  {
    path: '/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/community',
    name: 'Community',
    component: CommunityView
  },
  {
    path: '/community/create',
    name: 'CommunityCreate',
    component: CommunityCreateView
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
