<template>
    <Layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('favorite.favorite.title') }}
                </h2>
            </div>
            <hr>
            <div class="row">
                <div
                    v-for="favorite in favorites"
                    :key="favorite.uuid"
                    class="col-md-6 col-sm-12"
                    @dblclick="$router.push({name: 'createFavorite', params: {uuid: favorite.hotelid}})"
                >
                    <b-card
                        img-top
                        class="mb-2 p-1"
                        tag="article"
                    >
                        <b-card-img
                            :src="hotelImage(favorite.image)"
                            class="mb-2"
                            :height="300"
                        />
                        <b-card-title
                            :title="favorite.name"
                            title-tag="h2"
                            class="p-inline"
                        />
                        <p class="p-inline">
                            <b-form-rating
                                v-model="favorite.star"
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
                                {{ favorite.rating }} / 5
                            </b-badge>
                        </p>
                        <p>
                            <span class="font-weight-bolder">
                                {{ $t('hotel.hotel.address') }}
                            </span>
                            <span class="text-secondary">
                                {{ getAddress(favorite.address, favorite.ward, favorite.district, favorite.city) }}
                            </span>
                        </p>
                        <b-button
                            variant="danger"
                            @click="onDelete(favorite.uuid)"
                        >
                            {{ $t('hotel.hotel.discardBtn') }}
                        </b-button>
                    </b-card>
                </div>
            </div>
            <br>
            <span
                v-if="favorites.length === 0"
                style="font-style: italic"
            >
                {{ $t('favorite.favorite.noResult') }}
            </span>
        </template>
    </Layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";
import json from '../../mixin/data/db_en.json'
import {getDistrictsByProvinceCode, getWardsByDistrictCode, getProvinces} from 'sub-vn';
import dataUtil from "@/utils/data-view-utils"
import {validationMixin} from "vuelidate";


export default {
    name: "Favorite",
    components: {Layout},
    mixins: [validationMixin, dataUtil],
    data: function () {
        return {
            favorites: []
        }
    },
    created() {
        this.$store.dispatch('favorite/listFavorites').then(() => {
            this.favorites = this.$store.getters['favorite/favorites']
            this.favorites.sort(function (a, b){
                return a.name.localeCompare(b.name)
            })
        })
    },
    methods: {
        getAddress: function (address, ward, district, city) {
            // let city_en = city
            // let district_en = district
            // let ward_en = ward
            // if (localStorage.getItem("language") === "en") {
            //     let city_code = getProvinces().filter(option => option.name === city)[0].code
            //     const provinces = json.province
            //     city_en = provinces.filter(option => option.idProvince === city_code)[0].name
            //     let district_code = getDistrictsByProvinceCode(city_code).filter(option => option.name === district)[0].code
            //     const dists = json.district
            //     district_en = dists.filter(option => option.idDistrict === district_code)[0].name
            //     let ward_code = getWardsByDistrictCode(district_code).filter(option => option.name === ward)[0].code
            //     const communes = json.commune
            //     ward_en = communes.filter(option => option.idCoummune === ward_code)[0].name
            // }
            // if (address == null || address === "") {
            //     return ward_en + ", " + district_en + ", " + city_en
            // } else {
            //     return address + ", " + ward_en + ", " + district_en + ", " + city_en
            // }
            // // if (address == null || address === "") {
            // //     return ward + ", " + district + ", " + city
            // // } else {
            // //     return address + ", " + ward + ", " + district + ", " + city
            // // }
            return this.getTransAddress(address, ward, district, city)
        },
        hotelImage: function (uri) {
            // return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
            return this.getHotelImage(uri)
        },
        onDelete: function(uuid) {
            this.$store.dispatch('favorite/resetStatus')
            this.$store.dispatch('favorite/deleteFavoriteFromList', {favoriteId: uuid})
                .then(() => {
                    // Alert for failed api call
                    if (this.$store.getters['favorite/status'] === 'FAILED') {
                        this.makeToast(this.$t('favorite.favorite.errors.removeTitle'), this.$t('favorite.favorite.errors.exceptionOccurred'))
                    } else {
                        this.$bvToast.toast(this.$t('favorite.favorite.success.removeMessage'), {
                            title: this.$t('favorite.favorite.success.removeTitle'),
                            autoHideDelay: 2000,
                            variant: 'success'
                        })
                        setTimeout(location.reload.bind(location), 2000)
                    }
                })
        }
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