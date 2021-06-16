<template>
    <div>
        <b-form>
            <h3 class="p-inline">
                <span class="font-weight-bolder">
                    {{ hotel.name }}
                </span>
            </h3>
            <p class="p-inline">
                <b-form-rating
                    v-model="hotel.star"
                    variant="warning"
                    no-border
                    inline
                    readonly
                />
            </p>
            <b-form-group
                id="image-group"
                label=""
                label-for="image"
            >
                <b-card-img
                    :src="hotelImage(hotel.image)"
                />
                <!--                <div-->
                <!--                    id="map"-->
                <!--                    style="float: right"-->
                <!--                />-->
            </b-form-group>
            <p>
                <img
                    src="../../assets/phone.png"
                    alt="phone"
                    class="icon"
                    style="height:20px; width:20px"
                >
                <span>
                    {{ hotel.tel }}
                </span>
                -
                <img
                    src="../../assets/email.png"
                    alt="email"
                    class="icon"
                    style="height:20px; width:20px"
                >
                <span>
                    {{ hotel.email }}
                </span>
            </p>
            <p>
                <span class="font-weight-bolder">
                    {{ $t('hotel.hotel.address') }}
                </span>
                <span>
                    {{ getAddress(hotel.address, hotel.ward, hotel.district, hotel.city) }}
                </span>
            </p>
            <div>
                <span class="font-weight-bolder">
                    {{ $t('hotel.hotel.amenities') }}
                </span>
                <div class="test">
                    <ul
                        style="padding: 0; list-style-type: none"
                    >
                        <li
                            v-for="(amenity, index) in hotel.amenities"
                            :key="`${hotel.uuid}-amenity-${index}`"
                        >
                            <img
                                :src="getSrc(amenity)"
                                :alt="amenity"
                                class="icon"
                            >
                            {{ amenity }}
                        </li>
                    </ul>
                </div>
            </div>
            <div class="mt-3">
                <b-button
                    v-if="roleUser"
                    v-model="myToggle"
                    :disabled="myToggle === true"
                    variant="primary"
                    size="sm"
                    @click="onSubmit"
                >
                    {{ $t('hotel.hotel.favoriteBtn') }}
                </b-button>
                <b-button
                    v-if="roleUser"
                    v-model="myToggle"
                    :disabled="myToggle === false"
                    variant="danger"
                    size="sm"
                    @click="onDelete"
                >
                    {{ $t('hotel.hotel.removeBtn') }}
                </b-button>
                <b-button
                    v-if="roleHotelier"
                    variant="primary"
                    href="#"
                    size="sm"
                    style="width: 80px"
                    @click="$bvModal.show(`modal-${hotel.uuid}-update`)"
                >
                    {{ $t('hotel.hotel.updateBtn') }}
                </b-button>
                <b-button
                    v-if="roleHotelier"
                    class="ml-2"
                    variant="danger"
                    href="#"
                    size="sm"
                    style="width: 80px"
                    @click="$bvModal.show(`modal-${hotel.uuid}-delete`)"
                >
                    {{ $t('hotel.hotel.deleteBtn') }}
                </b-button>
            </div>
            <b-modal
                :id="`modal-${hotel.uuid}-update`"
                :title="$t('hotel.hotel.updateTitle')"
                size="lg"
                hide-footer
            >
                <hotel-form :hotel="hotel" />
            </b-modal>
            <b-modal
                :id="`modal-${hotel.uuid}-delete`"
                :title="$t('hotel.hotel.deleteTitle')"
                size="lg"
                button-size="sm"
                :ok-title="$t('button.submit')"
                :cancel-title="$t('button.unsubmit')"
                @ok="deleteHotel(hotel.uuid)"
            >
                {{ $t('hotel.hotel.confirmDelete') }}
            </b-modal>
        </b-form>
        <hr>
        <div
            v-if="roleUser"
            class="align-items-center d-flex"
        >
            <h2 class="flex-grow-1">
                {{ $t('hotel.hotel.recommendedLabel') }}
            </h2>
        </div>
        <br>
        <div
            v-if="roleUser"
            class="row"
        >
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
                    style="height: 505px"
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
    </div>
</template>

<script>
import HotelForm from '@/components/HotelForm';
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import addressMixin from '@/mixin/address-mixin'
import mapboxgl from "mapbox-gl";
import mapboxSdk from "@mapbox/mapbox-sdk/umd/mapbox-sdk";
import roleUtil from "@/utils/role-utils"
import dataUtil from "@/utils/data-view-utils"


