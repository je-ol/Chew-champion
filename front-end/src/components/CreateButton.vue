<template>
    <router-link :to="'/new-post'">
    <div class="flex h-[102px] w-[102px] bg-black/20 fixed bottom-[60px] right-[320px] rounded-full pl-1 pt-1 z-10">
        <img src="../assets/create.png" alt="" class=" h-[64px] w-[64px] m-auto">
    </div>
    </router-link>
</template>

<script>
export default {
    name: 'CreateButton',

}
</script>