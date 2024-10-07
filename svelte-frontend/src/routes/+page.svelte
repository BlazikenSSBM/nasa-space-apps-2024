<script>
  import Body from "./components/Body.svelte";
  import Footer from "./components/Footer.svelte";
  import Header from "./components/Header.svelte";
  import Particles from "./components/Particles.svelte";
</script>

<main>
  <Header />
  <Body>
    <Particles>
      <div class="main-text">
        <h1 class="group-name">Nerds From Space</h1>
        <h2 class="challenge-name">Landsat Imagery</h2>
        <h4>Input Coordinates:</h4>
        <div class="inputs">
          <form id="input" action="http://127.0.0.1:5000/getCoordinates" method="POST">
            <input
              type="text"
              name="latitude"
              placeholder="-180.000"
              required
            />
            <input
              type="text"
              name="longitude"
              placeholder="+180.000"
              required
            />
          </form>
        </div>
        <button type="submit" form="input">Launch Off!</button>
      </div>
    </Particles>
  </Body>
  <Footer />
</main>

<style>
  h2 {
    margin-top: -15px;
  }

  .main-text {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    color: white;
  }

  .group-name {
    font-size: 250%;
    font-weight: bold;
    font-style: italic;
  }

  .inputs > form {
    display: flex;
    justify-content: space-between;
    gap: 40px;
  }

  .challenge-name {
    font-size: 150%;
  }
</style>
