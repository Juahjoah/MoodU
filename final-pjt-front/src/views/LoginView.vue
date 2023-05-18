<template>
  <div class="login">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <label for="username">ID: </label>
      <input type="text" id="username" v-model="username" />
      <br />
      <label for="password">PW: </label>
      <input type="password" id="password" v-model="password" />
      <br />

      <input type="submit" value="logIn" />
    </form>
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
</style>