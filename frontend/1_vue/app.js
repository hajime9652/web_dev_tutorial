const Todo = {
  data() {
    return {
      title: "",
      items: [{"title": "Learn some frameworks!"}]
    }
  },
  methods: {
    submit(title) {
      this.items.push({"title": title})
    },
    deleteItem(index) {
      this.items.splice(index, 1)
    },
  }
}

Vue.createApp(Todo).mount('#todo')
