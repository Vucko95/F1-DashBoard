<template>
    <div class="left-sidebar">
      <img src="/logo.png" alt="logo" style="width: 80px;" />
      <!-- <img src="logo2.svg" alt="logo" style="width: 80px;" /> -->
      <div class="logo"> </div>
        <div class="icons_list">
          <button  @click="toggleHome">Show / Hide Home </button>
          <!-- <button @click="toggleSelectYear">Toggle Select Year</button> -->
          <div class="single_element">

              <svg @click="toggleArticles" :class="{ svgState3: ArticleInfoIcon }" fill="#ffffff" height="64px" width="64px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <g> <g> <path d="M470.573,350.316H72.618c-4.466,0-8.084,3.618-8.084,8.084c0,4.466,3.618,8.084,8.084,8.084h397.955 c4.466,0,8.084-3.618,8.084-8.084C478.657,353.934,475.039,350.316,470.573,350.316z"></path> <path d="M8.084,285.642H9.16c4.466,0,8.084-3.618,8.084-8.084c0-4.466-3.619-8.084-8.084-8.084H8.084 c-4.466,0-8.084,3.618-8.084,8.084C0,282.024,3.619,285.642,8.084,285.642z"></path> <path d="M40.351,350.316h-1.075c-4.466,0-8.084,3.618-8.084,8.084c0,4.466,3.618,8.084,8.084,8.084h1.075 c4.466,0,8.084-3.618,8.084-8.084C48.435,353.934,44.816,350.316,40.351,350.316z"></path> <path d="M400.662,253.305c-13.354,0-24.217,10.88-24.217,24.253c0,13.372,10.863,24.253,24.217,24.253 s24.218-10.88,24.218-24.253C424.88,264.186,414.016,253.305,400.662,253.305z M400.662,285.642 c-4.438,0-8.049-3.626-8.049-8.084c0-4.458,3.611-8.084,8.049-8.084c4.439,0,8.05,3.626,8.05,8.084 C408.712,282.016,405.101,285.642,400.662,285.642z"></path> <path d="M37.68,309.895c0-4.466-3.619-8.084-8.084-8.084H8.084c-4.466,0-8.084,3.618-8.084,8.084 c0,4.466,3.619,8.084,8.084,8.084h21.512C34.061,317.979,37.68,314.36,37.68,309.895z"></path> <path d="M9.16,350.316H8.084C3.619,350.316,0,353.934,0,358.4c0,4.466,3.619,8.084,8.084,8.084H9.16 c4.466,0,8.084-3.618,8.084-8.084C17.244,353.934,13.626,350.316,9.16,350.316z"></path> <path d="M325.911,253.305h-1.076c-4.466,0-8.084,3.619-8.084,8.084c0,4.466,3.619,8.084,8.084,8.084h1.076 c4.466,0,8.084-3.618,8.084-8.084C333.995,256.924,330.377,253.305,325.911,253.305z"></path> <path d="M510.923,293.725c0-22.628-15.168-42.773-36.884-48.991l-35.686-10.218c-0.457-0.131-0.917-0.22-1.376-0.269 c-9.825-8.283-22.499-13.277-36.314-13.277c-2.658,0-5.277,0.185-7.841,0.543c-0.224-0.086-0.454-0.163-0.69-0.231 l-86.807-24.856c-18.059-5.171-36.74-7.793-55.522-7.793c-25.827,0-51.08,4.873-75.059,14.487l-12.795,5.13l-12.789-42.724 c-3.582-11.968-14.37-20.008-26.845-20.008H28.026C12.573,145.516,0,158.108,0,173.585c0,10.698,5.935,20.318,15.488,25.104 l1.402,0.702c3.385,1.697,5.778,4.945,6.401,8.69l8.979,53.995c0.371,39.802,32.802,72.071,72.615,72.071 c13.925,0,26.947-3.946,38.01-10.784c0.095,0.003,0.19,0.005,0.286,0.005h224.357c9.312,6.779,20.76,10.779,33.126,10.779 c12.366,0,23.813-4,33.127-10.779h47.539C497.649,323.368,510.924,310.07,510.923,293.725z M39.241,205.427 c-1.469-8.827-7.116-16.486-15.108-20.492l-1.403-0.702c-4.047-2.029-6.561-6.108-6.561-10.648c0-6.562,5.319-11.901,11.858-11.9 h94.288c5.274,0,9.839,3.406,11.357,8.475l8.652,28.906c-10.938-6.623-23.753-10.435-37.438-10.435 c-26.558,0-49.833,14.358-62.495,35.734L39.241,205.427z M104.885,317.979c-31.079,0-56.373-25.307-56.449-56.445 c0.002-0.089,0.002-0.181,0-0.272C48.503,230.115,73.8,204.8,104.885,204.8c31.126,0,56.449,25.387,56.449,56.589 S136.011,317.979,104.885,317.979z M161.263,307.2c8.55-10.544,14.221-23.526,15.794-37.726h121.427 c4.466,0,8.084-3.618,8.084-8.084c0-4.466-3.618-8.084-8.084-8.084H177.057c-1.192-10.757-4.736-20.818-10.102-29.646 l13.806-5.534c22.057-8.842,45.286-13.325,69.042-13.325c17.277,0,34.459,2.411,51.072,7.168l67.35,19.286 c-14.533,10.25-24.047,27.186-24.047,46.304c0,10.86,3.07,21.017,8.385,29.642H161.263z M400.662,317.979 c-22.23,0-40.315-18.132-40.315-40.421c0-22.289,18.085-40.421,40.315-40.421c22.231,0,40.315,18.132,40.315,40.421 S422.893,317.979,400.662,317.979z M481.33,307.2h-32.569c5.314-8.625,8.385-18.782,8.385-29.642 c0-7.848-1.603-15.33-4.499-22.131l16.942,4.852c14.818,4.243,25.167,17.997,25.167,33.448 C494.756,301.156,488.733,307.2,481.33,307.2z"></path> <path d="M503.916,350.316h-1.076c-4.466,0-8.084,3.618-8.084,8.084c0,4.466,3.618,8.084,8.084,8.084h1.076 c4.466,0,8.084-3.618,8.084-8.084C512,353.934,508.382,350.316,503.916,350.316z"></path> <path d="M104.885,220.968c-22.25,0-40.351,18.132-40.351,40.421c0,22.289,18.1,40.421,40.35,40.421s40.351-18.132,40.351-40.421 C145.234,239.101,127.134,220.968,104.885,220.968z M104.885,285.642c-13.334,0-24.183-10.88-24.183-24.253 c0-13.372,10.847-24.253,24.182-24.253s24.183,10.88,24.183,24.253C129.066,274.762,118.218,285.642,104.885,285.642z"></path> </g> </g> </g> </g></svg> 
            
            <p>Articles</p> </div> <div class="single_element"> <svg @click="toggleStandingsComponents" :class="{ svgState: StandingsInfoIcon }" fill="#ffffff" width="64px" height="64px" viewBox="0 0 512 512" data-name="Layer 1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><title></title><path d="M488.14,251.87,501.92,214l-41.64-15.16h0l-37.87-13.78h0l-37.88-13.79h0L346.66,157.5h0l-28.48-10.37,5.27-14.48a8,8,0,1,0-15-5.48L256,271.19l-52.42-144a8,8,0,1,0-15,5.48l5.27,14.48L165.34,157.5h0l-37.87,13.78h0L89.59,185.07h0L51.72,198.85h0L10.08,214l13.78,37.86h0l13.78,37.86h0L52.8,331.36l37.87-13.79h0l37.88-13.79h0L166.42,290h0l37.88-13.78h0l32.23-11.73,11,30.09-30.86,84.77a8,8,0,0,0,15,5.48L256,318l24.33,66.86a8,8,0,0,0,15-5.48l-30.86-84.77,11-30.09,32.23,11.73h0L345.58,290h0l37.87,13.79h0l37.88,13.79h0l37.87,13.79,15.16-41.63h0l13.78-37.86Zm-371,8.92-12.4-34.09,34.11-12.42,12.41,34.09Zm75.75-27.57-1-2.66L180.5,199.13,209,188.77l12.41,34.08ZM128.84,175,163,162.62l1,2.67,11.44,31.43-34.11,12.42-6.21-17ZM87.2,190.19,99.61,224.3,65.5,236.71l-12.41-34.1ZM29,254.27l34.11-12.42,6.21,17,6.2,17L41.4,288.36Zm64.06,58.18-12.41-34.1,34.12-12.42L127.18,300Zm109.87-40-34.12,12.42-6.21-17.06-6.2-17,34.12-12.42,1,2.65Zm157.8-24.09,12.41-34.09,34.11,12.42-12.4,34.09ZM331.5,199.13l-11.44,31.43-1,2.66-28.48-10.37L303,188.77Zm115,37.58L412.39,224.3l12.41-34.11,34.11,12.42ZM377,192.1l-6.21,17-34.11-12.42,11.44-31.43,1-2.67L383.16,175ZM320.52,241l1-2.65,34.12,12.42-6.2,17-6.21,17.06-34.12-12.42Zm76.71,24.92,34.12,12.42-12.41,34.1L384.82,300Zm39.25,10,6.2-17,6.21-17L483,254.27l-12.4,34.09Z"></path></g></svg>
            <p>Standings</p>

          </div>
          <div class="single_element">

            <svg @click="toggleDriversComponents" :class="{ svgState2: DriverInfoIcon }" fill="#ffffff" width="64px" height="64px" viewBox="0 0 512 512" data-name="Layer 1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><title></title><path d="M447.49,364a69,69,0,0,0-23.18-23.13l-.05,0-89.85-55.19c1-1.51,2-3,2.87-4.53a141.9,141.9,0,0,0,18.21-56.07,3.11,3.11,0,0,0,0-.32,140.83,140.83,0,0,0,.76-14.53V145.41c0-1.38,0-2.75-.1-4.11a7.49,7.49,0,0,0-.23-3.42,89.18,89.18,0,0,0-88.75-81.54H243a89.19,89.19,0,0,0-88.75,81.53,8.25,8.25,0,0,0-.32,2.24,7.74,7.74,0,0,0,.1,1.19c-.06,1.36-.1,2.73-.1,4.11V210.2a140.3,140.3,0,0,0,.76,14.51c0,.12,0,.23,0,.35a141.9,141.9,0,0,0,18.21,56.06c1,1.77,2.16,3.55,3.39,5.32L87.7,340.87C67.85,353.05,56,373.07,56,394.42v53.24a8,8,0,0,0,8,8H448a8,8,0,0,0,8-8V394.41A59.5,59.5,0,0,0,447.49,364ZM194.17,283.38a67.69,67.69,0,0,1-7.37-10.26,125.79,125.79,0,0,1-12.66-30.69c22.18,13.58,50.63,21.14,81,21.14s58.79-7.56,81-21.14a125.79,125.79,0,0,1-12.66,30.69,67.23,67.23,0,0,1-6.81,9.6c-10.56,12.57-29.8,27.27-52.11,30.86a59.65,59.65,0,0,1-7.08.73c-.78,0-1.55.05-2.31.05a58.65,58.65,0,0,1-9.41-.78C227.4,310.64,207.65,299.07,194.17,283.38Zm-8.94-182.63,31.37,31.36H171.17A72.65,72.65,0,0,1,185.23,100.75Zm155.06,47.36V210.2c0,3.27-.15,6.53-.4,9.78-20.35,17.32-51.75,27.59-84.78,27.59S190.67,237.3,170.33,220c-.25-3.25-.4-6.51-.4-9.78V148.11ZM325,100.74a72.59,72.59,0,0,1,14.07,31.37H293.62ZM252.44,330.31c1.79.07,3.55.07,5.34,0V439.45h-5.34ZM273.78,328c18.12-4.52,36.54-15.41,50.44-29.82L401,345.35a52.18,52.18,0,0,0-10.26,7.8c-17.2,16.64-26.43,45.72-27.48,86.51H273.78ZM267.21,72.34a72.79,72.79,0,0,1,46.67,16.88L271,132.11H239.23L196.34,89.23A72.74,72.74,0,0,1,243,72.34ZM72,439.66V394.42c0-15,8.16-29.23,21.94-38.55,3.32.54,10.45,2.58,17.69,10.34,9.11,9.77,19.87,30.38,21.06,73.45Zm49.22-86.51a52.44,52.44,0,0,0-10.25-7.8l75.71-46.49c13.82,14.06,32,24.69,49.76,29.12V439.66H148.7C147.65,398.87,138.42,369.79,121.22,353.15ZM440,439.66H379.31c1.19-43.06,11.95-63.68,21.06-73.45,7.24-7.76,14.35-9.8,17.67-10.33a52.45,52.45,0,0,1,15.71,16.32A43.41,43.41,0,0,1,440,394.41Zm-223.29-96.2H178.3a8,8,0,0,0-8,8v23a8,8,0,0,0,8,8h38.41a8,8,0,0,0,8-8v-23A8,8,0,0,0,216.71,343.46Zm-8,23H186.3v-7h22.41Zm8,30.85H178.3a8,8,0,0,0-8,8v23a8,8,0,0,0,8,8h38.41a8,8,0,0,0,8-8v-23A8,8,0,0,0,216.71,397.28Zm-8,23H186.3v-7h22.41Zm113.49-76.8a36.69,36.69,0,1,0,36.68,36.68A36.73,36.73,0,0,0,322.2,343.46Zm0,57.37a20.69,20.69,0,1,1,20.68-20.69A20.71,20.71,0,0,1,322.2,400.83Z"></path></g></svg>
            <p>Driver Info</p>

          </div>
          <div class="single_element">

            <svg @click="toggleCircuitsComponents" :class="{ svgState4: CircuitInfoIcon }" fill="#ffffff" width="64px" height="64px" viewBox="0 0 512 512" data-name="Layer 1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><title></title><path d="M376.25,34.76H327.58A100.16,100.16,0,0,0,267,55a102,102,0,0,0-36,51.17,20.46,20.46,0,0,1-19.54,14.14h-19.6A157.4,157.4,0,0,0,34.67,277.05c-.1,41.4,16.23,80.64,46,110.47a158.37,158.37,0,0,0,101.2,46.64,8,8,0,0,0,2.51.41h53.86v34.66a8,8,0,0,0,8,8h128a8,8,0,0,0,8-8V434.4a101.2,101.2,0,0,0,95.09-100.9V135.84A101.2,101.2,0,0,0,376.25,34.76ZM215.67,354.58H191.81a77.15,77.15,0,0,1,0-154.3h81.91A32.81,32.81,0,0,0,306.5,167.5V135.84a21.11,21.11,0,0,1,21.08-21.08h48.67a21.1,21.1,0,0,1,21.08,21.08V333.5a21.1,21.1,0,0,1-21.08,21.08Zm-23.29,16h15.29v48H192.38Zm61.86,90.66V434.58h112v26.66ZM461.33,333.5a85.17,85.17,0,0,1-85.08,85.08H223.67v-48H376.25a37.12,37.12,0,0,0,37.08-37.08V135.84a37.12,37.12,0,0,0-37.08-37.08H327.58a37.13,37.13,0,0,0-37.08,37.08V167.5a16.8,16.8,0,0,1-16.78,16.78H191.81a93.15,93.15,0,0,0-15.43,185v16.18a108.74,108.74,0,0,1-20.61-5,8,8,0,1,0-5.3,15.09,124.47,124.47,0,0,0,25.91,6.06v15.95A142.73,142.73,0,0,1,92,376.23c-26.75-26.81-41.42-62-41.33-99.14A141.38,141.38,0,0,1,191.82,136.28h19.6a36.13,36.13,0,0,0,34.83-25.43,85.77,85.77,0,0,1,81.33-60.09h48.67a85.17,85.17,0,0,1,85.08,85.08Zm-331-156a8,8,0,0,1-1.84,11.16,113.49,113.49,0,0,0-13.79,11.72,115.47,115.47,0,0,0-7.85,8.72A8,8,0,0,1,94.4,199a130.11,130.11,0,0,1,9-10,126.84,126.84,0,0,1,15.77-13.4A8,8,0,0,1,130.32,177.45Zm124.89-17.17a8,8,0,0,1-8,8h-32a8,8,0,0,1,0-16h32A8,8,0,0,1,255.21,160.28Zm-64-.27a8,8,0,0,1-7.4,8.56,108,108,0,0,0-29.05,6.18,7.88,7.88,0,0,1-2.72.48,8,8,0,0,1-2.73-15.52,124.21,124.21,0,0,1,33.34-7.1A8,8,0,0,1,191.2,160ZM67.73,261a123.93,123.93,0,0,1,9-32.88,8,8,0,0,1,14.69,6.33,107.75,107.75,0,0,0-7.86,28.63,8,8,0,0,1-7.93,7,7.61,7.61,0,0,1-1-.07A8,8,0,0,1,67.73,261ZM277.39,118.56a53,53,0,0,0-2.88,17.28v11.74a8,8,0,1,1-16,0V135.84a68.68,68.68,0,0,1,3.76-22.5,8,8,0,1,1,15.12,5.22ZM91.91,321.4a8,8,0,1,1-14.63,6.46,123.8,123.8,0,0,1-9.37-32.77,8,8,0,0,1,15.84-2.25A108.42,108.42,0,0,0,91.91,321.4Zm4.34,24.2a8,8,0,0,1,11.26,1.09,110.42,110.42,0,0,0,21.83,20.2,8,8,0,1,1-9.18,13.1,125.89,125.89,0,0,1-25-23.13A8,8,0,0,1,96.25,345.6Zm349.09-14.08v2a69.05,69.05,0,0,1-8.19,32.6,8,8,0,1,1-14.09-7.57,53,53,0,0,0,6.28-25v-2a8,8,0,0,1,16,0Zm0-128v32a8,8,0,1,1-16,0v-32a8,8,0,0,1,16,0Zm0,64v32a8,8,0,0,1-16,0v-32a8,8,0,0,1,16,0Zm-8-136a8,8,0,0,1,8,8v32a8,8,0,1,1-16,0v-32A8,8,0,0,1,437.34,131.52ZM438,105a8,8,0,0,1-3.57,10.74,7.91,7.91,0,0,1-3.58.85,8,8,0,0,1-7.15-4.41,53.5,53.5,0,0,0-18.26-20.58,8,8,0,1,1,8.83-13.34A69.57,69.57,0,0,1,438,105ZM290.2,394.58a8,8,0,0,1-8,8h-32a8,8,0,0,1,0-16h32A8,8,0,0,1,290.2,394.58ZM387.88,75.34a8,8,0,0,1-8,7.53h-.47c-1.05-.07-2.12-.1-3.17-.1H347.9a8,8,0,0,1,0-16h28.36c1.36,0,2.74,0,4.11.12A8,8,0,0,1,387.88,75.34Zm-64.05-1a8,8,0,0,1-6.34,9.37A53.05,53.05,0,0,0,292.8,95.78a8,8,0,0,1-10.5-12.07A69,69,0,0,1,314.46,68,8,8,0,0,1,323.83,74.35Zm91.42,306.81a8,8,0,0,1-2.56,11,69,69,0,0,1-34.24,10.37h-.26a8,8,0,0,1-.25-16,53,53,0,0,0,26.29-8A8,8,0,0,1,415.25,381.16ZM354.2,394.58a8,8,0,0,1-8,8h-32a8,8,0,0,1,0-16h32A8,8,0,0,1,354.2,394.58Z"></path></g></svg>
            <p>Circuit Info</p>

          </div>

          </div>
    </div>
  </template>
  
