# Domain Fronting Using Azure

First, I signed up for an Azure student account [here](https://azure.microsoft.com/en-us/free/students/). They give you $100 free credit, which is what I used towards setting up my CDN. 

![](https://github.com/hmm14e/NetworkSecurity/blob/master/images/CDNProfile.png)

You dont want to use Akami because it doesnt work for domains outside of azure. 

![](https://github.com/hmm14e/NetworkSecurity/blob/master/images/ProfileOverview.png)

Next, we are going to add an edge server/endpoint which acts as our proxy. 

![](https://github.com/hmm14e/NetworkSecurity/blob/master/images/CreateEndpoint.png)

Name: this is going to be the sub domain which you’ll use in the Host header, so make it something that looks legit. I’ve been using names which imply advertising tracking or normal cdn usage.
Origin hostname: this is where it’ll forward your traffic.
I believe you can put the origin host name to any domain, but I just put a random domain because I thought it was a funny website and easy to test on.

![](https://github.com/hmm14e/NetworkSecurity/blob/master/images/Successful.png)

They're not lying when they say it takes 90 minutes to set up. Mine took a little longer than 90 minutes. So if you see a 404 error, that's why -- give it time. 

![](https://github.com/hmm14e/NetworkSecurity/blob/master/images/BypassCaching.png)

While this is configuring, go to the settings of your endpoint -> Caching rules and set the caching for the URL to be "bypass string caching behavior". You dont want this to cache your requests.

Once it's finally set up, I used [this](https://github.com/hmm14e/NetworkSecurity/blob/master/FontableAzureEdgeDomains) list to test some of these domains and see if it was fronting. Here is an example that worked. 
`wget -qO - https://admin.impulsescreen.com --header 'Host: studentfrontingdomaintest.azureedge.net' | grep title`




Credit to [this guy](https://theobsidiantower.com/2017/07/24/d0a7cfceedc42bdf3a36f2926bd52863ef28befc.html) for helping me set all of this up. 
