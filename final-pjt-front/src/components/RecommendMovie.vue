<template>
  <div>
    <p>제목 : {{movie.title}}</p>
    <img :src="getPoster" />
    장르 : <span v-for="genre in movie.genres" :key="genre.id">{{genre.name}},</span>
  </div>
</template>

<script>


export default {
    props: {
        movie: Object
    },

    computed: {
        getPoster() {
          return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`;
        },
    },
}
</script>

<style>
img {
    width: 100px;
}
</style>