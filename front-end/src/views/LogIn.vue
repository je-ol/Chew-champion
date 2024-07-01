<template>
    <div class="h-[80vh] flex flex-col justify-center items-center mt-[56px]">
      <div class="flex w-[24%] h-[60%] md:h-[70%] bg-[#758BFD] m-auto rounded-3xl text-white">
        <form @submit.prevent="handleSubmit" class="flex flex-col h-[80%] w-[70%] m-auto justify-around items-center [text-shadow:_1px_1px_1px_rgb(0_0_0_/_50%)]">
          <h1 class="text-3xl md:text-2xl font-extrabold">Welcome back!</h1>
          <input type="text" v-model="username" class="w-[100%] h-[12%] rounded pl-2 text-black mb-1" placeholder="Username">
          <input type="password" v-model="password" class="w-[100%] h-[12%] rounded pl-2 text-black" placeholder="Password">
          <p class="self-start underline font-bold cursor-pointer md:text-xs">Forgot your password?</p>
          <button class="text-xl md:text-sm font-extrabold bg-[#FA8531] py-2 px-6 rounded-md [text-shadow:_1px_1px_1px_rgb(0_0_0_/_60%)]">LOGIN</button>
          <p class="font-semibold cursor-pointer md:text-xs">Don't have an account? 
            <router-link to="/register" class="underline">Register</router-link></p>
        </form>
      </div>
      <p class="text-indigo-700">username: visitor | password: 1234</p>
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
        const response = await axios.post('https://chew-champion-ea4753cf27e6.herokuapp.com/login/', data);
        if (response.status === 200) {
          alert("Logged in successfully");
          this.authStore.setToken(response.data.token);
          await this.authStore.getUser();
          this.$router.push('/');
        }
      } catch (error) {
        console.error(error);
        if (error.response && (error.response.status === 400 || error.response.status === 404)) {
          alert("Invalid username or password");
        }
      }
    }
  }
};
</script>

  