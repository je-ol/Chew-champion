<template>
    <div class="h-[80vh] flex items-center mt-[60px]">
        <div class="flex w-[26%] h-[80%] bg-[#758BFD] m-auto rounded-3xl text-white ">
            <form @submit.prevent="handleSubmit" class="flex flex-col h-[90%] w-[70%] m-auto justify-around items-center [text-shadow:_1px_1px_1px_rgb(0_0_0_/_50%)]"> 
                <h1 class=" text-3xl font-extrabold ">Become a member!</h1>
                <input type="text" v-model="username"
                class="w-[100%] h-[40px] rounded pl-2 text-black"
                placeholder="Username" required>
                
                <input 
                type="email" v-model="email"
                class="w-[100%] h-[40px] rounded pl-2 text-black"
                placeholder="Email" required>
                <input 
                type="password" v-model="password"
                class="w-[100%] h-[40px] rounded pl-2 text-black"
                placeholder="Password" required>
                <input type="password" v-model="confirmPassword"
                class="w-[100%] h-[40px] rounded pl-2 text-black"
                placeholder="Confirm password" required>
                <div class="w-[100%] flex">
                    <input type="checkbox" required
                    class="mr-2">                
                    <p class="self-start font-bold cursor-pointer">You accept our <a href="/terms-of-service"
                    class="underline">terms of service</a></p>
                </div>

                <button class="text-xl font-extrabold bg-[#FA8531] py-2 px-6 rounded-md [text-shadow:_1px_1px_1px_rgb(0_0_0_/_60%)]"
                >REGISTER</button>
                <p class="font-semibold cursor-pointer">Already have an account? 
                    <router-link to="/login" class="underline">Login</router-link></p>
            </form>
        </div>    
    </div>

   
</template>

<script>
import axios from 'axios';
import { useAuthStore } from '../store/auth';

export default {
  name: 'Register',
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: ''
    };
  },
  methods: {
    async handleSubmit() {
      const data = {
        username: this.username,
        email: this.email,
        password: this.password,
      };
      if (this.password !== this.confirmPassword) {
        alert("Passwords do not match");
        return;
      }
      console.log("Registering user...");

      try {
        const response = await axios.post('https://chew-champion-43c72340b77a.herokuapp.com/signup/', data);
        if (response.status === 200) {
          alert("Registered successfully");
          this.authStore.setToken(response.data.token);
          await this.authStore.getUser();
          this.$router.push('/');
        }
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>
