<template>
  <div class="community">
    <h1>여러분의 생각을 들려주세요.</h1>
    <article>
      <CommunityListForm :communities="communities" />
    </article>
    <br />
    <hr />
    <router-link class="createbtn" :to="{ name: 'CommunityCreate' }">CREATE</router-link>
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

<style scoped>
.community {
  margin: 100px auto 0;
}
a {
  text-decoration: none;
}



.createbtn {
  margin: 20px;
  outline: none;
}
.createbtn {
  width: 100px;
  height: 40px;
  padding: 10px 25px;
  border: 2px solid #000;
  font-family: 'Lato', sans-serif;
  font-weight: 450;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
}
.createbtn {
  background: #000;
  color: #fff;
  line-height: 42px;
  padding: 0;
  border: none;
}
.createbtn:hover {
  background: transparent;
  color: #000;
   box-shadow:
   -7px -7px 20px 0px #fff9,
   -4px -4px 5px 0px #fff9,
   7px 7px 20px 0px #0002,
   4px 4px 5px 0px #0001;
}
.createbtn:before,
.createbtn:after{
  content:'';
  position:absolute;
  top:0;
  right:0;
  height:2px;
  width:0;
  background: #000;
  transition:400ms ease all;
}
.createbtn:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
}
.createbtn:hover:before,
.createbtn:hover:after{
  width:100%;
  transition:800ms ease all;
}

</style>