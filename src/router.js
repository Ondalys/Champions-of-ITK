import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/select',
            name: 'select',
            component: () => import('./views/Select.vue')
        },
        {
            path: '/decision',
            name: 'decision',
            component: () => import('./views/Decision.vue')
        },
        {
            path: '/create-entry',
            name: 'create-entry',
            component: () => import('./views/CreateEntry.vue')
        }
    ]
});
