<template>
    <layout>
        <template #content>
            <div>
                <b-form>
                    <h3 class="p-inline">
                        <span class="font-weight-bolder">
                            {{ hotel.name }}
                        </span>
                    </h3>
                    <p class="p-inline">
                        <b-form-rating
                            :value="hotel.star"
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
                    </b-form-group>
                    <p>
                        <span class="font-weight-bolder">
                            {{ $t('hotel.hotel.address') }}
                        </span>
                        <span class="text-secondary">
                            {{ getAddress() }}
                        </span>
                    </p>
                    <p>
                        <span class="font-weight-bolder">
                            {{ $t('hotel.hotel.amenities') }}
                        </span>
                        <b-list-group horizontal="md">
                            <b-list-group-item
                                v-for="(amenity, index) in hotel.amenities"
                                :key="`${hotel.uuid}-amenity-${index}`"
                                style="margin: 5px; border: none"
                            >
                                <img
                                    :src="getSrc(amenity)"
                                    :alt="amenity"
                                    class="icon"
                                >
                                {{ amenity }}
                            </b-list-group-item>
                        </b-list-group>
                    </p>
                    <div class="mt-2">
                        <b-button
                            :disabled="hotel.isActive === true"
                            variant="success"
                            href="#"
                            size="sm"
                            @click="$bvModal.show(`modal-${hotel.uuid}-approve`)"
                        >
                            {{ $t('hotel.hotel.approveBtn') }}
                        </b-button>

                        <b-button
                            :disabled="hotel.isActive === true"
                            class="ml-2"
                            variant="danger"
                            href="#"
                            size="sm"
                            @click="$bvModal.show(`modal-${hotel.uuid}-reject`)"
                        >
                            {{ $t('hotel.hotel.rejectBtn') }}
                        </b-button>
                    </div>
                    <b-modal
                        :id="`modal-${hotel.uuid}-approve`"
                        :title="$t('hotel.hotel.approveTitle')"
                        size="lg"
                        :ok-title="$t('button.submit')"
                        :cancel-title="$t('button.unsubmit')"
                        @ok="approveHotel(hotel.uuid)"
                    >
                        {{ $t('hotel.hotel.confirmApprove') }}
                    </b-modal>

                    <b-modal
                        :id="`modal-${hotel.uuid}-reject`"
                        :title="$t('hotel.hotel.rejectTitle')"
                        size="lg"
                        :ok-title="$t('button.submit')"
                        :cancel-title="$t('button.unsubmit')"
                        @ok="rejectHotel(hotel.uuid)"
                    >
                        {{ $t('hotel.hotel.confirmReject') }}
                    </b-modal>
                </b-form>
            </div>
        </template>
    </layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";

export default {
    name: "FormDetail",
    components: {Layout},
    // props: {
    //     // Hotel data
    //     hotel: {
    //         type: Object,
    //         default: () => {
    //             return null
    //         }
    //     }
    // },
    data: function () {
        return {
            updateForm: {
                is_active: null
            },
            hotel: this.$store.getters['hotel/hotels'].filter(hotel => hotel.uuid === this.$route.params.uuid)[0],
        }
    },
    methods: {
        getAddress: function () {
            if (this.hotel.address == null || this.hotel.address === "") {
                return this.hotel.ward + ", " + this.hotel.district + ", " + this.hotel.city
            } else {
                return this.hotel.address + ", " + this.hotel.ward + ", " + this.hotel.district + ", " + this.hotel.city
            }
        },
        hotelImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
        },
        getSrc: function (amenity) {
            let images = require.context('../../assets/', false, /\.png$/)
            return images('./' + amenity + ".png")
        },
        approveHotel: function (uuid) {
            this.$store.dispatch('hotel/resetStatus')
            this.updateForm.is_active = true
            this.updateForm.uuid = uuid
            this.$store.dispatch('hotel/approveHotel', this.updateForm).then(() => {
                if (this.$store.getters['hotel/status'] === 'FAILED') {
                    // Alert for failed api calls
                    this.makeToast(this.$t('hotel.hotel.errors.approveTitle'), this.$t('hotel.hotel.errors.exceptionOccurred'))
                } else {
                    // window.location.reload()
                    // this.$router.push('/admin/hotels')
                    this.$bvToast.toast(this.$t('hotel.hotel.success.approveMessage'), {
                        title: this.$t('hotel.hotel.success.approveTitle'),
                        autoHideDelay: 3000,
                        variant: 'success'
                    })
                    setTimeout(() => this.$router.push('/admin/hotels'), 3000)
                }
            })
        },
        // Handle delete hotel
        rejectHotel: function (uuid) {
            this.$store.dispatch('hotel/resetStatus')
            this.$store.dispatch('hotel/deleteHotel', uuid)
                .then(() => {
                    if (this.$store.getters['hotel/status'] === 'FAILED') {
                        // Alert for failed api call
                        this.makeToast(this.$t('hotel.hotel.errors.rejectTitle'), this.$t('hotel.hotel.errors.exceptionOccurred'))
                    } else {
                        this.$bvToast.toast(this.$t('hotel.hotel.success.rejectMessage'), {
                            title: this.$t('hotel.hotel.success.rejectTitle'),
                            autoHideDelay: 3000,
                            variant: 'success'
                        })
                        setTimeout(() => this.$router.push('/admin/hotels'), 3000)
                    }
                })
        },
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
</style>