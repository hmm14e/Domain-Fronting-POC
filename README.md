# Domain Fronting Using Azure

First, I signed up for an Azure student account [here](https://azure.microsoft.com/en-us/free/students/). They give you $100 free credit, which is what I used towards setting up my CDN. 

![](https://github.com/hmm14e/NetworkSecurity/blob/master/images/CDNProfile.png)

Name: this is going to be the sub domain which you’ll use in the Host header, so make it something that looks legit. 

You dont want to use Akami because it doesnt work for domains outside of azure. 
Next, we are going to add an edge server/endpoint which acts as our proxy. 

![](https://github.com/hmm14e/NetworkSecurity/blob/master/images/CreateEndpoint1.png)


![](https://github.com/hmm14e/NetworkSecurity/blob/master/images/ProfileOverview1.png)

Origin hostname: this is where it’ll forward your traffic.
I put my personal domain, `www.netsecproj.com` because it had cool ASCII art with a secret <title>

![](https://github.com/hmm14e/NetworkSecurity/blob/master/images/Successful.png)

It takes over 90 minutes to create your edge server. You will get 404 until it is set up. THIS IS NORMAL.

![](https://github.com/hmm14e/NetworkSecurity/blob/master/images/BypassCaching.png)

While this is configuring, go to the settings of your endpoint -> Caching rules and set the caching for the URL to be "bypass string caching behavior". You dont want this to cache your requests.

Once it's finally set up, I used [this](https://github.com/hmm14e/NetworkSecurity/blob/master/FontableAzureEdgeDomains) list to test some of these domains and see if it was fronting. Here is an example that worked. 

`wget -qO - https://admin.impulsescreen.com --header 'Host: studentfrontingdomaintest.azureedge1.net' | grep title`

I got back some HTTP stuff and

`<title>"I feel the need... " - Maverick " ...the need for speed!" - Maverick and Goose</title>`

It worked! It's important to note that the fronted domain needs to have **https://** in the beginning and the target domain should just be the domain. Not exactly sure why, but I had to figure this out the hard way. 

You can also do `curl -s -H "Host: studentfrontingdomaintest1.azureedge.net" -H "Connection: close" "https://admin.impulsescreen.com" | grep title` and get the same result. 






















Credit to [this guy](https://theobsidiantower.com/2017/07/24/d0a7cfceedc42bdf3a36f2926bd52863ef28befc.html) for helping me set all of this up. 
