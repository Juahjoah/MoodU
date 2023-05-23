<template>
    <div>
        <h1>모듀님의 기분에 따른 영화를 추천해 드릴게요!</h1>
        <div>
            <span @click="emotionSelect('happy')">행복해요</span> |
            <span @click="emotionSelect('sad')">슬퍼요</span> |
            <span @click="emotionSelect('soso')">그저 그래요</span> |
            <span @click="emotionSelect('joy')">신나요</span> |
            <span @click="emotionSelect('angry')">화나요</span> |
        </div>
        <RecommendMovie :emo='emo'/>
    </div>
</template>

<script>
import RecommendMovie from '@/components/RecommendMovie'
export default {
    data() {
        return {
            emo: null,
        }
    },
    methods: {
        emotionSelect(e) {
            console.log(e)
            this.emo = e
       }
    },
    components: {
        RecommendMovie,
    },
}
</script>

<style>

</style>