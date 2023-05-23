<template>
  <div class="login">
    <h1>오늘도 모듀와 함께해요!</h1>
    <div class="loginbox">
      <form @submit.prevent="login">
        <label for="username"
          >ID:
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

        <input class="login_btn btn-4" type="submit" value="logIn" />
      </form>
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
<style>
label {
  margin: 4px;
}

.loginbox {
  font-family: "Gamja Flower", cursive;
}

.logininput {
  font-family: "Gamja Flower", cursive;
  width: 16rem;
  height: 2.3rem;
  margin: 0px auto;
  border-radius: 5px;
  font-size: 20px;
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

.btn-4 {
  background-image: linear-gradient(
    to right,
    #72a8ff 0%,
    #c7e9f8 51%,
    #004ac0 100%
  );
}
</style>