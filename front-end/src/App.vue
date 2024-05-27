<template>
  <navbar :user="authStore.user"></navbar>
  <router-view></router-view>
  <footer-comp :copyright="copyright"></footer-comp>
</template>

<script>
import { onMounted } from 'vue';
import { useAuthStore } from './store/auth';
import Navbar from "./components/Navbar.vue";
import FooterComp from "./components/FooterComp.vue";

export default {
  name: "App",
  setup() {
    const authStore = useAuthStore();

    onMounted(() => {
      authStore.getUser();
    });

    return {
      authStore
    };
  },
  components: {
    Navbar,
    FooterComp,
  },
  data() {
    return {
      title: "Chew Champion",
      activePage: 0,
      copyright: "© 2024 Chew Champion. All rights reserved.",
    };
  }
}
</script>
