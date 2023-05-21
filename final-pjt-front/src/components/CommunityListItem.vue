<template>
  <div class="CommunityItem">
    <p>제목: {{ communityarticle.title }}</p>
    <p>이거 굴러가나요</p>
  </div>
</template>

<script>
export default {
  name: "CommunityListItem",
  data() {
    return {};
  },
  props: {
    communityarticle: Object,
  },
  methods: {},
};
</script>

<style>
</style>