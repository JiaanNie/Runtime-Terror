<template>
  <q-page padding class="absolute-center">
    <q-card inline style="width: 375px">
      <q-card-media>
        <q-img src="https://cdn.quasar.dev/img/parallax2.jpg"/>
      </q-card-media>
      <q-card-title>
        Cafe Basilico
      </q-card-title>
      <q-card-main style="height: 300px">
        <p>$・Italian, Cafe</p>
        <p class="text-faded">Small plates, salads & sandwiches in an intimate setting.</p>
      </q-card-main>
      <q-separator />
      <q-card-actions>
        <q-btn flat round icon="event" />
        <q-btn flat color="primary">
          Reserve
        </q-btn>
      </q-card-actions>
    </q-card>
</q-page>
</template>

<script>
import secret from 'src/keys'
export default {
  name: 'Discover',
  created: function () {
    console.log(secret)
    console.log('hi')
  }
}
</script>
