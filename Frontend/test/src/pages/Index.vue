<template>
  <q-page class="flex flex-center">
    <q-file v-model="model" label="Upload your images here!" />
    <q-btn
      :loading="loading1"
      :percentage="percentage1"
      color="primary"
      @click="startComputing(1)"
      style="width: 150px"
    >
      Sort Image
      <template v-slot:loading>
        <q-spinner-gears class="on-left" />
        Computing...
      </template>
    </q-btn>
  </q-page>

</template>

<script>
export default {
  name: 'PageIndex',
  data () {
    return {
      shape: 'line'
    }
  }
}

</script>
