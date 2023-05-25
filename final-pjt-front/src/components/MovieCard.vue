<template>
  <div class="card">
    <div class="each-movie-card">
      <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
        <img class="card-img-top" :src="getPoster" alt="Poster image" />
        <div class="textarea">
          <h3>{{ movie.title }}</h3>
        </div>
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

  computed: {
    getPoster() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`;
    },
  },
};
</script>

<style scoped>
@font-face {
  font-family: "KimjungchulGothic-Bold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302_01@1.0/KimjungchulGothic-Bold.woff2")
    format("woff2");
  font-weight: 700;
  font-style: normal;
}

a {
  color: #2c3e50;
  text-decoration: none;
}

.card {
  font-family: "KimjungchulGothic-Bold";
  font-size: 15px;
  /* width: 12rem; */
  /* height: auto; */
  margin: 20px;
  position: relative;
}
.textarea {
  text-align: left;
}

.each-movie-card {
  width: 13rem;
  height: auto;
  /* background-color: beige;
  box-shadow: 1px 1px 1px 1px black; */
}

.card img {
  width: 13rem;
  height: 19.375rem;
  object-fit: fill;
  overflow-x: hidden;
  transition: all 0.2s ease-in;
}

.each-movie-card:hover {
  box-shadow: 5px 5px 5px 5px gray;
  transform: scale(1.2);
  /* content: attr(data-hover); */
  /* opacity: 1; */
}

/* .hovertext::before {
  position:absolute;
  content:attr(data-hover);
  width: 100%;
  height: 80%;
  display: block;
  background: rgba(144, 144, 144, 0.521);
  top: 0;
  left: 0;
  opacity: 0;
  display: none;
} */

.hovertext:hover {
  /* 템플릿의 html 요소 p태그로 만들기 부모 포지션/위치에 만들고 투명도를 줬다가 hover를 하면 투명도를 100% */
  z-index: 1;
}
</style>
