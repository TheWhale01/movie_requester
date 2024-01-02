<template>
    <div class="loading_screen">
        <div class="loading_spinner"></div>
    </div>
</template>
<style>
.loading_screen {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.loading_spinner {
  border: 8px solid #121a2a;
  border-top: 8px solid #5046e5;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
  