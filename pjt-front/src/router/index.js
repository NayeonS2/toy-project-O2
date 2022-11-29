import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CartView from '../views/CartView.vue'
import LogInView from '../views/LogInView.vue'
import SearchView from '../views/SearchView.vue'
import SignUpView from '../views/SignUpView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/cart/',
    name: 'CartView',
    component: CartView
  },
  {
    path: '/login/',
    name: 'LoginView',
    component: LogInView
  },
  {
    path: '/search/',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/signup/',
    name: 'SignUpView',
    component: SignUpView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
