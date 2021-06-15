<template>
    <div>
        <b-list-group
            id="complaints-list"
            :current-page="currentPage"
            :per-page="perPage"
        >
            <b-list-group-item
                v-for="complaint in complaints.slice((currentPage-1)*perPage, (currentPage-1)*perPage+perPage)"
                :key="complaint.uuid"
                class="list-item"
            >
                <div>
                    <b-img
                        v-if="isNotNull(complaint.image)"
                        :src="complaintImage(complaint.image)"
                        alt="Complaint image"
                        thumbnail
                        fluid
                    />
                    <div
                        class="position-absolute"
                        style="right: 20px; top: 20px"
                    >
                        <b-form-checkbox
                            v-model="complaint.isProcessed"
                            value="true"
                            unchecked-value="false"
                            @change="updateStatus(complaint)"
                        >
                            {{ $t('complaint.complaint.status') }}
                        </b-form-checkbox>
                    </div>
                </div>
                <div>
                    <p
                        class="m-0 font-weight-bolder"
                    >
                        {{ complaint.title }}
                    </p>
                    <p
                        class="m-0 text-secondary"
                    >
                        {{ complaint.content }}
                    </p>
                    <p
                        class="m-0 font-weight-bolder text-right"
                    >
                        {{ toDate(complaint.created) }}
                    </p>
                    <small
                        class="d-block text-right"
                    >
                        {{ complaint.userName }} - {{ complaint.tel }} - {{ complaint.email }}
                    </small>
                </div>
            </b-list-group-item>
        </b-list-group>
        <br>
        <span
            v-if="complaints.length === 0"
            style="font-style: italic"
        >
            {{ $t('complaint.complaint.noComplaint') }}
        </span>
        <b-pagination
            v-if="complaints.length > perPage"
            v-model="currentPage"
            :per-page="perPage"
            :total-rows="rows"
            pills
            aria-controls="complaints-list"
        />
    </div>
</template>

<script>
import {library} from '@fortawesome/fontawesome-svg-core'
import {faEnvelopeOpen} from '@fortawesome/free-solid-svg-icons'
import Pusher from "pusher-js";


library.add(faEnvelopeOpen)

export default {
    name: "Complaint",
    data: function () {
        return {
            // Complaint data
            complaints: [],
            currentPage: 1,
            perPage: 10,
            rows: 0,
            form: {
                is_processed: null,
            }
        }
    },
    created: function () {
        this.$store.dispatch('complaint/listComplaints', this.$route.params.uuid)
            .then(() => {
                this.complaints = this.$store.getters['complaint/complaints']
                this.rows = this.complaints.length
                this.complaints.sort(function (a,b) {
                    return new Date(b.created) - new Date(a.created)
                })
                this.$store.commit('complaint/resetNewCount')
            })
        this.subscribe_complaint()
    },
    methods: {
        isNotNull: function (image) {
            return image != null;
        },

        mailtoUrl: function (email) {
            let url = 'mailto:' + email
            window.open(url)
        },

        complaintImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
        },
        toDate: function(datetime) {
            let date = new Date(datetime);
            return date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear() + " " +
                date.getHours() + ":" + date.getMinutes();
        },
        updateStatus: function (complaint) {
            this.$store.dispatch('complaint/resetStatus')
            this.form.hotelId = this.$route.params.uuid
            this.form.complaintId = complaint.uuid
            this.form.is_processed = complaint.isProcessed
            this.$store.dispatch('complaint/updateComplaint', this.form).then(() => {
                if (this.$store.getters['complaint/status'] === 'FAILED') {
                    // Alert for failed api calls
                    this.makeToast(this.$t('complaint.complaintForm.errors.createTitle'), this.$t('complaint.complaintForm.errors.exceptionOccurred'))
                }
            })
        },
        subscribe_complaint() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel');
            pusher.bind('an_event_2', data => {
                let user = this.$store.getters['user/user']
                if (user.role === 'hotelier' && user.uuid === data.complaint.owner_id) {
                    this.$store.commit('complaint/saveComplaint', data)
                    this.$store.commit('complaint/saveNewComplaint', data)
                    this.$store.commit('complaint/saveNewCount')
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
.img-thumbnail {
    object-fit: cover;
    height: 300px;
}
.list-item {
    margin: 10px 0;
    border-radius: 10px;
    border-style: solid;
}
</style>