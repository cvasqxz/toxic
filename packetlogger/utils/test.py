import base64
import binascii
from RC4Base64 import RC4Base64

possible_table = "cfa4debb4f28d4279d0f668aabba13810b8f7f4c7917eb1618296937c852d05a5d5f41ffc65c4d63bdacf22ebea27e913f56016fd6dae11ab749e068d59a99656ca8c91bf5779b4b03eda560fdc2742a2421517afa6242470e87f8c45edfbc59e650826e4a4810b9ca7df31e1db16175723354c564a67820e3b4dd5b3dd7b39f73a30d96053c71c795ae5707b611a04ead268eb5220cf9e7b2ee23f6bf9e76a7e5a1e9587c408583af3a8b7be8d13000fc86452f929738350206b0c398fb8dfe09f7c1e41ff18470d86d672d1c8ccc806bd332f025ef90a9ea08d26a89dbb8cbec4615f4e29c5544aa53c0d9883b433493ce0adc12cd2c1914942b36043e3139"

first_encrypted = "OaVKtwJ6BQni0004ZW4i56T9GNqb8jfdSdnPi97I8PvZOrCNGr74sXsK26ygbS5D0b/VeNvFlyu7oISlJiQUgUQXE7=="

for j in range(256):
    rc4 = RC4Base64(
        binascii.unhexlify(possible_table),
        164,
        j)

    rc4.undo_rc4(12)
    decipher = rc4.decipher(base64.b64decode(first_encrypted))
    if decipher != None:
        print(j, 164, decipher)


