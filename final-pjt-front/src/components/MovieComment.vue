<template>
  <div>
    <section class="user_comment">
      <p class="displaytext">여러분은 영화를 어떻게 보셨나요?</p>
      <form>
        <input type="text" v-model.trim="comment" @keyup.enter="createComment">
        <button @click.self.prevent="createComment">!</button>
      </form>
    </section>
    <div>
      <p v-for="con in contentList" :key="con.id">{{con.content}}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
const token = localStorage.getItem('jwt')

export default {
  data() {
    return {
      contentList: [],
      comment: null,
    }
      
  },
  methods: {
    createComment() {
      const comment = this.comment
      if (!comment) {
        alert('댓글을 달고 엔터를 눌러라')
      }
      else {
        axios({
          method: 'post',
          url: `${API_URL}/movies/${this.$route.params.id}/comments/create/`,
          headers: {
            Authorization: `Bearer ${token}`,
          },
          data: {
            content : comment,
            contentList : [],
          }
        })
        .then((res)=> {
          console.log(res)
          this.getCommentList()
          this.comment = ''
        })
        .catch((err)=> {
          console.log(err)
        })
      }
    },
    getCommentList() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/comments/`
      })
      .then((res)=> {
        // console.log(res)
        this.contentList = res.data
        console.log(this.contentList)
        // this.$router.push({name: 'MovieDetailView'})
      })
    }

  },
  created() {
    this.getCommentList()
  }
}
</script>

<style>

</style>