<template>
    <div
        class="layout-wrapper"
    >
        <!--  Navigation bar   -->
        <navbar />
        <div class="layout align-items-center d-flex justify-content-center">
            <div class="form-layout">
                <h2 class="title">
                    <!--    Form title   -->
                    <slot name="title" />
                </h2>
                <scrollable>
                    <template #content>
                        <!--   Form content    -->
                        <div class="form">
                            <slot name="form" />
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
    name: "AuthLayout",
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
        background: -webkit-linear-gradient(to right, #ef8e38, #3784aa);
        background: linear-gradient(to right, #ef8e38, #3784aa);

        .form-layout {
            border-radius: 21px;
            background-color: #fcfafa;

            .title {
                padding: 31px 31px 0;
            }

            .form {
                padding: 31px 31px;
                width: 37%;
                min-width: 701px;
                max-height: 751px;
                overflow-y: auto;
            }
        }
    }
}
</style>