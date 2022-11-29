<template>
  <div id="app">
    <NavigationBar/>


    <router-view/>
  </div>
</template>

<script>
import NavigationBar from '@/components/Nav/NavigationBar'
export default {
  name: 'AppView',
  components: {
    NavigationBar,
  },
}
</script>

<style>
  @import "./assets/css/style.css";
  @import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css");
  @import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSansNeo.css);
</style>