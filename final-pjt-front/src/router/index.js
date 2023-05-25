import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/Movie/MovieView.vue'
import CommunityView from '../views/Community/CommunityView.vue'
import SignupView from '../views/Accounts/SignupView.vue'
import LoginView from '../views/Accounts/LoginView.vue'
import MovieDetailView from '../views/Movie/MovieDetailView.vue'
import CommunityCreateView from '../views/Community/CommunityCreateView.vue'
import CommunityDetailView from '../views/Community/CommunityDetailView.vue'
import CommunityUpdateView from '../views/Community/CommunityUpdateView.vue'
import ProfileView from '../views/Accounts/ProfileView.vue'
import RecommendView from '@/views/Movie/RecommendView'
import MovieSearchView from '@/views/Movie/MovieSearchView'
import OtherProfileView from '@/views/Accounts/OtherProfileView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/community/create',
    name: 'CommunityCreateView',
    component: CommunityCreateView
  },
  {
    path: '/community/:id',
    name: 'CommunityDetailView',
    component: CommunityDetailView
  },
  {
    path: '/community/:id/update',
    name: 'CommunityUpdateView',
    component: CommunityUpdateView
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
    path: '/recommended',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: ProfileView,
  },
  {
    path: '/search/:movieTitle',
    name: 'MovieSearchView',
    component: MovieSearchView,
  },
  {
    path: '/profile/other/:username',
    name: 'OtherProfileView',
    component: OtherProfileView

  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
