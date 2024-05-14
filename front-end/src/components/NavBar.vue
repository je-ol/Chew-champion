<template>
    <nav class="flex justify-around items-center h-[80px] text-white " 
                :class="`${theme}`">
                    <div class="flex gap-3 items-center cursor-pointer text-white" 
                    >
                        <img src="../assets/burger.png" alt="">
                        <p class="text-3xl uppercase" id="logo">{{title}}</p>
                    </div>

                    <ul class="flex gap-3 w-[30%] justify-around cursor-pointer">
                        <li v-for="(page, index) in pages" :key="index">
                            <a 
                            :href="page.link.url" 
                            :title="`This link goes to the ${page.link.text} page`"
                            class="navLink font-bold  text-2xl" 
                            :class="{ active: activePage === index }"
                            @click.prevent="navLinkClick(index)">{{page.link.text}}</a>
                        </li>
                    </ul>
                    <div class="flex gap-6 text-base h-[50%] items-center">
                        <img src="../assets/dark-mode.png" alt="" 
                        @click.prevent="changeTheme()">
                        <button class="bg-[#758bfd] px-4 rounded-md h-[100%] font-bold"><a href="./login">LOGIN</a></button>
                        <button class="bg-[#758bfd] px-4 rounded-md h-[100%] font-bold"><a href="/register">REGISTER</a></button>
                        <div class="flex h-[48px] w-[48px] bg-white/80 rounded-full cursor-pointer border-solid border-white">
                            <img src="../assets/avatar-02.png" alt=""
                            class="h-[44px] w-[46px] m-auto rounded-full cover border-solid border-white border-[1px]">
                        </div>
                    </div>

                </nav>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    pages: Array,
    activePage: Number,
    title: String,
    navLinkClick: Function
  },
  data() {
    return {
      theme: "bg-[#27187e]",
    };
  },
  methods: {
/*     clickLogo() {
      activePage = 0;
    }, */
    changeTheme() {
      let theme = "bg-[#27187e]";

      if (this.theme == "bg-[#27187e]") {
        theme = "bg-[#ffc787]";
      }
      console.log("Updated theme:", theme);
      this.theme = theme;
    },
  },
};
</script>
