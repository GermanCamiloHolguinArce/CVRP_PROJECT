<template>
    <div>
        <b-row align-h='center'> 
            <b-col md='6'>
                <b-form-input v-model="buscar" 
                placeholder="Buscar Imagenes"
                @keypress.enter="buscarHijo"
                ></b-form-input>
            </b-col>
            <b-col md='1'>
                <b-button variant="primary" @click="buscarHijo">
                    Buscar
                </b-button>
            </b-col>
        </b-row>
        <b-row>
            <b-col v-for="img in pixaImagenes" :key="img.id" md="2" class="py-2 text-center">
                <!-- <b-img :id="img.id" :src="img.previewURL" thumbnail fluid></b-img>            -->
                <Imagen :img='img'/>
            </b-col>
        </b-row>
    </div>
</template>

<script>
export default {
    name:'Buscador'
    data(){
        return{
            buscar:''
        }
    },
    methods: {
        buscarHijo(){
            this.$emit('buscarDesdeHijo',this.buscar)
        }
        
    }
}
</script>
<style lang='stylus' scoped>

</style>