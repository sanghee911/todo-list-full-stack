<template>
  <div class="dashboard">
    <header>
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <a class="navbar-brand" href="#">Cocktail Demo</a>
        <button class="navbar-toggler d-lg-none" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarsExampleDefault">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Settings</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Profile</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Help</a>
            </li>
          </ul>
          <form class="form-inline mt-2 mt-md-0">
            <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" v-model="search">
          </form>
        </div>
      </nav>
    </header>
    <div class="container-fluid">
      <div class="row">
        <nav class="col-sm-3 col-md-2 d-none d-sm-block bg-light sidebar">
          <ul class="nav nav-pills flex-column">
            <li class="nav-item">
              <a class="nav-link active" href="#">Todo List <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Reports</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Analytics</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Export</a>
            </li>
          </ul>
        </nav>

        <main role="main" class="col-sm-9 ml-sm-auto col-md-10 pt-3">
          <div id="todo">
            <h1 id="dashboard-title">Todo List - Cocktail Demo on host: {{ hostname }}</h1>
            <button class="btn btn-outline-info btn-sm pull-right"  v-on:click.prevent="formShow=true">Add a todo</button>
            <div id="form-modal" v-if="formShow">
              <form id="todo-form">
                <div class="form-group">
                  <label>To do:</label>
                  <input type="text" class="form-control form-control-sm" required
                         placeholder="할일을 명확하게 입력해 주세요" v-model="todoItem.todo">
                </div>
                <div class="form-group">
                  <label>Started on:</label>
                  <input type="date" class="form-control form-control-sm" required  v-model="todoItem.started_on">
                </div>
                <div class="form-group">
                  <label>Due on:</label>
                  <input type="date" class="form-control form-control-sm" required  v-model="todoItem.due_on">
                </div>
                <div class="form-group">
                  <label>Owner:</label>
                  <input type="text" class="form-control form-control-sm" required
                         placeholder="담당자를 모두 입력해 주세요" v-model="todoItem.owner">
                </div>
                <div class="form-group">
                  <label>Description:</label>
                  <textarea class="form-control form-control-sm" placeholder="가능한한 상세하게 입력해 주세요"
                            v-model="todoItem.description"></textarea>
                </div>
                <button class="btn btn-outline-success btn-sm" v-on:click.prevent="postData">OK</button>
                <button class="btn btn-outline-danger btn-sm" v-on:click.prevent="hideForm">Cancel</button>
              </form>
            </div>
            <div class="table-responsive table-striped table-sm">
              <table class="table">
                <thead class="thead-dark">
                <tr>
                  <td></td>
                  <td>ID</td>
                  <td>Todo</td>
                  <td>Owner</td>
                  <td>Started on</td>
                  <td>Due on</td>
                  <td></td>
                </tr>
                </thead>
                <tbody>
                <template v-for="(todo, index) in filteredTodo">
                  <tr>
                    <td v-on:click="toggleDesc('child-' + index, $event); toggleStatus(index)">
                      <i class="fa fa-plus-circle" aria-hidden="true" v-bind:id="'icon-' + index"></i>
                    </td>
                    <td>{{ todo.id }}</td>
                    <td>{{ todo.todo }}</td>
                    <td>{{ todo.owner }}</td>
                    <td>{{ todo.started_on }}</td>
                    <td>{{ todo.due_on }}</td>
                    <td class="close-button" v-on:click.prevent="deleteData(todo.id, index)"><i class="fa fa-window-close-o" aria-hidden="true"></i></td>
                  </tr>
                  <tr v-bind:id="'child-' + index" class="desc">
                    <td colspan="7">Description: {{ todo.description }}</td>
                  </tr>
                </template>
                </tbody>
              </table>
            </div>
          </div>

        </main>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "dashboard",
    data: function () {
      return {
        title: 'Cocktail Demo',
        todoList: [],
        todoItem: {
          todo: "",
          started_on: "",
          due_on: "",
          owner: "",
          description: ""
        },
        formShow: false,
        search: "",
        apiUrl: $('#api-url').data('api-url'),
        hostname: $('#hostname').data('hostname'),
      }
    },
    methods: {
      toggleDesc: function (id, event) {
        $('#' + id).toggle();
      },
      submitForm: function () {
        console.log(this.todoItem);
      },
      getData: function () {
//        this.apiUrl = $('#api-url').data('api-url');
        console.log(this.apiUrl);
        this.$http.get(this.apiUrl)
          .then(function (data) {
            console.log(data);
            console.log(this.hostname)
            this.todoList = data.body.reverse();
          });
      },
      postData: function () {
        this.$http.post(this.apiUrl, this.todoItem)
          .then(function (data) {
            console.log(data);
            this.getData();
            this.hideForm();
          });
      },
      deleteData: function (id, index) {
        this.$http.delete(this.apiUrl + id).then(
          function(data) {
            this.getData();
          }
        );
      },
      toggleStatus: function (index) {
        $('#icon-' + index).toggleClass('fa-plus-circle fa-minus-circle');
      },
      hideForm: function () {
        this.formShow = false;
        this.todoItem.todo = "";
        this.todoItem.started_on = "";
        this.todoItem.due_on = "";
        this.todoItem.owner = "";
        this.todoItem.description = "";
      }
    },
    created: function () {
      this.getData();
      console.log(process.env.TEST_ENV)
    },
    computed: {
      filteredTodo: function () {
        const searchTerm = new RegExp(this.search, 'i');
        return this.todoList.filter((todo) => {
            return todo.todo.match(searchTerm) ||
              todo.owner.match(searchTerm) ||
              todo.description.match(searchTerm);
          }
        )}
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
  .fa-plus-circle {
    color: green;
    cursor: pointer;
  }
  .fa-minus-circle {
    color: orangered;
    cursor: pointer;
  }
  .fa-window-close-o {
    cursor: pointer;
    color: #777;
  }
  #form-modal {
    background: rgba(0,0,0,0.5);
    position: fixed;
    top: 0;
    bottom:0;
    left:0;
    right: 0;
    z-index: 10000;
  }
  #todo-form {
    width: 500px;
    margin: 0 auto;
    background: white;
    padding: 30px;
    vertical-align: middle;
  }
  .thead-dark {
    background: #d8e1f5;
    /*color: white;*/
  }
  .btn-sm {
    margin-bottom: 5px;
  }
  textarea {
    min-height: 100px;
  }
  #dashboard-title {
    font-size: 1.5em;
    color: #007bff;
  }
</style>
