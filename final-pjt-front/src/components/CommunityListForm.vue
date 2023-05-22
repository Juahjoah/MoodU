<template>
  <div class="CommunityListForm">
    <div
      class="communitylist"
      v-for="(community, idx) in communities"
      :key="idx"
    >
      <!-- <p>{{community}}</p> -->
      <router-link
        :to="{ name: 'CommunityDetail', params: { id: community.id } }"
      >
        <p>{{ community.id }} {{ community.title }} {{ community.content }}</p>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommunityListForm",
  props: {
    communities: Array,
  },
  methods: {},
};
</script>

<style>
</style>