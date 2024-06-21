<script lang="ts" setup>
import VerticalNavSectionTitle from '@/@layouts/components/VerticalNavSectionTitle.vue'
import VerticalNavLink from '@layouts/components/VerticalNavLink.vue'
</script>

<template>
  <!-- 👉 Dashboards -->
  <VerticalNavLink :item="{
    title: 'Dashboard',
    icon: 'ri-home-smile-line',
    to: '/dashboard',
  }" />
  <!-- 👉 Hospital -->
  <VerticalNavSectionTitle :item="{
    heading: 'HOSPITAL',
  }" />

  <VerticalNavLink :item="{
    title: 'Pacientes',
    icon: 'ri-hospital-line',
    to: '/patients',
  }" />

  <VerticalNavLink :item="{
    title: 'Medicamentos',
    icon: 'ri-capsule-line',
    to: '/medications',
  }" />

  <VerticalNavLink :item="{
    title: 'Doctores',
    icon: 'ri-health-book-line',
    to: '/doctors',
  }" />

  <VerticalNavLink :item="{
    title: 'Enfermeras',
    icon: 'ri-nurse-line',
    to: '/nurses',
  }" />



  <!-- <VerticalNavLink :item="{
    title: 'Account Settings',
    icon: 'ri-user-settings-line',
    to: '/account-settings',
  }" />

  <VerticalNavLink :item="{
    title: 'Login',
    icon: 'ri-login-box-line',
    to: '/login',
  }" />
  <VerticalNavLink :item="{
    title: 'Register',
    icon: 'ri-user-add-line',
    to: '/register',
  }" />
  <VerticalNavLink :item="{
    title: 'Error',
    icon: 'ri-information-line',
    to: '/no-existence',
  }" /> -->

  <!-- 👉 User Interface -->
  <VerticalNavSectionTitle :item="{
    heading: 'Reportes',
  }" />
  <VerticalNavLink :item="{
    title: 'Generar Reporte',
    icon: 'ri-file-chart-line',
    to: '/create-report',
  }" />
  <VerticalNavLink :item="{
    title: 'Reportes Generados',
    icon: 'ri-folder-chart-line',
    to: '/created-report',
  }" />

  <!-- 👉 Others -->
  <VerticalNavSectionTitle :item="{
    heading: 'Otros',
  }" />

  <VerticalNavLink :item="{
    title: 'Documentacióm',
    icon: 'ri-article-line',
    href: 'https://github.com/JassonCu/django-api-medic',
    target: '_blank',
  }" />
  <VerticalNavLink :item="{
    title: 'Manual de usuario',
    href: 'https://github.com/JassonCu/django-api-medic',
    icon: 'ri-lifebuoy-line',
    target: '_blank',
  }" />
</template>
