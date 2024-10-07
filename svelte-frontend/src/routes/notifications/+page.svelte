<script>
    import Body from "../components/Body.svelte";
    import Footer from "../components/Footer.svelte";
    import Header from "../components/Header.svelte";
    import Particles from "../components/Particles.svelte";


</script>

<main>
    <Header />
    <Body>
    <Particles>
        <div class="main-text">
            <h1>Sign Up For Notifications!</h1>
            <form id="input" action="http://127.0.0.1:5000/getEmail" method="POST">
                <div class="form-container">
                    <h3>Coordinates:</h3>
                    <div class="coords">
                        <input type="text" name="latitude" placeholder="-180.000" required>
                    <input type="text" name="longitude" placeholder="+180.000" required>
                    </div>
                    <h3>Email:</h3>
                    <input type="email" name="email" placeholder="...@.com" required>
                    <button type="submit" form="post">Send Off!</button>
                </div>
            </form>
        </div>
    </Particles>
    </Body>
    <Footer />
</main>

<style>
    .main-text{
        color: white;
    }
    
    .main-text{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }

    .form-container{
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .coords{
        display: flex;
        gap: 30px;
    }

    button{
        margin-top: 15%;
    }
</style>