<template>
  <div class="hello">
      <button>{{ startBtn }}</button>
  </div>
</template>

<script>
export default {
  name: 'MainMenu',
  props: {
    startBtn: String
  }
}
</script>

<style scoped>
button {
    color: gold;
    background-color: gray;
    border-radius: 1em;
    font-size: 2em;
    border: .3em solid gray;
}
</style>
