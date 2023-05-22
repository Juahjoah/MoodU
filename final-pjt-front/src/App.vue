<template>
  <div id="app">
    <nav class="main_nav">
      <section v-if="!$store.state.user">
        <router-link to="/">Movie</router-link> |
        <router-link :to="{ name: 'Community' }">Community</router-link> |
        <router-link :to="{ name: 'SignupView' }">Sign up page</router-link> |
        <router-link :to="{ name: 'LoginView' }">Login page</router-link>
      </section>
      <section v-else>
        <router-link to="/">Movie</router-link> |
        <router-link :to="{ name: 'Community' }">Community</router-link> |
        <a @click="logout">logout</a> |
        <router-link to="#">profile</router-link>
        <p class="navp">{{ $store.state.user }}님! 오늘도 반가워요!</p>
      </section>
    </nav>
    <hr />
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  height: 3rem;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

/* background-color: lemonchiffon; */
/* .main_nav {
  height: 3rem;
} */

/* .navp {
} */
</style>
