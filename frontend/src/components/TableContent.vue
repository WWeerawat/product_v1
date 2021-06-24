<template>
  <tr>
    <th></th>
    <td>
      <strong>
        {{ product.id }}
      </strong>
    </td>
    <td>{{ product.name }}</td>
    <td>{{ product.description }}</td>
    <td>{{ product.serie.name }}</td>
    <td>{{ product.brand.name }}</td>
    <td>{{ product.price }}</td>
  </tr>
</template>

<script>
export default {
  name: "TableContent",
  props: {
    product: Object,
  },
};
</script>
