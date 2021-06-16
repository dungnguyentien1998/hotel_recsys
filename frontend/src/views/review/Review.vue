<template>
    <div>
        <div>
            <b-button
                v-if="roleUser"
                variant="success"
                size="sm"
                @click="$bvModal.show('modal-create')"
            >
                {{ $t('review.review.createBtn') }}
            </b-button>
        </div>
        <br>
        <div
            v-if="loading"
            class="loader"
        />
        <b-list-group
            id="reviews-list"
            :current-page="currentPage"
            :per-page="perPage"
        >
            <b-list-group-item
                v-for="review in reviews"
                :key="review.uuid"
            >
                <!--   Review title         -->
                <div class="form-row">
                    <div class="col-sm-10 col-form-label">
                        <p class="m-0 text-secondary">
                            {{ toDate(review.created) }}
                        </p>
                        <p class="m-0 font-weight-bolder p-inline">
                            {{ review.title }}
                        </p>
                    </div>
                    <div class="col-sm-2">
                        <p />
                        <b-badge
                            pill
                            variant="info"
                            class="badge-size"
                        >
                            {{ review.rating }} / 5
                        </b-badge>
                    </div>
                </div>
                <p class="m-0 text-secondary">
                    {{ review.content }}
                </p>
                <small class="d-block text-right">
                    {{ review.userName }}
                </small>
            </b-list-group-item>
        </b-list-group>
        <br>
        <span
            v-if="reviews.length === 0"
            style="font-style: italic"
        >
            {{ $t('review.review.noReview') }}
        </span>
        <b-pagination
            v-if="rows > perPage"
            v-model="currentPage"
            :per-page="perPage"
            :total-rows="rows"
            pills
            aria-controls="reviews-list"
            @change="handlePageChange"
        />
        <b-modal
            id="modal-create"
            :title="$t('review.review.createTitle')"
            size="lg"
            hide-footer
        >
            <review-form />
        </b-modal>
    </div>
</template>

<script>
import ReviewForm from "@/views/review/ReviewForm";
import Pusher from "pusher-js";
import roleUtil from "@/utils/role-utils"
import {validationMixin} from "vuelidate";
import {getDistrictsByProvinceCode, getProvinces, getWardsByDistrictCode} from "sub-vn";
import camelcaseKeys from "camelcase-keys";

export default {
    name: "Review",
    components: {ReviewForm},
    mixins: [validationMixin, roleUtil],
    data: function () {
        return {
            reviews: [],
            currentPage: this.$store.getters['review/page'],
            perPage: 30,
            rows: 0,
            loading: false
        }
    },
    computed: {
        roleUser: function () {
            return this.getRoleUser()
        },
    },
    created() {
        this.retrieveReviews()
        let user = this.$store.getters['user/user']
        if (user.role === 'hotelier') {
            this.subscribe_review()
        }
    },
    methods: {
        getRequestParams(currentPage, perPage) {
            let params = []
            if (currentPage) {
                params["page"] = currentPage
                this.$store.commit('review/setPage', currentPage)
            } else {
                params["page"] = this.$store.getters['review/page']
            }
            if (perPage) {
                params["per_page"] = perPage
            }
            return params
        },
        retrieveReviews() {
            const params = this.getRequestParams(this.currentPage, this.perPage)
            params["hotelId"] = this.$route.params.uuid
            this.loading = true
            this.$store.dispatch('review/listReviews', params)
                .then(() => {
                    this.reviews = this.$store.getters['review/reviews']
                    this.rows = this.$store.getters['review/count']
                    this.loading = false
                    this.$store.commit('review/resetNewCount')
                })
        },
        handlePageChange(value) {
            this.currentPage = value
            this.retrieveReviews()
        },
        toDate: function(datetime) {
            let date = new Date(datetime);
            return date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear() + " " +
                date.getHours() + ":" + date.getMinutes();
        },
        subscribe_review() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel');
            pusher.bind('an_event_1', data => {
                let user = this.$store.getters['user/user']
                if (user.role === 'hotelier' && user.uuid === data.review.owner_id) {
                    data = camelcaseKeys(data, {deep: true})
                    let new_uuid = data.review.uuid
                    let check = true
                    let uuids = this.$store.getters['review/uuids']
                    for (let i=0; i<uuids.length; i++) {
                        if (uuids[i] === new_uuid) {
                            check = false
                            break
                        }
                    }
                    if (check === true) {
                        this.$store.commit('review/saveReview', data)
                        this.$store.commit('review/saveNewReview', data)
                        this.$store.commit('review/saveNewCount')
                    }
                    this.$store.commit('review/saveUuid', data.review.uuid)
                    // this.$store.commit('review/saveReview', data)
                    // this.$store.commit('review/saveNewReview', data)
                    // this.$store.commit('review/saveNewCount')
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
.p-inline {
    display: inline-block;
}
.badge-size {
    font-size: 1em;
    float: right;
}
.loader{
    position: absolute;
    top:0;
    right:0;
    width:100%;
    height:100%;
    background-color:#eceaea;
    background-image: url('../../assets/Spinner-3.gif');
    background-size: 50px;
    background-repeat:no-repeat;
    background-position:center;
    z-index:10000000;
    opacity: 0.4;
    filter: alpha(opacity=40);
}
</style>