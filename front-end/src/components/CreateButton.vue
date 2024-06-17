<template>
    <router-link :to="'/new-post'">
    <div class="flex h-[102px] md:h-[84px] w-[102px] md:w-[84px] bg-[#27187e]/70 fixed bottom-[60px] right-[2%] rounded-full pl-1 pt-1 z-10">
        <img src="../assets/create1.png" alt="" class=" h-[64px] md:h-[52px] w-[64px] md:w-[52px] m-auto">
    </div>
    </router-link>
</template>

<script>
export default {
    name: 'CreateButton',

}
</script>