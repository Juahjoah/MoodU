<template>
  <div class="create">
    <h1>커뮤니티 게시글 작성</h1>
    <form @submit.prevent="createCommunity"></form>
    <label for="title"> 제목: </label>
    <input type="text" id="title" v-model.trim="title" />
  </div>
</template>

<script>
export default {
  name: "CommunityCreateView",
};
</script>

<style>
</style>