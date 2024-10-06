<script >
    import Particles, { particlesInit } from '@tsparticles/svelte';
	import { loadFull } from "tsparticles"; 

    let particlesConfig = {
		particles: {
			color: { value: "#ffffff" },
      move: {
        direction: "none",
        enable: true,
        outModes: "out",
        random: true,
        speed: 0.3
      },
      number: {
        density: {
          enable: true
        },
        value: 600
      },
      opacity: {
        animation: {
          enable: true,
          speed: 5
        },
        value: { min: 0.3, max: 0.6 }
      },
      shape: {
        type: "circle"
      },
      size: {
        value: 1
      }
    }
	};


	let onParticlesLoaded = (event) => {
		const particlesContainer = event.detail.particles;

		// you can use particlesContainer to call all the Container class
		// (from the core library) methods like play, pause, refresh, start, stop
	};

	void particlesInit(async (engine) => {
		// call this once per app
		// you can use main to customize the tsParticles instance adding presets or custom shapes
		// this loads the tsparticles package bundle, it's the easiest method for getting everything ready
		// starting from v2 you can add only the features you need reducing the bundle size
		//await loadFull(engine);
		await loadFull(engine);
	});
</script>

<main>
    <div class="particles">
        <Particles
	id="tsparticles"
	class="put your classes here"
	style=""
	options="{particlesConfig}"
	on:particlesLoaded="{onParticlesLoaded}"
/>
<slot>
    
</slot>
    </div>
</main>

<style>

    
</style>