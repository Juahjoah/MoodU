<template>
  <div class="login">
    <div class="loginbox">
      <br />
      <h1>오늘도 모듀와 함께해요!</h1>
      <div class="logininfo">
        <form @submit.prevent="login">
          <label for="username"
            >I D:
            <input
              class="logininput"
              type="text"
              id="username"
              placeholder="Enter ID"
              v-model="username"
            />
          </label>
          <br />
          <label for="password"
            >PW:
            <input
              class="logininput"
              type="password"
              id="password"
              placeholder="Enter password"
              v-model="password"
            />
          </label>
          <br />
          <div id="loginbtncenter">
            <input class="login_btn loginbbtn" type="submit" value="logIn" />
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    login() {
      const username = this.username;
      const password = this.password;

      const payload = {
        username,
        password,
      };

      this.$store.dispatch("login", payload);
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Gamja+Flower&family=Pangolin&display=swap");
</style>
<style scoped>
.loginbox {
  font-family: 'TheJamsil5Bold';
  /* background-color: floralwhite; */
  margin: 100px auto 0;
  width: 30rem;
  height: 20rem;
}

.logininfo {
  width: 27rem;
  margin: 20px auto 0;
}

form {
  display: inline-block;
  text-align: right;
}

.logininput {
  border-style: dotted;
  border-left-width: 0;
  border-right-width: 0;
  border-top-width: 0;
  border-bottom-width: 1;
  font-family: "Pangolin", cursive;
  width: 16rem;
  height: 2.3rem;
  margin: 5px auto;
  font-size: 20px;
  letter-spacing: 2px;
}

.logininput:focus {
  outline: none;
}

.login_btn {
  font-family: "Pangolin", cursive;
  flex: 1 1 auto;
  margin: 10px;
  padding: 5px;
  text-align: center;
  text-transform: uppercase;
  transition: 0.5s;
  background-size: 200% auto;
  color: black;
  text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 20px #eee;
  border-radius: 5px;
}

.login_btn:hover {
  background-position: right center; /* change the direction of the change here */
}

.loginbbtn {
  background-image: linear-gradient(
    to right,
    #b2b0eb 0%,
    #fefefe 51%,
    #262630 100%
  );
}

#loginbtncenter {
  display: flex;
  text-align: center;
  width: 10rem;
  margin: 0px auto;
}
</style>