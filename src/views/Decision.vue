<style scoped>
.container {
    display: flex;
    flex-direction: column;
}

.outcome {
    margin-bottom: 2rem;
}

.decisions {
    justify-content: center;
}

.decision {
    font-size: 1rem;
}
</style>
<template>
    <div class="container">
        <div class="outcome">{{ outcome }}</div>
        <v-row class="decisions">
            <v-col
                md="4"
                sm="6"
                class="decision"
                v-for="decision in decisions"
                :key="decision.targetName"
            >
                <v-btn large v-on:click="decisionClick(decision)">{{
                    decision.description
                }}</v-btn>
            </v-col>
        </v-row>
    </div>
</template>

<script>
import { initialize, getNext } from '../lib/sampleDataApi';
import router from '../router';

export default {
    router,
    name: 'Decision.vue',
    data: function() {
        const initialData = initialize();
        return {
            ...initialData
        };
    },
    methods: {
        decisionClick: function(decision) {
            if (decision.targetName === 'start') {
                const { outcome, decisions } = initialize();
                this.outcome = outcome;
                this.decisions = decisions;
            } else if (decision.targetName === 'quit') {
                this.$router.push('/');
            } else {
                const { outcome, decisions } = getNext(decision);
                this.outcome = outcome;
                this.decisions = decisions;
            }
        }
    }
};
</script>
