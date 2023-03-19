<template>
  <div class="text-black flex justify-around items-center" style="width: 100%; height: 75%;">
    <div class="text-left text-9xl">
      FACE<br>CHECK
    </div>
    <div>
      <div style='width: 350px;' class="bg-black rounded-full text-right flex justify-center">
        <button @click='toSearch' class="text-2xl px-5 text-white"> Найти по фото </button>
        <img class="w-20 h-20" src="/static/MG.svg">
      </div>
      <p class="text-right mt-5 text-4xl">Сервис для поиска<br>информации по фото </p>
    </div>
  </div>
</template>

<script>

export default {
  methods: {
    toSearch() {
      this.$router.push('/search')
    }
  }
}
</script>
