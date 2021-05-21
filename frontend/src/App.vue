<template>
    <div
        id="app"
        @contextmenu="handleContextMenu($event)"
    >
        <!--   App component     -->
        <scrollable>
            <template #content>
                <div class="app-content">
                    <router-view :key="$route.fullPath" />
                </div>
            </template>
        </scrollable>
    </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Scrollable from '@/components/Scrollable';

export default {
    name: 'App',
    components: {Scrollable},
    methods: {
        // Handle right click
        handleContextMenu: function (e) {
            // e.preventDefault()
        }
    }
};
</script>

<style lang="scss">
//@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;1,100;1,200;1,300;1,400;1,500&display=swap');

#app {
    font-family: 'Montserrat', sans-serif;
    user-select: none;
    color: #273a4c;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;


    .app-content {
        overflow: auto;
        height: 100vh;
    }
}
</style>