export default {
    name: "FavoriteForm",
    components: {HotelForm},
    mixins: [validationMixin, formMixin, addressMixin, roleUtil, dataUtil],
    data: function () {
        return {
            myToggle: false,
            hotel: this.$store.getters['hotel/hotels'].filter(hotel => hotel.uuid === this.$route.params.uuid)[0],

            favorites: [],
            favorite: [],
            recommendations: [],
        }
    },
    computed: {
        roleUser: function () {
            return this.getRoleUser()
        },
        roleHotelier: function () {
            return this.getRoleHotelier()
        },
    },
    mounted() {
        const plugin = document.createElement("script")
        plugin.setAttribute("src", "https://unpkg.com/@mapbox/mapbox-sdk/umd/mapbox-sdk.min.js")
        document.head.appendChild(plugin)
        const style = document.createElement("link")
        style.setAttribute("href", "https://api.mapbox.com/mapbox-gl-js/v2.2.0/mapbox-gl.css")
        style.setAttribute("rel", "stylesheet")
        document.head.appendChild(style)
        const plugin1 = document.createElement("script")
        plugin1.setAttribute("src", "https://api.mapbox.com/mapbox-gl-js/v2.2.0/mapbox-gl.js")
        document.head.appendChild(plugin1)
        const plugin2 = document.createElement("script")
        plugin2.setAttribute("src", "https://unpkg.com/es6-promise@4.2.4/dist/es6-promise.auto.min.js")
        document.head.appendChild(plugin2)

        // mapboxgl.accessToken = 'pk.eyJ1IjoiZHVuZ250MjEzIiwiYSI6ImNrb3d5d3hoajA5ZGozMG1qZHlydXR0bmMifQ.PDS9TCnddZ0b0XuaxRW7yg';
        // let mapboxClient = mapboxSdk({ accessToken: mapboxgl.accessToken });
        // mapboxClient.geocoding
        //     .forwardGeocode({
        //         query: this.hotel.ward + ", " + this.hotel.district + ", " + this.hotel.city,
        //         autocomplete: false,
        //         limit: 1
        //     })
        //     .send()
        //     .then(function (response) {
        //         if (
        //             response &&
        //             response.body &&
        //             response.body.features &&
        //             response.body.features.length
        //         ) {
        //             let feature = response.body.features[0];
        //
        //             let map = new mapboxgl.Map({
        //                 container: 'map',
        //                 style: 'mapbox://styles/mapbox/streets-v11',
        //                 center: feature.center,
        //                 zoom: 15
        //             });
        //
        //             // Create a marker and add it to the map.
        //             new mapboxgl.Marker().setLngLat(feature.center).addTo(map);
        //         }
        //     });
    },
    created() {
        // Handle toggle data
        this.$store.dispatch('favorite/listFavorites', this.$route.params.uuid)
            .then(() => {
                this.favorites = this.$store.getters['favorite/favorites']
                this.favorite = this.favorites.filter(favorite => favorite.hotelid === this.$route.params.uuid)
                this.myToggle = this.favorite.length > 0;
            })
        this.$store.dispatch('type/listTypes', this.$route.params.uuid)
        this.$store.dispatch('recommendation/listRecommendations', this.$route.params.uuid).then(() => {
            this.recommendations = this.$store.getters['recommendation/recommendations']
        })
    },
    methods: {
        getAddress: function (address, ward, district, city) {
            return this.getTransAddress(address, ward, district, city)
        },
        hotelImage: function (uri) {
            return this.getHotelImage(uri)
        },
        getSrc: function (amenity) {
            return this.getImgSrc(amenity)
        },
        // Handle save to favorite
        onSubmit: function () {
            this.myToggle = !this.myToggle
            if (this.myToggle === true) {
                this.$store.dispatch('favorite/resetStatus')
                this.$store.dispatch('favorite/createFavorite', this.$route.params.uuid)
                // Alert for success
                this.$bvToast.toast(this.$t('favorite.favorite.success.saveMessage'), {
                    title: this.$t('favorite.favorite.success.saveTitle'),
                    autoHideDelay: 5000,
                    variant: 'success'
                })
            }
        },
        // Handle remove from favorite
        onDelete: function () {
            this.myToggle = !this.myToggle
            if (this.myToggle === false) {
                this.$store.dispatch('favorite/resetStatus')
                const favorites = this.$store.getters['favorite/favorites']
                const favoriteId = favorites.filter(favorite => favorite.hotelid === this.$route.params.uuid)[0].uuid
                this.$store.dispatch('favorite/deleteFavorite', {hotelId: this.$route.params.uuid, favoriteId: favoriteId})
                    .then(() => {
                        // Alert for failed api call
                        if (this.$store.getters['favorite/status'] === 'FAILED') {
                            this.makeToast(this.$t('favorite.favorite.errors.removeTitle'), this.$t('favorite.favorite.errors.exceptionOccurred'))
                        } else {
                            this.$bvToast.toast(this.$t('favorite.favorite.success.removeMessage'), {
                                title: this.$t('favorite.favorite.success.removeTitle'),
                                autoHideDelay: 5000,
                                variant: 'success'
                            })
                        }
                    })
            }
        },
        deleteHotel: function (uuid) {
            this.$store.dispatch('hotel/resetStatus')
            this.$store.dispatch('hotel/deleteHotel', uuid)
                .then(() => {
                    if (this.$store.getters['hotel/status'] === 'FAILED') {
                        // Alert for failed api call
                        this.makeToast(this.$t('hotel.hotel.errors.title'), this.$t('hotel.hotel.errors.exceptionOccurred'))
                    } else {
                        this.$router.push('/dashboard/hotels')
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
.card-img {
    height: 50%;
    width: 50%;
    object-fit: cover;
}
.icon {
    height: 30px;
    width: 30px;
}
.p-inline {
    display: inline-block;
}
#map {
    position: absolute;
    top: 150px;
    right: 30px;
    //bottom: 0;
    width: 25%;
    height: 15%;
}

.test ul {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
}
.test ul li {
    list-style: none;
    flex: 0 0 20%;
}

</style>