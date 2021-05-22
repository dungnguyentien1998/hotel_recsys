<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Thanks for purchasing!</h1>
                <hr><br>
                <router-link
                    :to="{name: 'dashboardBookings'}"
                    class="btn btn-primary btn-sm"
                >
                    Back Home
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "OrderSuccess"
}
</script>

<style scoped>

</style>