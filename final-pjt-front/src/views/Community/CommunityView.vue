<template>
  <div class="community">
    <h1>여러분의 생각을 들려주세요.</h1>
    <article>
      <p>article list가 들어올 예정</p>
      <CommunityListForm />
    </article>
    <br />
    <hr />
    <router-link :to="{ name: 'CommunityCreate' }">[CREATE]</router-link>
  </div>
</template>

<script>
import CommunityListForm from "@/components/CommunityListForm.vue";

export default {
  name: "CommunityView",
  components: {
    CommunityListForm,
  },
  methods: {},
};
</script>

<style>
</style>