<template>
  <div class="community">
    <br />
    <br />
    <br />
    <h1>여러분의 생각을 들려주세요.</h1>
    <article>
      <CommunityListForm :communities="communities" />
    </article>
    <br />
    <hr />
    <router-link :to="{ name: 'CommunityCreate' }">[CREATE]</router-link>
  </div>
</template>


<script>
import CommunityListForm from "@/components/CommunityListForm.vue";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";
export default {
  name: "CommunityView",
  components: {
    CommunityListForm,
  },
  data() {
    return {
      communities: [],
    };
  },
  methods: {
    setToken() {
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `Bearer ${token}`,
      };
      return config;
    },
    getCommunities() {
      axios({
        method: "get",
        url: `${API_URL}/community/`,
        headers: this.setToken(),
      })
        .then((response) => {
          console.log(response);
          this.communities = response.data;
        })
        .catch((error) => {
          confirm("로그인한 콩알님들만 볼 수 있어요😣!");
          this.$router.push({ name: "LoginView" });
          console.log(error);
        });
    },
  },
  created() {
    this.getCommunities();
  },
};
</script>

<style>
</style>