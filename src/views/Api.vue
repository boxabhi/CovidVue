<template>
    <div class="home mt-5 pt-5">
        <div class="container text-center mt-3">
            <img src="@/assets/virus.png" class="img-responsive img-fluid" style="height: 100px;">
            <h2 class="text-uppercase mt-2">Get your API key </h2>
            <div class="col-6 text-center mx-auto">
                <div class="input-group pt-2">
                    <input type="email" v-model="email" placeholder="Email" class="form-control">
                    <div class="input-group-append">
                        <button v-on:click="getApikey" class="input-group-text bg-primary text-white"><i
                                class="fas fa-location-arrow"></i>
                        </button>
                    </div>
                </div>
                <p>Your email {{email}}</p>
            </div>
            <div class="col-6 mx-auto mt-3">
                <input type="text" v-if="res.api_key" :value="res.api_key" disabled class="form-control text-center">

            </div>

<router-link to="/"><button class="btn btn-warning">Back </button> </router-link>   

        </div>

<div class="mt-5 pt-5"></div>
<div class="container text-center mt-5 pt-5">
    <img src="@/assets/quarantine.png" class="img-responsive imf-fluid" style="height:50px"> #BeatHome
</div>


<div class="container-fluid bg-dark mt-5">
    <footer class="text-center">
        <p class="mt-3 p-3 text-white" >Created by Abhijeet <i class="fas fa-mug-hot"></i></p>
    </footer>
</div>
    </div>
</template>

<script>
    // @ is an alias to /src
    export default {
        name: 'Api',
        data() {
            return {
                email: '',
                res : {},
                flag : true
            }
        },
        methods: {
            getApikey() {
            
        fetch(`https://cors-anywhere.herokuapp.com/https://whereiscovidapi.herokuapp.com/users/${this.email}`).
        then(response =>response.json())
        .then(data => {
            this.res = data
        })

            }
        }
    }
</script>