"""Medical prompts: long questions and exclamations, then short prompts by specialty."""

from __future__ import annotations

SPECIALTIES: list[str] = [
    # LONG QUESTIONS (30-37 WORDS)
    (
        "Given the patient's elevated creatinine and history of contrast allergy, should we proceed with the CT "
        "angiogram using premedication protocol or consider alternative imaging modalities?"
    ),
    (
        "Would you recommend adding a proton pump inhibitor for gastroprotection given the patient is on dual "
        "antiplatelet therapy and has a history of peptic ulcer disease?"
    ),
    (
        "Should we pursue liver transplant evaluation given the MELD score of twenty eight and recent episode of "
        "spontaneous bacterial peritonitis requiring hospitalization?"
    ),
    (
        "Is there a role for immunotherapy in this patient's treatment plan given the tumor's high PD L1 expression "
        "and absence of targetable driver mutations?"
    ),
    (
        "Would you recommend prophylactic bilateral mastectomy and oophorectomy given the confirmed BRCA2 mutation and "
        "strong family history of breast and ovarian cancer?"
    ),
    (
        "Should we consider mechanical thrombectomy given the large vessel occlusion on CT angiography and the "
        "patient's presentation within the extended treatment window?"
    ),
    (
        "Given the patient's frailty score and multiple comorbidities, would you recommend transcatheter versus "
        "surgical aortic valve replacement for the severe aortic stenosis?"
    ),
    (
        "Should we pursue aggressive surgical debulking or opt for neoadjuvant chemotherapy first given the extensive "
        "peritoneal carcinomatosis seen on imaging?"
    ),
    (
        "Would genetic testing for hereditary cancer syndromes be appropriate given the patient's young age at "
        "diagnosis and family history of multiple malignancies?"
    ),
    (
        "Is there a role for neuromodulation therapy such as spinal cord stimulation given the failure of conservative "
        "management for the chronic pain syndrome?"
    ),
    (
        "Should we consider ventricular assist device placement as a bridge to transplant or destination therapy given "
        "the patient's end stage heart failure?"
    ),
    (
        "Would you recommend bariatric surgery given the patient's BMI of forty five and multiple obesity related "
        "comorbidities including type two diabetes and sleep apnea?"
    ),
    (
        "Given the recurrent C. difficile infections despite multiple courses of vancomycin, should we consider fecal "
        "microbiota transplantation as the next step?"
    ),
    (
        "Should we pursue deep brain stimulation surgery given the patient's Parkinson's disease with motor "
        "fluctuations refractory to optimal medical management?"
    ),
    (
        "Would concurrent chemoradiation or sequential therapy be more appropriate for this locally advanced non small "
        "cell lung cancer given the patient's performance status?"
    ),
    # LONG EXCLAMATIONS (30-37 WORDS)
    (
        "The patient just went into ventricular fibrillation, charge the defibrillator to two hundred joules and "
        "prepare to shock, someone start timing and get the code team here now!"
    ),
    (
        "We have a ruptured ectopic pregnancy with hemoperitoneum, type and cross for six units of packed red blood "
        "cells and get the OR ready for emergency laparotomy!"
    ),
    (
        "The intracranial pressure is spiking to forty, we need to hyperventilate, give mannitol, and get neurosurgery "
        "here immediately for possible decompressive craniectomy!"
    ),
    (
        "This is a category one C section, the baby is in distress with prolonged decelerations, we need the patient "
        "in the operating room within five minutes!"
    ),
    (
        "The patient has signs of meningococcemia with purpura fulminans, start empiric ceftriaxone and dexamethasone "
        "immediately and prepare for possible DIC management!"
    ),
    (
        "We're losing the airway, the angioedema is progressing rapidly, prepare for surgical cricothyrotomy if the "
        "next intubation attempt fails with the video laryngoscope!"
    ),
    (
        "The aortic dissection is extending, blood pressure control is critical, start esmolol and nitroprusside drips "
        "and get cardiothoracic surgery on the phone immediately!"
    ),
    (
        "The patient is in cardiogenic shock post MI, we need intra aortic balloon pump placement and emergent cardiac "
        "catheterization with possible mechanical circulatory support!"
    ),
    (
        "Massive upper GI bleed with hemodynamic instability, activate the massive transfusion protocol and get GI for "
        "emergent endoscopy, the hemoglobin is four!"
    ),
    (
        "The transplanted kidney is showing signs of hyperacute rejection, we need to take the patient back to the OR "
        "for graft nephrectomy immediately!"
    ),
    (
        "Status epilepticus for over thirty minutes despite benzodiazepines, load phenytoin now and prepare for "
        "intubation if the seizures don't break with the next medication!"
    ),
    (
        "The patient developed tension pneumothorax during central line placement, needle decompression in the second "
        "intercostal space followed by chest tube insertion needed now!"
    ),
    (
        "Acute limb ischemia with the six Ps present, vascular surgery needs to take this patient to the OR for "
        "thrombectomy within the next two hours!"
    ),
    (
        "The patient is in thyroid storm with fever, tachycardia, and altered mental status, start propylthiouracil, "
        "propranolol, hydrocortisone, and cooling measures immediately!"
    ),
    (
        "Addisonian crisis suspected with hypotension and hyperkalemia, give stress dose hydrocortisone one hundred "
        "milligrams IV push and aggressive fluid resuscitation now!"
    ),
    # SPECIALTY-SPECIFIC - CARDIOLOGY
    "The twelve lead EKG shows ST elevations in leads two, three, and aVF consistent with inferior STEMI.",
    "Cardiac MRI revealed late gadolinium enhancement in the inferolateral wall suggestive of prior infarction.",
    "The stress echocardiogram was positive for inducible ischemia in the LAD territory.",
    "Holter monitoring captured multiple runs of non sustained ventricular tachycardia.",
    "The patient's BNP level of two thousand suggests significant heart failure exacerbation.",
    "Transesophageal echocardiography revealed a left atrial appendage thrombus, contraindicating cardioversion.",
    "The cardiac CT calcium score of four hundred places him in high cardiovascular risk category.",
    (
        "Implantable cardioverter defibrillator placement recommended for primary prevention given the low ejection "
        "fraction."
    ),
    "The patient underwent successful patent foramen ovale closure following cryptogenic stroke.",
    "Cardiac resynchronization therapy improved symptoms and ejection fraction in this heart failure patient.",
    # SPECIALTY-SPECIFIC - ONCOLOGY
    "The tumor board recommended pembrolizumab monotherapy for the MSI high colorectal cancer.",
    "CAR T cell therapy with tisagenlecleucel for relapsed diffuse large B cell lymphoma.",
    "Stereotactic body radiation therapy to the oligometastatic lung lesions.",
    "The patient achieved complete pathologic response after neoadjuvant chemotherapy.",
    "Tumor genomic profiling revealed an EGFR exon nineteen deletion mutation.",
    "The oncotype DX recurrence score was eighteen, favoring hormonal therapy alone.",
    "Palliative radiation to the painful bone metastases for symptom control.",
    "The patient is receiving maintenance rituximab following R CHOP chemotherapy.",
    "Targeted therapy with imatinib for the newly diagnosed chronic myeloid leukemia.",
    "Prophylactic cranial irradiation for limited stage small cell lung cancer.",
    # SPECIALTY-SPECIFIC - NEUROLOGY
    "The EEG showed three hertz spike and wave discharges consistent with absence seizures.",
    "MRI brain revealed multiple periventricular white matter lesions concerning for demyelination.",
    "The patient's NIHSS score improved from eighteen to six after thrombectomy.",
    "Lumbar puncture showed elevated opening pressure consistent with idiopathic intracranial hypertension.",
    "The nerve conduction study confirmed severe bilateral carpal tunnel syndrome.",
    "Botulinum toxin injections scheduled for chronic migraine prophylaxis.",
    "The patient was started on levodopa carbidopa for newly diagnosed Parkinson's disease.",
    "Intravenous immunoglobulin therapy for the acute Guillain Barré syndrome exacerbation.",
    "Ocrelizumab infusion scheduled for the relapsing remitting multiple sclerosis.",
    "The patient underwent microvascular decompression for trigeminal neuralgia.",
    # SPECIALTY-SPECIFIC - ORTHOPEDICS
    "The X ray confirmed a displaced distal radius fracture requiring closed reduction.",
    "Arthroscopic meniscectomy performed for the complex medial meniscus tear.",
    "The patient is scheduled for reverse total shoulder arthroplasty.",
    "Intramedullary nailing of the femoral shaft fracture with successful alignment.",
    "The MRI showed complete ACL tear with associated bone bruising.",
    "Kyphoplasty performed for the painful osteoporotic vertebral compression fracture.",
    "The patient underwent carpal tunnel release with immediate symptom improvement.",
    "External fixator applied for the open tibial fracture pending soft tissue healing.",
    "Platelet rich plasma injection for the chronic lateral epicondylitis.",
    "The patient received a cortisone injection for the subacromial bursitis.",
    # SPECIALTY-SPECIFIC - GASTROENTEROLOGY
    "The capsule endoscopy revealed multiple small bowel ulcerations consistent with Crohn's disease.",
    "ERCP with sphincterotomy and stone extraction for choledocholithiasis.",
    "The patient tested positive for H. pylori, starting triple therapy.",
    "Fibroscan showed liver stiffness of fourteen kilopascals indicating significant fibrosis.",
    "The colonoscopy found a two centimeter sessile polyp requiring endoscopic mucosal resection.",
    "Infliximab induction therapy for moderate to severe ulcerative colitis.",
    "The patient underwent radiofrequency ablation for Barrett's esophagus with dysplasia.",
    "Hepatic encephalopathy managed with lactulose and rifaximin.",
    "The TIPS procedure successfully reduced the portal pressure gradient.",
    "Endoscopic variceal ligation for the bleeding esophageal varices.",
    # SPECIALTY-SPECIFIC - PULMONOLOGY
    "Bronchoscopy with bronchoalveolar lavage for suspected Pneumocystis pneumonia.",
    "The patient requires home oxygen therapy with a flow rate of two liters.",
    "Pulmonary rehabilitation program initiated for the severe COPD.",
    "The chest CT showed ground glass opacities consistent with interstitial lung disease.",
    "Endobronchial ultrasound guided biopsy of the mediastinal lymphadenopathy.",
    "The patient was started on pirfenidone for idiopathic pulmonary fibrosis.",
    "BiPAP therapy initiated for the obesity hypoventilation syndrome.",
    "Thoracoscopic talc pleurodesis for the recurrent malignant pleural effusion.",
    "The methacholine challenge test was positive, confirming asthma diagnosis.",
    "Pulmonary embolism response team activated for the massive PE.",
    # SPECIALTY-SPECIFIC - NEPHROLOGY
    "The kidney biopsy showed IgA nephropathy with moderate mesangial proliferation.",
    "The patient started hemodialysis via tunneled catheter pending fistula maturation.",
    "Continuous renal replacement therapy for the hemodynamically unstable patient.",
    "The transplant team crossmatch came back negative, proceeding with surgery.",
    "Rituximab induction for the biopsy proven membranous nephropathy.",
    "The patient's GFR has declined to fifteen, discussing transplant options.",
    "Peritoneal dialysis training initiated for the end stage renal disease.",
    "Plasma exchange for the thrombotic thrombocytopenic purpura with renal involvement.",
    "The patient developed contrast induced nephropathy requiring temporary dialysis.",
    "Tolvaptan therapy for autosomal dominant polycystic kidney disease.",
    # SPECIALTY-SPECIFIC - ENDOCRINOLOGY
    "The patient's thyroid nodule FNA showed Bethesda category five, suspicious for malignancy.",
    "Continuous glucose monitoring initiated for the brittle type one diabetes.",
    "The twenty four hour urine cortisol confirmed Cushing's syndrome.",
    "Pituitary MRI revealed a macroadenoma causing visual field defects.",
    "The patient was started on testosterone replacement for hypogonadism.",
    "Bone density scan showed T score of negative three point two, severe osteoporosis.",
    "Radioactive iodine therapy scheduled for the Graves' disease.",
    "The patient developed diabetic ketoacidosis requiring ICU admission.",
    "Somatostatin analog therapy for the growth hormone secreting adenoma.",
    "Adrenal insufficiency confirmed with cosyntropin stimulation test.",
    # SPECIALTY-SPECIFIC - INFECTIOUS DISEASE
    "Blood cultures grew methicillin resistant Staphylococcus aureus, switching to vancomycin.",
    "The patient completed directly observed therapy for drug resistant tuberculosis.",
    "Empiric treatment with ceftriaxone and azithromycin for community acquired pneumonia.",
    "The lumbar puncture confirmed cryptococcal meningitis in the HIV patient.",
    "Antiretroviral therapy initiated with bictegravir, emtricitabine, and tenofovir.",
    "The patient developed Clostridium difficile colitis requiring oral vancomycin.",
    "Negative pressure isolation for suspected pulmonary tuberculosis.",
    "Doxycycline and hydroxychloroquine for the Q fever endocarditis.",
    "The patient received post exposure prophylaxis following needlestick injury.",
    "Empiric antifungal therapy with micafungin for suspected candidemia.",
    # SPECIALTY-SPECIFIC - PSYCHIATRY
    "The patient was admitted on a seventy two hour psychiatric hold for suicidal ideation.",
    "Electroconvulsive therapy recommended for treatment resistant depression.",
    "The patient was started on clozapine for refractory schizophrenia.",
    "Lithium levels need monitoring given the new NSAID prescription.",
    "Cognitive behavioral therapy combined with sertraline for OCD.",
    "The patient experienced serotonin syndrome requiring discontinuation of the SSRI.",
    "Naltrexone initiated for alcohol use disorder maintenance.",
    "The patient completed medically supervised benzodiazepine detoxification.",
    "Dialectical behavior therapy for borderline personality disorder.",
    "Transcranial magnetic stimulation for medication resistant depression.",
    # SPECIALTY-SPECIFIC - OB/GYN
    "The patient is at thirty two weeks gestation with preeclampsia requiring magnesium.",
    "Hysteroscopic myomectomy scheduled for the symptomatic submucosal fibroid.",
    "The amniocentesis revealed trisomy twenty one, genetic counseling arranged.",
    "Cerclage placed at fourteen weeks for cervical insufficiency.",
    "The patient underwent laparoscopic salpingectomy for ectopic pregnancy.",
    "Letrozole initiated for ovulation induction in the PCOS patient.",
    "The colposcopy showed high grade cervical dysplasia requiring LEEP.",
    "Betamethasone administered for fetal lung maturity at twenty eight weeks.",
    "The patient experienced postpartum hemorrhage requiring uterine balloon tamponade.",
    "In vitro fertilization cycle initiated with gonadotropin stimulation.",
    # SPECIALTY-SPECIFIC - PEDIATRICS
    "The infant received the DTaP, IPV, Hib, and PCV13 vaccines today.",
    "Kawasaki disease diagnosed, starting IVIG and high dose aspirin.",
    "The child's asthma exacerbation required nebulized albuterol and oral steroids.",
    "Developmental screening revealed delays requiring early intervention referral.",
    "The newborn's bilirubin level requires phototherapy for hyperbilirubinemia.",
    "Pyloric stenosis confirmed on ultrasound, scheduling pyloromyotomy.",
    "The child tested positive for strep throat, starting amoxicillin.",
    "Intussusception reduced with air enema under fluoroscopic guidance.",
    "The patient was diagnosed with attention deficit hyperactivity disorder.",
    "Growth hormone therapy initiated for the child with Turner syndrome.",
]
