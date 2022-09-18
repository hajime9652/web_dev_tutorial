<script setup>
import CustomInput from './components/CustomInput.vue'
import Counter from './components/Counter.vue'
import MouseTracker from './components/MouseTracker.vue'

import { ref } from 'vue'
const message = 'Hello Vue!!'
const snap = ref([])
const addText = ref('')

const addCounter = (e) => {
      snap.value.push(e)
}
</script>

<template>
  <div class="demo">
    {{ message }}
    <Counter :interval="1000" @snap-coutner="addCounter" />
    <Counter :interval="100" @snap-coutner="addCounter" />
  </div>

  <div class="demo">
    <div>
      子のカスタムインプット
      <CustomInput v-model="addText" />
    </div>
    <div>
      子のテキストを親で表示：{{ addText }}
    </div>
  </div>
  <div class="demo">
    snap counter
    <div v-for="item in snap" :key="item">
      snap: {{ item }}
    </div>
  </div>
  <div class="demo">
    <MouseTracker />
  </div>
</template>

<style scoped>
.demo {
    font-family: sans-serif;
    border: 1px solid #eee;
    border-radius: 2px;
    padding: 20px 30px;
    margin-top: 1em;
    margin-bottom: 20px;
    user-select: none;
    overflow-x: auto;
}
</style>
