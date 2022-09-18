<script setup>
import { computed } from "vue"
const addText = defineProps(['addText'])
const emit = defineEmits(['input'])
const inputedValue = computed({
  get() {
    return addText.value
  },
  set(newValue) {
    emit("input", newValue)
  }
})
</script>

<template>
  <input v-model="inputedValue" />
</template>

