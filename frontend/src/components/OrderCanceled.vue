<template>
    <Layout>
        <template #content>
            <div class="container">
                <div class="row">
                    <div class="col-sm-10">
                        <h3>{{ $t('payment.cancel') }}</h3>
                        <hr><br>
                        <router-link
                            :to="{name: 'dashboardBookings', params: {uuid: hotelId}}"
                            class="btn btn-primary btn-sm"
                        >
                            {{ $t('payment.back') }}
                        </router-link>
                    </div>
                </div>
            </div>
        </template>
    </Layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";

export default {
    name: "OrderCanceled",
    components: {Layout},
    computed: {
        hotelId() {
            return this.$store.getters['booking/hotel_id']
        }
    }
}
</script>

<style scoped>

</style>