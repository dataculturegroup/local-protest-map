<script>
  let { version } = $props();
</script>

<footer>
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <p>
          Protest Mapper is an 
          <a href="https://github.com/dataculturegroup/local-protest-map" target="_new">open-source project</a> 
          of the <a href="https://dataculture.northeastern.edu/" target="_new">Data Culture Group</a> in 
          the <a href="https://camd.northeastern.edu/journalism/" target="_new">School of Journalism and Media Innovation</a> 
          at Northeastern University.
        </p>
        <p>Created by <a href="https://bsky.app/profile/rahulbot.bsky.social">Rahul Bhargava</a>.</p>
        <p>Version {version}</p>
      </div>
      <div class="col-md-2 offset-4">
        <div class="logo-wrapper">
          <a href="https://dataculture.northeastern.edu" target=_new>
            <img src="https://dataculture.northeastern.edu/static/img/dcg-logo.png" alt="Data Culture Group Logo" style="width: 100px; height: auto;" />
          </a>
      </div>
    </div>
  </div>
</footer>

<style>
  footer {
    background-color: var(--palette-light-background);
    padding: 4rem 0 6rem 0;
    border-top: var(--palette-tertiary) 2px solid;

    a {
      color: var(--palette-primary);
    }

    .logo-wrapper {
      background-color: white;
      display: inline-block;
      padding: 1rem;
      border-radius: 15px;
    }
  }
</style>