<script>
import { EventBus } from "@/eventBus.js";



  export default {
    name: 'LeftSidebar',
    methods: {
      toggleHome() {
      // this.ArticleInfoIcon = !this.ArticleInfoIcon;

      EventBus.$emit("toggle-Home");
    },
      toggleArticles() {
      this.ArticleInfoIcon = !this.ArticleInfoIcon;

      EventBus.$emit("toggle-Articles");
    },
      toggleStandingsComponents() {
      this.StandingsInfoIcon = !this.StandingsInfoIcon;

      EventBus.$emit("toggle-Standings-Components");
    },
      toggleDriversComponents() {
      this.DriverInfoIcon = !this.DriverInfoIcon;

      EventBus.$emit("toggle-Drivers-Components");
    },
      toggleCircuitsComponents() {
      this.CircuitInfoIcon = !this.CircuitInfoIcon;

      EventBus.$emit("toggle-Circuits-Components");
    },

  },
  data() {
    return {
      ArticleInfoIcon: false,
      StandingsInfoIcon: false,
      DriverInfoIcon: false,
      CircuitInfoIcon: false,
    };
  },
  };
  </script>
  
  <style scoped>
  .left-sidebar {
    /* background-color: rgb(0, 0, 0); */
    /* background: rgb(6, 12, 7); */
    /* background: rgb(22, 27, 23); */
    background: rgb(27, 31, 36);


    width:10%;
    height: 100vh;
}
.left-sidebar img {
    margin-left: 10%;
}
.logo svg {
  width: 90%;
  margin-left: 5%;

}
.icons_list {
    display: flex;
    flex-direction: column;
    align-items: center;
    /* justify-content: center; */
    margin-left: 5%;

    /* margin-top: 90%; */
}
.single_element {
  width: 100%;
  margin-top: 40px;
  display: flex;
    flex-direction: row;
    align-items: center;
    /* vertical-align: bottom; */
}
.icons_list svg {
    /* margin-top: 40px; */
    height: 50px;
    /* margin-bottom: 20px; */
    transition: all 0.3s ease;
    fill: white;
}
.icons_list svg:hover {
  fill: rgb(238, 157, 8); /* Change the color to orange on hover */
  stroke: rgb(238, 157, 8); /* Change the stroke color to orange on hover */
  transform: scale(1.2); /* Add this line for scaling effect on hover */
}

.icons_list svg.svgState {
  fill: rgb(238, 157, 8); /* Change the color to orange on hover */
  stroke: rgb(238, 157, 8); /* Change the stroke color to orange on hover */
}
.icons_list svg.svgState2 {
  fill: rgb(238, 157, 8); /* Change the color to orange on hover */
  stroke: rgb(238, 157, 8); /* Change the stroke color to orange on hover */
}
.icons_list svg.svgState3 {
  fill: rgb(238, 157, 8); /* Change the color to orange on hover */
  stroke: rgb(238, 157, 8); /* Change the stroke color to orange on hover */
}
.icons_list svg.svgState4 {
  fill: rgb(238, 157, 8); /* Change the color to orange on hover */
  stroke: rgb(238, 157, 8); /* Change the stroke color to orange on hover */
}

  </style>

