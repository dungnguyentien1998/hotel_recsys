<template>
    <div class="row">
        <div
            v-for="recommendation in recommendations"
            :key="recommendation.uuid"
            class="col-md-4 col-sm-10"
            @dblclick="$router.push({name: 'createFavorite', params: {uuid: recommendation.uuid}})"
        >
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
import json from '../../mixin/data/db_en.json'
import {getDistrictsByProvinceCode, getWardsByDistrictCode, getProvinces} from 'sub-vn';

export default {
    name: "Recommendation",
    data: function () {
        return {
            recommendations: []
        }
    },
    created() {
        this.$store.dispatch('recommendation/listRecommendations', this.$route.params.uuid).then(() => {
            this.recommendations = this.$store.getters['recommendation/recommendations']
            this.recommendations.sort(function (a,b) {
                return new Date(b.created) - new Date(a.created)
            })
        })
    },
    methods: {
        getAddress: function (address, ward, district, city) {
            let city_en = city
            let district_en = district
            let ward_en = ward
            if (localStorage.getItem("language") === "en") {
                let city_code = getProvinces().filter(option => option.name === city)[0].code
                const provinces = json.province
                city_en = provinces.filter(option => option.idProvince === city_code)[0].name
                let district_code = getDistrictsByProvinceCode(city_code).filter(option => option.name === district)[0].code
                const dists = json.district
                district_en = dists.filter(option => option.idDistrict === district_code)[0].name
                let ward_code = getWardsByDistrictCode(district_code).filter(option => option.name === ward)[0].code
                const communes = json.commune
                ward_en = communes.filter(option => option.idCoummune === ward_code)[0].name
            }
            if (address == null || address === "") {
                return ward_en + ", " + district_en + ", " + city_en
            } else {
                return address + ", " + ward_en + ", " + district_en + ", " + city_en
            }
            // if (address == null || address === "") {
            //     return ward + ", " + district + ", " + city
            // } else {
            //     return address + ", " + ward + ", " + district + ", " + city
            // }
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