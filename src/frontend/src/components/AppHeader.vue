<template>
  <div>
    <button @click='login'>Войти</button>
  </div>
  <div>Регистрация</div>
</template>

<script>
export default {
    name: 'AppHeader',
    methods: {
        async login() {
            console.log('sfamfmsamf')
            let data = await this.$store.dispatch('auth/login', {
                name: 'myrrhax',
                password: '17983'
            })
            console.log(data)
        }
    }
}
</script>

<style>

</style>