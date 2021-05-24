<template>
    <b-list-group>
        <b-list-group-item
            v-for="complaint in complaints"
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
                <b-button
                    class="position-absolute"
                    variant="outline-secondary"
                    style="right: 20px"
                    :href="mailtoUrl(complaint.email)"
                >
                    {{ $t('complaint.complaint.sendEmail') }}
                    <font-awesome-icon
                        :icon="['fas', 'envelope-open']"
                    />
                </b-button>
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
                    {{ complaint.userName }} - {{ complaint.email }}
                </small>
            </div>
        </b-list-group-item>
    </b-list-group>
</template>

<script>
import {library} from '@fortawesome/fontawesome-svg-core'
import {faEnvelopeOpen} from '@fortawesome/free-solid-svg-icons'


library.add(faEnvelopeOpen)

export default {
    name: "Complaint",
    data: function () {
        return {
            // Complaint data
            complaints: []
        }
    },
    created: function () {
        this.$store.dispatch('complaint/listComplaints', this.$route.params.uuid)
            .then(() => {
                this.complaints = this.$store.getters['complaint/complaints']
                this.complaints.sort(function (a,b) {
                    return new Date(b.created) - new Date(a.created)
                })
            })
    },
    methods: {
        isNotNull: function (image) {
            return image != null;
        },
        // Handle send email
        mailtoUrl: function (email) {
            return `https://mail.google.com/mail/?view=cm&fs=1&to=${email}&tf=cm`
        },
        // Get complaint image
        complaintImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
        },
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
.img-thumbnail {
    object-fit: cover;
    height: 300px;
}
.list-item {
    margin: 10px 0;
    border-radius: 10px;
    border-style: solid;
    //border-color: black;
}
</style>