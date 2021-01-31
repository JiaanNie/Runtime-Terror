<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-blue-grey-2 text-blue-10">
      <q-toolbar>
        <q-toolbar-title>
          Discover
        </q-toolbar-title>
        <q-btn dense flat >
      <i class="fas fa-search" style="font-size: 20px;"></i>
    </q-btn>
         <q-btn dense flat>
      <i class="fa fa-filter" aria-hidden="true" style="font-size: 20px;"></i>
    </q-btn>
         <q-btn dense flat>
      <i class="fa fa-bell" aria-hidden="true" style="font-size: 20px;"></i>
    </q-btn>
    </div>
      </q-toolbar>
    </q-header>

<q-footer elevated class="bg-blue-grey-2 text-blue-10">
        <q-tabs
        v-model="tab"
         indicator-color="transparent"
         active-color="blue-8"
        dense
      >
      <q-route-tab 
      to="/"
      name="albums" 
      icon="photo_library" 
      label="Albums" />

        <q-route-tab 
        to="/Discover"
        name="discover" 
        icon="explore" 
        label="Discover" />

        <q-route-tab 
        to="/Favourites"
        name="favourites" 
        icon="grade" 
        label="Favourites" />

        <q-route-tab 
        to="/Settings"
        name="settings" 
        icon="settings" 
        label="Settings" />
      </q-tabs>
      </q-footer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
