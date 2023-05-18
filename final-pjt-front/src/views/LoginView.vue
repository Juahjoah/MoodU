<template>
  <div class="login">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <label for="userid">ID: </label>
      <input type="text" id="userid" v-model="userid" />
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
      userid: null,
      password: null,
    };
  },
  methods: {
    login() {
      const userid = this.userid;
      const password = this.password;

      const payload = {
        userid,
        password,
      };

      this.$store.dispatch("login", payload);
    },
  },
};
</script>

<style>
</style>