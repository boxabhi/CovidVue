<template>
<div>
   <div class="text-center">
    <h2 class="text-center mt-5 p-3 text-uppercase btn btn-primary">Coronavirus Real time Data</h2>
    </div>
  <div class="container text-center  pt-3">
      <img src="@/assets/virus.png" class="img-responsive img-fluid" style="height: 100px;" >
      <h1 class="text-uppercase">Location - {{real_data[0].state}}</h1>
      <h4 >Active cases : <span v-if="real_data[0].confirmed">{{real_data[0].confirmed}}</span> | Deaths : {{real_data[0].deaths}}</h4>
      <h5 v-if="real_data ">Recovered : {{real_data[0].discharged}} </h5>

      <div class="row">
      <div class="col-3"></div>
      <div class="col-6 text-center d-flex justify-content-center">
      <div class="input-group pt-2">
        <input type="text" v-model="new_state"   class="form-control">
        <div class="input-group-append">
        <button v-on:click="getCovid" class="input-group-text bg-primary text-white"><i class="fas fa-location-arrow"></i>
       </button>
        </div>
        </div>
      </div>
  </div>
  <p class="pt-2 ">Fetch any state in India {{new_state}}</p>
  </div>

  <div class="container pt-3">
  <ul class="nav justify-content-center">
    <li class="nav-item">
    <router-link to="/precaution">   
    <a class="nav-link active">Precautions <i class="fas fa-capsules"></i> </a>
      </router-link>
      </li>
    <li class="nav-item">
      <a class="nav-link active" href="https://github.com/boxabhi/CovidVue">Code on <i class="fab fa-github"></i> </a>
    </li>
    <li class="nav-item">
       <router-link to="/api">   
      <a class="nav-link">Get API <i class="fab fa-firefox-browser"></i></a>
     </router-link>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="https://www.linkedin.com/in/gupta-abhijeet/">Linkedin <i class="fab fa-linkedin"></i></a>
    </li>
  </ul>
</div>


<div class="container text-center mt-5">
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

export default {
  data(){
    return {
      state : {},
      city : {},
      real_data : {},
      new_state : '',
      all_data : {}
    }
  },
  methods : {
    getCovid(){
      var s = this.new_state;
      console.log(s)
      fetch(`https://cors-anywhere.herokuapp.com/https://whereiscovidapi.herokuapp.com/api/${s}`)
    .then(response => response.json())
    .then(data => {
 this.real_data = data

    })
    },

    getIp(){
    fetch('https://api.ipify.org/?format=json')
     .then(response=> response.json())
     .then(data => {
       fetch(`https://ipapi.co/${data.ip}/json/`)
       .then(response => response.json())
       .then(data =>{ 
        this.state = data.region
        this.state = (JSON.parse(JSON.stringify(this.state)))
      
         fetch(`https://cors-anywhere.herokuapp.com/https://whereiscovidapi.herokuapp.com/api/${data.region}`)
    .then(response =>response.json())
    .then(data => {
      this.real_data = data
    })

         }
     )})
    },

  allData(){
     fetch(`https://cors-anywhere.herokuapp.com/https://whereiscovidapi.herokuapp.com/api`)
    .then(response => response.json())
    .then(data => {
     
      this.all_data = data
     
    })
  }

  },

  created(){
    this.getIp()
    this.allData()
  },

  
}

</script>