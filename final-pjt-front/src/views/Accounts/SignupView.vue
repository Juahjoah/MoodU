<template>
  <div class="signup">
    <div class="signupbox">
      <h1>Welcome to MoodU!</h1>
      <h5>모듀에서 사용할 정보를 입력해주세요!</h5>
      <div class="signupinfo">
        <form @submit.prevent="signup">
          <br />
          <label class="id" for="username"> ID </label> :
          <input
            class="signupinput"
            type="text"
            id="username"
            placeholder="Enter ID"
            v-model="username"
          />
          <!-- <button @click.self.prevent="checkid()">중복 확인</button> -->
          <br />

          <label class="pw" for="password1"> PW </label> :
          <input
            class="signupinput"
            type="password"
            id="password1"
            placeholder="Enter password"
            v-model="password1"
          />
          <br />

          <label class="pw2" for="password2">PW check </label> :
          <input
            class="signupinput"
            type="password"
            id="password2"
            placeholder="Enter password one more time"
            v-model="password2"
          />
          <br />

          <label class="email" for="email"> E-mail </label> :
          <input
            class="signupinput"
            type="email"
            id="email"
            placeholder="Enter E-mail"
            v-model.trim="email"
          />
          <br />

          <label class="name" for="last_name">NAME </label> :
          <input
            class="signupinput"
            type="text"
            id="last_name"
            placeholder="Enter Your name"
            v-model="last_name"
          />
          <input class="signup_btn signupbbtn" type="submit" value="Signup" />
        </form>
      </div>
      <br />
    </div>
  </div>
</template>


<script>
export default {
  name: "SignupView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      last_name: null,
      email: null,
    };
  },
  methods: {
    signup() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;
      const last_name = this.last_name;
      const email = this.email;

      const payload = {
        username,
        password1,
        password2,
        last_name,
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

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Gamja+Flower&family=Pangolin&display=swap");
</style>
<style>
/* @font-face {
  font-family: "Pangolin";
  src: url("https://fonts.googleapis.com/css2?family=Hi+Melody&display=swap");
  unicode-range: U+0041-005A, U+0061-007A;
} */

label {
  margin: 15px;
}

.signupbox {
  font-family: "Gamja Flower", cursive;
  width: 37rem;
  height: 40rem;
  margin: 0px auto;
  /* background-color: #f8eded; */
  border-radius: 5px;
}

.signupinfo {
  width: 35rem;
  display: inline-block;
  text-align: right;
}

.signupinput {
  /* width: 12rem; */
  font-family: "Gamja Flower", cursive;
  width: 80%;
  height: 2rem;
  border-radius: 5px;
  font-size: 20px;
  letter-spacing: 2px;
}

.signup_btn {
  font-family: "Pangolin", cursive;
  flex: 1 1 auto;
  margin: 10px;
  padding: 7px;
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

.signupbbtn {
  background-image: linear-gradient(
    to right,
    #b2b0eb 0%,
    #fefefe 51%,
    #6e6bd7 100%
  );
}

.id {
  letter-spacing: 10px;
  display: inline-block;
  text-align: right;
}
.pw {
  letter-spacing: 10px;
  display: inline-block;
  text-align: right;
}
.email {
  letter-spacing: 4px;
  display: inline-block;
  text-align: right;
}
.name {
  letter-spacing: 8px;
  display: inline-block;
  text-align: right;
}
</style>