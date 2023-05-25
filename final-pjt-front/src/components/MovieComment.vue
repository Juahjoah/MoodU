<template>
  <div>
    <section class="user_comment">
      <hr />
      <h3 class="displaytext">여러분은 영화를 어떻게 보셨나요?</h3>
      <h2>의견을 자유롭게 남겨주세요!</h2>
      <form @submit.prevent="createComment">
        <input class="commentinput" type="text" v-model.trim="comment" />
        <button @click.self.prevent="createComment">입력</button>
      </form>
    </section>
    <div v-for="con in contentList" :key="con.id">
      <div class="rgyPostIt">
        <span class="commentpost"
          >{{ con.content }} 📃 작성자 {{ con.username }}
        </span>
        <button
          @click="commentDelete(con.id)"
          v-if="con.username === $store.state.user"
        >
          X
        </button>
      </div>
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
        alert("댓글을 쓰고 제출을 해주세요!");
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
.commentinput {
  border-left-width: 0;
  border-right-width: 0;
  border-top-width: 0;
  border-bottom-width: 1;
  width: 70%;
  height: 1.5rem;
  margin: 5px auto;
  font-size: 20px;
  letter-spacing: 3px;
  padding-right: 2rem;
}
.commentinput:focus {
  outline: none;
}

div.rgyPostIt {
  width: 90%;
  position: relative;
  display: inline-block;
  padding: 20px 45px 20px 15px;
  margin: 5px 0;
  border: 1px solid #f8f861;
  border-left: 30px solid #f8f861;
  border-bottom-right-radius: 60px 10pxz;
  /* font-family: "Nanum Pen Script"; */
  font-size: 20px;
  color: #555;
  word-break: break-all;
  background: #ffff88; /* Old browsers */
  background: -moz-linear-gradient(
    -45deg,
    #ffff88 81%,
    #ffff88 82%,
    #ffff88 82%,
    #ffffc6 100%
  ); /* FF3.6+ */
  background: -webkit-gradient(
    linear,
    left top,
    right bottom,
    color-stop(81%, #ffff88),
    color-stop(82%, #ffff88),
    color-stop(82%, #ffff88),
    color-stop(100%, #ffffc6)
  ); /* Chrome,Safari4+ */
  background: -webkit-linear-gradient(
    -45deg,
    #ffff88 81%,
    #ffff88 82%,
    #ffff88 82%,
    #ffffc6 100%
  ); /* Chrome10+,Safari5.1+ */
  background: -o-linear-gradient(
    -45deg,
    #ffff88 81%,
    #ffff88 82%,
    #ffff88 82%,
    #ffffc6 100%
  ); /* Opera 11.10+ */
  background: -ms-linear-gradient(
    -45deg,
    #ffff88 81%,
    #ffff88 82%,
    #ffff88 82%,
    #ffffc6 100%
  ); /* IE10+ */
  background: linear-gradient(
    135deg,
    #ffff88 81%,
    #ffff88 82%,
    #ffff88 82%,
    #ffffc6 100%
  ); /* W3C */
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffff88', endColorstr='#ffffc6', GradientType=1); /* IE6-9 fallback on horizontal gradient */
  transition: all 0.2s;
  -webkit-transition: all 0.2s;
}

div.rgyPostIt::after {
  content: " ";
  position: absolute;
  z-index: -1;
  right: 0;
  bottom: 35px;
  width: 150px;
  height: 30px;
  background-color: rgba(0, 0, 0, 0);
  box-shadow: 2px 35px 5px rgba(0, 0, 0, 0.4);
  -webkit-box-shadow: 2px 35px 5px rgba(0, 0, 0, 0.4);
  transform: matrix(-1, -0.1, 0, 1, 0, 0);
  -webkit-transform: matrix(-1, -0.1, 0, 1, 0, 0);
  -moz-transform: matrix(-1, -0.1, 0, 1, 0, 0);
  -ms-transform: matrix(-1, -0.1, 0, 1, 0, 0);
  -o-transform: matrix(-1, -0.1, 0, 1, 0, 0);
  transition: all 0.2s;
  -webkit-transition: all 0.2s;
}

div.rgyPostIt:hover {
  border-bottom-right-radius: 75px 30px;
}

div.rgyPostIt:hover::after {
  box-shadow: 2px 37px 7px rgba(0, 0, 0, 0.37);
  -webkit-box-shadow: 2px 37px 7px rgba(0, 0, 0, 0.37);
}

div.rgyPostIt > p {
  padding: 5px 0 !important;
}

div.rgyPostIt > p::before {
  content: "\f198";
  margin-right: 7px;
  font-family: "FontAwesome";
  font-weight: normal;
  font-size: 20px;
  vertical-align: middle;
}

div.rgyPostIt > p > a {
  color: #555;
}
</style>