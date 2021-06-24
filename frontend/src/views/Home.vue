<template>
  <div class="home">
    <h1 class="is-size-1 has-text-centered mb-4">Home</h1>
    <ProductTable />
  </div>
</template>

<script>
// @ is an alias to /src
import ProductTable from "../components/ProductTable.vue";
export default {
  name: "Home",
  components: { ProductTable },
};
</script>
