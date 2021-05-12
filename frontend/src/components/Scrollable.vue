<template>
    <div class="scrollable">
        <slot name="content" />
    </div>
</template>

<script>
export default {
    // Scrollable component
    name: "Scrollable",
}
</script>

<style
    lang="scss"
    scoped
>
.scrollable {
    ::-webkit-scrollbar {
        background-color: rgba(0,0,0,0);
        width: 7px;
    }

    ::-webkit-scrollbar-track {
        background-color: rgba(0,0,0,0);
    }

    ::-webkit-scrollbar-thumb {
        border-radius: 5px;
        background-color: #aaa5a5;
    }
}
</style>