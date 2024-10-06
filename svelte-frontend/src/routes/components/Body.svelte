<main>
    <body>
        <div class="container">
            <slot>
                
            </slot>
        </div>
    </body>
</main>

<style>
    *{
        box-sizing: border-box;
        padding: 0;
        margin: 0;
    }
    
    body{
        display: flex;
        flex-direction: column;
        min-height: 100vh;
        background-color: rgb(14, 13, 13);
    }

    .container{
        height: 80vh;
    }
</style>