<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn flat round dense icon="menu" class="q-mr-sm" />
        <q-toolbar-title>Photo Organizer</q-toolbar-title>
        <q-btn flat round dense icon="whatshot" />
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
    <q-footer elevated>
      <q-toolbar/>
    </q-footer>
  </q-layout>
</template>
