<template>
  <q-header elevated
  class="bg-primary text-white shadow-2">
    <q-toolbar>
      <q-toolbar-title>
        Albums
      </q-toolbar-title>
      <q-btn v-if="!isReady" dense flat>
         <i class="fa fa-search" aria-hidden="true" style="font-size: 20px;" @click="isReady = true"></i>
      </q-btn>
      <q-input v-if="isReady" dark dense standout v-model="text" input-class="text-right" class="q-ml-md">
        <template v-slot:append>
          <q-icon v-if="text === ''" name="search" @click="isReady = false"/>
          <q-icon v-else name="clear" class="cursor-pointer" @click="text = ''; isReady = false" />
        </template>
      </q-input>
      <!-- <q-btn dense flat>
         <i class="fa fa-filter" aria-hidden="true" style="font-size: 20px;" ></i>
      </q-btn> -->
      <q-btn-dropdown color="primary">
      <q-list>
        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>Photos</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>Videos</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onItemClick">
          <q-item-section>
            <q-item-label>Articles</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
      <q-btn dense flat>
        <i class="fas fa-cog" aria-hidden="true" style="font-size: 20px;"></i>
      </q-btn>
    </q-toolbar>
  </q-header>
</template>
<script>
import axios from 'axios'
// const URL = 'http://ec2-3-97-34-208.ca-central-1.compute.amazonaws.com:5000/'
const URL = 'http://localhost:5000/'
export default {
  data () {
    return {
      isReady: false,
      labels: [],
      showLabels: false
    }
  },
  created: function () {
    var vm = this
    axios.get(URL + 'labels').then((res) => {
      for (var index in res.data) {
        vm.labels.push(res.data[index])
      }
    })
  }
}
</script>
