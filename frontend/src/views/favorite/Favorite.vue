<template>
    <Layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('favorite.favorite.title') }}
                </h2>
            </div>
            <hr>
            <!--   Favorite list         -->
            <div class="row">
                <div
                    v-for="favorite in favorites"
                    :key="favorite.uuid"
                    class="col-md-6 col-sm-12"
                    @dblclick="$router.push({name: 'createFavorite', params: {uuid: favorite.hotelid}})"
                >
                    <!--      Hotel info              -->
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
        </template>
    </Layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";


export default {
    name: "Favorite",
    components: {Layout},
    data: function () {
        return {
            favorites: []
        }
    },
    created() {
        this.$store.dispatch('favorite/listFavorites').then(() => {
            this.favorites = this.$store.getters['favorite/favorites']
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
        hotelImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
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
                            autoHideDelay: 3000,
                            variant: 'success'
                        })
                        setTimeout(location.reload.bind(location), 3000)
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