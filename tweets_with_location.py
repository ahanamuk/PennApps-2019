from random import randrange
import json
ny = [(40.8448, -73.8648), (40.6782, -73.9442), (40.7282, -73.7949), (40.7831, -73.9712), (40.712776, -74.005974), (40.8448, -73.8648), (40.7891, -73.1350), (40.7128, -74.0060)]
staten_island = [(40.5795, 74.1502), (40.5083, -74.2355), (40.5790, 74.1500), (40.643501, -74.076202), (40.6424, -74.076036)]
matawan = [(40.4148, -74.2296)]
miller = [(40.5674, -74.0990)]
gerritsen = [(40.5870, -73.9228)]
nj = [(38.940782, -74.903198), (40.574627, -74.498259), (41.174024, -74.455183), (40.443266, -74.21796), (40.4333, -73.9885), (39.833851, -74.871826)]
rand = [(41.54786, -72.089488), (41.577343, -72.619665), (41.879005, -73.461611), (41.026444, -73.723707), (40.704374, -73.619445), (40.732762, -73.446471), (40.868057, -73.531053)]

tweets_lst = [{
	"handle": "Dominic_Smith",
	"body": " Will be working relief for hurricane Sandy for the foreseeable future. If you can help with a donation plead http://t.co/pR57f92T",
	"timestamp": "18 Nov 2012"
}, {
	"handle": "Anthony_Johnson",
	"body": " @benveekay please check 170k sea pine drive it the blue house second house in, bay side left thank you stay safe! #lbi #sandy #lbirecovery",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Matthew_Williams",
	"body": " My block. Reason we have #nopower #hurricanesandy http://t.co/lZroP316",
	"timestamp": "26 Nov 2012"
}, {
	"handle": "Eleanor_Brown",
	"body": " Petrides hs taking donations until 8pm water, clothes, food come help those in need #HurricaneSandy #donations #si",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Dylan_Jones",
	"body": " #fema battery #tunnel still closed #thoasands w/o #power #finances are #decimated. Where is the #aid to #sandy #victims",
	"timestamp": "26 Nov 2012"
}, {
	"handle": "Mateo_Miller",
	"body": " Thanks to lack of financial relief , hurricane sandy has forced me to cash in savings bonds to pay utilities. SAD! Thanks Fema",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Jacob_Davis",
	"body": " To make a donation to victims of Hurricane Sandy please do so here... http://t.co/INZa6SYE",
	"timestamp": "27 Nov 2012"
}, {
	"handle": "Chloe_Garcia",
	"body": " I have no power but nothing is stopping me from watching #GiulianaandBill !! @GiulianaRancic @BillRancic #idols #Sandy",
	"timestamp": "26 Oct 2012"
}, {
	"handle": "Grace_Rodriguez",
	"body": " Power went out again an hour ago. Drive around, see no lights on anywhere. #sandy #statenisland",
	"timestamp": "28 Nov 2012"
}, {
	"handle": "Layla_Wilson",
	"body": " @CNN No Red Cross helping #StatenIsland. Residents on #NBC stating bodies being pulled out of water. No one is helping. #Sandy",
	"timestamp": "29 Oct 2012"
}, {
	"handle": "Jonathan_Martinez",
	"body": " There are no first responders in the devastated areas of #StatenIsland. Get some help to this people, NOW. Not Later, NOW! #Sandy",
	"timestamp": "3 Nov 2012"
}, {
	"handle": "Kevin_Anderson",
	"body": " Help #Sandy survivors. Donate to the @RedCross via @iTunesMusic at http://t.co/N1gjnqA1 . Out of US, visit http://t.co/y8Xls89K",
	"timestamp": "26 Oct 2012"
}, {
	"handle": "Savannah_Taylor",
	"body": " \"Im at Frankenstorm Apocalypse - Hurricane Sandy (New York, NY) w/ 3673 others http://t.co/aiXVqT5d\\n\", \"Im at Frankenstorm Apocalypse - Hurricane Sandy (Matawan, NJ) w/ 7 others http://t.co/yBGfpT09, @MarieAmes @CarolineManzo @Theorossi plz RT *NYC Board of Election Post Hurricane Sandy Polling Place Changes* | http://t.co/22jk8PDk",
	"timestamp": "13 Nov 2012"
}, {
	"handle": "Zachary_Thomas",
	"body": " \"@Theorossi Plz RT Cant decide where to donate? 100% of donations to the Bini Fund will go to #HelpSI #Sandy victims.|http://t.co/VwyICw1g, @HeyNowJO Can YOU help expedite? 11 days post #Sandy #GreatKills victims still w/o power&heat due to scuttled yachts. |http://t.co/Fd3BWZ0K",
	"timestamp": "29 Oct 2012"
}, {
	"handle": "Samuel_Hernandez",
	"body": " Midnight reading by flashlight #hurricanesandy #johngiles @secondcaptains http://t.co/UifiLy2t",
	"timestamp": "11 Nov 2012"
}, {
	"handle": "Connor_Moore",
	"body": " A boat next to Hylan Blvd #HurricaneSandy http://t.co/zF0OEHPx",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Adam_Martin",
	"body": " One of saddest Sandy stories &gt; Search for two Staten Island boys swept away from mom during Hurricane Sandy to resume http://t.co/rJVL7Ivp",
	"timestamp": "8 Nov 2012"
}, {
	"handle": "Emma_Jackson",
	"body": " \"Wow it sure is packed here at BRC! Lots of members and non-members using the club for a hot shower and electricity! #sandy, Still no power. Extremely limited cell signal. #sandy sucks",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Lincoln_Thompson",
	"body": " @paleomagazine Can you do a series of articles on storing food for EmPreparedness? Current prod.s arent Paleo friendly. #UhOh #Sandy, There are unclaimed dogs and cats at Wagner HS on #statenisland-- please spread the word so we can reunite #pets with their families! #sandy",
	"timestamp": "13 Nov 2012"
}, {
	"handle": "Lillian_White",
	"body": " Cut and sold wood all day! Still no power! #HurricaneSandy http://t.co/soChfATV",
	"timestamp": "26 Oct 2012"
}, {
	"handle": "Sofia_Lopez",
	"body": " \"come support vin sunday donate to hurricane sandy for the staten islanders affected please 4pm kilmeyers!!!... http://t.co/T9KnNZZD\\n\", How to donate to Hurricane #Sandy relief through iTunes http://t.co/JISQzjz2\\n",
	"timestamp": "24 Nov 2012"
}, {
	"handle": "Olivia_Lee",
	"body": " Cute and Cuddly Critters: Need to Be Adopted After Being Displaced By Hurricane Sandy http://t.co/rpNRnElt\\n",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Jack_Gonzalez",
	"body": " Basement flooded all the way to first floor #hurricane #sandy #helpstatenisland http://t.co/buFwnJh2\\n",
	"timestamp": "11 Nov 2012"
}, {
	"handle": "Hailey_Harris",
	"body": " Water pushed the front door open and moved and threw around all the furniture #hurricane #sandy #helpstateni http://t.co/q2KQMjjk\\n",
	"timestamp": "29 Oct 2012"
}, {
	"handle": "Bella_Clark",
	"body": " Water destroyed everything threw everything out of te cabinets #hurricane #sandy #helpstatenisland http://t.co/mOHc7T1e\\n",
	"timestamp": "9 Nov 2012"
}, {
	"handle": "Isaac_Lewis",
	"body": " \"#hurricanesandy #statenisland its really bad here News nt showing1/2 of whats going on We need help people still stranded donations needed\\n\", Im over here looking like a refugees refugee. No type of clean water or power.5 DAYS NOW!!! ran outta bottled water. #sandy #HUNGRY #Njstorm\\n",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Kayden_Robinson",
	"body": " @nycarecs: Portion of Staten Island that had electricity just lost electricity. 12:30pm #sandy #nyc #statenisland o no. Plz lights stay on\\n",
	"timestamp": "25 Nov 2012"
}, {
	"handle": "Aiden_Walker",
	"body": " @NYPDnews; there is a tree in front of 35 Raymond Pl in S.I. #sandy made it lean and soon will fall. please help. http://t.co/xTspKUn7\\n",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Kennedy_Perez",
	"body": " \"Looks like its gonna take FEMA awhile to get things going around here. Its up to us. Donate whatever you can. We did. You can too. #sandy\\n\", Cant really take more of this no one train if it doesnt come back soon i gunna go nuts 4 train is terrible #sandy\\n",
	"timestamp": "21 Nov 2012"
}, {
	"handle": "Ellie_Hall",
	"body": " Let there be current! Hurricane sandy messed up everything!\\n",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Cooper_Young",
	"body": " Warming Charlie the #snake in the #car . #nopower #nolights #hurricanesandy #hurricane #storm #2012 #njprobl http://t.co/5BEGoF5F\\n",
	"timestamp": "9 Nov 2012"
}, {
	"handle": "Levi_Allen",
	"body": " Currently in the #car charging my #phone while #drinking #vodka :) #fuckyousandy #hurricanesandy #hurricane http://t.co/GHw45Fd0\\n",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Xavier_Sanchez",
	"body": " At #Walmart buying the necessities #nopower #nolights #boardgames #life #soup #hurricanesandy #hurricane #st http://t.co/sVaR4MuS\\n",
	"timestamp": "18 Nov 2012"
}, {
	"handle": "Elijah_Wright",
	"body": " Smell of # gas #outside the #house . #firemen #cops . #aftermath #hurricanesandy #hurricane #storm #scary #n http://t.co/aWeQfIej\\n",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Sophia_King",
	"body": " #boats on the #street at our #waterfront :( everything is gone. My area got nuked by #hurricanesandy . #stor http://t.co/Y1XHGZrO\\n",
	"timestamp": "6 Nov 2012"
}, {
	"handle": "Ezra_Scott",
	"body": " Please help NYC schools get the supplies they need. Drop offs in SI & BK: http://t.co/uVUYzQSt #Sandy\\n",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Roman_Green",
	"body": " Going to donate blood with @kaay_graz later, Staten Island needs a lot of help after Hurricane #Sandy ...\\n",
	"timestamp": "7 Nov 2012"
}, {
	"handle": "Penelope_Baker",
	"body": " Residential Claim for Food and Medicine Spoilage for ConEd customers: http://t.co/kA7SwrOz #Sandy\\n",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Madison_Adams",
	"body": " My cousin and aunt got torn up breaking through windows #sandy #dam @ George L. Egbert Intermediate School 2 http://t.co/THk3vNST\\n",
	"timestamp": "15 Nov 2012"
}, {
	"handle": "Sebastian_Nelson",
	"body": " ship in the middle of the road #sandy @ Staten Island http://t.co/niLl2n3l\\n",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Gabriella_Hill",
	"body": " @pispdjs 110% of proceeds will go to the victims of hurricane sandy. Restore, retweet! http://t.co/Oq51PWfY #helpsi #donate #hurricanesandy\\n",
	"timestamp": "28 Nov 2012"
}, {
	"handle": "Jason_Ramirez",
	"body": " @CBSNewsFan donate here for victims of hurricane sandy started by #STJ alumni #HelpStatenIsland #donate #SandyRelief RT http://t.co/7GeJDvgR\\n",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Riley_Campbell",
	"body": " \"Its been 3 weeks since #hurricanesandy and there is still alot to be done ..donate here http://t.co/Oq51PWfY via @GiveForward\\n\", \"@stjohnsalumni please spread this #hurricanesandy charity started by St. Johns alumni via @GiveForward http://t.co/Oq51PWfY #donate #help\\n\", http://t.co/Oq51PWfY donate here to the victims of hurricane sandy #StatenStrong #donate #HelpStatenIsland - thankful to be alive\\n",
	"timestamp": "6 Nov 2012"
}, {
	"handle": "Claire_Mitchell",
	"body": " \"Chillin by the candle light. Thanks Sandy. #hurricanesandy @ Casa de Kel Kel http://t.co/CVzOl3rk\\n\", @clubindustry @PrecorInc Continued support 4 all affected by #Sandy in the 5 Borough, LI, NJ areas. Many families still without power.\\n",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Mason_Roberts",
	"body": " Flooding On Arthur Rd. Staten Island - Hurricane Sandy this is right in my neighborhood down the block http://t.co/iCnXZB42\\n",
	"timestamp": "5 Nov 2012"
}, {
	"handle": "Colton_Carter",
	"body": " 700 Ton Tanker John B Caddell runs aground in Staten Island by Hurricane Sandy this is nuts http://t.co/sI1Y7oJN\\n",
	"timestamp": "29 Oct 2012"
}, {
	"handle": "Victoria_Phillips",
	"body": " Seems like all of Staten Island has lost power completely now! #Sandy\\n",
	"timestamp": "13 Nov 2012"
}, {
	"handle": "Evan_Evans",
	"body": " \"Its been a very challenging couple of weeks for #Americans that were affected by #Sandy #SandyNJ remember to donate what you can @gogreenhc, On #Thanksgiving Day @gogreenhc will be our 7th month Anniversary. Please donate to the #victims of #Sandy #SandyNJ Give to @salvationarmy\\n",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Easton_Turner",
	"body": " Water is already all the way under the boardwalk, bet it will be in the street by tonight or tomrw. This is crazy.. #water #hurricanesandy",
	"timestamp": "13 Nov 2012"
}, {
	"handle": "Genesis_Torres",
	"body": " Ive never seen darkness like this. #sandy, @NYGovCuomo how about getting on con Edison? 15 days of no power in my development on Staten Island! #sandy\\n",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Ryan_Parker",
	"body": " @DNDailyPolitics what if you don\u2019t need repairs to your home? I had licensed electrician give an ok. Still no power from Con Ed! #Sandy\\n",
	"timestamp": "25 Nov 2012"
}, {
	"handle": "Elizabeth_Collins",
	"body": " is there any more gas available on the island? #sandy #siopen\\n",
	"timestamp": "24 Oct 2012"
}, {
	"handle": "Kaylee_Edwards",
	"body": " I GOT CHILLS, THEYRE MULTIPLYIN!! #hurricanesandy @ Wagner College http://t.co/6uN5rfRr\\n\", \"Its so warm in my car... since no heat, no home #Sandy #StatenIsland http://t.co/wQm3th6C\\n\", @CoryBooker Help my kids in the S. Ward after Hurricane Sandy with this @DonorsChoose project, anything helps! http://t.co/P4XgJA5t",
	"timestamp": "8 Nov 2012"
}, {
	"handle": "Benjamin_Stewart",
	"body": " @neilhimself Please RT and help my Newark kids after Hurricane Sandy with this @DonorsChoose project, anything helps! http://t.co/P4XgJA5t",
	"timestamp": "29 Oct 2012"
}, {
	"handle": "Skylar_Flores",
	"body": " We are far from out of the woods. Please keep donating to homeless families due to #Sandy http://t.co/gPUhUmBr",
	"timestamp": "25 Nov 2012"
}, {
	"handle": "Jaxon_Morris",
	"body": " Please donate to help homeless families due to #Sandy http://t.co/gPUhUmBr funds will go to #StatenIsland families #StatenIslandStrong",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Avery_Nguyen",
	"body": " \"Christmas is a time of giving. We havent raised enough to reach our goal. Please help by donating $$ to buy new toys for victims of #Sandy\\n\", Help Staten Island Pets: Donate Pet supplies on Saturday Nov 3rd at 5 PM @ Kmart Plaza (Hylan/New Dorp Lane) #Sandy #HelpSIPets",
	"timestamp": "23 Nov 2012"
}, {
	"handle": "Hunter_Murphy",
	"body": " Collecting pet supplies for pets affected by #Sandy on Staten Island. Follow @HelpSIPets and RT to help!",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "John_Rivera",
	"body": " The only thing still keeping me going while I have no power. @taylorswift13 &lt;3&lt;3&lt;3 #HurricaneSandy http://t.co/AaVlqvNJ",
	"timestamp": "17 Nov 2012"
}, {
	"handle": "Logan_Cook",
	"body": " Preparing to evacuate! #zoneA #hurricanesandy #thissucks",
	"timestamp": "26 Oct 2012"
}, {
	"handle": "Caleb_Rogers",
	"body": " We goin down (@ Frankenstorm Apocalypse - Hurricane Sandy w/ 37 others) http://t.co/juM1cnkM",
	"timestamp": "8 Nov 2012"
}, {
	"handle": "Michael_Morgan",
	"body": " @IAMNikkiMonique Im tweeting in the middle of Hurricane Sandy and I have no power. cheer up beautiful. we got rocked by this bitch, And so it begins no more jersey shore everyones evacuating and powers dying out.Its like the beginning of a horror movie #hurricanesandy",
	"timestamp": "24 Oct 2012"
}, {
	"handle": "ashley_jonas",
	"body": "Id like to thank hurricane Sandy for giving me the opportunity to sit in the dark over the next few days, How do the Amish do this whole no power thing? Its only been 15 hours, and were going crazy. #NoPower #Sandy, Power has been out for about 24 hours yet I still turn the lights on when I go into a room. #habit #nolights #nycissleeping #HurricaneSandy",
	"timestamp": "13 Oct 2012"
}, {
	"handle": "Aubrey_Peterson",
	"body": " Photo: sittin by the fire waiting for some electricity",
	"timestamp": "13 Nov 2012"
}, {
	"handle": "Aria_Cooper",
	"body": " Please donate all you can! Shelters in #StatenIsland are looking for items. Get through this together. #StayStrong #HurricaneSandy #NYC",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Maya_Reed",
	"body": " The amount of water on my block ..... #hurricanesandy http://t.co/VsLQctn0",
	"timestamp": "12 Nov 2012"
}, {
	"handle": "Caroline_Bailey",
	"body": " @CarolineManzo Wagner HS has 44 infants living there. Desperate need of baby supplies. Please RT #Sandy #StatenIslandStrong",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Zoe_Bell",
	"body": " \"@caroljanedabest Wagner HS has 44 infants living there. Theyre desperate for baby supplies. Please RT #Sandy #StatenIslandStrong, help toys r us donate to victims of hurricane sandy #JGF http://t.co/tWjSRxkz",
	"timestamp": "23 Nov 2012"
}, {
	"handle": "Jordan_Gomez",
	"body": " Thank you all for participating in the hurricane sandy drive.... joeygiggles is still collecting care packages... http://t.co/Yv28QsKM",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Parker_Kelly",
	"body": " Starting in december will be a toy drive for the kids of hurricane sandy #JGf pls join in thanks #JGF jump on board\\n",
	"timestamp": "22 Nov 2012"
}, {
	"handle": "James_Howard",
	"body": " Click here to support Hurricane Sandy Relief Funding by Daphany Sanchez http://t.co/lXeI4qQx\\n",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Christian_Ward",
	"body": " Better security needed in Staten Island neighborhoods ravaged by Hurricane Sandy | http://t.co/kvoh6yeo http://t.co/nDGAOaVu\\n",
	"timestamp": "1 Nov 2012"
}, {
	"handle": "Alexa_Cox",
	"body": " Donate to help Staten Island rebuild after Hurricane Sandy | http://t.co/kvoh6yeo http://t.co/7bwqKfOo\\n",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Nathan_Diaz",
	"body": " Search for two Staten Island boys swept away from mom during Hurricane Sandy to resume Thursday | http://t.co/0qj40iVn http://t.co/ReK5vJ2u\\n",
	"timestamp": "5 Nov 2012"
}, {
	"handle": "Landon_Richardson",
	"body": " @ConEdison need someone to come check the transformer on Heberton Ave/Ann St. damaged during #Sandy no power for 4 days #StatenIsland\\n",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Ariana_Wood",
	"body": " \"A tree on my uncles block #Sandy http://t.co/lwTiOCqF\\n\", Searching SI for any type of boxes to pack clothes in, if you have any bring them to Mount Loretta #hurricanesandy #helpsi\\n",
	"timestamp": "11 Nov 2012"
}, {
	"handle": "Lily_Watson",
	"body": " Please donate! https://t.co/BGq9UteG #nyc #statenisland #hurricane #sandy #h http://t.co/MRttiTay\\n",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Theodore_Brooks",
	"body": " Come to 780 Olympia blvd and volunteer! #statenisland #hurricane #sandy http://t.co/pfrMzCHx\\n",
	"timestamp": "12 Nov 2012"
}, {
	"handle": "Julian_Bennett",
	"body": " Donate to Books of Hope for Hurricane Sandy Victims GIVE HOPE to those affected by Hurricane Sandy through books... http://t.co/RhTfAYdS\\n",
	"timestamp": "29 Oct 2012"
}, {
	"handle": "Serenity_Gray",
	"body": " GIVE HOPE to those affected by Hurricane Sandy through books of hope and comfort for children and adults. SHARE... http://t.co/wIs2bURZ\\n",
	"timestamp": "11 Nov 2012"
}, {
	"handle": "Andrew_James",
	"body": " @FoodBank4NYC New Dorp High Culinary arts is giving out food to the victims of hurricane sandy They were wondering if you can donate food\\n",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Audrey_Reyes",
	"body": " @konaworld Unit vs. big tree down! Thanks Hurricane Sandy for messing up my trails! http://t.co/ZYEIo0Tx\\n",
	"timestamp": "23 Nov 2012"
}, {
	"handle": "Ian_Cruz",
	"body": " Living all Amish style with my candles. Now I know how Kevin Holshner feels #seafam #hurricanesandy #hurricane #hurricaneprobs\\n",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Leo_Hughes",
	"body": " \"@MichaelDelZotto can i get a reply/retweet? Rangers fan in SI and havent had power since Monday. #Sandy #LoveMikeyD\\n\", Please read & donate #mets #sandy http://t.co/iFStqDXk\\n",
	"timestamp": "22 Nov 2012"
}, {
	"handle": "Joseph_Price",
	"body": " A great way to help the great people of #StatenIsland! Donate to help Staten Island rebuild after Hurricane #Sandy http://t.co/sokSE9dZ\\n",
	"timestamp": "29 Oct 2012"
}, {
	"handle": "Lucy_Myers",
	"body": " @louislegacy MT PLEASE HELP New York dog on death row following death of owner in Hurricane Sandy http://t.co/NUuHyFWY via @examinercom\\n",
	"timestamp": "4 Nov 2012"
}, {
	"handle": "Anna_Long",
	"body": " @ExcuseMeWWE RT for Staten Island ! #Sandy did so much damage here, we need all the help we can get! Text redcross to 90999 !\\n",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Oliver_Foster",
	"body": " \"The elections over--lets get back to being better people. Start by donating to the #Sandy relief efforts: http://t.co/11ryTac9\\n\", @joannakrupa will u be donating food for animals for #sandy\\n",
	"timestamp": "3 Nov 2012"
}, {
	"handle": "Charles_Sanders",
	"body": " Will need to determine whether the trees near my parking spot will fall during Hurricane Sandy. #hurricanesandy\\n",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Jackson_Ross",
	"body": " @DennisDMZ If anyone wants to donate to Staten Islann #Sandy victims go to http://t.co/mnMFcPsg. No $ will be wasted. Can I get a RT please\\n",
	"timestamp": "25 Nov 2012"
}, {
	"handle": "Gavin_Morales",
	"body": " @JerrySeinfeld If anyone wants to donate directly to Staten Island #Sandy victims go to http://t.co/mnMFcPsg . No $ will be wasted.RT please\\n",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Leonardo_Powell",
	"body": " @sutterink If anyone wants to donate directly to Staten Island #Sandy victims go to http://t.co/mnMFcPsg. No $ will go to waste. RT please.\\n",
	"timestamp": "4 Nov 2012"
}, {
	"handle": "Ella_Sullivan",
	"body": " 23 and a half hours Fuck you #sandy #nopower\\n",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Peyton_Russell",
	"body": " 37 hours and counting Fuck you #sandy #nopower #coned where you be!!\\n",
	"timestamp": "10 Nov 2012"
}, {
	"handle": "Austin_Ortiz",
	"body": " \"No power for 3 days +boredom means Ive gained at least 5(+)lbs #hurricanesandy #fatass\\n\", For those of us who were effected by Hurricane Sandy are trying our hardest to help our community. Please donate! Xo http://t.co/VzdV5gDg\\n",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Harper_Jenkins",
	"body": " St. Charles is open for donations of clothes, games, anything that could be of use for victims of Hurricane Sandy tomorrow from 9am to 7pm!\\n",
	"timestamp": "3 Nov 2012"
}, {
	"handle": "Adrian_Gutierrez",
	"body": " \"We need #help #hurricane #Sandy Im collecting #donations for friends & Fam that lost their homes & belongings. https://t.co/spOZGAXU\\n\", Drop off site Olympia blvd and Sand Lane needs Similac formula, size 3, 4 & 5 diapers - Staten Island #Sandy\\n",
	"timestamp": "26 Oct 2012"
}, {
	"handle": "Nora_Perry",
	"body": " Please donate blood its needed #Sandy @Moes_HQ\\n",
	"timestamp": "23 Nov 2012"
}, {
	"handle": "Natalie_Butler",
	"body": " I lost my house in #Sandy but @HSBCUSA will not give me a month extension to pay the credit card bill w/o hitting my credit report Thanks!\\n",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Paisley_Barnes",
	"body": " Update for Thursday, November 1st - Due to the after math of Hurricane Sandy we are still without power and no... http://t.co/ky2lPlef\\n",
	"timestamp": "28 Nov 2012"
}, {
	"handle": "Allison_Fisher",
	"body": " Ship wrecked boat down the street from my house. And they wanted me to report to Rubber Room today? #Sandy http://t.co/oF6DHgYD\\n",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Aaron_Henderson",
	"body": " \"Survived #HurricaneSandy still dont have power though.\\n\", Make sure every1 donates a toy to #ToysForTots they will be distributed to the #sandy victims as well as less fortunate children\\n",
	"timestamp": "24 Nov 2012"
}, {
	"handle": "Piper_Coleman",
	"body": " Donate to Tunnel to Towers to specify where you want #sandy relief donations to go.... http://t.co/zSXub1zW Staten Island #helpsi\\n",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Jayden_Simmons",
	"body": " Donate to Tunnel to Towers to specify where you want #sandy relief donations to go.... http://t.co/zSXub1zW Staten Island #helpsi\\n",
	"timestamp": "13 Nov 2012"
}, {
	"handle": "Thomas_Patterson",
	"body": " #usguys please help me coordinate Staten Island #sandy Recovery efforts here http://t.co/c41YVUSk #helpsi\\n",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Nathaniel_Jordan",
	"body": " #smalltown2012 I am one of you please help me help with #Sandy recovery on Staten Island please RT alerts with hashtag #helpsi Thanks!\\n",
	"timestamp": "22 Nov 2012"
}, {
	"handle": "Elias_Reynolds",
	"body": " \"@andreacook @ipgossip @timwasher @jeffpulver Power on & off on Staten Island 1000s without homes we need a lot of help #helpsi #sandy\\n\", \"Grimm seeks housing for Staten Islands Hurricane Sandy victims | http://t.co/ay7gXeF3 http://t.co/J2U2y766\\n\", Feeling like the only person left who still doesnt have electricity since hurricane sandy -.-\\n",
	"timestamp": "26 Oct 2012"
}, {
	"handle": "Sadie_Hamilton",
	"body": " @NoelElizabethx3 ok good thats better :) mine shut down and its pitch black lol but we just lit a few candels #StaySafe #HurricaneSandy\\n",
	"timestamp": "6 Nov 2012"
}, {
	"handle": "Leah_Graham",
	"body": " Going Home Thinking Powers on : NOPE #FML #HurricaneSandy #Stupid\\n",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Josiah_Kim",
	"body": " Several members of family have to evacuate...we are 1/2 block from evac zone & 1/2 mi from coast...#notcool #HurricaneSandy #fingerscrossed\\n",
	"timestamp": "12 Nov 2012"
}, {
	"handle": "Ava_Gonzales",
	"body": " @SINYCliving: Volunteers are needed at Monsignor Farrell tomorrow morning at 8am to sort donations #statenisland #sandy\\n",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Mia_Alexander",
	"body": " #statenisland Monsignor Farrell needs volunteers this morning to sort donations! #sandy\\n",
	"timestamp": "28 Nov 2012"
}, {
	"handle": "Brayden_Ramos",
	"body": " 18,000+ without power on Staten Island, as Hurricane Sandy nears http://t.co/GmPZafIC\\n",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Jace_Wallace",
	"body": " Port reading ave is already flooded as usual. #HurricaneSandy http://t.co/irMpXoUO\\n",
	"timestamp": "26 Nov 2012"
}, {
	"handle": "Noah_Griffin",
	"body": " Should be evacuated by now but no thanks :) #fucksandy #gotmyfloaties #hurricanesandy",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Charlotte_West",
	"body": " My updated wish list...a generator!!! #HurricaneSandy\\n",
	"timestamp": "17 Nov 2012"
}, {
	"handle": "Brandon_Cole",
	"body": " Ok papa johns I see u.. #donate #papajohns #hurricanesandy #sandy http://t.co/SGAUWlZ1",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Madelyn_Hayes",
	"body": " Please help Tara raise much needed money for the victims of Hurricane Sandy by attending her Thursday Morning... http://t.co/s8ufosOZ\\n",
	"timestamp": "24 Nov 2012"
}, {
	"handle": "Tyler_Chavez",
	"body": " Im not evacuating my mandatory evacuation for #hurricanesandy #sandy and im in Zone A :P\\n",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Aaliyah_Gibson",
	"body": " No power for 40 hours now in Tottenville, Staten Island, NY. God Bless everyone during this disaster. #Sandy\\n",
	"timestamp": "1 Nov 2012"
}, {
	"handle": "Owen_Bryant",
	"body": " @ConEdison Still w/out power in South shore of Staten Island (tottenville, p bay, p plains etc.). Any updates on service? #Sandy\\n",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Nolan_Ellis",
	"body": " Power line went down huge explosion and all these people aint doing shit but stand there #Sandy http://t.co/Wizyowwy, Asbury Park firehouse needs blankets for seniors who lost power during the transformer fire at the senior ctr today. #sandy",
	"timestamp": "18 Nov 2012"
}, {
	"handle": "Gabriel_Stevens",
	"body": " Im raising money for Hurricane Sandy Relief for Staten Island Families. Click to Donate: http://t.co/eWU72r12 #gofundme, @TheRealXtina Please ask your followers 2 donate 2 red cross for #Sandy victims which affected your hometown staten island : )",
	"timestamp": "26 Oct 2012"
}, {
	"handle": "Stella_Murray",
	"body": " \"@XChadballX hurricane sandy hit me bad. Ive had no Internet or anything at all. Still no power... Is there any shirts left over at all?\\n\", Tree fell around the corner. #hurricanesandy #statenisland http://t.co/FcQSqPT6",
	"timestamp": "15 Nov 2012"
}, {
	"handle": "Hudson_Ford",
	"body": " This #CharityTuesday, give to those affected by Hurricane Sandy in New Jersey - http://t.co/0qGEWL3J #sandyhelp #sandynj #donate #nonprofit\\n",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Alexander_Marshall",
	"body": " Join us in Readington Township next Saturday! Well be collecting donations for Hurricane Sandy relief in New Jersey. http://t.co/AcyMy3BH\\n\", Still no word from my boyfriend .. #Worried #Sandy",
	"timestamp": "16 Nov 2012"
}, {
	"handle": "Sawyer_Owens",
	"body": " Help us provide aid to survivors of sandy on Staten Island. Donate now! http://t.co/oq50wgde #Sandy #SandyHelp #SandyFund",
	"timestamp": "24 Oct 2012"
}, {
	"handle": "Blake_Mcdonald",
	"body": " Volunteer with the Hurricane Sandy relief effort with NYC Public Advocate @BilldeBlasio. Join him! http://t.co/yl4mJ42j via @BilldeBlasio",
	"timestamp": "25 Nov 2012"
}, {
	"handle": "Luke_Harrison",
	"body": " People on line waiting for gas!!!!!! Woah #wtf damn #sandy http://t.co/MLAA4jaT",
	"timestamp": "22 Oct 2012"
}, {
	"handle": "Carson_Ruiz",
	"body": " The water is rising.... #hurricanesandy #statenisland @ Staten Island, NY http://t.co/a0K5uGXM",
	"timestamp": "21 Nov 2012"
}, {
	"handle": "Jaxson_Kennedy",
	"body": " \"No power, no heat. Its getting cold. #Sandy\\n\", Second day of waking up to total darkness + total silence. #Sandy\\n",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Ayden_Wells",
	"body": " SILive community, if you know of any open business, tweet us using #SIopen. People are looking for places to buy food, gas, etc. #sandy",
	"timestamp": "21 Nov 2012"
}, {
	"handle": "Eli_Alvarez",
	"body": " Want to volunteer in aftermath of Hurricane Sandy NYC Click Here: http://t.co/Lonc1CEi http://t.co/1Nt4A8dm",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Isabella_Woods",
	"body": " Volunteers are needed at Monsignor Farrell tomorrow morning at 8am to sort donations #statenisland #sandy",
	"timestamp": "21 Nov 2012"
}, {
	"handle": "Camden_Mendoza",
	"body": " Lost Yorkie Puppy Roxie Last seen at Lincoln Ave & N. Railroad 347 417 0362 #sandy #helpsi",
	"timestamp": "23 Oct 2012"
}, {
	"handle": "Daniel_Castillo",
	"body": " Need SMALL First aid kits? Need leads on where a few (dozen) (hundred) can be purchased (donated)? Staten Island #sandy #helpsi",
	"timestamp": "21 Nov 2012"
}, {
	"handle": "Cameron_Olson",
	"body": " Any groups or restaurants that can provide hot soup today Staten Island #Sandy please email nysassembly60@gmail.com #helpsi",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Autumn_Webb",
	"body": " Staten island Recovery No more clothing we need new underwear mens womens children 4 #sandy evacuees drop at any shelter #helpsi",
	"timestamp": "15 Nov 2012"
}, {
	"handle": "Henry_Washington",
	"body": " Miller Field Staten Island needs Hot food or sandwiches NOW #helpsi #sandy",
	"timestamp": "24 Oct 2012"
}, {
	"handle": "William_Tucker",
	"body": " Staten island Recovery No more clothing we need new underwear mens womens children 4 #sandy evacuees drop at any shelter #helpsi",
	"timestamp": "10 Nov 2012"
}, {
	"handle": "Lucas_Freeman",
	"body": " #Sandy Recovery Brooklyn Gerritsen Beach Fire Department needs low Carb Hot Food Donations http://t.co/UNV6Btc1",
	"timestamp": "29 Oct 2012"
}, {
	"handle": "Hazel_Burns",
	"body": " \"Canned goods, dry pasta, meats fish needed 4 Brooklyn #Sandy Relief ASAP deliver 2 St Marys Church on 81st & ridge #helpsi CC: @robicellis, Staten Island #sandy pet relief email newyork@louieslegacy.org to request pet food delivery #helpsi http://t.co/IDYZsmgM",
	"timestamp": "2 Nov 2012"
}, {
	"handle": "Addison_Henry",
	"body": " Staten island Recovery No more clothing we need new underwear mens womens children 4 #sandy evacuees drop at any shelter #helpsi\\n",
	"timestamp": "24 Oct 2012"
}, {
	"handle": "Christopher_Snyder",
	"body": " @louieslegacy needs donations of Cat food to feed our feline friends who have been displaced from #sandy\\n",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Ryder_Simpson",
	"body": " LOOKING FOR VOLUNTEERS & SUPPLIES FOR ALL T2T RELIEF CENTERS #Sandy #helpsi Please feel free to contact any... http://t.co/UUXZ6YeW\\n",
	"timestamp": "15 Nov 2012"
}, {
	"handle": "Nevaeh_Crawford",
	"body": " Help needed in Gerritsen Beach #sandy DAY 15: What we need. VOLUNTEER MANPOWER (Demolition and Construction)... http://t.co/yNoCT1wR\\n",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Camila_Jimenez",
	"body": " ATTN: Caterers, Restaurants, community orgs, religious orgs., Please alert us of any Thanksgiving dinners for #Sandy on Staten Island",
	"timestamp": "11 Nov 2012"
}, {
	"handle": "Violet_Porter",
	"body": " MT @ThrRoyalHer Hot meals needed Today 192 Ebbits St. Staten Island 300 for lunch 500 for dinner #sandy #helpsi",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Joshua_Shaw",
	"body": " ATTN: Caterers, Restaurants, community orgs, religious orgs., Please alert us of any Thanksgiving dinners for #Sandy on Staten Island\\n",
	"timestamp": "29 Oct 2012"
}, {
	"handle": "David_Gordon",
	"body": " @TomMcKennaNY we cannot locate any large organized Thanksgiving dinner planned for the folks affected by #sandy on Staten Island.) #HELPSI",
	"timestamp": "28 Nov 2012"
}, {
	"handle": "Carter_Wagner",
	"body": " I am not seeing ANY organized Thanksgiving Dinners planned for Staten Island -ers affected by #sandy #helpsi",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Wyatt_Romero",
	"body": " Please let us know of any organized Thanksgiving Dinners planned for those affected by #Sandy on Staten Island #helpsi\\n",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Robert_Hicks",
	"body": " Please let us know of any organized Thanksgiving Dinners planned for those affected by #Sandy on Staten Island #helpsi\\n",
	"timestamp": "10 Nov 2012"
}, {
	"handle": "Ethan_Palmer",
	"body": " Please let us know of any organized Thanksgiving Dinners planned for those affected by #Sandy on Staten Island #helpsi\\n",
	"timestamp": "24 Oct 2012"
}, {
	"handle": "Brooklyn_Black",
	"body": " Holiday Toy Drive for Staten Island children New Toys or Gift Cards #sandy http://t.co/Z6qhLYT5\\n",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Chase_Holmes",
	"body": " Volunteers for #Sandy Recovery please go to 2361 Hylan Blvd Staten Island to receive an assignment... everyday after 8:30am.\\n",
	"timestamp": "8 Nov 2012"
}, {
	"handle": "Mila_Stone",
	"body": " Please consider donating to Staten Island families in need after #Sandy - http://t.co/2IPuCR6Q\\n",
	"timestamp": "28 Oct 2012"
}, {
	"handle": "Jeremiah_Meyer",
	"body": " Just watch a FDNY engine for second night in row have to make U-turn because of downed trees on the block. They loose precious time #Sandy",
	"timestamp": "8 Nov 2012"
}, {
	"handle": "Nicholas_Boyd",
	"body": " @Xistnt i have had no power, no Internet or phone service. My Dad has lost power too. Hope to get video soon #Sandy",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Tristan_Mills",
	"body": " Moms actin up, its ight though. Hurricane sandy gonna get that bitch if she thinks shes leavin this house.",
	"timestamp": "7 Nov 2012"
}, {
	"handle": "Emily_Warren",
	"body": " \"I see the blackout on Staten Island from where Im at hurricane sandy is not playin wtf is going on rt, Extreme tree damage #statenisland #randallmanor HartBlvd #sandy @NY1headlines @patkiernan http://t.co/YR6fEqfu",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Evelyn_Fox",
	"body": " @silivedotcom: if u know of any open biz, tweet #SIopen Gas gas gas! So many stations closed or 2hr lines. Whats the gas story? #sandy, @InterOcc Needed on Staten Island, Tools, Hardware, and Outdoor Living from this Amazon Regitry. http://t.co/kaAsUxmV #StrikeDebt #Sandy",
	"timestamp": "26 Nov 2012"
}, {
	"handle": "Angel_Rose",
	"body": " They just announced our evacuation and this what my family decides to do #survivors #hurricanesandy #hurrica http://t.co/OgWMpt7E",
	"timestamp": "26 Oct 2012"
}, {
	"handle": "Mackenzie_Rice",
	"body": " u201c@SINYCliving: Sea Gate Brooklyn needs Food! Food trucks Hot Food. #sandy #recovery\u201d call #Obama , Im sure hell be there tomorrow, @AskCapitalOne Is there any way to get a credit increase so I can purchase a generator still no power in NJ #SANDY",
	"timestamp": "28 Nov 2012"
}, {
	"handle": "Liam_Moreno",
	"body": " If you can volunteer to demo sheet rock email theroyalher@aol.com with when/group size #siopen #helpstatenisland #helpsi #sandy volunteer",
	"timestamp": "24 Oct 2012"
}, {
	"handle": "Jose_Schmidt",
	"body": " \"Tradesmen, if youll have some time to help with the rebuild email theroyalher@aol.com #siopen #helpstatenisland #helpsi #sandy volunteer, Foster a cat!! SIWC needs foster homes! #sandyvolunteer #rebuildsi #sirecovers #sandy #helpsi #sihelp NYC Animal task force 347-573-1561",
	"timestamp": "11 Nov 2012"
}, {
	"handle": "Abigail_Patel",
	"body": " 80 Animals saved from #sandy are going to be put down unless they get adopted. #sirecovers #sihelp #rebuildsi #sivolunteer #helpsi",
	"timestamp": "27 Oct 2012"
}, {
	"handle": "Asher_Ferguson",
	"body": " After 20 hours, power is back with wifi no cell service here on SI. #sandy #sandyabc7",
	"timestamp": "11 Nov 2012"
}, {
	"handle": "Amelia_Nichols",
	"body": " My only way out... My family and I are trapped",
	"timestamp": "25 Oct 2012"
}, {
	"handle": "Isaiah_Herrera",
	"body": " We found a buddy washed up from the creek!",
	"timestamp": "10 Nov 2012"
}, {
	"handle": "Bentley_Medina",
	"body": " \"@TXBrad Not doing too well, Brad. Hurricane Sandy has basically left a good portion of my house in a shipwreck and Im in a standstill, now. EVERYONE BRING CLOTHES AND DONATIONS DOWN TO FARRELL FOR THE VICTIMS OF HURRICANE SANDY WHO HAVE NOTHING PLEASE RT\\n",
	"timestamp": "29 Oct 2012"
}, {
	"handle": "Zoey_Ryan",
	"body": " @elvisduran Pls mentn Seabreeze Fishery 3095 Rte 35 Hazlet, NJ Hurricane Sandy victims car wash fundraiser 11/10-11, 10-4 all $ go 2 victims",
	"timestamp": "3 Nov 2012"
}, {
	"handle": "Scarlett_Fernandez",
	"body": " It would really mean a lot to me if you guys donated a lil cash to help a family in need after Hurricane Sandy http://t.co/3WYCGdgR",
	"timestamp": "29 Oct 2012"
}]
foodWater = ["food","storing","medicine", "canned", "sandwiches",
      "soup", "hot food", "cat", "dog", "water", "dinner", "meals needed",
      "thanksgiving", "Thanksgiving"]
