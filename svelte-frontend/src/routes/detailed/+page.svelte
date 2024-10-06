<script lang="ts">
    import Body from "../components/Body.svelte";
    import Footer from "../components/Footer.svelte";
    import Header from "../components/Header.svelte";
    import Particles from "../components/Particles.svelte";
    import Slider from "../components/Slider.svelte";

    let NImage = "https://landsatlook.usgs.gov/gen-browse?size=rrb&type=refl&product_id=LC09_L1TP_020031_20240905_20240905_02_T1";
    let SImage = "https://landsatlook.usgs.gov/gen-browse?size=rrb&type=qb&product_id=LC09_L1TP_020031_20240905_20240905_02_T1";
    let BWImage = "https://landsatlook.usgs.gov/gen-browse?size=rrb&type=tir&product_id=LC09_L1TP_020031_20240905_20240905_02_T1";
    
    let current = NImage;

    function changeToN(){
        current = NImage;
    }

    function changeToBW(){
        current = BWImage;
    }

    function ChangeToS(){
        current = SImage;
    }

</script>

<main>
    <Header />
    <Body>
    <Particles>
        <div class="page-container">
            <form >
                <h2>Coordinates:</h2>
                <div class="coordinates">
                    <input type="text" placeholder="-180.000" required>
                    <input type="text" placeholder="+180.000" required>
                </div>
                <h2>Date Range:</h2>
                <div class="date-range">
                    <input type="date" required>
                </div>
                <button type="submit">Send Off Data!</button>
            </form>
            <div class="picture">
                <div class="slideshow">
                    <div class="tabs">
                        <button on:click={changeToN} class="Normal" >Normal</button>
                        <button on:click={changeToBW} class="BW">BW</button>
                        <button on:click={ChangeToS} class="Saturated">Saturated</button>
                    </div>
                    <img src={current} height="400px" width="400px" alt="landsat image" class="Landsat">
                </div>
                <div class="slider">
                    <h3 class="slider-date">Date Range:</h3>
                    <Slider></Slider>
                </div>
            </div>

        </div>
    </Particles>
    </Body>
    <Footer />
</main>

<style>
    .page-container{
        display: flex;
        justify-content: space-around;
        align-items: center;
    }

    @media screen and (max-width: 550px) {
        .page-container{
            display: flex;
            flex-direction: column;
            max-width: 500px;
        }
    }

    .coordinates{
        display: flex;
        gap: 20px;
    }

    form {
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    button{
        margin-top: 15%;
    }

    .tabs{
        display: flex;
        justify-content: space-around;
        margin: 20px;
    }

    .slider-date{
        color: white;
        justify-content: center;
    }
</style>