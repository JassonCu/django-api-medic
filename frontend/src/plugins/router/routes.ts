export const routes = [
  { path: '/', redirect: '/dashboard' },
  {
    path: '/',
    component: () => import('@/layouts/default.vue'),
    children: [
      {
        path: 'dashboard',
        component: () => import('@/pages/dashboard.vue'),
      },
      {
        path: 'patients',
        component: () => import('@/pages/patients.vue'),
      },
      {
        path: 'medications',
        component: () => import('@/pages/medications.vue'),
      },
      {
        path: 'doctors',
        component: () => import('@/pages/doctors.vue'),
      },
      {
        path: 'nurses',
        component: () => import('@/pages/nurses.vue'),
      },
      {
        path: 'create-report',
        component: () => import('@/pages/create-report.vue'),
      },
      {
        path: 'created-report',
        component: () => import('@/pages/created-report.vue'),
      },
    ],
  },
  {
    path: '/',
    component: () => import('@/layouts/blank.vue'),
    children: [
      {
        path: 'login',
        component: () => import('@/pages/login.vue'),
      },
      {
        path: 'register',
        component: () => import('@/pages/register.vue'),
      },
      {
        path: '/:pathMatch(.*)*',
        component: () => import('@/pages/[...error].vue'),
      },
    ],
  },
]