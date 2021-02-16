<template>
    <b-container>
        <b-row>
            <b-cols>
                <h1>proyecto CVRP</h1>
            </b-cols>
        </b-row>
        <b-row>
            <b-col v-for='red in redes' :key="red.red">
                <b-link :href="red.url" tarjet= '_blanck'>
                    <b-alert :variant='red.color' show>
                        {{red.red}}
                    </b-alert>
                </b-link>

            </b-col>
        </b-row>
    </b-container>
</template>

<script>

export default {
  name: 'Home',
  data(){
      return{
          redes:[
              {
                  red:'CVRP/FACEBOOK',
                  url:'https://www.facebook.com',
                  color:'info'  
              },
              {
                  red:'CVRP/INSTAGRAM',
                  url:'https://www.INSTAGRAM.com',
                  color:'warning'
              },
              {
                  red:'CVRP/TWITTER',
                  url:'https://www.TWITTER.com',
                  color:'danger'
              }
          ]
      }
  }
      }
</script>

<style 


 scoped>

</style>