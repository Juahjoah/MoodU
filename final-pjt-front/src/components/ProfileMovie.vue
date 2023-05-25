<template>
  <div class="card">
    <div class="each-movie-card">
      <router-link :to="{ name: 'MovieDetail', params: { id: like.id } }">
        <img class="card-img-top" :src="getPoster" alt="Poster image" />
        <p class="hovertext" data-hover="More information" />
        <p>{{ like.title }}</p>
      </router-link>
    </div>
  </div>
</template>
  
<script>
export default {
  name: "ProfileMovie",
  props: {
    like: Object,
  },

  computed: {
    getPoster() {
      return `https://image.tmdb.org/t/p/original/${this.like.poster_path}`;
    },
  },
};
</script>

<style scoped>
a {
  color: #42b983;
  text-decoration: none;
}

.card {
  width: 13rem;
  height: auto;
  margin: 20px;
  position: relative;
}
.card img {
  width: 13rem;
  height: 19.375rem;
  object-fit: fill;
  overflow-x: hidden;
  transition: all 0.2s ease-in;
}

.card-img-top:hover {
  box-shadow: 5px 5px 5px 5px gray;
  transform: scale(1.2);
}

.hovertext:hover {
  z-index: 1;
}
</style>
  