<template>
  <div>
    <h1>
    "{{newMovieTitle}}"로 찾은 영화들 !
    </h1>
    <input type="text" v-model="newMovieTitle" @keyup.enter="newFind()">
    <div v-if="noMovie">
        {{noMovie}}
    </div>
    <div v-else>

        <div v-for="(movie, index) in searchMovieList" :key="index">
            <p>{{movie.title}}</p>
            <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" />
        </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            newMovieTitle: null, // 화면에 보여질 (기준)
            movieTitle : this.$route.params.movieTitle, // 한번 params로 받는
            searchMovieList: [],
            noMovie: null,
            
        }
    },
    methods: {
        getSearchMovie() { // MovieView 컴포넌트에서 엔터를 하면 넘어오는 그 순간만 실행될 함수
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/movies/search/${this.movieTitle}`
            })
            .then((res)=> {
                console.log(res.data.find_movie)
                this.newMovieTitle = this.movieTitle 
                this.searchMovieList = res.data.find_movie
                this.noMovie = null
                
            })
            .catch((err)=> {
                console.log(err)
                if (err.response.status === 404) {
                    this.newMovieTitle = this.movieTitle
                    this.noMovie = '영화가 없어요'
                }
            })

        },
        newFind() { // 검색화면에서 계속해서 검색할 함수
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/movies/search/${this.newMovieTitle}`
            })
            .then((res)=> {
                console.log(res)
                this.searchMovieList = res.data.find_movie
                this.noMovie = null
            })
            .catch((err)=> {
                console.log(err)
                if (err.response.status === 404) {
                    this.noMovie = '영화가 없어요'
                }
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