<template>
  <table class="table">
    <thead>
      <tr>
        <th>#</th>
        <th>ID</th>
        <th>Name</th>
        <th>Desc</th>
        <th>Serie</th>
        <th>Brand</th>
        <th>Price</th>
      </tr>
    </thead>
    <tfoot>
      <tr>
        <th>#</th>
        <th>ID</th>
        <th>Name</th>
        <th>Desc</th>
        <th>Serie</th>
        <th>Brand</th>
        <th>Price</th>
      </tr>
    </tfoot>
    <tbody>
      <TableContent
        v-for="product in productsList"
        :key="product.id"
        :product="product"
      />
    </tbody>
  </table>
</template>

<script>
import axios from "axios";
import TableContent from "../components/TableContent.vue";
export default {
  name: "ProductTable",
  data() {
    return {
      productsList: [],
    };
  },
  components: { TableContent },
  mounted() {
    this.getProductsList();
  },
  methods: {
    async getProductsList() {
      await axios
        .get("/api/productsList/")
        .then((response) => {
          this.productsList = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
