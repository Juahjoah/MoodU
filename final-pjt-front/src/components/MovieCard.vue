<template>
  <div class="card">
    <!-- <h1>MovieCard</h1> -->
    <div class="each-movie-card"
    data-glide-el="track"
    ref="slider"
    type="carousel"
    :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
    <!-- <div class="each-movie-card"
    type="carousel"
    perView="6"
    data-glide-el="track"
    ref="slider"
    :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
    > -->
      <router-link :to="{ name: 'MovieDetail', params: { id: movie.id } }">
        <img class="card-img-top" :src="getPoster" alt="Poster image" />
        <p>{{ movie.title }}</p>
        <p>{{ movie.overview }}</p>
        <!-- <vue-glide 
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="carousel"
        :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
      >
      <p>{{ movie.title }}</p> -->
        <!-- <vue-glide-slide
          v-for="(movie, idx) in movie"
          :key="idx">
          
        </vue-glide-slide> -->
      <!-- </vue-glide> -->
      </router-link>
    </div>
  </div>
</template>

<script>
import { Glide, GlideSlide } from 'vue-glide-js'

export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
  components:{
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide
  },
  computed: {
    getPoster() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`;
    },
  },
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.card {
  width: 13rem;
  height: auto;
}
.card img {
  width: 13rem;
  height: auto;
}


</style>
