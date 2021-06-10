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
                v-for="review in reviews.slice((currentPage-1)*perPage, (currentPage-1)*perPage+perPage)"
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
            v-if="reviews.length > perPage"
            v-model="currentPage"
            :per-page="perPage"
            :total-rows="rows"
            pills
            aria-controls="reviews-list"
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

export default {
    name: "Review",
    components: {ReviewForm},
    mixins: [validationMixin, roleUtil],
    data: function () {
        return {
            reviews: [],
            currentPage: 1,
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
        // Get review data
        this.loading = true
        this.$store.dispatch('review/listReviews', this.$route.params.uuid)
            .then(() => {
                this.reviews = this.$store.getters['review/reviews']
                this.rows = this.reviews.length
                this.reviews.sort(function (a,b) {
                    return new Date(b.created) - new Date(a.created)
                })
                this.loading = false
            })
    },
    methods: {
        toDate: function(datetime) {
            let date = new Date(datetime);
            return date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear() + " " +
                date.getHours() + ":" + date.getMinutes();
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