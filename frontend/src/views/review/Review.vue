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
        <b-list-group>
            <!--        <span class="font-weight-bolder">-->
            <!--            {{ reviews.length }} {{ $tc('hotel.hotel.review', reviews.length) }}-->
            <!--        </span>-->
            <br>
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
                <!--            <p class="m-0 font-weight-bolder p-inline">-->
                <!--                {{ review.title }}-->
                <!--            </p>-->
                <!--  Review rating          -->
                <!--            <b-form-rating-->
                <!--                :value="review.rating"-->
                <!--                class="pl-0 p-inline"-->
                <!--                variant="warning"-->
                <!--                inline-->
                <!--                no-border-->
                <!--                readonly-->
                <!--            />-->
                <!--            <b-badge-->
                <!--                pill-->
                <!--                variant="info"-->
                <!--                class="badge-size"-->
                <!--            >-->
                <!--                {{ review.rating }} / 5-->
                <!--            </b-badge>-->
                <!--            <p-->
                <!--                class="m-0 text-secondary"-->
                <!--            >-->
                <!--                {{ toDate(review.created) }}-->
                <!--            </p>-->
                <p class="m-0 text-secondary">
                    {{ review.content }}
                </p>
                <small class="d-block text-right">
                    {{ review.userName }}
                </small>
            </b-list-group-item>
        </b-list-group>
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

export default {
    name: "Review",
    components: {ReviewForm},
    data: function () {
        return {
            reviews: []
        }
    },
    computed: {
        roleHotelier: function () {
            return (this.$store.getters['user/user'].role === 'hotelier')
        },
        // Check if role user
        roleUser: function () {
            return (this.$store.getters['user/user'].role === 'user')
        },
    },
    created() {
        // Get review data
        this.$store.dispatch('review/listReviews', this.$route.params.uuid)
            .then(() => {
                this.reviews = this.$store.getters['review/reviews']
                this.reviews.sort(function (a,b) {
                    return new Date(b.created) - new Date(a.created)
                })
            })
    },
    methods: {
        toDate: function(datetime) {
            let date = new Date(datetime);
            return date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear() + " " +
                date.getHours() + ":" + date.getMinutes();
        },
        subcribe() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel');
            pusher.bind('an_event_1', data => {

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
.badge-size {
    font-size: 1em;
    float: right;
}
</style>