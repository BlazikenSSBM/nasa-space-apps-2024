<script>
    import logo from '$lib/img/logo.png';
</script>

<main>
    <div class="header">
        <img class="header-logo" src={logo} alt="Nerds From Space Logo">
        <div class="right-links">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/detailed">Detailed View</a></li>
                <li><a href="/notifications">Notifications</a></li>
            </ul>
        </div>
    </div>
</main>
<style>
    *{
        box-sizing: border-box;
        padding: 0;
        margin: 0;
    }

    .header {
        display: flex;
        justify-content: space-around;
        padding: 11px;
        align-items: center;
        background-color:rgb(14, 13, 13);
    } 
    .header-logo{
        height: 90px;
        width: 90px;
        border-radius: 50%;
    }

    ul{
        display: flex;
        list-style-type: none;
        gap: 15px;
    }

    a{
        text-decoration: none;
        color: #E5E7EB;
    }
</style>