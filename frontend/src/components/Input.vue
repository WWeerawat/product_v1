<template>
  <div class="field is-horizontal">
    <div class="field-label is-normal">
      <label class="label">{{ label1 }}</label>
    </div>
    <div class="field-body">
      <div class="field">
        <p class="control is-expanded ">
          <input class="input" :type="type1" placeholder="" />
        </p>
      </div>
    </div>

    <div class="field-label is-normal">
      <label class="label">{{ label2 }}</label>
    </div>
    <div class="field-body">
      <div class="field">
        <p class="control is-expanded ">
          <input class="input" :class="hide" :type="type2" placeholder="" />
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Input",
  props: {
    label1: String,
    type1: String,
    label2: String,
    type2: String,
    hide: String,
  },
};
</script>

<style scoped>
.field-label {
  margin-left: 1rem;
  text-align: left;
}
</style>
