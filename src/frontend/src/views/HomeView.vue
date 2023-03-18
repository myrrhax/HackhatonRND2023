<template>
  <div class='container'>
    <div v-if='currentUser'>{{ currentUser }}</div>
    <div v-else>НЕ ЗАРЕГАН</div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  computed: {
    currentUser() {
      return this.$store.state.auth.user 
    }
  },
  mounted() {

  }
}
</script>
