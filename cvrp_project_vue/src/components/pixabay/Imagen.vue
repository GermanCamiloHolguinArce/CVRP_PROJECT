<template>
    <div>
        <b-img :id="img.id" :src="img.previewURL" thumbnail fluid
        v-b-popover.hover.top='img.tags'
        ></b-img>
    </div>
</template>

<script>
export default {
    name:'Imagen',
    props:['img']
}
</script>
<style lang='stylus' scoped>

</style>