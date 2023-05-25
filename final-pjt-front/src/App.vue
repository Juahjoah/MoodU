<template>
  <div id="app">
    <nav class="main_nav">
      <section class="nlogin" v-if="!$store.state.user">
        <div class="boundary1">
          <router-link :to="{ name: 'MovieView' }">
            <img
              class="logoimg"
              src="./assets/logo_black_width.png"
              alt="moodU_logo"
            />
          </router-link>
          <router-link :to="{ name: 'MovieView' }">Movie</router-link>
          <router-link :to="{ name: 'CommunityView' }">Community</router-link>
        </div>
        <div class="boundary2">
          <router-link :to="{ name: 'SignupView' }">Sign up</router-link>
          <router-link :to="{ name: 'LoginView' }">Login</router-link>
        </div>
      </section>
      <section class="ylogin" v-else>
        <div class="boundary1">
          <router-link :to="{ name: 'MovieView' }">
            <img
            class="logoimg"
            src="./assets/logo_black_width.png"
            alt="moodU_logo"
            />
          </router-link>
          <router-link to="/">Movie</router-link>
          <router-link :to="{ name: 'CommunityView' }">Community</router-link>
        </div>
        <div class="boundary2">
          <a @click="logout">logout</a>
          <router-link
            :to="{
              name: 'ProfileView',
              params: { username: $store.state.user },
            }"
            @click="profile">my profile</router-link
          >
        </div>
      </section>
      <hr />
      
      <!-- <header>
        <div class="hidiv" v-if="!$store.state.user">
          <h6 align="right">오늘도 모듀와 함께 행복해요.</h6>
        </div>
        <div class="hidiv" v-else>
          <h6 align="right" class="navp">
            {{ $store.state.user }}님! 오늘도 반가워요!
          </h6>
        </div>
      </header> -->
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchMovie: null,
    };
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
    },
    profile() {
      this.$store.dispatch('profile')
    }
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR&display=swap');
</style>
<style>
html, body, div, span, applet, object, iframe, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}

@font-face {
    font-family: 'TheJamsil5Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302_01@1.0/TheJamsil5Bold.woff2') format('woff2');
    font-weight: 700;
    font-style: normal;
}

#app {
  font-family: 'TheJamsil5Bold';
  font-size: 20px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 1rem;
  height: 1.5rem;

}

nav section {
  display: flex;
  justify-content: space-between;
  font-size: 20px;
  align-items: end;
}

.boundary1 {
  width: 30rem;
  display: flex;
  justify-content: space-evenly;
  align-items: end;
}
.boundary2 {
  width: 15rem;
  display: flex;
  justify-content: space-evenly;
}

nav a {
  font-weight: bold;
  color: hsl(213, 5%, 37%);
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: black;
}

.logoimg {
  width: 9rem;
  height: auto;
  margin-right: 1rem;
}

header {
  padding-top: 1.0rem;
  padding-right: 1rem;
  height: 2rem;
  /* background-color: #ebe8e1 ; */
}

.hidiv {
  height: 3rem;
}

</style>
