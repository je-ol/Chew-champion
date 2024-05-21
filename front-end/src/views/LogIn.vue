<template>
    <div class="h-[80vh] flex items-center">
      <div class="flex w-[24%] h-[60%] bg-[#758BFD] m-auto rounded-3xl text-white">
        <form @submit.prevent="handleSubmit" class="flex flex-col h-[80%] w-[70%] m-auto justify-around items-center [text-shadow:_1px_1px_1px_rgb(0_0_0_/_50%)]">
          <h1 class="text-3xl font-extrabold">Welcome back!</h1>
          <input type="text" v-model="username" class="w-[100%] h-[40px] rounded pl-2 text-black" placeholder="Username">
          <input type="password" v-model="password" class="w-[100%] h-[40px] rounded pl-2 text-black" placeholder="Password">
          <p class="self-start underline font-bold cursor-pointer">Forgot your password?</p>
          <button class="text-xl font-extrabold bg-[#FA8531] py-2 px-6 rounded-md [text-shadow:_1px_1px_1px_rgb(0_0_0_/_60%)]">LOGIN</button>
          <p class="font-semibold cursor-pointer">Don't have an account? <span class="underline">Register</span></p>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { useAuthStore } from '../store/auth';
  
  export default {
    name: 'LogIn',
    setup() {
      const authStore = useAuthStore();
      return { authStore };
    },
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      async handleSubmit() {
        const data = { username: this.username, password: this.password };
        try {
          const response = await axios.post('https://chew-champion-43c72340b77a.herokuapp.com/login/', data);
          if (response.status === 200) {
            alert("Logged in successfully");
            localStorage.setItem('token', response.data.token);
            localStorage.setItem('user', JSON.stringify(response.data.user));
            this.authStore.getToken();
            this.authStore.getUser();
            this.$router.push('/');
          }
        } catch (error) {
          console.error(error);
          if (error.response && error.response.status === 400) {
            alert("Invalid username or password");
          }
        }
      }
    }
  };
  </script>
  