<template>
  <div class="CommunityListForm">
    <div class="communitylist" v-for="(community, idx) in communities" :key="idx">
        <!-- <p>{{community}}</p> -->
        <p> {{community.id}} {{community.title}} {{community.content}} </p>
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