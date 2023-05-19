<template>
  <div class="community">
    <h1>여러분의 생각을 들려주세요.</h1>
    <article>
      <p>article list가 들어올 예정</p>
      <!-- <CommunityListForm /> -->
      <p v-for="comment in comments" :key="comment.id">{{ comment }}</p>
    </article>
    <br />
    <hr />
    <router-link :to="{ name: 'CommunityCreate' }">[CREATE]</router-link>
  </div>
</template>

<script>
// import CommunityListForm from "@/components/CommunityListForm.vue";
import axios from "axios";

export default {
  name: "CommunityView",
  // components: {
  //   CommunityListForm,
  // },
  data() {
    return {
      comments: [],
    };
  },
  methods: {
    // createmove() {
    //   this.$router.push({ name: "CommunityCreate" });
    // },
    getComments() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/community/",
      })
        .then((response) => {
          console.log(response);
          this.comments = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getComments();
  },
};
</script>

<style>
</style>