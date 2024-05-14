<template>
  <nav-bar 
        id="navbar"
        :pages="pages" 
        :active-page="activePage" 
        :title="title"
        :nav-link-click="(index) => activePage = index">
  </nav-bar>

  <router-view />  
  
<!--   <page-content 
        :page="pages[activePage]">
  </page-content> -->
  <footer-component
        :copyright="copyright">
  </footer-component>
</template>

<script>
import NavBar from "./components/NavBar.vue";
/* import PageContent from "./components/PageContent.vue"; */
import FooterComponent from "./components/FooterComponent.vue";
/* import LogIn from "./components/LogIn.vue"; */



export default {
  name: "App",
  components: {
    NavBar,
    /* PageContent, */
    FooterComponent,
    /* LogIn */
  },
  data() {
    return {
      title: "Chew Champion",
      activePage: 0,
      pages: [
        {
          link: { text: "Front page", url: "/index.html" },
          pageTitle: "Front page",
          pageContent: "This is the front page content",
        },
        {
          link: { text: "Feed", url: "/feed.html" },
          pageTitle: "Feed",
          pageContent: "This is the feed page content",
        },
        {
          link: { text: "Contact", url: "/contact.html" },
          pageTitle: "Contact",
          pageContent: "This is the contact page content",
        },
        {
          link: { text: "About", url: "/about.html" },
          pageTitle: "About",
          pageContent: "This is the about page content",
        
        },
      ],
      copyright:
        "© 2024 Chew Champion. All rights reserved.",
    };
  },
};
</script>

<style>
#app {
}
</style>
