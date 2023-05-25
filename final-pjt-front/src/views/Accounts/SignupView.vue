<template>
  <div class="signup">
    <div class="signupbox">
      <h1>Welcome to MoodU!</h1>
      <br>
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

          <!-- <label class="name" for="last_name">NAME </label> :
          <input
            class="signupinput"
            type="text"
            id="last_name"
            placeholder="Enter Your name"
            v-model="last_name"
          /> -->
          <div id="btncenter">
            <input class="signup_btn clickbtn signupbbtn" type="submit" value="Signup" />
          </div>
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
      // const last_name = this.last_name;
      const email = this.email;

      const payload = {
        username,
        password1,
        password2,
        // last_name,
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
<style scoped>

label {
  margin: 15px;
}

.signupbox {
  font-family: 'TheJamsil5Bold';
  /* background-color: floralwhite; */
  margin: 100px auto 0;
  width: 45rem;
  height: 40rem;
  /* background-color: #f8eded; */
  border-radius: 5px;
  font-size: 15px;
}

.signupinfo {
  width: 40rem;
  display: inline-block;
  text-align: right;
}

.signupinput {
  border-style: dotted;
  border-left-width: 0;
  border-right-width: 0;
  border-top-width: 0;
  border-bottom-width: 1;
  font-family: "Gamja Flower", cursive;
  width: 80%;
  height: 2.3rem;
  font-size: 17px;
  letter-spacing: 2px;
}

.signupinput:focus {
  outline: none;
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
  letter-spacing: 3px;
  display: inline-block;
  text-align: right;
}
.name {
  letter-spacing: 8px;
  display: inline-block;
  text-align: right;
}

.signup_btn {
  width: 9rem;
  position: relative;
  display: inline-block;
  font-size: 17px;
  padding: 10px 20px;
  color: black;
  margin: 20px 10px 10px;
  border-radius: 6px;
  text-align: center;
  transition: top 0.01s linear;
  text-shadow: 0 4px 0 rgba(0, 0, 0, 0.15);
}
.signup_btn.clickbtn:hover {
  background-color: #e6d3ed;
}

.signup_btn:active {
  top: 9px;
}
/* 3D button colors */
.signup_btn.clickbtn {
  background-color: #e6d3ed;
  box-shadow: 0 0 0 1px #f8eded inset, 0 0 0 2px rgba(255, 255, 255, 0.15) inset,
    0 8px 0 0 #b2b0eb, 0 8px 0 1px rgba(0, 0, 0, 0.4),
    0 8px 8px 1px rgba(0, 0, 0, 0.5);
}
.signup_btn.clickbtn:active {
  box-shadow: 0 0 0 1px #f8eded inset, 0 0 0 2px rgba(255, 255, 255, 0.15) inset,
    0 0 0 1px rgba(0, 0, 0, 0.4);
}
#btncenter {
  margin: 0px auto;
  width: 10rem;
}

</style>