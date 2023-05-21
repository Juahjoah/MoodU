<template>
  <div class="CommunityListForm">
    <div class="communitylist" v-for="(community, idx) in communities" :key="idx">
        <p>{{community}}</p>
        <p> {{community.id}} </p>
        <p> {{community.title}} </p>
        <p> {{community.content}} </p>
    </div>
  </div>
</template>

<script>

export default {
  name: "CommunityListForm",
  props: {
    communities: Array,
  },
  methods: {

  }
};
</script>

<style>
</style>