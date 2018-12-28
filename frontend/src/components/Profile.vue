<template>
    <div class="container">
        <div class="jumbotron mt-5">
            <div class="col-sm-8 mx-auto">
                <h1 class="text-center">PROFILE</h1>
            </div>
            <table class="table col-md-6 mx-auto">
                <tbody>
                    <tr>
                        <td>First Name</td>
                        <td>{{first_name}}</td>
                    </tr>
                    <tr>
                        <td>Last Name</td>
                        <td>{{last_name}}</td>
                    </tr>
                    <tr>
                        <td>Email</td>
                        <td>{{email}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="jumbotron text-center">
            <div align="center">
                <h3>AH!-ZOM GIF Search</h3>
                <button @click="searchGIF()" type="button">Search</button>
                <input v-model="searchTerm" type="text">
            </div>
            <!-- Working but NOT in used -->
            <!-- <button @click="removeFavsFromUser()" type="button" class="btn btn-danger">Save Dislikes</button> -->
        </div>
        <!-- ****Favorite Results**** -->
        <div class="jumbotron centered">
                <div align="center">
                    <button @click="removeFavsFromUser()" type="button" class="btn btn-danger">Remove Favorites</button>
                    <button @click="addFavsToUser()" type="button" class="btn btn-success">Save Favorites</button>
                    <br>
                    <br>
                </div>
            <div class="container-fluid centered">
                <br>
                <div class="list-item" v-for="fg in favs" :key="fg.id">
                    <div @click="removeFromArray(fg)" class="animated-fav-gifdev float-left">
                        <img v-bind:src="fg" class="animated-fav-gif"/>
                    </div>
                </div>
            </div>
        </div>
        <!-- ****Search Results**** -->
        <div class="jumbotron jumbotron-fluid">
            <br>
            <br>
            <br>
            <div class="list-item" v-for="gif in gifs" :key="gif.id">
                <div class="img-fluid img-thumbnail float-left">
                    <img v-bind:src="gif" class="animated-gif"/>
                    <br>
                    <div style="text-align:center ">
                        <button @click="appendToArray(gif)" type="button" class="btn btn-success btn-sm">Favorite</button>
                        <!-- <button @click="removeFromArray(gif)" type="button" class="btn btn-danger btn-sm">Dislike</button> -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import jwtDecode from 'jwt-decode'
import axios from 'axios'
export default {
  data () {
    const token = localStorage.usertoken
    const decode = jwtDecode(token)
    // console.log(decode)
    return {
      searchTerm: '',
      gifs: [],
      favs: [],
      disfavs: [],
      getfavsflg: 0,
      first_name: decode.identity.first_name,
      last_name: decode.identity.last_name,
      email: decode.identity.email
    }
  },
  methods: {
    searchGIF () {
      var apiKey = 'VyPAXFIWXspP74xOxdch0FecuQF8tuJO'
      var searchPoint = 'https://api.giphy.com/v1/gifs/search?'
      var limit = 10
      var rating = 'g'
      var url = `${searchPoint}&api_key=${apiKey}&q=${this.searchTerm}&limit=${limit}&rating=${rating}`
      fetch(url)
        .then(response => {
          return response.json()
        })
        .then(json => {
          this.buildUrlGifs(json)
          // console.log(json)
        })
        .catch(err => console.log(err))
    },
    buildUrlGifs (json) {
      this.gifs = json.data.map(gif => gif.id).map(gifId => {
        // console.log(`https://media.giphy.com/media/${gifId}/giphy.gif`)
        return `https://media.giphy.com/media/${gifId}/giphy.gif`
      })
      // console.log(this.gifs)
    },
    appendToArray (gifUrlFav) {
      var i
      var flagf
      flagf = 0
      if (this.favs.length === 1) {
        if (this.favs[0].localeCompare(gifUrlFav) === 0) {
          flagf = 1
        }
      } else {
        for (i = 0; i < this.favs.length; i++) {
          if (this.favs[i].localeCompare(gifUrlFav) === 0) {
            flagf = 1
          }
        }
      }
      // add to array if not present
      if (flagf === 0) {
        this.favs.push(gifUrlFav)
      }
      console.log(this.favs)
    },
    appendToArrayDisFav (gifUrlFav) {
      var i
      var flagf
      flagf = 0
      if (this.disfavs.length === 1) {
        if (this.disfavs[0].localeCompare(gifUrlFav) === 0) {
          flagf = 1
        }
      } else {
        for (i = 0; i < this.disfavs.length; i++) {
          if (this.disfavs[i].localeCompare(gifUrlFav) === 0) {
            flagf = 1
          }
        }
      }
      // add to array if not present
      if (flagf === 0) {
        this.disfavs.push(gifUrlFav)
      }
      console.log(this.disfavs)
    },
    removeFromArray (gifUrlFav) {
      var i
      // adds to the dislike array to later be remove
      this.appendToArrayDisFav(gifUrlFav)
      if (this.favs.length === 1) {
        if (this.favs[0].localeCompare(gifUrlFav) === 0) {
          this.favs.splice(0, 1)
        }
      } else {
        for (i = 0; i < this.favs.length; i++) {
          if (this.favs[i].localeCompare(gifUrlFav) === 0) {
            this.favs.splice(i, 1)
          }
        }
      }
      console.log(this.favs)
    },
    getFavoritesFromDB () {
      const path = 'users/favorites'
      if (this.getfavsflg === 0) {
        this.getfavsflg = 1
        axios.post(path, {'email': this.email, 'action': 'get'})
          .then((response) => {
            var i
            for (i = 0; i < response.data.favorites.length; i++) {
              this.favs[i] = response.data.favorites[i]
            }
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },
    addFavsToUser () {
      const path = 'users/favorites'
      axios.post(path, {'email': this.email, 'favorites': this.favs, 'action': 'add'})
        .then(() => {
          console.log('addFavtsToUserWORKS')
        })
        .catch((error) => {
          console.error(error)
        })
    },
    removeFavsFromUser () {
      const path = 'users/favorites'
      axios.post(path, {'email': this.email, 'favorites': this.disfavs, 'action': 'remove'})
        .then(() => {
          console.log('removeFavsFromUserWORKS')
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  beforeMount () {
    this.getFavoritesFromDB()
  }
}
</script>
