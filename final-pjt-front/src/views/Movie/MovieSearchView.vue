<template>
  <div>
    <div v-for="(movie, index) in searchMovieList" :key="index">
        <p>{{movie.title}}</p>
        <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            movieTitle : this.$route.params.movieTitle,
            searchMovieList: [],
        }
    },
    methods: {
        getSearchMovie() {
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/movies/search/${this.movieTitle}`
            })
            .then((res)=> {
                console.log(res.data.find_movie)
                this.searchMovieList = res.data.find_movie
            })
            .catch((err)=> {
                console.log(err)
            })
        }
    },
    created() {
        this.getSearchMovie()
    },
}
</script>

<style>
img {
    width: 100px;
    height: 100px;
}
</style>