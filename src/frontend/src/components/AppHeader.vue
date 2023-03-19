<template>
  <div class='w-full h-24 bg-transparent'>
        <div class='h-24 flex justify-end' v-if='!currentUser'>
            <button @click='login' class='bg-black mt-2 rounded-3xl text-base text-white mr-7 w-28 h-10'>Войти</button>
            <button @click='registration' class='bg-black mt-2 rounded-3xl text-base text-white mr-7 w-36 h-10'>Регистрация</button>
        </div>
        <div class='flex justify-end' v-else>
            <button @click='logout' class='bg-black mt-2 rounded-3xl text-base text-white mr-7 w-28 h-10'>Выйти</button>
        </div>
   </div>
</template>

<script>
export default {
    name: 'AppHeader',
    computed:{
        currentUser() {
            console.log(this.$store.state.auth.user )
            return this.$store.state.auth.user 
        }
    },
    methods: {
        async login() {
            this.$router.push('/login')
        },
        async registration() {
            this.$router.push('/registration')
        },
        async logout(){
            this.$store.dispatch('auth/logout')
        }
    }
}
</script>

<style>

</style>