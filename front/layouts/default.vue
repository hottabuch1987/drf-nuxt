<template>
  <div class="page">
    <AppHeader />
    
    <main class="main mt-20" >
    <Toast />
    
      <slot></slot>
    </main>
    
   
    <AppFooter />
  </div>
</template>

<script setup>
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';
import Toast from './components/Toast.vue';

</script>