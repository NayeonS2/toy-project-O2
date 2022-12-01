<template>
  <div id="home-carousel">
    <div class="carousel-window">
      <div class="carousel-box">
        <HomeCarouselItem
        v-for="item in popularItems"
        :key="item.title"
        :item = item
        class="content"
        />
      </div>
      <div class="carousel-btn">
        <div class="prev" @click="GetPrevContent"><i class="bi bi-chevron-left"></i></div>
        <div class="next" @click="GetNextContent"><i class="bi bi-chevron-right"></i></div>
      </div>
      <div class="carousel-flag">
        <div class="flag"></div>
        <div class="flag"></div>
        <div class="flag"></div>
        <div class="flag"></div>
      </div>
    </div>
  </div>
</template>

<script>
import HomeCarouselItem from '@/components/Home/HomeCarouselItem'
export default {
  components: {
    HomeCarouselItem,
  },
  data() {
    return {
      popularItems: [
        { title:'4번입니다', content: '4번 컨텐츠입니다' },
        { title:'3번입니다', content: '3번 컨텐츠입니다' },
        { title:'2번입니다', content: '2번 컨텐츠입니다' },
        { title:'1번입니다', content: '1번 컨텐츠입니다' },
      ]
    }
  },
  methods: {
    GetPrevContent() {
      const box = document.getElementById('home-carousel').querySelector('.carousel-box')
      const first = document.getElementById('home-carousel').querySelector('.carousel-box :nth-child(1)' )
      const now = document.getElementById('home-carousel').querySelector('.carousel-box :nth-child(4)' )
      box.appendChild(first)
      first.style.opacity = '0'
      setTimeout(()=>{
      first.style.transitionDuration = '1s'
      first.style.opacity = '1'
      now.style.opacity = '0'
      }, 30); 
    },
    GetNextContent() {
      const box = document.getElementById('home-carousel').querySelector('.carousel-box')
      const first = document.getElementById('home-carousel').querySelector('.carousel-box :nth-child(1)' )
      const now = document.getElementById('home-carousel').querySelector('.carousel-box :nth-child(4)' )
      const next = document.getElementById('home-carousel').querySelector('.carousel-box :nth-child(3)')
      next.style.opacity = '0'
      now.style.opacity = '1'
      box.insertBefore(now, first)
      setTimeout(()=>{
      next.style.transitionDuration = '1s'
      now.style.transitionDuration = '1s'
      next.style.opacity = '1'
      now.style.opacity = '0'
      }, 30); 
    },
  },
  computed: {},
}
</script>

<style>
  #home-carousel {}
  #home-carousel .carousel-window {
    position: relative;
    height: 440px;
    background-color: aquamarine;
  }
  #home-carousel .carousel-box {
    position: relative;
  }
  #home-carousel .carousel-box .content {
    position: absolute;
    height: 440px;
    width: 100%;
    font-weight: 900;
    font-size: 60px;
    text-align: center;
    background-color: aquamarine;
    transition-duration: 1s;
  }

  #home-carousel .carousel-box .content:not(:nth-child(4)) {
    opacity: 0;
  }

  #home-carousel .carousel-btn {
    position: absolute;
    bottom: 60px;
    left: 100px;
    display: flex;
    justify-content: space-between;
    width: 200px;
    border: 1px solid #000;
  }
  #home-carousel .carousel-btn > div {
    cursor: pointer;
  }
  #home-carousel .carousel-btn .prev {}
  #home-carousel .carousel-btn .next {}
  #home-carousel .carousel-flag {
    position: absolute;
  }
  #home-carousel .carousel-flag .flag {}
</style>