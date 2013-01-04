  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Emulator-Shader-Pack/tools/cg2xml.py at master · Themaister/Emulator-Shader-Pack · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon-precomposed" sizes="57x57" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="apple-touch-icon-144.png" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="apple-touch-icon-144.png" />
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="QJQ42jNGEBFqK6Z1kvxCRCEGcRoeQ2UtzerUHVu29N8=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-122cbe2bb79cff402163ef90653885eef495d468.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-2af5790b990d9a26fadc25174dc35eb2bdc545fb.css" media="screen" rel="stylesheet" type="text/css" />
    


    <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-971f385ccf2fcbf04f87e9ffca82e855620eb233.js" type="text/javascript"></script>
    <script src="https://a248.e.akamai.net/assets.github.com/assets/github-44260b1fca293cb0de2ed4a53426536a1af440c9.js" type="text/javascript"></script>
    

        <link rel='permalink' href='/Themaister/Emulator-Shader-Pack/blob/7ab5b1510482efb2a50221a173fe9e6e7d5ffe95/tools/cg2xml.py'>
    <meta property="og:title" content="Emulator-Shader-Pack"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/Themaister/Emulator-Shader-Pack"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/5cddab5babde6f527c35335d5c7195c3?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="Emulator-Shader-Pack - Various pixel shaders in Cg for oldschool emulators"/>

    <meta name="description" content="Emulator-Shader-Pack - Various pixel shaders in Cg for oldschool emulators" />

  <link href="https://github.com/Themaister/Emulator-Shader-Pack/commits/master.atom" rel="alternate" title="Recent Commits to Emulator-Shader-Pack:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob  vis-public env-production ">
    <div id="wrapper">

      

      

      


        <div class="header header-logged-out">
          <div class="container clearfix">

            <a class="header-logo-wordmark" href="https://github.com/">
              <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1337118071" />
              <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1337118071" />
            </a>

              
<ul class="top-nav">
    <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
  <li class="search"><a href="https://github.com/search">Search</a></li>
  <li class="features"><a href="https://github.com/features">Features</a></li>
    <li class="blog"><a href="https://github.com/blog">Blog</a></li>
</ul>


            <div class="header-actions">
                <a class="button primary classy" href="https://github.com/signup">Sign up for free</a>
              <a class="button classy" href="https://github.com/login?return_to=%2FThemaister%2FEmulator-Shader-Pack%2Fblob%2Fmaster%2Ftools%2Fcg2xml.py">Sign in</a>
            </div>

          </div>
        </div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu">
          <div class="container">
            <div class="title-actions-bar">
              


                  <ul class="pagehead-actions">


          <li>
            <span class="star-button"><a href="/login?return_to=%2FThemaister%2FEmulator-Shader-Pack" class="minibutton js-toggler-target entice tooltipped leftwards" title="You must be signed in to use this feature" rel="nofollow"><span class="mini-icon mini-icon-star"></span>Star</a><a class="social-count js-social-count" href="/Themaister/Emulator-Shader-Pack/stargazers">15</a></span>
          </li>
          <li>
            <a href="/login?return_to=%2FThemaister%2FEmulator-Shader-Pack" class="minibutton js-toggler-target fork-button entice tooltipped leftwards"  title="You must be signed in to fork a repository" rel="nofollow"><span class="mini-icon mini-icon-fork"></span>Fork</a><a href="/Themaister/Emulator-Shader-Pack/network" class="social-count">2</a>
          </li>
    </ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/Themaister" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">Themaister</span>
                  </a></span> /
                <strong><a href="/Themaister/Emulator-Shader-Pack" class="js-current-repository">Emulator-Shader-Pack</a></strong>
              </h1>
            </div>

            

  <ul class="tabs">
    <li><a href="/Themaister/Emulator-Shader-Pack" class="selected" highlight="repo_sourcerepo_downloadsrepo_commitsrepo_tagsrepo_branches">Code</a></li>
    <li><a href="/Themaister/Emulator-Shader-Pack/network" highlight="repo_network">Network</a></li>
    <li><a href="/Themaister/Emulator-Shader-Pack/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/Themaister/Emulator-Shader-Pack/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>



    <li><a href="/Themaister/Emulator-Shader-Pack/graphs" highlight="repo_graphsrepo_contributors">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/Themaister/Emulator-Shader-Pack/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
    
  </span>

  <div class="tabnav-widget scope">


    <div class="context-menu-container js-menu-container js-context-menu">
      <a href="#"
         class="minibutton bigger switcher js-menu-target js-commitish-button btn-branch repo-tree"
         data-hotkey="w"
         data-ref="master">
         <span><em class="mini-icon mini-icon-branch"></em><i>branch:</i> master</span>
      </a>

      <div class="context-pane commitish-context js-menu-content">
        <a href="#" class="close js-menu-close"><span class="mini-icon mini-icon-remove-close"></span></a>
        <div class="context-title">Switch branches/tags</div>
        <div class="context-body pane-selector commitish-selector js-navigation-container">
          <div class="filterbar">
            <input type="text" id="context-commitish-filter-field" class="js-navigation-enable js-filterable-field js-ref-filter-field" placeholder="Filter branches/tags">
            <ul class="tabs">
              <li><a href="#" data-filter="branches" class="selected">Branches</a></li>
                <li><a href="#" data-filter="tags">Tags</a></li>
            </ul>
          </div>

          <div class="js-filter-tab js-filter-branches">
            <div data-filterable-for="context-commitish-filter-field" data-filterable-type=substring>
                <div class="commitish-item branch-commitish selector-item js-navigation-item js-navigation-target selected">
                  <span class="mini-icon mini-icon-confirm"></span>
                  <h4>
                      <a href="/Themaister/Emulator-Shader-Pack/blob/master/tools/cg2xml.py" class="js-navigation-open" data-name="master" rel="nofollow">master</a>
                  </h4>
                </div>
            </div>
            <div class="no-results">Nothing to show</div>


          </div>

            <div class="js-filter-tab js-filter-tags filter-tab-empty" style="display:none">
              <div data-filterable-for="context-commitish-filter-field" data-filterable-type=substring>
              </div>
              <div class="no-results">Nothing to show</div>
            </div>

        </div>
      </div><!-- /.commitish-context-context -->
    </div>
  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/Themaister/Emulator-Shader-Pack" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/Themaister/Emulator-Shader-Pack/commits/master" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/Themaister/Emulator-Shader-Pack/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:56008231dc530dd1bef2555f6e0e1acc -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:56008231dc530dd1bef2555f6e0e1acc -->

