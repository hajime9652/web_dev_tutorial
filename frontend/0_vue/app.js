
const HelloVueApp = {
  data() {
    return {
      message: 'Hello Vue!!'
    }
  },
  template: `<div>{{ message }}</div>`
}

const app = Vue.createApp({})
app.component(HelloVueApp)

const Counter = {
  props: ['interval'],
  data() {
    return {
      counter: 0
    }
  },
  methods: {
    resetCounter() {
      this.counter = 0
    }
  },
  mounted() {
    setInterval(() => {
      this.counter++
    }, this.interval)
  },
  template: `<div class="demo">
  Counter: {{ counter }}
  <button @click="resetCounter()">reset conuter</button>
  </div>`
}

app.component('Counter', Counter)
app.mount('#hello-vue')
