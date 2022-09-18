<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps(['interval'])
const counter = ref(0)
const resetCounter = () => {
      counter.value = 0
}
onMounted(() => {
  setInterval(() => {
    counter.value++
  }, props.interval)
})
</script>

<template>
  <div class="counter">
    Counter: {{ counter }}
    <button @click="resetCounter">reset conuter</button>
    <button @click="$emit('snap-coutner', counter)">snap conuter</button>
  </div> 
</template>

<style>
.counter {
  color: plum;
  font-weight: bold;
}
</style>

