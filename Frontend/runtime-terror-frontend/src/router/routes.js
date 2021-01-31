
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },
  
  {
    path: '/Discover',
    component: () => import('layouts/DiscoverLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Discover.vue') }
    ]
  },

  {
    path: '/Favourites',
    component: () => import('layouts/FavouritesLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Favourites.vue') }
    ]
  },

  {
    path: '/Settings',
    component: () => import('layouts/SettingsLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Settings.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
