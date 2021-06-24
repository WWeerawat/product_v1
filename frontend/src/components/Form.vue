<template>
  <div class="Form ">
    <Input
      :label1="'1. รหัสสินค้า'"
      :label2="'2. รหัสอ้างอิง'"
      :type1="'text'"
      :type2="'text'"
    />
    <Input :label1="'3. ชื่อ'" :type1="'text'" :hide="'is-hidden'" />
    <Input :label1="'4. ประเภท'" :type1="'text'" :hide="'is-hidden'" />
    <Input :label1="'5. หน่วย'" :type1="'text'" :hide="'is-hidden'" />
    <Input :label1="'6. ชนิด'" :type1="'text'" :hide="'is-hidden'" />
    <Input :label1="'7. ยี่ห้อ'" :type1="'text'" :hide="'is-hidden'" />
    <Input :label1="'8. รุ่นรถ'" :type1="'text'" :hide="'is-hidden'" />
    <Input :label1="'9. รหัสสินค้าแทน'" :type1="'text'" :hide="'is-hidden'" />
    <Input :label1="'10. รหัสสินค้าเก่า'" :type1="'text'" :hide="'is-hidden'" />
    <Input
      :label1="'11. จน.ต่ำสุด'"
      :type1="'text'"
      :label2="'12. จน.สูงสุด'"
      :type2="'text'"
    />
    <Input :label1="'13. ราคาห้าง'" :type1="'text'" :hide="'is-hidden'" />
    <Input :label1="'14. ราคาขายมาตรฐาน'" :type1="'text'" :hide="'is-hidden'" />
    <Input :label1="'15. ลักษณะพิเศษ'" :type1="'text'" :hide="'is-hidden'" />
    <Input :label1="'16. ต้นทุน/หน่วย'" :type1="'text'" :hide="'is-hidden'" />
  </div>
</template>

<script>
import Input from "@/components/Input.vue";
export default {
  name: "Form",
  components: {
    Input,
  },
};
</script>
