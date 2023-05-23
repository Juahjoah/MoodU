import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/Movie/MovieView.vue'
import CommunityView from '../views/Community/CommunityView.vue'
import SignupView from '../views/Accounts/SignupView.vue'
import LoginView from '../views/Accounts/LoginView.vue'
import MovieDetailView from '../views/Movie/MovieDetailView.vue'
import CommunityCreateView from '../views/Community/CommunityCreateView'
import CommunityDetailView from '../views/Community/CommunityDetailView'
import RecommendView from '@/views/Movie/RecommendView'
import RecommendMovie from '@/components/RecommendMovie'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Movie',
    component: MovieView
  },
  {
    path: '/:id',
    name: 'MovieDetail',
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
    path: '/community/:id',
    name: 'CommunityDetail',
    component: CommunityDetailView
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
  },
  {
    path: 'recommended/:emtion',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: 'recommendMovie/',
    name: 'RecommendMovie',
    component: RecommendMovie
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
