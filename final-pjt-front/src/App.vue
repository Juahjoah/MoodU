<template>
  <div id="app">
    <nav>
      <router-link to="/">Movie</router-link> |
      <router-link to="/community">Community</router-link> |
      <router-link :to="{ name: 'SignupView' }">Sign up page</router-link> |
      <router-link :to="{ name: 'LoginView' }">Login page</router-link>
    </nav>
    <router-view />
  </div>
</template>

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
</style>
