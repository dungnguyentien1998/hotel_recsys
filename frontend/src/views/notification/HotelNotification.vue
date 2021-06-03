<template>
    <Layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('hotel.hotel.notificationTitle') }}
                </h2>
            </div>
            <br>
            <b-list-group>
                <b-list-group-item
                    v-for="hotel in hotels"
                    :key="hotel.uuid"
                    class="list-item"
                >
                    <div>
                        <b-img
                            :src="hotelImage(hotel.image)"
                            style="float: right"
                            alt="image"
                            thumbnail
                            fluid
                        />
                    </div>
                    <div>
                        <b-card-title
                            :title="hotel.name"
                            title-tag="h2"
                            class="p-inline"
                        />
                        <p class="p-inline">
                            <b-form-rating
                                v-model="hotel.star"
                                variant="warning"
                                no-border
                                inline
                                readonly
                            />
                        </p>
                        <p>
                            <span class="font-weight-bolder">
                                {{ $t('hotel.hotel.address') }}
                            </span>
                            <span class="text-secondary">
                                {{ getAddress(hotel.address, hotel.ward, hotel.district, hotel.city) }}
                            </span>
                        </p>
                        <p>
                            <span class="font-weight-bolder">
                                {{ $t('hotel.hotel.status') }}:
                            </span>
                            <span class="text-secondary">
                                {{ getStatus(hotel.status) }}
                            </span>
                        </p>
                        <p
                            v-if="showReason(hotel.rejectReason)"
                        >
                            <span class="font-weight-bolder">
                                {{ $t('hotel.hotel.reasonTitle') }}:
                            </span>
                            <span class="text-secondary">
                                {{ hotel.rejectReason }}
                            </span>
                        </p>
                    </div>
                </b-list-group-item>
            </b-list-group>
        </template>
    </Layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";
import Pusher from 'pusher-js'

export default {
    name: "Hotelier",
    components: {Layout},
    data: function() {
        return {
            hotels: [],
        }
    },
    created() {
        this.$store.dispatch('hotel/notifyHotels')
            .then(() => {
                this.hotels = this.$store.getters['hotel/notify_hotels']
                this.hotels.sort(function (a,b) {
                    return new Date(b.created) - new Date(a.created)
                })
                // let count = this.$store.getters['hotel/count_hotelier']
                let count = this.$store.getters['hotel/notify_hotels'].length
                this.$store.commit('hotel/setHotelierCount', 0)
                this.$store.commit('hotel/setOldHotelierCount', count)
                this.subcribe()
            })
    },
    methods: {
        hotelImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
        },
        getStatus: function (status) {
            if (status === "active") {
                return this.$t('hotel.hotel.approveStatus')
            } else {
                return this.$t('hotel.hotel.rejectStatus')
            }
        },
        showReason: function(reason) {
            if (reason == null || reason === '') {
                return false
            } else {
                return true
            }
        },
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
        subcribe() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel_1');
            pusher.bind('an_event_1', data => {
                let user_id = this.$store.getters['user/user'].uuid
                let owner_id = data.hotel.user
                if (user_id === owner_id) {
                    this.$store.commit('hotel/saveNotifyHotel', data)
                }
                let count = this.$store.getters['hotel/notify_hotels'].length
                let old_count = this.$store.getters['hotel/old_count_hotelier']
                this.$store.commit('hotel/setHotelierCount', count - old_count)
            })
        }
    }
}
</script>

<style
    lang="scss"
    scoped
>
.list-item {
    margin: 10px 0;
    height: 225px;
    border-radius: 10px;
}
#time li {
    display: inline;
    list-style-type: none;
    float: left;
    margin: 0 10px 0 0;
}
.p-inline {
    display: inline-block;
}
.u-inline {
    display: inline-block;
    padding: 0;
}
.img-thumbnail {
    object-fit: cover;
    height: 200px;
    width: 200px;
}
.icon {
    height: 20px;
    width: 20px;
}
.card-img {
    object-fit: cover;
}
.required:before {
    content: " *";
    color: red;
}
.p-inline {
    display: inline-block;
}
.badge-size {
    font-size: 1em;
}
</style>