<template>
    <div class="row">
        <!--  Recommendation list      -->
        <div
            v-for="recommendation in recommendations"
            :key="recommendation.uuid"
            class="col-md-4 col-sm-10"
            @dblclick="$router.push({name: 'createFavorite', params: {uuid: recommendation.uuid}})"
        >
            <!--    Recommendation hotel info        -->
            <b-card
                img-top
                class="p-1 mb-2"
                tag="article"
            >
                <b-card-img
                    :src="hotelImage(recommendation.image)"
                    class="mb-2"
                    style="height: 200px; width: 100%"
                />
                <b-card-title
                    :title="recommendation.name"
                    title-tag="h2"
                    class="p-inline"
                />
                <p class="p-inline">
                    <b-form-rating
                        v-model="recommendation.star"
                        variant="warning"
                        no-border
                        inline
                        readonly
                    />
                </p>
                <p>
                    <span class="font-weight-bolder">
                        {{ $t('hotel.hotel.rating') }}:
                    </span>
                    <b-badge
                        pill
                        variant="info"
                        class="badge-size"
                    >
                        {{ recommendation.rating }} / 5
                    </b-badge>
                </p>
                <p>
                    <span class="font-weight-bolder">
                        {{ $t('hotel.hotel.address') }}
                    </span>
                    <span class="text-secondary">
                        {{ getAddress(recommendation.address, recommendation.ward, recommendation.district, recommendation.city) }}
                    </span>
                </p>
            </b-card>
        </div>
    </div>
</template>

<script>
export default {
    name: "Recommendation",
    data: function () {
        return {
            // Recommendation data
            recommendations: []
        }
    },
    created() {
        // Get recommendation data
        this.$store.dispatch('recommendation/listRecommendations', this.$route.params.uuid).then(() => {
            this.recommendations = this.$store.getters['recommendation/recommendations']
        })
    },
    methods: {
        getAddress: function (address, ward, district, city) {
            if (address == null || address === "") {
                return ward + ", " + district + ", " + city
            } else {
                return address + ", " + ward + ", " + district + ", " + city
            }
        },
        // Get hotel image
        hotelImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
        },
    }
}
</script>

<style
    lang="scss"
    scoped
>
.p-inline {
    display: inline-block;
}
</style>