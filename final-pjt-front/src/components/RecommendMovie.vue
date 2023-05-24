<template>
  <div class="card">
    <div class="recommend-card">
      <router-link :to="{ name: 'MovieDetail', params: { id: movie.id } }">
        <img class="card-img-top" :src="getPoster" alt="Poster image" />
        <p>제목 : {{ movie.title }}</p>
        장르 :
        <span v-for="genre in movie.genres" :key="genre.id"
          >{{ genre.name }},</span
        >
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    movie: Object,
  },

  computed: {
    getPoster() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`;
    },
  },
};
</script>

<style>
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
  height: auto;
  overflow-x: hidden;
  transition: all 0.2s ease-in;
}

.card-img-top:hover {
  box-shadow: 5px 5px 5px 5px gray;
  transform: scale(1.2);
}

.hovertext:hover {
  /* 템플릿의 html 요소 p태그로 만들기 부모 포지션/위치에 만들고 투명도를 줬다가 hover를 하면 투명도를 100% */
  z-index: 1;
}
</style>