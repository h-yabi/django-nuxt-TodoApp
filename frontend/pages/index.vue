<template>
  <div class="container contai my-5">
      <h1 class="title">TodoList</h1>
      <ul class="todo-list">
        <li v-for="todo in data" :key="todo.id" class="justify-content-between">
          <div class="d-flex align-items-center">
            <div  class="todo-image">
              <img v-if="todo.picture" :src="todo.picture" :alt="todo.title">
              <img v-else src="https://placehold.jp/150x150.png" :alt="todo.title">
            </div>
            {{todo.title}}
          </div>
          <button @click="onDelete(todo.id)" class="btn btn-sm btn-danger">
            削除
          </button>
        </li>
      </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  async asyncData (context: any) {
    const { $axios, params } = context
    console.log($axios)
    try {
      const todoData = await $axios.$get('/todo/')
      return { todoData }

    } catch (error) {
      console.log(error)
    }
  },
  data() {
    return {
      data: ''
    }
  },
  mounted() {
    this.data =this.$data.todoData
  },
  methods: {
    async onDelete(id) {
      try {
        await this.$axios.$delete(`/todo/${id}/`)
        const newData = await this.$axios.$get('/todo/')
        this.data = newData
      } catch (e) {
        console.log(e)
      }
    }
  }
})
</script>

<style lang="scss" scoped>
.title {
  margin-bottom: 20px;
  text-align: center;
}
.todo-list {
  li {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    padding: 10px;
    background: #eee;
  }
}
.todo-image {
  margin-right: 15px;
  img {
    width: 50px;
    height: 50px;
    object-fit: cover;
  }
}

</style>



