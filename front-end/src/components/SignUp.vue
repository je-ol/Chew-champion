<template>
    <div class="h-[62.2vh] mb-[60px]">
        <div class="flex w-[26%] h-[94%] bg-[#758BFD] mx-auto mt-[100px] rounded-3xl text-white ">
            <form class="flex flex-col h-[90%] w-[70%] m-auto justify-around items-center [text-shadow:_1px_1px_1px_rgb(0_0_0_/_50%)]"> 
                <h1 class=" text-3xl font-extrabold ">Become a member!</h1>
                <input type="text"
                class="w-[100%] h-[40px] rounded pl-2"
            placeholder="Username">
                
                <input 
            type="email"
            class="w-[100%] h-[40px] rounded pl-2"
            placeholder="Email">
                <input 
            type="password"
            class="w-[100%] h-[40px] rounded pl-2"
            placeholder="Password">
            <input type="password"
            class="w-[100%] h-[40px] rounded pl-2"
            placeholder="Confirm password">
            <div class="w-[100%] flex">
                <input type="checkbox" required
                class="mr-2">                
                <p class="self-start font-bold cursor-pointer">You accept our <a href="/terms-of-service"
                class="underline">terms of service</a> </p>
            </div>

                <button class="text-xl font-extrabold bg-[#FA8531] py-2 px-6 rounded-md [text-shadow:_1px_1px_1px_rgb(0_0_0_/_60%)]">REGISTER</button>
                <p class="font-semibold cursor-pointer">Already have an account? <span class="underline">Login</span></p>
            </form>
        </div>    
    </div>

   
</template>

<script>
export default {
    name: 'SignUp',
}
</script>