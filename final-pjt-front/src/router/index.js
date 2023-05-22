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
    path: '/community/:id/update',
    name: 'CommunityUpdate',
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
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
