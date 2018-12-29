<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6 mt-5 mx-auto">
                <form v-on:submit.prevent="login">

                    <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input type="email" v-model="email" class="form-control" name="email" placeholder="Enter Email">
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" v-model="password" class="form-control" name="password" placeholder="Enter Password">
                    </div>
                    <button class="btn btn-lg btn-primary btn-block">Sign In</button>

                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
import EventBus from './EventBus'

export default {
  data () {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    /*
    *  Function to send a request to the server for logging in a user
    */
    login () {
      axios.post('users/login', {
        email: this.email,
        password: this.password
      }).then(res => {
        localStorage.setItem('usertoken', res.data.token)
        this.email = ''
        this.password = ''
        /* If email and password is no valid, return to the login page
        *  and WILL NOT log in to any profile
        */
        if (res.data.token === undefined) {
          localStorage.removeItem('usertoken')
          router.push({name: 'Retry'})
        } else {
          this.emitMethod()
          router.push({name: 'Profile'})
        }
      }).catch((err) => {
        console.log(err)
      })
    },
    /*
    *  Function to communicate with other vue components that a user is logged in
    */
    emitMethod () {
      EventBus.$emit('logged-in', 'loggedin')
    }
  }
}

</script>
