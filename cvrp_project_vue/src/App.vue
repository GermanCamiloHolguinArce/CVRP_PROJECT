<template>
    <v-app>
      <v-system-bar>
        <v-app-bar-nav-icon @click.stop="mostrarMenu=!mostrarMenu">

        </v-app-bar-nav-icon>
      </v-system-bar>
      <v-navigation-drawer
        v-model="mostrarMenu"
        expand-on-hover
        temporary
        absolute
        :mini-variant='miniVariant'
      >
        <v-list>
          <v-list-item class="px-2">
            <v-list-item-avatar>
              <v-img src="./assets/cvrp.png"></v-img>
            </v-list-item-avatar>
          </v-list-item>

          <v-list-item link>
            <v-list-item-content>
              <v-list-item-title class="title">
                CVRP
              </v-list-item-title>
              <v-list-item-subtitle>CAMILO HOLGUIN</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list nav dense>
          <div v-for="m in menu"
          :key="m.nombre">
            <router-link :to='m.ruta'>
              <v-list-item link>
                <v-list-item-icon> 
                  <v-icon>
                    {{m.icono}}
                  </v-icon>    
                </v-list-item-icon>
                <v-list-item-title>
                  {{m.nombre}}
                </v-list-item-title>
              </v-list-item>
            </router-link>    
          </div>  
        </v-list>
      </v-navigation-drawer>
      <router-view></router-view>
    </v-app>
</template>

<script>

export default {
  name: 'App',
  components:{

  },
  data(){
    return{
      menu:[
        {ruta:'/', nombre:'Inicio', icono:'mdi-folder'},
        {ruta:'/pixa', nombre:'Imagenes', icono:'mdi-folder'},
      ],
      mostrarMenu:false,
      miniVariant:true,
    }
  }

}
</script>


<style>

    a:link{
      text-decoration: none;
    }

</style>
