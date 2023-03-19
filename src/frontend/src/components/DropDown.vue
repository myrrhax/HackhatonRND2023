<template>
    <div class='flex justify-center items-center' style="width: 100%; height:50%;">
        <div style='height: 120%; width: 50%; border-radius: 50px;' class="flex justify-center items-center p-12 bg-black opacity-80" @dragover="dragover" @dragleave="dragleave" @drop="drop">
            <input type="file" name="fields[assetsFieldHandle][]" id="assetsFieldHandle" 
            class="w-px h-px opacity-0 overflow-hidden absolute" @change="onChange" ref="file" accept=".pdf,.jpg,.jpeg,.png" />
        
            <label for="assetsFieldHandle" class="block cursor-pointer">
            <div class='flex flex-col justify-center align-center text-white' v-if='filelist.length === 0'>
                <div class='flex justify-center'>
                  <img class='w-10 h-10' src='../../public/static/upload.png' />
                </div>
                <span>Перетащите изображение для загрузки</span>
            </div>
            </label>
            <ul class="mt-4" v-if="this.filelist.length" v-cloak>
            <li class="text-sm p-1" v-for="file in filelist" :key='file'>
                <span class='text-black font-semibold'>{{file.name}}</span>
                <div class='flex items-end'>
                    <button style="width:150px;height:50px;background-color: #FFD098;border-radius:30px;" @click="submit">Загрузить</button>
                </div>
            </li>
            </ul>
        </div>
</div>
</template>

<script>
export default{
  data() {
    return {
        filelist: [], // Store our uploaded files,
    }
  },
  methods: {
    submit() {
        console.log("SFAMFSNANFA!284821848214")
        this.$emit('onSubmit', this.filelist[0])
    },
    onChange() {
      this.filelist = [...this.$refs.file.files];
    },
    remove(i) {
      this.filelist.splice(i, 1);
    },
    dragover(event) {
      event.preventDefault();
      // Add some visual fluff to show the user can drop its files
      if (!event.currentTarget.classList.contains('bg-green-300')) {
        event.currentTarget.classList.remove('bg-gray-100');
        event.currentTarget.classList.add('bg-green-300');
      }
    },
    dragleave(event) {
      // Clean up
      event.currentTarget.classList.add('bg-black');
      event.currentTarget.classList.remove('bg-green-300');
    },
    drop(event) {
      event.preventDefault();
      this.$refs.file.files = event.dataTransfer.files;
      this.onChange(); // Trigger the onChange event manually
      // Clean up
      event.currentTarget.classList.add('bg-gray-100');
      event.currentTarget.classList.remove('bg-green-300');
    }
  }
}
</script>


