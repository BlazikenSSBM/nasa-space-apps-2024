<script>
  import Footer from "./components/Footer.svelte";
  import Header from "./components/Header.svelte";

  let count = 0;
  let message = '';

  function button_pressed() {
    count += 1;
  }

  async function get_message() {
    const response = await fetch('http://127.0.0.1:5000/api/data');
    const data = await response.json();
    message = data.message;
  };


</script>

<main>
  <body>
    <Header />
    <div class="container">
      <div class="main-text">
        <h1 class="group-name">Nerds From Space</h1>
        <h2 class="challenge-name">Landsat Imagery</h2>
        <h4>Input Coordinates:</h4>
        <div class="inputs">
          <form action="http://127.0.0.1:5000/getCoordinates" method="POST">
            <input type="text" name = "longitude" placeholder="+180.000" required/>
            <input type="text" name = "latitude" placeholder="+180.000" required />
            <button type="submit">Submit</button>
          </form>
        </div>
        <button on:click={button_pressed}>Launch Off! {count}</button>
        <button on:click={get_message}>Get Message from Server!</button>
        <p>Message from server:</p>
        <h1>{message}</h1>
      </div>
    </div>
    <Footer />
  </body>
</main>

<style>
  * {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
  }
  body {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background-color: white;
  }
  .container {
    height: 700px;
    margin-top: 10%;
  }

  h2 {
    margin-top: -15px;
  }

  .main-text {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
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
