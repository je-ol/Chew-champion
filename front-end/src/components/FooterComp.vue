<template>
    <footer class="flex h-[100px] bg-[#aeb8fe] text-white sticky top-[100vh]">
            <p class="m-auto font-bold [text-shadow:_1px_1px_1px_rgb(0_0_0_/_50%)]">{{ copyright }}</p>
    </footer>  
</template>

<script>
export default {
    name: 'FooterComp',
    props: {
        copyright: String,
    }
}
</script>