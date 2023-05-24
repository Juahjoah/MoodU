<template>
  <div class="CommunityListForm">
    <table class="communitytable">
      <tr>
        <th>   게시글 번호   </th>
        <th>   제목   </th>
        <th>   작성자   </th>
        <th>   작성일   </th>
      </tr>
      <tr
        class="communitylist"
        v-for="(community, idx) in communities"
        :key="idx"
        
      >
        <td @click.self.prevent="CommunityDetail(community)">{{ community.id }}</td>
        <td @click.self.prevent="CommunityDetail(community)"
          class="articletitle"
          
        >
          {{ community.title }}
        </td >
        <td @click.self.prevent="CommunityDetail(community)">{{ community.username }}</td>
        <td @click.self.prevent="CommunityDetail(community)">{{ community.created_at }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "CommunityListForm",
  props: {
    communities: Array,
  },
  methods: {
    CommunityDetail(community) {
      this.$router.push({
        name: "CommunityDetail",
        params: { id: community.id },
      });
    },
  },
};
</script>

<style scoped>
* {
  font-size: 15px;
}


.communitytable {
  margin: 20px auto 0px auto;
  display: inline-block;
}

.communitytable,
.communitytable th,
.communitytable td {
  border: 1px solid gray;
  border-width: 1px 0;
  border-collapse: collapse;
  text-align: center;
  padding: 8px;
}

.communitytable th {
  background-color: #AFAEAB;
  font-size: 1.1em;
  color: #fff;
  border-width: 2px 0;
}

.communitytable td {
  border-style: dotted;
  /* display: inline-block; */
  margin: 0.5rem;
  text-align: center;
  align-items: center;
}

.communitytable tr:hover td {
  background-color: #f8eded;
  cursor: pointer;
}
</style>