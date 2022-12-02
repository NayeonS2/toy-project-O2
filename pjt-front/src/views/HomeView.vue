<template>
  <div id="home-view">
    <h2>home</h2>
    <router-link :to="{ name: 'SignUpView' }">Signup</router-link><br>
    <router-link :to="{ name: 'LoginView' }">Login</router-link>
    <HomeCarousel/>
    <h2>home</h2>
  </div>
</template>

<script>
import HomeCarousel from '@/components/Home/HomeCarousel'
export default {
  name: 'HomeView',
  components: {
    HomeCarousel,
  },

}
</script>

<style>


</style>