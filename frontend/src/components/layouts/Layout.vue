<template>
    <div
        class="layout-wrapper"
    >
        <navbar />
        <div class="layout align-items-center d-flex justify-content-center">
            <div class="list-layout">
                <scrollable>
                    <template #content>
                        <div class="content">
                            <slot name="content" />
                        </div>
                    </template>
                </scrollable>
            </div>
        </div>
    </div>
</template>

<script>
import Scrollable from '@/components/Scrollable';
import Navbar from '@/components/Navbar';

export default {
    name: "Layout",
    components: {Navbar, Scrollable}
}
</script>

<style
    lang="scss"
    scoped
>
.layout-wrapper {
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;

    .layout {
        flex-grow: 1;
        background: #3784aa;
        //background: -webkit-linear-gradient(to right, #ef8e38, #5fadd0);
        //background: linear-gradient(to right, #ef8e38, #5fadd0);

        .list-layout {
            //border-radius: 20px;
            background-color: #fcfafa;

            .content {
                padding: 31px 31px;
                width: 90vw;
                height: 90vh;
                min-width: 701px;
                overflow-y: auto;
            }
        }
    }
}
</style>