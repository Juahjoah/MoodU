<template>
  <div id="app">
    <nav class="main_nav">
      <section class="nlogin" v-if="!$store.state.user">
        <router-link to="/">Movie</router-link>
        <div>..................</div>
        <router-link :to="{ name: 'Community' }">Community</router-link>
        <img class="logoimg" src="./assets/MoodU.png" alt="moodU_logo" />
        <router-link :to="{ name: 'SignupView' }">Sign up page</router-link>
        <router-link :to="{ name: 'LoginView' }">Login page</router-link>
      </section>
      <section class="ylogin" v-else>
        <router-link to="/">Movie</router-link>
        <router-link :to="{ name: 'Community' }">Community</router-link>
        <img class="logoimg" src="./assets/MoodU.png" alt="moodU_logo" />
        <a @click="logout">logout</a>
        <router-link :to="{ name: 'ProfileView' }">my profile</router-link>
      </section>
      <hr />
      <div v-if="!$store.state.user">
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
/* reset.css */
/* html,
body,
div,
span,
object,
a,
img,
q,
s,
samp,
small,
strike,
strong,
sub,
sup,
tt,
var,
center,
fieldset,
form,
article,
footer,
header,
menu,
nav,
section {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
} */

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
  justify-content: space-between;
  align-items: end;
  font-size: 20px;

  /* text-align: justify, :after; */
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
  width: 8rem;
  margin: 0px auto;
}
</style>