<div id="slider">


    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>
      <div class="breadcrumb">
        <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Themaister/Emulator-Shader-Pack" class="js-slide-to" data-direction="back" itemscope="url"><span itemprop="title">Emulator-Shader-Pack</span></a></span></span> / <span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Themaister/Emulator-Shader-Pack/tree/master/tools" class="js-slide-to" data-direction="back" itemscope="url"><span itemprop="title">tools</span></a></span> / <strong class="final-path">cg2xml.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="tools/cg2xml.py" data-copied-hint="copied!" title="copy to clipboard"><span class="mini-icon mini-icon-clipboard"></span></span>
      </div>

      <a href="/Themaister/Emulator-Shader-Pack/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>

        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/5cddab5babde6f527c35335d5c7195c3?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/Themaister" rel="author">Themaister</a></span>
    <time class="js-relative-date" datetime="2012-11-16T15:01:02-08:00" title="2012-11-16 15:01:02">November 16, 2012</time>
    <div class="commit-title">
        <a href="/Themaister/Emulator-Shader-Pack/commit/7ab5b1510482efb2a50221a173fe9e6e7d5ffe95" class="message">Retrain directory structure.</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/5cddab5babde6f527c35335d5c7195c3?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/Themaister">Themaister</a>
        </li>
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/Themaister/Emulator-Shader-Pack/blob/7ab5b1510482efb2a50221a173fe9e6e7d5ffe95/tools/cg2xml.py" data-title="Emulator-Shader-Pack/tools/cg2xml.py at master · Themaister/Emulator-Shader-Pack · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">executable file</span>
                  <span>342 lines (275 sloc)</span>
                <span>11.361 kb</span>
              </div>
              <ul class="button-group actions">
                  <li>
                      <a class="grouped-button minibutton bigger lighter js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  </li>
                <li><a href="/Themaister/Emulator-Shader-Pack/raw/master/tools/cg2xml.py" class="minibutton grouped-button bigger lighter" id="raw-url">Raw</a></li>
                  <li><a href="/Themaister/Emulator-Shader-Pack/blame/master/tools/cg2xml.py" class="minibutton grouped-button bigger lighter">Blame</a></li>
                <li><a href="/Themaister/Emulator-Shader-Pack/commits/master/tools/cg2xml.py" class="minibutton grouped-button bigger lighter" rel="nofollow">History</a></li>
              </ul>
            </div>
                <div class="data type-python">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