'''
Waiting for connection...
Habbo client connected to Toxic
Toxic connected to Habbo server
[INCOMING]: @@[1]
[OUTGOING]: @@BCN
[INCOMING]: DU630114384978504943452153[2][1]
[OUTGOING]: @BKCJBG185892761403833496149520070574745098240264226507480733766118242246241162251458265341091584416299609304540386602494049609660113220805688
[INCOMING]: @A15821372430166921457625661069311258674644334867267317173551190587696146928910594912352435092486932306557168586997829995970600329706848[2][1]
[OUTGOING]: OaVKtwJ6BQni0004ZW4i56T9GNqb8jfdSdnPi97I8PvZOrCNGr74sXsK26ygbS5D0b/VeNvFlyu7oISlJiQUgUQXE7
[OUTGOING]: QzTS7w1SncgkjKjriC5p1onsKcmAf5pK0ONcGTQIfs
[INCOMING]: DARAHHIIKHJHPAIQAdd-MM-yyyy[2][1]
[OUTGOING]: XeH34gkt8myEkUfMJIH08FBkNqVeggfchEqIL1EcwQ
[INCOMING]: @Bfuse_login[2]fuse_buy_credits[2]fuse_trade[2]fuse_create_flat[2]fuse_ignore_room_owner[2][1]@C[1]
[INCOMING]: PdJZC[CJpresent_gen[2]present_gen[2][1]
[INCOMING]: ze2152527534195021701729509[2]M[2][1]
[INCOMING]: @J44992914-7634-481d-9014-1900631ec509-1398.MUS[2][1]@DH[1]
[OUTGOING]: xwxP/gNxc
[OUTGOING]: pbXWjQczglKgukwC5sjI8p5gZb87oGjNQ0/sxo+VpwLbkVOGLCw/Iv731EXdthNiXReOL0
[INCOMING]: @Euser_id=1398[13]name=Hell[13]figure=2152527534195021701729509[13]sex=M[13]customData=waiworinao[13]ph_tickets=24[13]ph_figure=ch=s02/250,56,49[13]photo_film=0[13]directMail=1[13]onlineStatus=1[13]publicProfileEnabled=1[13]friendRequestsEnabled=1[13]offlineMessagingEnabled=1[13]followMeEnabled=1[1]
[OUTGOING]: HslyuA0F5TpGA
[OUTGOING]: 73herA6iT7IPvrsSl4eAjms
[INCOMING]: @F31[2][1]
[INCOMING]: CeHHH[1]HfSAsexual_content[2]PAexplicit_sexual_talk[2]Iauto_reply[2]cybersex[2]Jauto_reply[2]sexual_webcam_images[2]Kauto_reply[2]sex_links[2]PIauto_reply[2]pii_meeting_irl[2]Jmeet_irl[2]RAauto_reply[2]asking_pii[2]PBauto_reply[2]scamming[2]QAscamsites_promoting[2]QBauto_reply[2]selling_buying_accounts_or_furni[2]RBauto_reply[2]stealing_accounts_or_furni[2]SBauto_reply[2]hacking_scamming_tricks[2]PHauto_reply[2]fraud[2]QHauto_reply[2]trolling_bad_behavior[2]PBbullying[2]PCauto_reply[2]habbo_name[2]QCauto_reply[2]inappropiate_room_group_event[2]RHauto_reply[2]swearing[2]RCauto_reply[2]drugs_promotion[2]SCauto_reply[2]gambling[2]PDauto_reply[2]staff_impersonation[2]QDauto_reply[2]minors_access[2]RDauto_reply[2]violent_behavior[2]Khate_speech[2]SDauto_reply[2]violent_roleplay[2]PEauto_reply[2]self_threatening[2]QEwarn[2]game_interruption[2]PAflooding[2]REauto_reply[2]door_blocking[2]SEauto_reply[2]raids[2]QGauto_reply[2]scripting[2]SHauto_reply[2]account_merge[2]Iaccount_merge[2]SIauto_reply[2][1]DtI[1]@Gclub_habbo[2]HHHI[1]@H[515,260,520,265,266,267,525,270,530,275,535,280,281,540,285,545,290,550,295,555,300,305,565,570,575,580,585,590,595,596,600,605,610,100,615,105,620,110,625,626,882,115,627,883,630,120,635,125,640,130,645,135,650,140,655,145,660,150,665,155,667,669,670,160,675,165,680,170,685,175,176,177,178,690,180,695,696,185,700,190,705,195,710,200,715,205,206,207,720,210,725,215,730,220,735,225,740,230,235,240,500,245,505,250,510,255][1]@Bfuse_login[2]fuse_buy_credits[2]fuse_trade[2]fuse_create_flat[2]fuse_ignore_room_owner[2][1]@Lasdf[2]ZIBZIBXSDSLX[127]AVIP[2]IHabbo Hotel[2]HHoffline[2]28-02-2025 18:49:41[2]1251426519275011800229510[2]HZVBSergio[2]IHabbo Hotel[2]HHoffline[2]09-02-2025 23:08:43[2]3000523515801442851418020[2]HYeBAlberto[2]I[2]HHoffline[2]27-02-2025 15:20:41[2]2151230004140021901328015[2]HYDCSr.Tripartito[2]IHabbo Hotel[2]HHoffline[2]19-02-2025 16:27:11[2]2550429510170191800227016[2]HYcC77[2]INo risk, no fun![2]HHoffline[2]-[2]1350519019290092670128015[2]HXnCToni[2]IHabbo Hotel[2]HHoffline[2]24-06-2024 23:07:50[2]1400718002215252850129509[2]HYuCXENTINAL[2]Imercadohabbo.com[2]HHoffline[2]02-12-2024 15:11:01[2]281013050220725[2]H[lDReverso[2]IHabbo Hotel[2]HHoffline[2]18-06-2024 19:47:25[2]1150425506285133000418001[2]HYyDzibo[2]IRank null[2]HHoffline[2]18-02-2025 09:47:15[2]1250524515290011900928501[2]HZbEErKoWo[2]I[2]HHoffline[2]01-03-2025 18:56:32[2]2750119022255041550529509[2]HXiEArtMiner[2]IHabbo Hotel[2]HHoffline[2]16-02-2025 03:14:07[2]2950928101205011650826001[2]HYqFpaco.corl[2]I2006[2]HHoffline[2]20-02-2025 15:37:57[2]8084528511185013050380203[2]HXSHSihin[2]IMade In Chile[2]HHoffline[2]08-07-2024 05:12:11[2]2750183101205122950925518[2]HYWHMrBingo[2]I[2]HHoffline[2]25-12-2024 18:28:55[2]2950918001255048440528502[2]HY[127]Hgym[2]Iestoi aziendo pexo[2]HHoffline[2]28-02-2025 09:46:32[2]8450180816281021951830502[2]HYbISalzeda[2]Ien .COM[2]HHoffline[2]09-01-2025 23:32:27[2]2551729510170172810918513[2]HZqLNasty[2]IHabbo Hotel[2]HHoffline[2]17-02-2025 21:28:44[2]2750129501800462550119001[2]H[MMadrid[2]I[2]HHoffline[2]11-02-2025 16:17:46[2]2810919001215051550129509[2]HX^Omartychisto[2]IHabbo Hotel[2]HHoffline[2]25-01-2025 22:44:56[2]1800183108255042950127516[2]HXjPSagnidnam[2]IHabbo Hotel[2]HHoffline[2]12-09-2024 12:24:15[2]1400230503205022751925504[2]HXPQAldo[2]IHabbo Hotel[2]HHoffline[2]28-08-2024 00:22:43[2]1800121501140022750129501[2]HZUVAngelboy[2]IHabbo Hotel[2]HHoffline[2]18-06-2024 14:18:06[2]2700129001100012600118001[2]H[[VKnd[2]IHabbo Hotel[2]HHoffline[2]29-06-2024 12:53:12[2]1250229510195022810925504[2]HX_WAlvia[2]IHabbo Hotel[2]HHoffline[2]20-06-2024 03:55:27[2]2600127001100011800129001[2]HYhYCanexy[2]IHabbo Hotel[2]HHoffline[2]29-06-2024 20:41:59[2]2150428104160021900129510[2]HYd]Puto[2]IHabbo Hotel[2]HHoffline[2]26-06-2024 07:42:18[2]2150117801195182750630502[2]H[mbPoseid0n[2]I.[2]HHoffline[2]01-03-2025 20:25:26[2]2151615501275341802429510[2]HXKcCaribbeno[2]Iel putamo[2]HHoffline[2]27-06-2024 15:18:07[2]1780127501300011800121503[2]H[Ocpeo[2]Ixlony[2]HHoffline[2]11-10-2024 20:53:50[2]2753425517145043050118022[2]HY[csool[2]H |[2]HHoffline[2]07-02-2025 05:52:03[2]6050366004720018360174001[2]H[HjMiigueMorxe[2]IHabbo Hotel[2]HHoffline[2]03-12-2024 12:34:54[2]1802126001300062851612522[2]HZvkStray[2]IHabbo Hotel[2]HHoffline[2]16-01-2025 20:32:02[2]2950925516185061150427518[2]H[hu000[2]IHabbo Hotel[2]HHoffline[2]28-12-2024 21:18:25[2]2851330501205012550417001[2]Ha~@AMirsha[2]IAPOCALiPSTICK[2]HHoffline[2]02-03-2025 00:00:18[2]1600225006180093050127534[2]H`{NASiete[2]I[2]HHoffline[2]07-02-2025 10:52:29[2]2302128501180033000512501[2]HcNSAel-linense[2]Imacklebee[2]HHoffline[2]24-01-2025 19:36:34[2]2000125504160022850229510[2]H`SmAGenio[2]Iig: @sinmetropolitano[2]HHoffline[2]22-07-2024 03:09:57[2]205142900328515[2]HcUoAIrreconocible[2]Idesconocido[2]HHoffline[2]20-06-2024 19:15:06[2]1000129001180012700126001[2]HayoARealista[2]I[2]HHoffline[2]15-08-2024 14:50:34[2]2750530005130012552219001[2]HbppAe-sabella[2]H[2]HHoffline[2]07-01-2025 23:24:49[2]6001266004700317300551508[2]HcUrALord.William[2]ICoronados de gloria[2]HHoffline[2]01-03-2025 10:53:10[2]2552427501190011701829510[2]HcrAali-oli[2]I[2]HHoffline[2]05-02-2025 21:32:27[2]1400218001255042750129509[2]H`svAitaliano19[2]IHabbo Hotel[2]HHoffline[2]21-06-2024 14:37:05[2]2200320518110012800730001[2]H`P[127]ADOVAHKIIN[2]IDOVA[2]HHoffline[2]02-03-2025 18:30:23[2]1550130501210211800127014[2]HczIBRelassed[2]Itoni[2]HHoffline[2]29-08-2024 22:43:45[2]2900116501180142750621525[2]H`ZKBJesusxD!!![2]I[2]HHoffline[2]02-03-2025 17:09:03[2]8081429009180012851482816[2]H`[127]NBDont.tony[2]Ii dont[2]HHoffline[2]01-12-2024 20:54:29[2]1850527532140013000521519[2]HbQgBMonsoon[2]ITokio Hotel[2]HHoffline[2]01-03-2025 16:55:02[2]8410228501207018044329510[2]Hb@wBVercetty[2]Ihola[2]HHoffline[2]23-01-2025 17:28:06[2]2150517019190012951027015[2]Hc`BCSickVicious[2]I[2]HHoffline[2]18-09-2024 19:57:20[2]2150428501290011350319001[2]HaDHCsipotter[2]ISince 2005[2]HHoffline[2]24-01-2025 14:55:13[2]1000129001185012750621508[2]HHHHHH[1]
[OUTGOING]: Y2NkNQtdqz
[OUTGOING]: RB5K1gLwA
[INCOMING]: CHKHPublic Rooms[2]HRLHPDKAvance de la temporada clasificatoria [2]HRLKbb_lobby_1[2]PDHhh_game_bb,hh_game_bb_room,hh_game_bb_ui,hh_gamesys[2]HIHQHKEl Recibidor[2]HPYKwelcome_lounge[2]QHHhh_room_nlobby[2]HIHQGKLa Antec[195][161]mara[2]HRLKmain_lobby[2]QGHhh_room_lobby[2]HISPSPKEl Teatro[2]HSRKtheatredrome[2]SPIhh_room_theater[2]HIHY@DHEntretenimiento[2]HZWAKZ@DHEspacios Exteriores[2]HR~K[@DHJuegos: Battle Ball[2]HPYKXADHJuegos: Sal[195][179]n de Juegos[2]HR~KYADHCafeter[195][173]as[2]HReKZADHHabbo Club[2]HPYK[ADHRestaurantes[2]HReKXBDHBares & Clubes Noturnos[2]IPYKYBDHVest[195][173]bulos[2]HPYK[1]
[INCOMING]: FdH[1]
[INCOMING]: CHPAJGuest Rooms[2]HHHHX[127]CHSalas de chat[2]JXjGPAY[127]CHHabitaciones Laberinto[2]HYPEPAZ[127]CHSalas de negociaci[195][179]n[2]SEXQGPA[[127]CHCentros de ayuda[2]HYGFPAX@DHSalas de juegos y carreras[2]I[hGPA[1]
[INCOMING]: DyHH[1]DzHH[1]
[OUTGOING]: INySMghoM
[INCOMING]: C]RAJSin categor[195][173]a[2]PESalas de chat[2]QEHabitaciones Laberinto[2]RESalas de negociaci[195][179]n[2]SECentros de ayuda[2]PFSalas de juegos y carreras[2][1]
[INCOMING]: @r1740944557778[2][1]
MITM process error: [Errno 9] Bad file descriptor
[INCOMING]: @r1740944587777[2][1]
'''