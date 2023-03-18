<template>
  <div class='header' style="width: 100%;height: 50px;background-color: green;">
    <div class='wrapper'>
        <div class='auth' v-if='!currentUser'>
            <button @click='login'>Войти</button>
            <button @click='registration'>Регистрация</button>
        </div>
        <div v-else>
            <button @click='logout'>Выйти</button>
        </div>
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