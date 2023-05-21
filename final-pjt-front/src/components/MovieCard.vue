<template>
  <div class="card">
    <div class="each-movie-card">
      <router-link :to="{ name: 'MovieDetail', params: { id: movie.id } }">
        <img class="card-img-top" :src="getPoster" alt="Poster image" />
          <p> {{movie.title}}</p>
        </router-link>
    </div>
  </div>
</template>

<script>

export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
  components:{
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
  margin: 20px;
}
.card img {
  width: 13rem;
  height: auto;
  overflow-x: hidden;
}

</style>
