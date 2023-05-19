<template>
  <div id="app">
    <nav class="main_nav">
      <p>{{ $store.state.user }}</p>
      <div v-if="!$store.state.user">
        <router-link :to="{ name: 'SignupView' }">Sign up page</router-link> |
        <router-link :to="{ name: 'LoginView' }">Login page</router-link>
      </div>
      <div v-else>
        <a @click="logout">logout</a> |
        <router-link to="#">profile</router-link>
      </div>
      <router-link to="/">Movie</router-link> |
      <router-link :to="{ name: 'Community' }">Community</router-link> |
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
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.main_nav {
  /* background-color: lemonchiffon; */
  height: 3rem;
}
</style>
