"""Medical prompts of thirty to thirty-seven words about diagnoses and treatment plans."""

from __future__ import annotations

DIAGNOSES: list[str] = [
    (
        "The patient's severe aplastic anemia is being treated with antithymocyte globulin and cyclosporine "
        "immunosuppression, with plan for matched unrelated donor transplant if no response."
    ),
    (
        "The vascular surgery team performed carotid endarterectomy for the symptomatic high grade internal carotid "
        "artery stenosis with intraoperative shunting and patch angioplasty technique."
    ),
    (
        "The patient developed heparin induced thrombocytopenia with thrombosis, requiring immediate heparin cessation "
        "and transition to argatroban with subsequent warfarin bridging therapy."
    ),
    (
        "The thoracic surgery team performed video assisted thoracoscopic surgery lobectomy for the stage one non "
        "small cell lung cancer with mediastinal lymph node sampling and negative margins."
    ),
    (
        "The patient's systemic mastocytosis was confirmed on bone marrow biopsy with KIT D816V mutation, initiating "
        "midostaurin therapy for the advanced disease with organ involvement."
    ),
    (
        "The gynecologic oncology team performed radical hysterectomy with bilateral pelvic lymphadenectomy for the "
        "stage one B cervical squamous cell carcinoma with clear surgical margins."
    ),
    (
        "The patient underwent successful orthotopic heart transplant for the dilated cardiomyopathy with end stage "
        "heart failure, with good early biventricular function on post operative echocardiogram."
    ),
    (
        "The hematology team initiated ruxolitinib for the myelofibrosis with constitutional symptoms and "
        "splenomegaly, achieving significant reduction in spleen size and symptom improvement."
    ),
    (
        "The patient's autoimmune hepatitis was diagnosed on liver biopsy with interface hepatitis and plasma cells, "
        "initiating prednisone and azathioprine combination therapy."
    ),
    (
        "The neurosurgery team performed microvascular decompression for the medication refractory hemifacial spasm, "
        "identifying the offending vessel and achieving immediate resolution of symptoms."
    ),
    (
        "The patient developed febrile neutropenia during induction chemotherapy, requiring broad spectrum antibiotics "
        "with cefepime and vancomycin, antifungal prophylaxis, and growth factor support."
    ),
    (
        "The endocrine surgery team performed bilateral adrenalectomy for the Cushing's syndrome secondary to "
        "bilateral adrenal hyperplasia, requiring lifelong steroid replacement therapy."
    ),
    (
        "The patient's primary hyperparathyroidism was localized with sestamibi scan, and the surgeon performed "
        "minimally invasive parathyroidectomy with intraoperative PTH monitoring confirming cure."
    ),
    (
        "The colorectal surgery team performed transanal total mesorectal excision for the low rectal cancer, "
        "achieving complete mesorectal envelope with sphincter preservation."
    ),
    (
        "The patient underwent successful small bowel transplant for the short gut syndrome secondary to extensive "
        "mesenteric ischemia, with good early graft function and enteral feeding."
    ),
    (
        "The rheumatology team initiated tofacitinib for the rheumatoid arthritis refractory to multiple biologic "
        "agents, with discussion of increased cardiovascular and malignancy risks."
    ),
    (
        "The patient's hereditary angioedema was diagnosed with low C4 and C1 esterase inhibitor levels, initiating "
        "lanadelumab prophylaxis and providing icatibant for acute attacks."
    ),
    (
        "The cardiac electrophysiology team performed His bundle pacing for the patient with heart failure and left "
        "bundle branch block, achieving electrical resynchronization."
    ),
    (
        "The patient developed vancomycin resistant Enterococcus bacteremia, requiring daptomycin therapy with "
        "infectious disease guidance and central line removal for source control."
    ),
    (
        "The surgical team performed pancreaticoduodenectomy with portal vein resection and reconstruction for the "
        "borderline resectable pancreatic adenocarcinoma following neoadjuvant folfirinox chemotherapy."
    ),
    (
        "The patient's sarcoidosis with cardiac involvement was confirmed on PET scan and cardiac MRI, initiating high "
        "dose corticosteroids and methotrexate with cardiology monitoring."
    ),
    (
        "The neurology team diagnosed anti NMDA receptor encephalitis with positive CSF antibodies, initiating first "
        "line immunotherapy with steroids, IVIG, and plasma exchange."
    ),
    (
        "The patient underwent successful islet cell transplantation for the brittle type one diabetes with severe "
        "hypoglycemic unawareness, achieving insulin independence at six months."
    ),
    (
        "The ophthalmology team performed trabeculectomy with mitomycin C for the medically refractory open angle "
        "glaucoma, achieving target intraocular pressure reduction."
    ),
    (
        "The patient's hemophilia A with inhibitors is being treated with emicizumab prophylaxis, with bypassing "
        "agents available for breakthrough bleeding episodes."
    ),
    (
        "The urology team performed robotic partial nephrectomy for the renal cell carcinoma, achieving negative "
        "margins with warm ischemia time under twenty minutes."
    ),
    (
        "The patient developed acute pancreatitis from hypertriglyceridemia, requiring insulin infusion, "
        "plasmapheresis, and ICU level care for the severe necrotizing disease."
    ),
    (
        "The pediatric cardiology team performed transcatheter closure of the secundum atrial septal defect with the "
        "Amplatzer device, achieving complete occlusion without residual shunt."
    ),
    (
        "The patient's Fabry disease was diagnosed with low alpha galactosidase A enzyme activity and confirmed GLA "
        "mutation, initiating enzyme replacement therapy with agalsidase beta."
    ),
    (
        "The surgical team performed emergent exploratory laparotomy for the perforated duodenal ulcer, finding four "
        "quadrant peritonitis requiring Graham patch repair and extensive washout."
    ),
    (
        "The patient underwent successful allogeneic hematopoietic stem cell transplant from a matched sibling donor "
        "for the high risk acute lymphoblastic leukemia in first complete remission."
    ),
    (
        "The interventional cardiology team performed transcatheter edge to edge repair for the severe tricuspid "
        "regurgitation with improvement in right heart failure symptoms."
    ),
    (
        "The patient's pheochromocytoma was localized with MIBG scan, and after alpha and beta blockade, underwent "
        "successful laparoscopic adrenalectomy with blood pressure normalization."
    ),
    (
        "The neurosurgery team performed endoscopic transsphenoidal resection of the pituitary macroadenoma causing "
        "visual field defects, with improvement in vision post operatively."
    ),
    (
        "The patient developed acute liver failure from acetaminophen overdose, meeting King's College criteria for "
        "transplant listing with emergent evaluation ongoing."
    ),
    (
        "The thoracic surgery team performed extrapleural pneumonectomy with heated chemotherapy for the malignant "
        "pleural mesothelioma as part of the trimodality treatment approach."
    ),
    (
        "The patient's Wilson's disease was diagnosed with low ceruloplasmin and elevated twenty four hour urine "
        "copper, initiating D penicillamine chelation therapy with zinc supplementation."
    ),
    (
        "The gastroenterology team performed endoscopic submucosal dissection for the large flat colonic polyp with "
        "high grade dysplasia, achieving en bloc resection with clear margins."
    ),
    (
        "The patient underwent successful kidney pancreas transplant for the type one diabetes with end stage renal "
        "disease, achieving insulin independence and dialysis freedom."
    ),
    (
        "The hematology team initiated luspatercept for the transfusion dependent myelodysplastic syndrome with ring "
        "sideroblasts, achieving reduction in transfusion requirements."
    ),
    (
        "The patient's dermatomyositis was diagnosed with classic heliotrope rash, Gottron's papules, and elevated CK, "
        "initiating prednisone and screening for occult malignancy."
    ),
    (
        "The cardiac surgery team performed the Bentall procedure for the aortic root aneurysm with severe aortic "
        "regurgitation, using a mechanical composite graft."
    ),
    (
        "The patient developed acute chest syndrome in sickle cell disease, requiring exchange transfusion, "
        "supplemental oxygen, and broad spectrum antibiotics with pain management."
    ),
    (
        "The interventional radiology team performed selective internal radiation therapy with yttrium-90 microspheres "
        "for the unresectable hepatocellular carcinoma not amenable to ablation."
    ),
    (
        "The patient's primary sclerosing cholangitis was diagnosed on MRCP showing multifocal biliary strictures, "
        "initiating ursodeoxycholic acid and surveillance for cholangiocarcinoma."
    ),
    (
        "The surgical team performed emergent craniotomy for evacuation of the acute subdural hematoma with midline "
        "shift, achieving good decompression and neurologic improvement."
    ),
    (
        "The patient underwent successful corneal transplant for the keratoconus refractory to contact lens fitting, "
        "with good early graft clarity and visual improvement."
    ),
    (
        "The oncology team initiated osimertinib for the EGFR T790M mutant non small cell lung cancer progressing on "
        "first generation TKI, achieving partial response."
    ),
    (
        "The patient's autoimmune polyendocrine syndrome type one was diagnosed with chronic mucocutaneous "
        "candidiasis, hypoparathyroidism, and adrenal insufficiency requiring multi hormone replacement."
    ),
    (
        "The vascular surgery team performed fenestrated endovascular aneurysm repair for the juxtarenal abdominal "
        "aortic aneurysm, preserving renal artery perfusion with custom stent graft."
    ),
]
