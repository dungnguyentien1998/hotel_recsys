<template>
    <layout>
        <template #content>
            <div>
                <b-form>
                    <div>
                        <b-img
                            v-if="isNotNull(reply.complaintImage)"
                            :src="complaintImage(reply.complaintImage)"
                            alt="Complaint image"
                            thumbnail
                            fluid
                        />
                    </div>
                    <div>
                        <p
                            class="m-0 font-weight-bolder"
                        >
                            {{ reply.complaintTitle }}
                        </p>
                        <p
                            class="m-0 text-secondary"
                        >
                            {{ reply.complaintContent }}
                        </p>
                        <p
                            class="m-0 font-weight-bolder text-right"
                        >
                            {{ toDate(reply.complaintCreated) }}
                        </p>
                    </div>
                    <br>
                    <hr>
                    <div class="align-items-center d-flex">
                        <h2 class="flex-grow-1">
                            {{ $t('reply.replyDetail.title') }} {{ reply.hotelName }}
                        </h2>
                    </div>
                    <div>
                        <b-img
                            v-if="isNotNull(reply.image)"
                            :src="complaintImage(reply.image)"
                            alt="Reply image"
                            thumbnail
                            fluid
                        />
                    </div>
                    <div>
                        <p
                            class="m-0 font-weight-bolder"
                        >
                            {{ reply.title }}
                        </p>
                        <p
                            class="m-0 text-secondary"
                        >
                            {{ reply.content }}
                        </p>
                        <p
                            class="m-0 font-weight-bolder text-right"
                        >
                            {{ toDate(reply.created) }}
                        </p>
                        <small
                            class="d-block text-right"
                        >
                            {{ $t('reply.replyDetail.title') }}: {{ reply.ownerTel }} - {{ reply.ownerEmail }}
                        </small>
                    </div>
                </b-form>
            </div>
        </template>
    </layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";

export default {
    name: "ReplyDetail",
    components: {Layout},
    data: function () {
        return {
            reply: this.$store.getters['reply/replys'].filter(reply => reply.uuid === this.$route.params.uuid)[0],
        }
    },
    methods: {
        isNotNull: function (image) {
            return image != null;
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

<style scoped>

</style>