<footer>
  <div class="container">
    <div class="row">
      <div class="col-md-10">
        <p>
          Created by <a href="https://bsky.app/profile/rahulbot.bsky.social">Rahul Bhargava</a>.
          <br />
          A project of the <a href="https://dataculture.northeastern.edu/" target="_new">Data Culture Group</a> in the School of Journalism and Media Innovation at Northeastern University.
          <br />
          Created as <a href="">an open-source project</a> using the Svelte component library.
        </p>
      </div>
      <div class="col-md-2">
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
  padding: 2rem 0 4rem 0;
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