<header>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div id="title-wrapper">
          <h1>Protest Mapper</h1>
          <img id="logo" src="logo.png" alt="Logo" class="logo"/>
        </div>
      </div>
    </div>
  </div>
</header>

<section class="subheader">
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <p>
          Protests have sprung up across the US since President Trump was re-elected, on a wide variety of topics.
          Journalists writing about local events often want to contextualize those individual incidents within larger
          trends. This website is here to help.
        </p>
      </div>
      <div class="col-md-4">
        <p>
          Use the simple tool below to create an embeddable simple map of protests in your area. The underlying data is 
          updated once a week on Mondays, and includes protests from the start of the year till that date.
          <a href="https://www.storybench.org/try-this-tool-to-map-protests-for-local-news/">Learn more on the Storybench blog post</a>.
        </p>
      </div>
      <div class="col-md-4">
        <p>
          Clicking a pin on the map shows a short summary of what the protest was about. The underlying data is from two
          groups that track protests: the 
          <a href="https://acleddata.com/" target=_new>Armed Conflict Location & Event Data Project (ACLED)</a> and 
          the <a href="https://ash.harvard.edu/programs/crowd-counting-consortium/" target=_new>Crowd Counting Consortium (CCC)</a>.
        </p>
      </div>
    </div>
  </div>
</section>

<style>
header {
    background-color: var(--palette-primary);
    color: #fff;
    padding: 2rem;
    border-bottom: var(--palette-tertiary) 2px solid;
}
.subheader {
    background-color: var(--palette-light-background);
    padding: 2rem;
    a {
      color: var(--palette-primary);
    }
}
#title-wrapper {
  position: relative;  
}
#logo {
  position: absolute;
  top: 0;
  right: 2rem;
  height: 80px;
}

@media (max-width: 575.98px) {
  #logo {
    display: none;
  }
}

section {
  border-left: 0px;
}
</style>