</pre>
          </td>
          <td width="100%">
                <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC4'><span class="sd">Python 3 script which converts simple RetroArch Cg shaders to modern XML/GLSL format.</span></div><div class='line' id='LC5'><span class="sd">Author: Hans-Kristian Arntzen (Themaister)</span></div><div class='line' id='LC6'><span class="sd">License: Public domain</span></div><div class='line' id='LC7'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC10'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC11'><span class="kn">import</span> <span class="nn">errno</span></div><div class='line' id='LC12'><span class="kn">import</span> <span class="nn">subprocess</span></div><div class='line' id='LC13'><br/></div><div class='line' id='LC14'><span class="n">batch_mode</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="o">*</span><span class="n">arg</span><span class="p">):</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">batch_mode</span><span class="p">:</span></div><div class='line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="o">*</span><span class="n">arg</span><span class="p">)</span></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="k">def</span> <span class="nf">remove_comments</span><span class="p">(</span><span class="n">source_lines</span><span class="p">):</span></div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;<span class="n">ret</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;<span class="n">killed_comments</span> <span class="o">=</span> <span class="p">[</span><span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;//&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">source_lines</span><span class="p">]</span></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">filter</span><span class="p">(</span><span class="k">lambda</span> <span class="n">line</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">line</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">,</span> <span class="n">killed_comments</span><span class="p">):</span></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ret</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ret</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><span class="k">def</span> <span class="nf">keep_line_if</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">lines</span><span class="p">):</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;<span class="n">ret</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">filter</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">lines</span><span class="p">):</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ret</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ret</span></div><div class='line' id='LC32'><br/></div><div class='line' id='LC33'><span class="k">def</span> <span class="nf">replace_global_vertex</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;<span class="n">replace_table</span> <span class="o">=</span> <span class="p">[</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;POSITION&#39;</span><span class="p">,</span> <span class="s">&#39;rubyVertexCoord&#39;</span><span class="p">),</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;TEXCOORD0&#39;</span><span class="p">,</span> <span class="s">&#39;rubyTexCoord&#39;</span><span class="p">),</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;TEXCOORD&#39;</span><span class="p">,</span> <span class="s">&#39;rubyTexCoord&#39;</span><span class="p">),</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;uniform vec4 _modelViewProj1[4]&#39;</span><span class="p">,</span> <span class="s">&#39;uniform mat4 rubyMVPMatrix&#39;</span><span class="p">),</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;_modelViewProj1&#39;</span><span class="p">,</span> <span class="s">&#39;rubyMVPMatrix&#39;</span><span class="p">),</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;rubyMVPMatrix[0]&#39;</span><span class="p">,</span> <span class="s">&#39;rubyMVPMatrix_[0]&#39;</span><span class="p">),</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;rubyMVPMatrix[1]&#39;</span><span class="p">,</span> <span class="s">&#39;rubyMVPMatrix_[1]&#39;</span><span class="p">),</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;rubyMVPMatrix[2]&#39;</span><span class="p">,</span> <span class="s">&#39;rubyMVPMatrix_[2]&#39;</span><span class="p">),</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;rubyMVPMatrix[3]&#39;</span><span class="p">,</span> <span class="s">&#39;rubyMVPMatrix_[3]&#39;</span><span class="p">),</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;_IN1._video_size&#39;</span><span class="p">,</span> <span class="s">&#39;rubyInputSize&#39;</span><span class="p">),</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;_IN1._texture_size&#39;</span><span class="p">,</span> <span class="s">&#39;rubyTextureSize&#39;</span><span class="p">),</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;_IN1._output_size&#39;</span><span class="p">,</span> <span class="s">&#39;rubyOutputSize&#39;</span><span class="p">),</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;input&#39;</span><span class="p">,</span> <span class="s">&#39;input_dummy&#39;</span><span class="p">),</span> <span class="c"># &#39;input&#39; is reserved in GLSL.</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;output&#39;</span><span class="p">,</span> <span class="s">&#39;output_dummy&#39;</span><span class="p">),</span> <span class="c"># &#39;output&#39; is reserved in GLSL.</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;<span class="p">]</span></div><div class='line' id='LC50'><br/></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">replacement</span> <span class="ow">in</span> <span class="n">replace_table</span><span class="p">:</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span> <span class="o">=</span> <span class="n">source</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">replacement</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">replacement</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">source</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'><span class="k">def</span> <span class="nf">translate_varyings</span><span class="p">(</span><span class="n">varyings</span><span class="p">,</span> <span class="n">source</span><span class="p">):</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;<span class="n">dictionary</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">varying</span> <span class="ow">in</span> <span class="n">varyings</span><span class="p">:</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">source</span><span class="p">:</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">varying</span> <span class="ow">in</span> <span class="n">line</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="s">&#39;//var&#39;</span> <span class="ow">in</span> <span class="n">line</span><span class="p">):</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Found line for&#39;</span><span class="p">,</span> <span class="n">varying</span> <span class="o">+</span> <span class="s">&#39;:&#39;</span><span class="p">,</span> <span class="n">line</span><span class="p">)</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dictionary</span><span class="p">[</span><span class="n">varying</span><span class="p">]</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">dictionary</span></div><div class='line' id='LC66'><br/></div><div class='line' id='LC67'><span class="k">def</span> <span class="nf">destructify_varyings</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;<span class="c"># We have to change varying structs that Cg support to single varyings for GL. Varying structs aren&#39;t supported until later versions</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;<span class="c"># of GLSL.</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;<span class="n">struct_types</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">source</span><span class="p">:</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;struct&#39;</span> <span class="ow">in</span> <span class="n">line</span><span class="p">:</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">struct_types</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Struct types:&#39;</span><span class="p">,</span> <span class="n">struct_types</span><span class="p">)</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;<span class="n">last_struct_decl_line</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;<span class="n">varyings</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;<span class="n">varyings_name</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;<span class="c"># Find all varyings in structs and make them &quot;global&quot; varyings.</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">struct</span> <span class="ow">in</span> <span class="n">struct_types</span><span class="p">:</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;struct &#39;</span> <span class="o">+</span> <span class="n">struct</span> <span class="ow">in</span> <span class="n">line</span><span class="p">:</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">j</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="p">(</span><span class="n">j</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">source</span><span class="p">))</span> <span class="ow">and</span> <span class="p">(</span><span class="s">&#39;};&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">source</span><span class="p">[</span><span class="n">j</span><span class="p">]):</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">j</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">varyings</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="s">&#39;varying &#39;</span> <span class="o">+</span> <span class="n">string</span> <span class="k">for</span> <span class="n">string</span> <span class="ow">in</span> <span class="n">source</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span> <span class="p">:</span> <span class="n">j</span><span class="p">]])</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">names</span> <span class="o">=</span> <span class="p">[</span><span class="n">string</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;;&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">string</span> <span class="ow">in</span> <span class="n">source</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span> <span class="p">:</span> <span class="n">j</span><span class="p">]]</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">varyings_name</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">names</span><span class="p">)</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Found elements in struct&#39;</span><span class="p">,</span> <span class="n">struct</span> <span class="o">+</span> <span class="s">&#39;:&#39;</span><span class="p">,</span> <span class="n">names</span><span class="p">)</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">last_struct_decl_line</span> <span class="o">=</span> <span class="n">j</span></div><div class='line' id='LC92'><br/></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;<span class="n">varyings_tmp</span> <span class="o">=</span> <span class="n">varyings</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;<span class="n">varyings</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;<span class="n">variables</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC96'><br/></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;<span class="c"># Don&#39;t include useless varyings like IN.video_size, IN.texture_size, etc as they are not actual varyings ...</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">filter</span><span class="p">(</span><span class="k">lambda</span> <span class="n">v</span><span class="p">:</span> <span class="p">(</span><span class="s">&#39;_video_size&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">v</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="s">&#39;_texture_size&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">v</span><span class="p">)</span> <span class="ow">and</span> <span class="s">&#39;_output_size&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">v</span><span class="p">,</span> <span class="n">varyings_tmp</span><span class="p">):</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">varyings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span></div><div class='line' id='LC100'><br/></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;<span class="c"># Find any global variable struct that is supposed to be the output varying, and redirect all references to it to</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;<span class="c"># the actual varyings we just declared ...</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;<span class="c"># Globals only come before main() ...</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;<span class="c"># Make sure to only look after all struct declarations as there might be overlap.</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">source</span><span class="p">[</span><span class="n">last_struct_decl_line</span><span class="p">:]:</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;void main()&#39;</span> <span class="ow">in</span> <span class="n">line</span><span class="p">:</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC108'><br/></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">struct</span> <span class="ow">in</span> <span class="n">struct_types</span><span class="p">:</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">struct</span> <span class="ow">in</span> <span class="n">line</span><span class="p">:</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">variable</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;;&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Found struct variable for&#39;</span><span class="p">,</span> <span class="n">struct</span> <span class="o">+</span> <span class="s">&#39;:&#39;</span><span class="p">,</span> <span class="n">variable</span><span class="p">)</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">variables</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">variable</span><span class="p">)</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;<span class="n">varyings_dict</span> <span class="o">=</span> <span class="n">translate_varyings</span><span class="p">(</span><span class="n">varyings_name</span><span class="p">,</span> <span class="n">source</span><span class="p">)</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Varyings dict:&#39;</span><span class="p">,</span> <span class="n">varyings_dict</span><span class="p">)</span></div><div class='line' id='LC117'><br/></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;<span class="c"># Append all varyings. Keep the structs as they might be used as regular values.</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">varying</span> <span class="ow">in</span> <span class="n">varyings</span><span class="p">:</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">varying</span><span class="p">)</span></div><div class='line' id='LC121'><br/></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;<span class="c"># Replace struct access with global access, e.g. (_co1._c00 =&gt; _c00)</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;<span class="c"># Also replace mangled Cg name with &#39;real&#39; name.</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">variable</span> <span class="ow">in</span> <span class="n">variables</span><span class="p">:</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">source</span><span class="p">[</span><span class="n">index</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">variable</span> <span class="o">+</span> <span class="s">&#39;.&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">);</span></div><div class='line' id='LC127'><br/></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">varying_name</span> <span class="ow">in</span> <span class="n">varyings_name</span><span class="p">:</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">varying_name</span> <span class="ow">in</span> <span class="n">varyings_dict</span><span class="p">:</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">source</span><span class="p">[</span><span class="n">index</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">varying_name</span><span class="p">,</span> <span class="n">varyings_dict</span><span class="p">[</span><span class="n">varying_name</span><span class="p">])</span></div><div class='line' id='LC132'><br/></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">source</span></div><div class='line' id='LC134'><br/></div><div class='line' id='LC135'><br/></div><div class='line' id='LC136'><span class="k">def</span> <span class="nf">hack_source_vertex</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;<span class="n">transpose_index</span> <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;<span class="n">code_index</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;void main()&#39;</span> <span class="ow">in</span> <span class="n">line</span><span class="p">:</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">index</span> <span class="o">+</span> <span class="mi">2</span><span class="p">,</span> <span class="s">&#39;    mat4 rubyMVPMatrix_ = transpose_(rubyMVPMatrix);&#39;</span><span class="p">)</span> <span class="c"># transpose() is GLSL 1.20+, doesn&#39;t exist in GLSL ES 1.0</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="s">&#39;uniform vec2 rubyInputSize;&#39;</span><span class="p">)</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="s">&#39;uniform vec2 rubyTextureSize;&#39;</span><span class="p">)</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="s">&#39;uniform vec2 rubyOutputSize;&#39;</span><span class="p">)</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC146'><span class="s">         mat4 transpose_(mat4 matrix)</span></div><div class='line' id='LC147'><span class="s">         {</span></div><div class='line' id='LC148'><span class="s">            mat4 ret;</span></div><div class='line' id='LC149'><span class="s">            for (int i = 0; i &lt; 4; i++)</span></div><div class='line' id='LC150'><span class="s">               for (int j = 0; j &lt; 4; j++)</span></div><div class='line' id='LC151'><span class="s">                  ret[i][j] = matrix[j][i];</span></div><div class='line' id='LC152'><br/></div><div class='line' id='LC153'><span class="s">            return ret;</span></div><div class='line' id='LC154'><span class="s">         }</span></div><div class='line' id='LC155'><span class="s">         &quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC157'><br/></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;<span class="n">source</span> <span class="o">=</span> <span class="n">destructify_varyings</span><span class="p">(</span><span class="n">source</span><span class="p">)</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">source</span></div><div class='line' id='LC160'><br/></div><div class='line' id='LC161'><span class="k">def</span> <span class="nf">replace_global_fragment</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;<span class="n">replace_table</span> <span class="o">=</span> <span class="p">[</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;_IN1._video_size&#39;</span><span class="p">,</span> <span class="s">&#39;rubyInputSize&#39;</span><span class="p">),</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;_IN1._texture_size&#39;</span><span class="p">,</span> <span class="s">&#39;rubyTextureSize&#39;</span><span class="p">),</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;_IN1._output_size&#39;</span><span class="p">,</span> <span class="s">&#39;rubyOutputSize&#39;</span><span class="p">),</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;input&#39;</span><span class="p">,</span> <span class="s">&#39;input_dummy&#39;</span><span class="p">),</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;output&#39;</span><span class="p">,</span> <span class="s">&#39;output_dummy&#39;</span><span class="p">),</span> <span class="c"># &#39;output&#39; is reserved in GLSL.</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;<span class="p">]</span></div><div class='line' id='LC169'><br/></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">replacement</span> <span class="ow">in</span> <span class="n">replace_table</span><span class="p">:</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span> <span class="o">=</span> <span class="n">source</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">replacement</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">replacement</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC172'><br/></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">source</span></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'><span class="k">def</span> <span class="nf">hack_source_fragment</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;void main()&#39;</span> <span class="ow">in</span> <span class="n">line</span><span class="p">:</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="s">&#39;uniform vec2 rubyInputSize;&#39;</span><span class="p">)</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="s">&#39;uniform vec2 rubyTextureSize;&#39;</span><span class="p">)</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="s">&#39;uniform vec2 rubyOutputSize;&#39;</span><span class="p">)</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC182'><br/></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">source</span><span class="p">:</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="s">&#39;TEXUNIT0&#39;</span> <span class="ow">in</span> <span class="n">line</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="s">&#39;semantic&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">line</span><span class="p">):</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sampler</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Fragment: Sampler:&#39;</span><span class="p">,</span> <span class="n">sampler</span><span class="p">)</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC188'><br/></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;<span class="n">ret</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">source</span><span class="p">:</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ret</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">sampler</span><span class="p">,</span> <span class="s">&#39;rubyTexture&#39;</span><span class="p">))</span></div><div class='line' id='LC192'><br/></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;<span class="n">ret</span> <span class="o">=</span> <span class="n">destructify_varyings</span><span class="p">(</span><span class="n">ret</span><span class="p">)</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ret</span></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'><span class="k">def</span> <span class="nf">validate_shader</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">target</span><span class="p">):</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;<span class="n">command</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;cgc&#39;</span><span class="p">,</span> <span class="s">&#39;-noentry&#39;</span><span class="p">,</span> <span class="s">&#39;-ogles&#39;</span><span class="p">]</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">(</span><span class="n">command</span><span class="p">,</span> <span class="n">stdin</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span> <span class="n">stdout</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span> <span class="n">stderr</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">)</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;<span class="n">stdout_ret</span><span class="p">,</span> <span class="n">stderr_ret</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">communicate</span><span class="p">(</span><span class="n">source</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span></div><div class='line' id='LC200'><br/></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Shader:&#39;</span><span class="p">)</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;===&#39;</span><span class="p">)</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="n">source</span><span class="p">)</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;===&#39;</span><span class="p">)</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;CGC:&#39;</span><span class="p">,</span> <span class="n">stderr_ret</span><span class="o">.</span><span class="n">decode</span><span class="p">())</span></div><div class='line' id='LC206'><br/></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">p</span><span class="o">.</span><span class="n">returncode</span> <span class="o">==</span> <span class="mi">0</span></div><div class='line' id='LC208'><br/></div><div class='line' id='LC209'><span class="k">def</span> <span class="nf">convert</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">dest</span><span class="p">):</span></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;<span class="n">vert_cmd</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;cgc&#39;</span><span class="p">,</span> <span class="s">&#39;-profile&#39;</span><span class="p">,</span> <span class="s">&#39;glesv&#39;</span><span class="p">,</span> <span class="s">&#39;-entry&#39;</span><span class="p">,</span> <span class="s">&#39;main_vertex&#39;</span><span class="p">,</span> <span class="n">source</span><span class="p">]</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">(</span><span class="n">vert_cmd</span><span class="p">,</span> <span class="n">stderr</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span> <span class="n">stdout</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">)</span></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;<span class="n">vertex_source</span><span class="p">,</span> <span class="n">stderr_ret</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">communicate</span><span class="p">()</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="n">stderr_ret</span><span class="o">.</span><span class="n">decode</span><span class="p">())</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;<span class="n">vertex_source</span> <span class="o">=</span> <span class="n">vertex_source</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span></div><div class='line' id='LC215'><br/></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">p</span><span class="o">.</span><span class="n">returncode</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Vertex compilation failed ...&#39;</span><span class="p">)</span></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="mi">1</span></div><div class='line' id='LC219'><br/></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;<span class="n">frag_cmd</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;cgc&#39;</span><span class="p">,</span> <span class="s">&#39;-profile&#39;</span><span class="p">,</span> <span class="s">&#39;glesf&#39;</span><span class="p">,</span> <span class="s">&#39;-entry&#39;</span><span class="p">,</span> <span class="s">&#39;main_fragment&#39;</span><span class="p">,</span> <span class="n">source</span><span class="p">]</span></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">(</span><span class="n">frag_cmd</span><span class="p">,</span> <span class="n">stderr</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span> <span class="n">stdout</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">)</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;<span class="n">fragment_source</span><span class="p">,</span> <span class="n">stderr_ret</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">communicate</span><span class="p">()</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="n">stderr_ret</span><span class="o">.</span><span class="n">decode</span><span class="p">())</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;<span class="n">fragment_source</span> <span class="o">=</span> <span class="n">fragment_source</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span></div><div class='line' id='LC225'><br/></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">p</span><span class="o">.</span><span class="n">returncode</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Vertex compilation failed ...&#39;</span><span class="p">)</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="mi">1</span></div><div class='line' id='LC229'><br/></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;<span class="n">vertex_source</span>   <span class="o">=</span> <span class="n">replace_global_vertex</span><span class="p">(</span><span class="n">vertex_source</span><span class="p">)</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;<span class="n">fragment_source</span> <span class="o">=</span> <span class="n">replace_global_fragment</span><span class="p">(</span><span class="n">fragment_source</span><span class="p">)</span></div><div class='line' id='LC232'><br/></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;<span class="n">vertex_source</span>   <span class="o">=</span> <span class="n">vertex_source</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;<span class="n">fragment_source</span> <span class="o">=</span> <span class="n">fragment_source</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC235'><br/></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;<span class="c"># Cg think we&#39;re using row-major matrices, but we&#39;re using column major.</span></div><div class='line' id='LC237'>&nbsp;&nbsp;&nbsp;<span class="c"># Also, Cg tends to compile matrix multiplications as dot products in GLSL.</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;<span class="c"># Hack in a fix for this.</span></div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;<span class="n">vertex_source</span>   <span class="o">=</span> <span class="n">hack_source_vertex</span><span class="p">(</span><span class="n">vertex_source</span><span class="p">)</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;<span class="n">fragment_source</span> <span class="o">=</span> <span class="n">hack_source_fragment</span><span class="p">(</span><span class="n">fragment_source</span><span class="p">)</span></div><div class='line' id='LC241'><br/></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;<span class="c"># We compile to GLES, but we really just want modern GL ...</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;<span class="n">vertex_source</span>   <span class="o">=</span> <span class="n">keep_line_if</span><span class="p">(</span><span class="k">lambda</span> <span class="n">line</span><span class="p">:</span> <span class="s">&#39;precision&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">line</span><span class="p">,</span> <span class="n">vertex_source</span><span class="p">)</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;<span class="n">fragment_source</span> <span class="o">=</span> <span class="n">keep_line_if</span><span class="p">(</span><span class="k">lambda</span> <span class="n">line</span><span class="p">:</span> <span class="s">&#39;precision&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">line</span><span class="p">,</span> <span class="n">fragment_source</span><span class="p">)</span></div><div class='line' id='LC245'><br/></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;<span class="c"># Kill all comments. Cg adds lots of useless comments.</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;<span class="c"># Remove first line. It contains the name of the cg program.</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;<span class="n">vertex_source</span>   <span class="o">=</span> <span class="n">remove_comments</span><span class="p">(</span><span class="n">vertex_source</span><span class="p">[</span><span class="mi">1</span><span class="p">:])</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;<span class="n">fragment_source</span> <span class="o">=</span> <span class="n">remove_comments</span><span class="p">(</span><span class="n">fragment_source</span><span class="p">[</span><span class="mi">1</span><span class="p">:])</span></div><div class='line' id='LC250'><br/></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;<span class="n">out_vertex</span> <span class="o">=</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">vertex_source</span><span class="p">)</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;<span class="n">out_fragment</span> <span class="o">=</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s">&#39;#ifdef GL_ES&#39;</span><span class="p">,</span> <span class="s">&#39;precision mediump float;&#39;</span><span class="p">,</span> <span class="s">&#39;#endif&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">fragment_source</span><span class="p">)</span></div><div class='line' id='LC253'><br/></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">validate_shader</span><span class="p">(</span><span class="n">out_vertex</span><span class="p">,</span> <span class="s">&#39;glesv&#39;</span><span class="p">):</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Vertex shader does not compile ...&#39;</span><span class="p">)</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="mi">1</span></div><div class='line' id='LC257'><br/></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">validate_shader</span><span class="p">(</span><span class="n">out_fragment</span><span class="p">,</span> <span class="s">&#39;glesf&#39;</span><span class="p">):</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">log</span><span class="p">(</span><span class="s">&#39;Fragment shader does not compile ...&#39;</span><span class="p">)</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="mi">1</span></div><div class='line' id='LC261'><br/></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">dest</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;&lt;!-- XML/GLSL shader autogenerated by cg2xml.py --&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;&lt;shader language=&quot;GLSL&quot; style=&quot;GLES2&quot;&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;    &lt;vertex&gt;&lt;![CDATA[</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC267'><br/></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">out_vertex</span><span class="p">)</span></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC270'><br/></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39; ]]&gt;&lt;/vertex&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC272'><br/></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;    &lt;fragment&gt;&lt;![CDATA[</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC274'><br/></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">out_fragment</span><span class="p">)</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC277'><br/></div><div class='line' id='LC278'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39; ]]&gt;&lt;/fragment&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC279'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;&lt;/shader&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC280'><br/></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="mi">0</span></div><div class='line' id='LC282'><br/></div><div class='line' id='LC283'><span class="k">def</span> <span class="nf">main</span><span class="p">():</span></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">3</span><span class="p">:</span></div><div class='line' id='LC285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;Usage: {} prog.cg prog.shader&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span></div><div class='line' id='LC286'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="mi">1</span></div><div class='line' id='LC287'><br/></div><div class='line' id='LC288'>&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]):</span></div><div class='line' id='LC289'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">batch_mode</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">batch_mode</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">OSError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span></div><div class='line' id='LC294'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">e</span><span class="o">.</span><span class="n">errno</span> <span class="o">!=</span> <span class="n">errno</span><span class="o">.</span><span class="n">EEXIST</span><span class="p">:</span></div><div class='line' id='LC295'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span></div><div class='line' id='LC296'><br/></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">failed_cnt</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">success_cnt</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC299'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">failed_files</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">dirname</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">filenames</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">walk</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]):</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">source</span> <span class="ow">in</span> <span class="nb">filter</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="s">&#39;cg&#39;</span> <span class="o">==</span> <span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="p">[</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dirname</span><span class="p">,</span> <span class="n">filename</span><span class="p">)</span> <span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">filenames</span><span class="p">]):</span></div><div class='line' id='LC302'><br/></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span> <span class="n">source</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="s">&#39;&#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">:])</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;.cg&#39;</span><span class="p">,</span> <span class="s">&#39;.shader&#39;</span><span class="p">)</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dirpath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">dest</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;Dirpath:&#39;</span><span class="p">,</span> <span class="n">dirpath</span><span class="p">)</span></div><div class='line' id='LC306'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">dirpath</span><span class="p">):</span></div><div class='line' id='LC307'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">dirpath</span><span class="p">)</span></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">OSError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">e</span><span class="o">.</span><span class="n">errno</span> <span class="o">!=</span> <span class="n">errno</span><span class="o">.</span><span class="n">EEXIST</span><span class="p">:</span></div><div class='line' id='LC311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span></div><div class='line' id='LC312'><br/></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ret</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC315'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="s">&#39;-&gt;&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="p">,</span> <span class="s">&#39;...&#39;</span><span class="p">,</span> <span class="s">&#39;suceeded!&#39;</span> <span class="k">if</span> <span class="n">ret</span> <span class="o">==</span> <span class="mi">0</span> <span class="k">else</span> <span class="s">&#39;failed!&#39;</span><span class="p">)</span></div><div class='line' id='LC316'><br/></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">ret</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC318'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">success_cnt</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC319'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">failed_cnt</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">failed_files</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">source</span><span class="p">)</span></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="n">e</span><span class="p">)</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">failed_files</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">source</span><span class="p">)</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">failed_cnt</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC326'><br/></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="n">success_cnt</span><span class="p">,</span> <span class="s">&#39;shaders converted successfully.&#39;</span><span class="p">)</span></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="n">failed_cnt</span><span class="p">,</span> <span class="s">&#39;shaders failed.&#39;</span><span class="p">)</span></div><div class='line' id='LC329'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">failed_cnt</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;Failed shaders:&#39;</span><span class="p">)</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">failed_files</span><span class="p">:</span></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="n">path</span><span class="p">)</span></div><div class='line' id='LC333'><br/></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span>   <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span></div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="n">convert</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">dest</span><span class="p">))</span></div><div class='line' id='LC338'><br/></div><div class='line' id='LC339'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="n">main</span><span class="p">())</span></div><div class='line' id='LC341'><br/></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>
      </div>

      <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
      <div id="jump-to-line" style="display:none">
        <h2>Jump to Line</h2>
        <form accept-charset="UTF-8" class="js-jump-to-line-form">
          <input class="textfield js-jump-to-line-field" type="text">
          <div class="full-button">
            <button type="submit" class="classy">
              Go
            </button>
          </div>
        </form>
      </div>

    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1347543534" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.04661s from fe14.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    

    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus command bar</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last js-hidden-pane" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
        <dd>Submit comment</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> shift p</dt>
        <dd>Preview comment</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle selection</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
          <dd>Submit comment</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> shift p</dt>
          <dd>Preview comment</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Issues Dashboard</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div class="js-hidden-pane" >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first js-hidden-pane" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>w</dt>
          <dd>Switch branch/tag</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first">
        <h3>Browsing Commits</h3>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
          <dd>Submit comment</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>escape</dt>
          <dd>Close form</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>p</dt>
          <dd>Parent commit</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o</dt>
          <dd>Other parent commit</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>
    <h3>Notifications</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open notification</dd>
        </dl>
      </div><!-- /.column.first -->

      <div class="column second">
        <dl class="keyboard-mappings">
          <dt>e <em>or</em> shift i <em>or</em> y</dt>
          <dd>Mark as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift m</dt>
          <dd>Mute thread</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:

> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>


    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.04783' data-host='fe14'></span>
    
  </body>
</html>

