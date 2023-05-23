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
          <input class="login_btn loginbbtn" type="submit" value="logIn" />
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
  font-family: "Gamja Flower", cursive;
  /* background-color: floralwhite; */
  margin: 0px auto;
  width: 30rem;
  height: 20rem;
}

.logininfo {
  width: 27rem;
  margin: 0px auto;
}

form {
  display: inline-block;
  text-align: right;
}

.logininput {
  font-family: "Gamja Flower", cursive;
  width: 16rem;
  height: 1.8rem;
  margin: 5px auto;
  border-radius: 5px;
  font-size: 20px;
  letter-spacing: 2px;
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
    #6e6bd7 100%
  );
}
</style>