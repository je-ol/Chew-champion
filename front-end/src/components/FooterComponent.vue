<template>
    <footer class="flex h-[100px] bg-[#aeb8fe] text-white">
            <p class="m-auto font-bold [text-shadow:_1px_1px_1px_rgb(0_0_0_/_100%)]">{{ copyright }}</p>
    </footer>  
</template>

<script>
export default {
    name: 'FooterComponent',
    props: {
        copyright: String,
    }
}
</script>