power = ["#nopower", "power", "electricity", "lights",
      "blackout", "current", "flash", "batteries", "lantern",
      "flashlight", "candle", "dark"]
donations = ["#donations", "donations", "financial", "relief",
      "cash", "savings", "http", "donate", "fund", "supplies", "$",
      "drive", "money", "charity", "aid", "volunteer", "shelter",
      "contact"]
stranded = ["house", "transportation", "first", "responders",
      "red cross", "displaced", "pets", "reunite", "adopted", "flooded",
      "flooding", "basement", "evacuate", "evacuation", "homeless",
      "destroyed", "boats", "trucks", "ruined", "breaking", "no", "home",
      "block"]
clothes = ["underwear", "clothing", "clothes"]
helpWebsites = ["http", "contact", "Contact"]

for yeet in tweets_lst:
	tweet = yeet["body"]
	split = tweet.split(" ")
	category = "undefined"
	print(split)
	for word in split:
		word = word.lower()
		if word in foodWater:
			category = "food/water"
		elif word in power:
			category = "power"
		elif word in donations:
			category = "donations"
		elif word in stranded:
			category = "stranded"
		elif word in clothes:
			category = "clothes"
		elif word in "helpWebsites":
			category = "helpWebsites"
	yeet["category"] = category

for tweet in tweets_lst:
    if "statten island" in tweet["body"].lower() or "staten island" in tweet["body"].lower() or "statenisland" in tweet["body"].lower():
        lat, lng = staten_island[randrange(0, len(staten_island))]
    elif "matawan" in tweet["body"].lower():
        lat, lng = matawan[0]
    elif "miller" in tweet["body"].lower():
        lat, lng = miller[0]
    elif "gerritsen" in tweet["body"].lower():
        lat, lng = gerritsen[0]
    elif "nj" in tweet["body"].lower() or "new jersey" in tweet["body"].lower():
        lat, lng = nj[randrange(0, len(nj))]
    elif "ny" in tweet["body"].lower() or "new york" in tweet["body"].lower():
        lat, lng = ny[randrange(0, len(ny))]
    else:
        lat, lng = rand[randrange(0, len(rand))]
    tweet["position"] = {"lat": lat, "lng": lng}

with open('data.json', 'w') as outfile:
    json.dump(tweets_lst, outfile)
