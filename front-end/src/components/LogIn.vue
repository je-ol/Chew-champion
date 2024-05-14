<template>
    <div class="h-[62.2vh] mb-[60px]">
        <div class="flex w-[26%] h-[80%] bg-[#758BFD] mx-auto mt-[100px] rounded-3xl text-white">
            <form class="flex flex-col h-[80%] w-[70%] m-auto justify-around items-center [text-shadow:_1px_1px_1px_rgb(0_0_0_/_50%)]"> 
                <h1 class=" text-3xl font-extrabold ">Welcome back!</h1>
                <input 
            type="email"
            class="w-[100%] h-[40px] rounded pl-2"
            placeholder="Email">
                <input 
            type="password"
            class="w-[100%] h-[40px] rounded pl-2"
            placeholder="Password">
                <p class="self-start underline font-bold cursor-pointer">Forgot your password?</p>
                <button class="text-xl font-extrabold bg-[#FA8531] py-2 px-6 rounded-md [text-shadow:_1px_1px_1px_rgb(0_0_0_/_60%)]">LOGIN</button>
                <p class="font-semibold cursor-pointer">Don't have an account? <span class="underline">Register</span></p>
            </form>
        </div>    
    </div>

   
</template>

<script>
export default {
    name: 'LogIn',
}
</script>