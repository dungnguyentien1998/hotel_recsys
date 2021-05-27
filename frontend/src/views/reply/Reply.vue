<template>
    <Layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('reply.reply.title') }}
                </h2>
            </div>
            <br>
            <b-list-group>
                <b-list-group-item
                    v-for="reply in replys"
                    :key="reply.uuid"
                    class="list-item"
                >
                    <div>
                        <b-img
                            v-if="isNotNull(reply.complaintImage)"
                            :src="complaintImage(reply.complaintImage)"
                            alt="Complaint image"
                            thumbnail
                            fluid
                        />
                        <b-button
                            class="position-absolute"
                            variant="outline-secondary"
                            style="right: 20px"
                            href="#"
                            @click="onHandle(reply.uuid)"
                        >
                            {{ $t('reply.reply.view') }}
                        </b-button>
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
                </b-list-group-item>
            </b-list-group>
        </template>
    </Layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";

export default {
    name: "Reply",
    components: {Layout},
    data: function() {
        return {
            replys: []
        }
    },
    created: function () {
        this.$store.dispatch('reply/listReplys', this.$route.params.uuid)
            .then(() => {
                this.replys = this.$store.getters['reply/replys']
                this.replys.sort(function (a,b) {
                    return new Date(b.created) - new Date(a.created)
                })
            })
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
        onHandle: function(uuid) {
            this.$router.push({name: 'replysDetail', params: {uuid: uuid}})
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