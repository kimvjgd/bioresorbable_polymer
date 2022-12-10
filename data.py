
# list_num	
# Name	
# Bioegradation Condition (1)-Solution	
# Biodegradation Condition (2)-Sample size	
# Biodegradation Rate
# erosion	
# Glass Transition Temperature(°C)	
# Melting Point(°C)	
# Elongation(%)	
# Tensile Strength(MPa)	
# Young's Modulus(Mpa)	
# Density(g/cm3)	
# Ref

poly_data = [
['0','Poly(L-lactide)_PLLA','PBS (pH: 7.4, 37℃)','cylindrical (diameter:15mm)','0.130%/day (154 days)','bulk','55 ~ 65','170 ~ 200','3.0 ~ 10.0','15.5 ~ 150','2.7 ~ 4.14','1.24 ~ 1.30','1~6',],
['1','Poly(dl-lactide)_PDLLA','PBS (pH: 7.4±0.2, 37℃)','cylindrical (diameter:0.91±0.12μm)','0.179%/day (84 days)','dong_min','50 ~ 60','dong_min','2.0 ~ 10.0','27.6 ~ 50','1 ~ 3.45','1.25 ~ 1.27','1,5~8',],
['2','Poly(glycolic acid)_PGA','PBS (pH: 7.3, 37℃)','rectangular (40mm x 40mm x 0.1mm)','2%/day (20 days)','bulk','35 ~  45','220 ~ 233','1.5 ~ 20','60 ~ 99.7','6 ~ 7','1.50 ~ 1.71','1,3,9~11',],
['3','P(L/D)LA 96L/4D','dong_min','rectangular (10mmx 10mm x 1.6mm)','0.03%/day (77 days)','bulk','10 ~ 15','156.5','3.9 ~ 6.9','49.5 ~ 51.7','3.0 ~ 3.8','dong_min','12,13',],
['4','poly(ε-caprolactone) (PCL)','PBS (pH: 7.4, 37°C)','film (30mm x 5mm)','0.0164%/day (365 days)','surface','-60','59 ~ 64','300 ~ 500','20.7 ~ 34.5','210 ~ 340','1.15','14~18, 155',],
['5','Poly(γ-caprolactone)_PCL','PBS (37℃)','rectangular (2cm x 1cm x 0.01cm)','0.028%/day (560 days)','bulk and surface','-65 ~ -60','58 ~ 65','300 ~ 1000','20.7 ~ 42','0.21 ~ 0.44','1.11 ~ 1.146','1, 20~22',],
['6','Poly(l-lactide-co-ε-caprolactone)_PLCL','PBS (pH: 7.2, 37℃)','film (thickness:156±24μm, 28±2mg)','1.111%/day (63 days)','surface','16.4 ~ 57.3','136 ~ 174','314 ~ 486','17.2 ~ 26.6','0.01 ~ 1.34','dong_min','23,24',],
['7','Double-bond-cured Poly(ε-caprolactone/D,L-lactide)','PBS (pH: 7.0, 37°C, 20mL)','rectangular (200mm x 200mm x 2mm)','0.357%/day (84 days)','dong_min','-55 ~ 16','35','50 ~ 350','0.7 ~ 9.72','0.25 ~ 25.2','dong_min','26,27',],
['8','L-Latide Poly(lactic acid-co-glycolic acid),L-PLGA,LA:GA=95:5','PBS (pH: 7.4, 37°C, 20mL)','film (thickness: 0.3mm, 0,3g)','1.2%/day (50 days)','bulk','dong_min','dong_min','dong_min','dong_min','dong_min','dong_min','28',],
['9','L-Latide Poly(lactic acid-co-glycolic acid),L-PLGA,LA:GA=75:25','PBS (pH: 7.4, 37°C, 20mL)','film (thickness: 0.3mm, 0,3g)','2%/day (50 days)','bulk','dong_min','dong_min','dong_min','dong_min','dong_min','dong_min','28',],
['10','L-Latide Poly(lactic acid-co-glycolic acid),L-PLGA,LA:GA=50:50','PBS (pH: 7.4, 37°C, 20mL)','film (thickness: 0.3mm, 0,3g)','3.75%/day (20 days)','bulk','42','dong_min','1.9','39','3320','dong_min','23,28',],
['11','L-Latide Poly(lactic acid-co-glycolic acid),L-PLGA,LA:GA=65:35','PBS (pH: 7.4, 37°C, 20mL)','film (thickness: 0.3mm, 0,3g)','2.5%/day (40 days)','bulk','dong_min','dong_min','dong_min','dong_min','dong_min','dong_min','28',],
['12','Poly(glycolic acid-co-ε-caprolactone),PGC,LA:GA=80:20','PBS (pH: 7.4, 37°C)','cylindrical (diameter: 10mm, thickness: 0.5mm)','0.088%/day (385 days)','bulk','-63','15 ~ 40','dong_min','32.9','dong_min','dong_min','23, 29~31',],
['13','Poly(glycolic acid-co-ε-caprolactone),PGC,LA:GA=50:50','PBS (pH: 7.4, 37°C, 25mL)','film (5mm x 10mm x 1mm)','0.893%/day (84 days)','bulk','-16','15 ~ 40','653','5.13','0.007','dong_min','23, 29~32',],
['14','L-Lactide Poly(lactic acid-glycolic acid-co-ε-caprolactone),L-PLGC,L:G:C=10:40:50','PBS (pH: 7.4, 37°C, 25mL)','rectangular (5mm x 10mm x 1mm)','1.07%/day (84 days)','bulk','-14','dong_min','561','0.014','0.00009','dong_min','23, 33',],
['15','L-Lactide Poly(lactic acid-glycolic acid-co-ε-caprolactone),L-PLGC,L:G:C=20:30:50','PBS (pH: 7.4, 37°C, 25mL)','rectangular (5mm x 10mm x 1mm)','0.833%/day (84 days)','bulk','-10','dong_min','555','0.034','0.00014','dong_min','23, 33',],
['16','L-Lactide Poly(lactic acid-glycolic acid-co-ε-caprolactone),L-PLGC,L:G:C=27:63:10','PBS (pH: 7.4, 37°C, 0.10M)','film (thickness: 0.5mm, 0.25-0.35g)','2.21%/day (42 days)','bulk','8','dong_min','674','19.7','dong_min','dong_min','23, 34',],
['17','L-Lactide Poly(lactic acid-glycolic acid-co-ε-caprolactone),L-PLGC,L:G:C=45:45:10','PBS (pH: 7.4, 37°C, 0.10M)','film (thickness: 0.5mm, 0.25-0.35g)','1.60%/day (42 days)','bulk','17','dong_min','608','24.8','dong_min','dong_min','23, 34',],
['18','L-Lactide Poly(lactic acid-glycolic acid-co-ε-caprolactone),L-PLGC,L:G:C=63:27:10','PBS (pH: 7.4, 37°C, 0.10M)','film (thickness: 0.5mm, 0.25-0.35g)','0.821%/day (84 days)','bulk','22','dong_min','570','25.6','dong_min','dong_min','23, 34',],
['19','D,L-Lactide Poly(lactic acid-glycolic acid-co-ε-caprolactone),D,L-PLGC,L:G:C=40:40:20','PBS (pH: 7.4, 37°C)','cylindrical (length: 20mm)','1.82%/day (49 days)','bulk','22','dong_min','393','7.41','9.19','dong_min','23, 35',],
['20','D,L-Lactide Poly(lactic acid-glycolic acid-co-ε-caprolactone),D,L-PLGC,L:G:C=30:30:40','PBS (pH: 7.4, 37°C)','cylindrical (length: 20mm)','1.57%/day (49 days)','bulk','-6','dong_min','520','1.38','3.7','dong_min','23, 35',],
['21','PLGA-PCL-PLGA (d,l-)L:G=50:50','PBS (pH: 7.4, 37°C, 0.01M, 5mL), sodium azide (w/v: 0.02%)','film (thickness: 100μm)','1.13%/day (56 days)','dong_min','22','dong_min','401','2.4','26','dong_min','23, 36',],
['22','PLGA-PCL-PLGA (d,l-)L:G=75:25','PBS (pH: 7.4, 37°C, 0.01M, 5mL), sodium azide (w/v: 0.02%)','film (thickness: 100μm)','0.893%/day (56 days)','dong_min','29','dong_min','478','1.9','19.8','dong_min','23, 36',],
['23','Poly(D-lactide-co-glycolide)_PDLGA(50:50)','PBS (37℃)','cylindrical (dimeter:1.03±0.05cm)','0.595%/day (168 days)','surface','45','dong_min','2.0 ~ 10.0','41.4 ~ 55.2','1 ~ 4.34','1.30 ~ 1.40','1,8,37,38',],
['24','Poly(lactide-co-glycolide)_PLGA(50:50)','PBS (pH: 7.4, 37℃)','cylindrical (thickness: 0.3±0.03mm)','3.5%/day (28 days)','bulk','dong_min','dong_min','dong_min','dong_min','dong_min','dong_min','39~41',],
['25','PGA/PCL','PBS (37℃)','cylindrical (dimeter:150μm, thickness:100mm)','0.260%/day (77 days)','dong_min','dong_min','dong_min','dong_min','dong_min','dong_min','dong_min','42',],
['26','PLA/PCL','PBS (37℃)','cylindrical (dimeter:150μm, thickness:100mm)','0.139%/day (360-720 days 0.106%/day (189 days)','bulk','20','100~125','dong_min','dong_min','20 ~ 40','dong_min','8,42,43',],
['27','Polyhydroxybutyrate_PHB','PBS(pH: 7.4, 37°C)','rectangular (10×5x100mm, 5mg)','0.003%/day (364 days)','dong_min','5.0 ~ 15.0','168 ~ 182','5.0 ~ 8.0','40','40','1.18 ~ 1.262','1,5,44',],
['28','Poly(3-hydroxybutyrate-co-3-hydroxyvalerate)_PHBV','PBS (pH: 7.2, 37℃)','film (weight:50mg)','0.0083%/day (300 days)','surface','1.4 ~ 2.8','170','20','30 ~ 38','700 ~ 2900','dong_min','23,45~47',],
['29','Poly(4-Hydroxybutyrate)_P4HB','PBS (pH: 7.2 ,37℃)','film (weight: 50mg)','0.01%/day (250 days)','surface','-51','60','1000','50','70','dong_min','3, 49~53',],
['30','Polydioxanone(PDO)','PBS (pH: 7.4, 37°C)','cylindrical (diameter: 0.1~1μm, thickness: 0.3mm)','1%/day (50 days)','bulk','-10 ~ 0','110','62','139','1500','1.318','54,55,57~60',],
['31','Polybutylene succinate_PBS','PBS (pH: 7.4, 37℃, Enzyme (0.15ml))','rectangular (3cm x 1cm x 0.5mm)','23.33%/day (3 days)','surface','-32','110 ~ 120','321','32.1','330','1.25','23,61~63',],
['32','Poly(trimethylene carbonate)_PTMC','PBS (pH: 7.4, 37℃, Enzyme)','rectangular (10mm x 10mm x0.5mm)','0.595%/day (84 days) (Mn: 329)0.229%/day (84 days) (Mn: 72)','surface','-27 ~ -19','113','610 ~ 670','1.8 ~ 2.4','5 ~ 6','dong_min','23,64~66',],
['33','Poly(butylene adipate-co-terephthalate)_PBAT','PBS (pH: 7, 37℃)','rectangular (15mm x 10mm x 0.5-6 mm)','0.083%/day (72days)','dong_min','11 ~ 20','110 ~ 120','500 ~ 800','11 ~ 20','40 ~ 80','dong_min','23, 67, 68',],
['34','Poly(ethylene glycol citrate)_PEC','PBS (pH: 7.4, 37℃)','cylindrical (dimaeter:10mm, thickness:1-1.5mm)','50%/day (1 day)','surface','-28.2 ~ 2.9','dong_min','140 ~ 1505','0.51 ~ 1.51','0.25 ~ 1.91','dong_min','26,49,69,70',],
['35','Poly(1,8-octanediol citrate)_POC','PBS (pH: 7.4, 37℃)','cylindrical (dimaeter: 7mm, thickness: 1-1.5mm)','0.556%/day (180 days)','bulk','-10 ~ 0','dong_min','117 ~ 502','2.93 ~ 11.15','1.85 ~ 13.98','dong_min','26, 49, 72,73',],
['36','Poly(octamethylene maleate (anhydride) citrate)_POMC4/6','PBS (pH: 7.4, 37℃)','cylindrical (dimaeter: 7mm, thickness: 3mm)','0.778%/day (90 days)','surface','-36 ~ -9','dong_min','55.02 ~ 322.09','0.29 ~ 0.88','0.07 ~ 1.06','dong_min','26,74',],
['37','Poly(1,8~octanediol malate)_POM','PBS (pH: 7.4, 37 °C, 10mL)','cylindrical (diameter: 7mm, thickness: 1~1.5mm)','1.10%/day (91 days)','dong_min','-70 ~ -60','170~175','11.8 ~ 16.88','6.69 ~ 7.95','3100','dong_min','75, 76',],
['38','Crosslinked urethane~doped polyester_CUPE','PBS (pH: 7.4, 37 °C, 10mL, 0.01M)','cylindrical (diameter:7 mm)','0.27%/day (60 days)','dong_min','27.47','dong_min','222.66 ~ 337.558','14.6 ~ 41.07','6.78 ~ 9.22','1.25 ~ 1.35','49, 77',],
['39','Poly(glycerol sebacate)_PGS','PBS (pH: 7, 37℃, Enzyme)','cylindrical (diameter: 10mm, thickness: 2mm)','0.214%/day (70 days)','surface','-80','dong_min','40 ~ 448','0.2 ~ 0.5','0.056 ~ 1.2','1.13','49, 79, 80',],
['40','Poly(1,2-propanediol-sebacate-citrate)_PPSC','PBS (pH: 7.4, 37℃)','cylindrical (dimaeter:10mm, thickness:1-1.5mm)','3%/day (20 days)','dong_min','-13.8 ~ 9.8','dong_min','226 ~ 432','0.87 ~ 2.12','0.6 ~ 1.23','dong_min','26, 45, 49, 81, 82',],
['41','Poly(1,8-octanediol-citrate-sebacate)_POCS','PBS (pH: 7.4, 37 °C, 10mL, 0.01M)','cylindrical (diameter: 10mm, thickness: ~0.1mm)','1.43%/day (49 days)','surface','-40','28','168','0.24','0.19','1.09','83',],
['42','Poly(glycerol-sebacate-citrate)_PGSC','PBS (pH: 7.4, 37 °C, 20 mL)','cylindrical (diameter: 10mm, thickness: 1mm)','0.571%/day (28 days)','dong_min','-27.7 ~ -12','dong_min','51 ~ 170','0.63 ~ 1.46','0.61 ~ 3.26','dong_min','26, 84,85',],
['43','Poly(polyol sebacate)_PPS','PBS (pH: 7.4, 37 °C, 20mL)','cylindrical (diameter: 10mm, thickness: 1mm)','0.149%/day (105 days)','surface','18.1','80~100','192.24','0.57 ~ 0.79','0.37 ~ 2.21','1.13','86',],
['44','Poly(glycerol dodecanoate)_PGD','PBS (pH: 7.4, 37 °C)','cylindrical (diameter: 8mm, thickness: 2mm)','1.43%/day (14 days)','surface','32.1','dong_min','123.2 ~ 225','0.46 ~ 7.2','1.08 ~ 136.55','dong_min','26,86,88',],
['45','Poly(triol α-ketoglutarate)_PTK','PBS (pH: 7.4, 37 °C)','rectangular (10mm × 3mm × 1.5mm)','3.57%/day (28 days)','dong_min','-22.5','dong_min','22 ~ 583','0.2 ~ 30.8','0.1 ~ 657.4','dong_min','26, 89',],
['46','Poly(erythritol dicarboxylate)_PErD','PBS (pH: 7.4, 37 °C)','rectangular (10mm x 3mm x 1.5mm)','4.76%/day (21 days)','bulk and surface','-35.8 ~ 3.8','dong_min','22 ~ 466','0.14 ~ 16.65','0.08 ~ 80.37','dong_min','21,26',],
['47','Poly(1,12-dodecandiol malate)_PDDM','PBS (pH: 7.4, 37 °C, 15mL)','rectangular (6mm x 0.5mm x 18mm)','0.3%/day (30 days)','dong_min','dong_min','dong_min','25.86 ~ 737.48','0.21 ~ 4.16','0.98 ~ 4.04','dong_min','26,91',],
['48','poly(DTE carbonate)','PBS (pH 7.4, 37°C)','rectangular (5mm x 5mm x 0.1mm)','0.5%/day (140 days)','surface','90','98 ~ 101','4','44 ~ 90','1471','1.324','3,92,93,113,115',],
['49','Polyurethane_PU','PBS (pH: 7.4, enzymatic)','rectangular (15mm x 15mm x 0.1mm)','24.004%/day (4.166 days)','surface','-41','dong_min','dong_min','0.1','dong_min','0.8 ~ 1.47 ','3,94~96, 116',],
['50','Poly(vinyl alcohol) PVA','PBS (pH: 7.4, 37 °C)','rectangular (1cm x 1cm x 0.1mm)','0.4%/day (50 days)','dong_min','80~90','200','220','48.4','707.9','dong_min','98, 101',],
['51','Poly (ethylene oxide)_PEO','PBS (pH: 7, 37℃)','cylindrical (dimeter: 10mm, thickness: 250μm)','1.607%/day (56 days)','dong_min','-56','dong_min','dong_min','dong_min','650','dong_min','3, 102',],
['52','Poly(methyl methacrylate)_PMMA','PBS (pH: 7.5, 37℃, 0.1M, enzyme)','rectangular (10mm x 10mm x 0.2mm)','0.013%/day (3 days)','bulk and surface','116','dong_min','dong_min','dong_min','3000','dong_min','3, 103',],
['53','2,2-bis(ɛ-CL-4-yl)-propane(BCP) cured poly(ɛ-CL-co-d,l-LA)','PBS (pH 7.4, 37 °C, 12mL)','rectangular (100mm x 6mm x 3mm)','1.19%/day (84 days)','bulk','-32','dong_min','65 ~ 154','0.21 ~ 0.6','0.55 ~ 1.55','dong_min','26,105',],
['54','Double-bond-cured poly(1,8-octanediol citrate) (POC)','PBS (pH: 7.4, 37°C, 10mL)','cylindrical (diameter: 6mm, thickness: 1mm)','0.4%/day (30 days)','bulk','-12.7 ~ -1.6','dong_min','86 ~ 260','2.8 ~ 15.7','7.4 ~ 75.9','dong_min','26,97',],
['55','poly(glycolic acid-co-trimethylene carbonate),PGTMC,LA:GA=32.5:67.5','PBS (pH: 7.4, 37°C)','rectangular (20mm x 5mm x 0.2mm)','0.612%/day (49 days)','bulk','21','153.8','615','202','202','dong_min','23,106',],
['56','PGA-PTMC-PGA','PBS (pH: 7.4, 37°C)','rectangular (20mm x 5mm x 0.2mm)','0.404%/day (42 days)','bulk','-12','215','23','36','659','dong_min','23,106',],
['57','PGA-PGTMC-PGA','PBS (pH: 7.4, 37°C)','rectangular (20mm x 5mm x 0.2mm)','0.429%/day (42 days)','bulk','20','209.9','287','26','377','dong_min','23,106',],
['58','PLLA-PGCBlock length 2000g/molL:G:C=80:7:13','PBS (pH: 7.4, 37°C, 0.10M)','film (thickness: 0.1mm)','0.286%/day (210 days)','dong_min','40.9','dong_min','415','34','dong_min','dong_min','23,107',],
['59','PLLA-PGCBlock length 4000g/molL:G:C=80:7:13','PBS (pH: 7.4, 37°C, 0.10M)','film (thickness: 0.1mm)','0.262%/day (210 days)','dong_min','41.2','dong_min','363','26','dong_min','dong_min','23,107',],
['60','PLLA-PGCBlock length 6000g/molL:G:C=80:7:13','PBS (pH: 7.4, 37°C, 0.10M)','film (thickness: 0.1mm)','0.202%/day (210 days)','dong_min','45.1','149.1','600','32.5','dong_min','dong_min','23,107',],
['61','L-Lactide Poly(lactic acid-glycolic acid-co-trimethylene carbonate),L-PLGT,L:G:T=87:3:10','PBS (pH: 7.4, 37°C, 10mL), sodium azide  (0.03 mg/L)','rectangular (4mm × 75mm × 0.3mm)','0.0235%/day (196 days)','bulk','49.8','154.2','15','55','1255','dong_min','108',],
['62','L-Lactide Poly(lactic acid-glycolic acid-co-trimethylene carbonate),L-PLGT,L:G:T=85:5:10','PBS (pH: 7.4, 37°C, 10mL), sodium azide  (0.03 mg/L)','rectangular (4mm × 75mm × 0.3mm)','0.0730%/day (196 days)','bulk','49.3','153.8','18','50','1250','dong_min','108',],
['63','L-Lactide Poly(lactic acid-glycolic acid-co-trimethylene carbonate),L-PLGT,L:G:T=83:7:10','PBS (pH: 7.4, 37°C, 10mL), sodium azide  (0.03 mg/L)','rectangular (4mm × 75mm × 0.3mm)','0.187%/day (196 days)','bulk','48.6','151.8','37','47','1240','dong_min','108',],
['64','L-Lactide Poly(lactic acid-glycolic acid-co-trimethylene carbonate),L-PLGT,L:G:T=75:5:20','PBS (pH: 7.4, 37°C, 10mL), sodium azide  (0.03 mg/L)','rectangular (4mm × 75mm × 0.3mm)','0.124%/day (196 days)','bulk','44.9','dong_min','160.1','40.6','1030.5','dong_min','108',],
['65','L-Lactide Poly(lactic acid-glycolic acid-co-trimethylene carbonate),L-PLGT,L:G:T=60:34:6','PBS (pH: 7.4, 37°C)','film (surface area: 1cm2, weight: 70mg)','0.714%/day (140 days)','bulk','51','dong_min','300','44','17.6','dong_min','23,109',],
['66','L-Lactide Poly(lactic acid-glycolic acid-co-trimethylene carbonate),L-PLGT,L:G:T=54:34:12','PBS (pH: 7.4, 37°C)','film (surface area: 1cm2, weight: 70mg)','0.840%/day (119 days)','bulk','44','dong_min','325','51','13.3','dong_min','23,109',],
['67','PLGA-PTMC-PLGA (l-)L:G:T=70:10:20','PBS (pH: 7.4, 37°C, 0.1M)','film (10mm x 10mm x 0.3mm)','0.222%/day (168 days)','dong_min','44','dong_min','297.9 ~ 364.7','19.8 ~ 25.2','252.9 ~ 335.3','dong_min','110',],
['68','PLGA-PTMC-PLGA (l-)L:G:T=73:7:20','PBS (pH: 7.4, 37°C, 0.1M)','film (10mm x 10mm x 0.3mm)','0.0988%/day (168 days)','dong_min','43.6','dong_min','280.7 ~ 351.9','21.2 ~ 28.2','415.7 ~ 556.5','dong_min','110',],
['69','Tyrosine-Derived Polycarbonate (TyrPC)','PBS (pH: 7.4, 37°C)','cylindrical (diameter: 9mm, thickness 2mm)','4.28%/day (21 days)','surface','80 ~ 90','dong_min','dong_min','dong_min','dong_min','dong_min','111,112',],
['70','polyanhydride (poly(sebacic acid), diacetoxy terminated) PSADT','PBS (pH: 7.4, 37°C)','cylindrical (diameter: 12.5mm, thickness 1.2mm)','7.57%/day (7 days)','surface','dong_min','133','dong_min','dong_min','dong_min','dong_min','114',],
['71','Poly[α,α′-bis(ortho-carboxyphenoxy)-para-xylene](oCPX)','PBS (pH: 7.4, 37°C) 0.0027 M potassium chloride and 0.137 M sodium chloride)','cylindrical (diameter: 13mm, thickness: 1mm)','0.8%/day (90 days)','surface','68','114','dong_min','dong_min','dong_min','dong_min','117,118',],
['72','Poly[(glycine ethyl ester)(aniline pentamer)(phosphazene]_PGAP','PBS (pH: 7.4, 37℃)','cylindrical (diameter: 16mm, thickness: 100μm)','0.714%/day (70 days)','bulk and surface','-20~-10','dong_min','dong_min','0.15 ~ 0.21','0.067 ~ 0.079','dong_min','119~121',],
['73','Polypyrrole_PPy/Poly(lactic acid)_PLA','PBS (pH: 7.4, 37℃)','cylindrical (diemeter: 300nm)','0.297%/day (84 days)','dong_min','dong_min','dong_min','20','2','40','dong_min','3,122,123',],
['74','Dextran-based hydrogel(~50%)','PBS (pH: 7.2)','cylindrical (diameter: 0.46cm, thickness: 2cm)','10%/day (9 days)','bulk','172.5','dong_min','dong_min','dong_min','0.0015','dong_min','3,124',],
['75','hyaluronan','PBS (pH 7.4, 37°C) containing hyaluronidase','cylindrical (diameter: 1cm, thickness: 5 mm)','5%/day (14 days)','surface','135~160','dong_min','300','0.11','0.2','dong_min','126~129',],
['76','Pullulan','PBS (pH7.4, CaCl2 (0.25mM), MgSO4 (0.09mM) ,NH4Cl (0.09mM), FeCl3 (0.9μM)) (*BOD test)','polymer powder(20mg) (*BOD test)','2.6%/day (25 days)','dong_min','dong_min','dong_min','1.1 ~ 5.3','23.0 ~ 41.0','1300 ~ 2300','dong_min','130',],
['77','chitosan','PBS (pH 7.4, 37°C) 0.5 mg/mL lysozyme  (70,000)U/mg, Fluka, USA) and 0.5 mg/mL NaN3','cylindrical (diameter: 13mm, thickness: 662±34 μm)','1.75%/day (40 days0','bulk','140~150','dong_min','dong_min','dong_min','65000','1.444','3,131~133',],
]

print(len(poly_data))