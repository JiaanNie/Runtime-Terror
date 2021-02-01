<template>
  <q-layout
  view="lHh Lpr lFf">
    <po_header></po_header>
    <q-page-container>
      <router-view />
    </q-page-container>
    <po_footer></po_footer>
  </q-layout>
</template>

<script>
import footer from 'src/components/footer.vue'
import header from 'src/components/header.vue'
export default {
  components: {
    po_footer: footer,
    po_header: header
  }
}

</script>
