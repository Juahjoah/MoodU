<template>
  <div>
    <section class="user_comment">
      <h3 class="displaytext">여러분은 영화를 어떻게 보셨나요?</h3>
      <form @submit.prevent="createComment">
        <input type="text" v-model.trim="comment" />
        <button @click.self.prevent="createComment">+</button>
      </form>
    </section>

    <div v-for="con in contentList" :key="con.id">
      <span>{{ con.content }} | 작성자 {{ con.username }} </span>
      <button
        @click="commentDelete(con.id)"
        v-if="con.username === $store.state.user"
      >
        X
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
const token = localStorage.getItem("jwt");

export default {
  data() {
    return {
      contentList: [],
      comment: null,
    };
  },

  methods: {
    // 댓글 생성
    createComment() {
      const comment = this.comment;

      if (comment) {
        axios({
          method: "post",
          url: `${API_URL}/movies/${this.$route.params.id}/comments/create/`,
          headers: {
            Authorization: `Bearer ${token}`,
          },
          data: {
            content: comment,
            contentList: [],
          },
        })
          .then(() => {
            // console.log(res);
            this.getCommentList();
            this.comment = "";
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        alert("댓글을 쓰고 제출을 해주겠어? ^^");
      }
    },

    // 댓글 리스트 조회
    getCommentList() {
      axios({
        method: "get",
        url: `${API_URL}/movies/${this.$route.params.id}/comments/`,
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then((res) => {
          // console.log(res)
          this.contentList = res.data;
          // console.log(this.contentList);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // 댓글 삭제
    commentDelete(comment_id) {
      axios({
        method: "delete",
        url: `${API_URL}/movies/${this.$route.params.id}/comments/${comment_id}/`,
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then(() => {
          // console.log(res)
          this.getCommentList();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },

  created() {
    this.getCommentList();
  },
};
</script>

<style>
</style>