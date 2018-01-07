<template>
  <div id="todo">
    <h2>Todo List</h2>
    <div class="table-responsive table-striped">
      <table class="table">
        <thead>
        <tr>
          <td>ID</td>
          <td>Todo</td>
          <td>Owner</td>
          <td>Started on</td>
          <td>Due on</td>
          <td></td>
        </tr>
        </thead>
        <tbody>
        <template v-for="(todo, index) in todoList">
          <tr v-on:click="toggleDesc('child-' + index, $event)">
            <td>{{ todo.id }}</td>
            <td>{{ todo.todo }}</td>
            <td>{{ todo.owner }}</td>
            <td>{{ todo.started_on }}</td>
            <td>{{ todo.due_on }}</td>
            <td class="close-button"><i class="fa fa-window-close-o" aria-hidden="true"></i></td>
          </tr>
          <tr v-bind:id="'child-' + index" class="desc">
            <td colspan="6">Description: {{ todo.description }}</td>
          </tr>
        </template>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  export default {
    name: "todo",
    data: function () {
      return {
        todoList: []
      }
    },
    methods: {
      toggleDesc: function (id, event) {
        $('#' + id).toggle();
      },
      getData: function () {
        this.$http.get('http://localhost:8000/api/todo-list/')
          .then(function (data) {
            console.log(data);
            this.todoList = data.body;
          });
      },
    },
    beforeMount: function () {
      this.getData();
    }
  }
</script>

<style scoped>
  .desc {
    display: none;
    transition: all 0.5s;
  }
  .table-striped tbody tr:nth-of-type(odd) {
    background-color: white;
  }
  .table-striped tbody tr:nth-of-type(even)  {
    background-color: #e9fde6;
  }
  .close-button {

  }
</style>
