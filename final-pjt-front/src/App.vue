<template>
  <div id="app">
    <nav class="main_nav">
      <section class="nlogin" v-if="!$store.state.user">
        <div class="boundary1">
          <router-link :to="{ name: 'Movie'}">Movie</router-link>
          <router-link :to="{ name: 'Community' }">Community</router-link>
        </div>
        <router-link :to="{ name: 'Movie'}">
          <img class="logoimg" src="./assets/logo_black_width.png" alt="moodU_logo" />
        </router-link>
        <div class="boundary2">
          <router-link :to="{ name: 'SignupView' }">Sign up page</router-link>
          <router-link :to="{ name: 'LoginView' }">Login page</router-link>
        </div>
      </section>
      <section class="ylogin" v-else>
        <div class="boundary1">
          <router-link to="/">Movie</router-link>
          <router-link :to="{ name: 'Community' }">Community</router-link>
        </div>
        <router-link :to="{ name: 'Movie'}">
          <img class="logoimg" src="./assets/logo_black_width.png" alt="moodU_logo" />
        </router-link>
        <div class="boundary2">
          <a @click="logout">logout</a>
          <router-link :to="{ name: 'ProfileView' , params:{username: $store.state.user}}">my profile</router-link>
        </div>
      </section>
      <hr />
      <div class="hidiv" v-if="!$store.state.user">
        <p align="right">오늘도 모듀와 함께 행복해요.</p>
      </div>
      <div v-else>
        <p align="right" class="navp">
          {{ $store.state.user }}님! 오늘도 반가워요!
        </p>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$store.dispatch("logout");
    },
    
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
</style>
<style>
#app {
  font-family: "Jua", sans-serif;
  font-size: 15px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 50px;
  height: 3rem;
}

nav section {
  display: flex;
  justify-content: space-around;
  align-items: end;
  font-size: 20px;

  /* text-align: justify, :after; */
}
.hidiv {
  height: 10rem;
}

.navp {
  height: 0.5rem;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #e6d3ed;
}

/* background-color: lemonchiffon; */
.main_nav {
  height: 5rem;
  /* display: flex;
  flex-direction: column-reverse; */
}

.logoimg {
  width: 14rem;
  margin: 0px auto;
}

.boundary1 {
  width: 20rem;
  display: flex;
  justify-content: space-evenly;
  padding: 10px;
}
.boundary2 {
  width: 20rem;
  display: flex;
  justify-content: space-evenly;
  padding: 10px;
}





</style>
