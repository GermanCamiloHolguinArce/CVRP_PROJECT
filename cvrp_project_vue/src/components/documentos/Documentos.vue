<template>
<div id="app"></div>
    
</template>

<script>
export default {
    name:'documentos',
    component:{

    },
    data:() => {
        return{
            nuevo:{
                id:-1,
                nombre: 'Nuevo Documento',
                siglas: 'Siglas Documento',
            },
            item: []
        }
    },
    mounted(){
        try{
            this.$store.commit('setItems');
        }
        catch (error){
            console.log(error);
        }
    },
    computed:{
        allItems(){
            return this.$store.state.items;
        }
    }
}
</script>

<style  scoped>

</style>