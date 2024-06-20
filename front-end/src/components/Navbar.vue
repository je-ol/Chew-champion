<template>
  <nav class="flex justify-around fixed items-center h-[80px] md:h-[56px] w-[100%] text-white z-[10]" :class="theme">
    <router-link to="./">
      <div class="flex gap-3 items-center cursor-pointer text-white">
        <img src="../assets/burger.png" alt="" class="md:h-[48px] md:w-[48px]">
        <p class="text-3xl md:text-2xl uppercase" id="logo">Chew Champion</p>
      </div>
    </router-link>

    <div class="flex gap-9 w-[30%] justify-around items-center cursor-pointer">
        <p class="font-bold text-2xl md:text-xl"><router-link to="./">Grid</router-link></p>
        <p class="font-bold text-2xl md:text-xl"><router-link to="./all">List</router-link></p>
        <SearchBar />
    </div>
    
    <div class="flex gap-6 text-base h-[50%] items-center">
<!--       <img src="../assets/dark-mode.png" alt="" @click.prevent="changeTheme"> -->
      <div v-if="!user" class="flex gap-6 text-base md:text-sm h-[50%] items-center">
        <router-link to="./login" class="bg-[#758bfd] px-4 py-2 rounded-md font-bold">LOGIN</router-link>
        <router-link to="./register" class="bg-[#758bfd] px-4 py-2 rounded-md font-bold">REGISTER</router-link>
      </div>
      <div v-if="user" class="flex gap-6 text-base md:text-sm h-[50%] items-center">
        <a href="javascript:void(0)" class="bg-[#758bfd] px-4 py-2 rounded-md font-bold cursor-pointer" @click="handleLogout">LOG OUT</a>
      </div>
      <router-link to="./profile">
        <div v-if="user" class="flex md:h-[40px] md:w-[40px] h-[48px] w-[48px] bg-white/80 rounded-full cursor-pointer border-solid border-white">
          <img :src="getAvatarUrl(user.id)" alt="" class="h-[46px] w-[46px] md:h-[40px] md:w-[40px] m-auto rounded-full cover border-solid border-white border-[2px]">
        </div>
      </router-link>
    </div>
  </nav>
</template>

<script>
import { computed } from 'vue';
import { useAuthStore } from '../store/auth';
import { getAvatarUrl } from '../utils/getAvatars.js';
import SearchBar from './SearchBar.vue';
import { useRouter } from 'vue-router';

export default {
  name: 'Navbar',
  components: {
    SearchBar,
  },
  setup() {
    const authStore = useAuthStore();
    const user = computed(() => authStore.user);
    const router = useRouter();

    const handleLogout = async () => {
      localStorage.removeItem('user');
      localStorage.removeItem('token');
      sessionStorage.clear();
      await authStore.getUser(); // Update the store state
      alert("Hope to see you back soon!");
      authStore.$reset(); // Reset the store to clear the user
      router.push('/');
    };

    return {
      user,
      handleLogout,
    };
  },
  data() {
    return {
      theme: "bg-[#27187e]",
    };
  },
  methods: {
    changeTheme() {
      this.theme = this.theme === "bg-[#27187e]" ? "bg-[#ffc787]" : "bg-[#27187e]";
    },
    getAvatarUrl,
  },
};
</script>
