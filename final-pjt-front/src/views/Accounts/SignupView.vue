<template>
  <div class="signup">
    <h1>Welcome to MoodU!</h1>
    <h5>모듀에서 사용할 정보를 입력해주세요!</h5>
    <div class="signupbox">
      <form @submit.prevent="signup">
        <label for="username">
          <br />
          ID:
          <input
            class="signupinput"
            type="text"
            id="username"
            placeholder="Enter ID"
            v-model="username"
          />
        </label>
        <!-- <button @click.self.prevent="checkid()">중복 확인</button> -->
        <br />

        <label for="password1">
          PW:
          <input
            class="signupinput"
            type="password"
            id="password1"
            placeholder="Enter password"
            v-model="password1"
          />
        </label>
        <br />

        <label for="password2">
          PW check:
          <input
            class="signupinput"
            type="password"
            id="password2"
            placeholder="Enter password one more time"
            v-model="password2"
          />
        </label>
        <br />

        <label for="email">
          email:
          <input
            class="signupinput"
            type="email"
            id="email"
            placeholder="Enter email"
            v-model.trim="email"
          />
        </label>
        <br />

        <label for="lastname">
          이름:
          <input
            class="signupinput"
            type="text"
            id="lastname"
            placeholder="Enter Your name"
            v-model="lastname"
          />
        </label>
        <br />

        <input class="signup_btn btn-4" type="submit" value="Signup" />
      </form>
    </div>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Pangolin&display=swap");
</style>
<script>
export default {
  name: "SignupView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      lastname: null,
      email: null,
    };
  },
  methods: {
    signup() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;
      const lastname = this.lastname;
      const email = this.email;

      const payload = {
        username,
        password1,
        password2,
        lastname,
        email,
      };

      this.$store.dispatch("signup", payload);
    },
    // checkid() {
    //   const username = this.username;
    //   this.$store.dispatch("signup", username);
    // },
  },
};
</script>

<style>
.signupinput {
  /* width: 12rem; */
  font-family: "Pangolin", cursive;
  width: 70%;
  height: 2rem;
  border-radius: 5px;
}

label {
  margin: 4px;
}

.signupbox {
  width: 30rem;
  margin: 0px auto;
}

.signup_btn {
  font-family: "Pangolin", cursive;
  flex: 1 1 auto;
  margin: 10px;
  padding: 10px;
  text-align: center;
  text-transform: uppercase;
  transition: 0.5s;
  background-size: 200% auto;
  color: black;
  text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 20px #eee;
  border-radius: 5px;
}

.signup_btn:hover {
  background-position: right center; /* change the direction of the change here */
}

.btn-4 {
  background-image: linear-gradient(
    to right,
    #a1c4fd 0%,
    #c2e9fb 51%,
    #a1c4fd 100%
  );
}
</style>