<template>
  <navbar :user="authStore.user"></navbar>
  <router-view :user="authStore.user"></router-view>
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
      pages: [
        { link: { text: "Front page", url: "/index.html" }, pageTitle: "Front page", pageContent: "This is the front page content" },
        { link: { text: "Feed", url: "/feed.html" }, pageTitle: "Feed", pageContent: "This is the feed page content" },
        { link: { text: "Contact", url: "/contact.html" }, pageTitle: "Contact", pageContent: "This is the contact page content" },
        { link: { text: "About", url: "/about.html" }, pageTitle: "About", pageContent: "This is the about page content" }
      ],
      copyright: "© 2024 Chew Champion. All rights reserved.",
    };
  }
}
</script>
