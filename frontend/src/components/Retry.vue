<template>
    <div class="container">
        <div class="jumbotron mt-5">
            <div class="col-sm-8 mx-auto">
               <h3 class="text-center">Incorrect Email or Password. Try Again.</h3>
               <h4 class="text-center font-italic">Redirecting to Login in 10 seconds...</h4>
            </div>
        </div>
    </div>
</template>

<script>
import router from '../router'

export default {
  /*
  *  Function to redirect user upon loading the retry page for the error message
  */
  created () {
    setTimeout(() => router.push({name: 'Login'}), 10000)
  }
}
</script>
