<template>
  <div id="app">
   <home> </home>
   <Pixabay></Pixabay> 
  </div>
</template>

<script>

import Home from './components/Home'
import Pixabay from './components/pixabay/Pixabay'

export default {
  name: 'App',
  components: {
    Home,
    Pixabay,
  }
}
</script>


<style>

</style>
