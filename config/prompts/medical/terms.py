"""Medical prompts: short terms, treatments, procedures, questions, and exclamations, then clinical statements."""

from __future__ import annotations

TERMS: list[str] = [
    # ULTRA SHORT - MEDICAL TERMS & REACTIONS
    "Stat!",
    "Code blue!",
    "Clear!",
    "Vitals stable.",
    "BP dropping!",
    "Pulse thready.",
    "Intubate now!",
    "Administer epinephrine!",
    "Suction ready.",
    "Scalpel.",
    "Clamp.",
    "Retractor.",
    "Sutures.",
    "Gauze.",
    "Saline.",
    "Morphine drip.",
    "CT scan ordered.",
    "MRI scheduled.",
    "Labs pending.",
    "Biopsy results.",
    "Negative for malignancy.",
    "Benign tumor.",
    "Malignant cells detected.",
    "Metastasis confirmed.",
    "Remission achieved.",
    "Discharge tomorrow.",
    "NPO after midnight.",
    "Allergic to penicillin.",
    "DNR on file.",
    "Consent signed.",
    # SHORT STATEMENTS - MEDICATIONS & TREATMENTS
    "The patient is on metformin for type two diabetes management.",
    "Administer fifty milligrams of Benadryl for the allergic reaction.",
    "She's been taking lisinopril for hypertension for three years.",
    "The oncologist prescribed Keytruda for the immunotherapy protocol.",
    "We're starting him on Humira for the rheumatoid arthritis.",
    "The Pfizer BioNTech vaccine requires two doses twenty one days apart.",
    "Moderna's mRNA technology revolutionized vaccine development.",
    "Ozempic has shown remarkable results for weight management.",
    "The patient responded well to the Remicade infusion.",
    "Prednisone taper starting at sixty milligrams daily.",
    "Gabapentin three hundred milligrams three times daily for neuropathy.",
    "Xarelto twenty milligrams once daily for anticoagulation.",
    "Lantus insulin forty units at bedtime.",
    "Advair diskus one puff twice daily for COPD.",
    "Synthroid one hundred micrograms every morning on empty stomach.",
    "Zoloft fifty milligrams for generalized anxiety disorder.",
    "Lexapro ten milligrams for major depressive disorder.",
    "Adderall XR twenty milligrams for attention deficit hyperactivity disorder.",
    "Suboxone for opioid use disorder maintenance therapy.",
    "Narcan nasal spray for opioid overdose reversal.",
    "Tamiflu within forty eight hours of influenza symptom onset.",
    "Paxlovid for high risk COVID nineteen patients.",
    "Augmentin for the bacterial sinus infection.",
    "Cipro five hundred milligrams twice daily for UTI.",
    "Diflucan one hundred fifty milligrams single dose for yeast infection.",
    "Valtrex for herpes simplex outbreak suppression.",
    "Truvada for HIV pre exposure prophylaxis.",
    "Harvoni cured her hepatitis C in twelve weeks.",
    "Eliquis five milligrams twice daily post atrial fibrillation diagnosis.",
    "Jardiance for heart failure with reduced ejection fraction.",
    # SHORT STATEMENTS - PROCEDURES & SURGERIES
    "The laparoscopic cholecystectomy went smoothly with minimal blood loss.",
    "We're scheduling the total knee replacement for next Thursday.",
    "The cardiac catheterization revealed a ninety percent blockage.",
    "Robotic assisted prostatectomy offers faster recovery times.",
    "The appendectomy was performed emergently at two AM.",
    "Endoscopic retrograde cholangiopancreatography showed common bile duct stones.",
    "The colonoscopy revealed three polyps requiring removal.",
    "Upper GI endoscopy confirmed Barrett's esophagus.",
    "Lumbar puncture results showed elevated protein levels.",
    "Bone marrow biopsy confirmed acute myeloid leukemia.",
    "The thoracentesis drained two liters of pleural fluid.",
    "Paracentesis relieved the ascites pressure significantly.",
    "Central line placement in the right internal jugular.",
    "Arterial line for continuous blood pressure monitoring.",
    "Foley catheter inserted for accurate urine output measurement.",
    "Chest tube placed for pneumothorax decompression.",
    "Tracheostomy performed for prolonged mechanical ventilation.",
    "Percutaneous gastrostomy tube for long term feeding.",
    "Dialysis catheter placement for acute kidney injury.",
    "Port a cath insertion for chemotherapy administration.",
    # SHORT QUESTIONS
    "What's the patient's current pain level on a scale of one to ten?",
    "Has she had any previous surgeries or hospitalizations?",
    "Is there a family history of heart disease or cancer?",
    "When did the symptoms first begin?",
    "Are you allergic to any medications or latex?",
    "Have you been vaccinated against hepatitis B?",
    "Did you take your morning medications today?",
    "Is the patient oriented to person, place, and time?",
    "What's the Glasgow Coma Scale score?",
    "Can you rate your shortness of breath?",
    "Have you noticed any blood in your stool?",
    "When was your last menstrual period?",
    "Is there any chance you could be pregnant?",
    "Do you smoke cigarettes or use tobacco products?",
    "How many alcoholic drinks do you consume per week?",
    "Have you traveled internationally in the past month?",
    "Are you currently taking any blood thinners?",
    "Did the antibiotic course resolve the infection?",
    "Has the swelling decreased since starting the steroids?",
    "When was your last tetanus booster?",
    # SHORT EXCLAMATIONS
    "We need a crash cart in room three twelve immediately!",
    "The patient is coding, start chest compressions now!",
    "Blood pressure is dropping rapidly, push fluids!",
    "She's going into anaphylactic shock!",
    "The wound is hemorrhaging, apply direct pressure!",
    "Oxygen saturation is falling, increase the FiO2!",
    "He's having a grand mal seizure!",
    "The airway is compromised, prepare for intubation!",
    "Sepsis protocol initiated, draw blood cultures stat!",
    "The stroke team has been activated!",
    "Massive transfusion protocol in effect!",
    "The trauma bay is ready for incoming!",
    "STEMI alert, cath lab is standing by!",
    "The baby's heart rate is decelerating!",
    "Placental abruption suspected, prepare for emergency C section!",
    # MEDIUM STATEMENTS - DIAGNOSES & CONDITIONS
    "The echocardiogram revealed moderate mitral regurgitation with an ejection fraction of forty five percent.",
    "Imaging confirmed a herniated disc at L4 L5 with nerve root impingement causing radiculopathy.",
    "The patient presents with classic symptoms of Guillain Barré syndrome following a viral infection.",
    "Rheumatoid factor and anti CCP antibodies are both elevated, consistent with rheumatoid arthritis.",
    "The skin biopsy confirmed psoriasis vulgaris with characteristic Munro microabscesses.",
    "Thyroid function tests indicate Hashimoto's thyroiditis with elevated TSH and low free T4.",
    "The lumbar MRI shows spinal stenosis at multiple levels requiring surgical decompression.",
    "Pulmonary function tests reveal severe obstructive pattern consistent with emphysema.",
    "The angiogram demonstrated triple vessel coronary artery disease requiring bypass surgery.",
    "Genetic testing confirmed BRCA1 mutation, increasing breast and ovarian cancer risk significantly.",
    "The sleep study diagnosed severe obstructive sleep apnea with an AHI of forty two.",
    "Electromyography confirmed carpal tunnel syndrome with moderate axonal loss.",
    "The PET scan showed metabolically active lymph nodes consistent with lymphoma.",
    "Cerebrospinal fluid analysis revealed oligoclonal bands suggestive of multiple sclerosis.",
    "The patient meets diagnostic criteria for systemic lupus erythematosus with positive ANA.",
    "Hemoglobin A1C of nine point two indicates poorly controlled diabetes mellitus.",
    "Troponin levels are markedly elevated, confirming acute myocardial infarction.",
    "D dimer is positive, CT angiography confirmed bilateral pulmonary emboli.",
    "The pathology report shows invasive ductal carcinoma, estrogen receptor positive.",
    "Creatinine has doubled, indicating acute kidney injury stage two.",
    # MEDIUM QUESTIONS
    "Should we add metoprolol to the regimen given the persistent tachycardia and hypertension?",
    "Would you recommend starting anticoagulation given the CHADS VASc score of four?",
    "Is the patient a candidate for thrombolytic therapy given the time of symptom onset?",
    "Should we consult interventional radiology for the hepatic abscess drainage?",
    "Would biologic therapy be appropriate given the failure of conventional DMARDs?",
    "Is hospice care something the family has considered given the prognosis?",
    "Should we obtain a psychiatric consultation for the suicidal ideation?",
    "Would you recommend surgical versus conservative management for this fracture?",
    "Is the patient stable enough for transfer to a step down unit?",
    "Should we continue aggressive treatment or transition to comfort care?",
    "Would a second opinion from a tertiary center be beneficial?",
    "Is there a role for radiation therapy in this case?",
    "Should we add vancomycin to cover for MRSA given the clinical picture?",
    "Would you recommend genetic counseling for the family?",
    "Is the patient appropriate for clinical trial enrollment?",
    # MEDIUM EXCLAMATIONS
    "The lactate is fourteen, we need to address the septic shock immediately!",
    "Potassium is seven point two, get calcium gluconate and prepare for dialysis!",
    "The INR is eight, hold all anticoagulation and give vitamin K!",
    "Blood glucose is twenty eight, push D50 and recheck in fifteen minutes!",
    "The patient pulled out the endotracheal tube, we need to reintubate now!",
    "Chest X ray shows complete whiteout, tension pneumothorax suspected!",
    "The surgical site is dehiscing, we need to return to the OR!",
    "Massive hematemesis, activate the GI bleed protocol immediately!",
    "The graft is failing, vascular surgery needs to see this now!",
    "Compartment syndrome developing, fasciotomy needs to happen within the hour!",
    "The shunt is malfunctioning, neurosurgery consult stat!",
    "Necrotizing fasciitis suspected, broad spectrum antibiotics and surgical debridement!",
    "The patient is in DIC, transfuse platelets, FFP, and cryoprecipitate!",
    "Malignant hyperthermia protocol, stop all triggering agents and give dantrolene!",
    "Thyroid storm, give propylthiouracil, propranolol, and hydrocortisone!",
    # LONG STATEMENTS - CLINICAL SCENARIOS (30-37 WORDS)
    (
        "The sixty seven year old male with a history of coronary artery disease, hypertension, and type two diabetes "
        "presented to the emergency department with crushing substernal chest pain radiating to the left arm."
    ),
    (
        "Following the motor vehicle accident, the trauma team performed a FAST exam which revealed free fluid in "
        "Morrison's pouch, prompting emergent exploratory laparotomy for suspected splenic laceration."
    ),
    (
        "The patient underwent successful transcatheter aortic valve replacement using the Edwards SAPIEN valve, with "
        "post procedure echocardiography showing no paravalvular leak and normal valve gradients."
    ),
    (
        "The multidisciplinary tumor board recommended neoadjuvant chemotherapy with FOLFOX regimen followed by "
        "surgical resection and adjuvant radiation for the stage three rectal adenocarcinoma."
    ),
    (
        "The infectious disease team recommended a six week course of intravenous ceftriaxone for the confirmed case "
        "of Lyme neuroborreliosis with facial nerve palsy and lymphocytic meningitis."
    ),
    (
        "Post operative day two following the Whipple procedure, the patient developed a pancreatic fistula requiring "
        "percutaneous drain placement and total parenteral nutrition initiation."
    ),
    (
        "The neonatal intensive care unit admitted the twenty eight week premature infant with respiratory distress "
        "syndrome requiring surfactant administration and high frequency oscillatory ventilation support."
    ),
    (
        "The stroke neurologist recommended tissue plasminogen activator administration given the patient's "
        "presentation within the four and a half hour window and absence of contraindications."
    ),
    (
        "The rheumatology consultation suggested initiating tocilizumab after inadequate response to methotrexate and "
        "sulfasalazine combination therapy for the erosive rheumatoid arthritis."
    ),
    (
        "The patient's refractory status epilepticus required continuous electroencephalography monitoring, midazolam "
        "infusion titration, and eventual burst suppression to achieve seizure control."
    ),
    (
        "The cardiothoracic surgery team performed a minimally invasive mitral valve repair using the da Vinci robotic "
        "system with excellent visualization and reduced recovery time."
    ),
    (
        "The hematology oncology team initiated induction chemotherapy with cytarabine and daunorubicin for the newly "
        "diagnosed acute myeloid leukemia with favorable cytogenetics."
    ),
    (
        "The interventional radiology department performed successful transjugular intrahepatic portosystemic shunt "
        "placement for refractory ascites in the setting of decompensated cirrhosis."
    ),
    (
        "The patient required extracorporeal membrane oxygenation support following massive pulmonary embolism with "
        "hemodynamic collapse despite systemic thrombolysis with alteplase."
    ),
    (
        "The orthopedic trauma service performed open reduction internal fixation of the comminuted tibial plateau "
        "fracture using locking plates and bone graft augmentation."
    ),
    (
        "The gastroenterology team performed endoscopic ultrasound guided fine needle aspiration of the pancreatic "
        "mass, with cytology revealing adenocarcinoma requiring oncologic staging."
    ),
    (
        "The maternal fetal medicine specialist recommended cervical cerclage placement at fourteen weeks gestation "
        "given the history of cervical insufficiency and previous preterm delivery."
    ),
    (
        "The neurosurgery team performed awake craniotomy with intraoperative mapping for resection of the left "
        "temporal glioma near eloquent cortex to preserve language function."
    ),
    (
        "The patient developed hospital acquired pneumonia requiring escalation to piperacillin tazobactam and "
        "vancomycin pending culture results and infectious disease consultation."
    ),
    (
        "The palliative care team facilitated a family meeting to discuss goals of care and transition to comfort "
        "focused measures given the terminal diagnosis."
    ),
    (
        "The electrophysiology lab performed successful catheter ablation for atrial fibrillation using cryoballoon "
        "technology with pulmonary vein isolation confirmed by entrance block."
    ),
    (
        "The vascular surgery team performed endovascular aneurysm repair of the infrarenal abdominal aortic aneurysm "
        "using a bifurcated stent graft with successful exclusion."
    ),
    (
        "The patient underwent total laryngectomy with bilateral neck dissection for advanced laryngeal squamous cell "
        "carcinoma, requiring permanent tracheostomy and voice rehabilitation."
    ),
    (
        "The pediatric intensive care unit managed the child with diabetic ketoacidosis using the two bag insulin "
        "infusion protocol with careful monitoring for cerebral edema."
    ),
    (
        "The interventional cardiology team performed percutaneous coronary intervention with drug eluting stent "
        "placement to the proximal left anterior descending artery with TIMI three flow."
    ),
    (
        "The urology team performed robot assisted radical prostatectomy with bilateral nerve sparing technique for "
        "the Gleason seven prostate adenocarcinoma with negative surgical margins."
    ),
    (
        "The hepatobiliary surgery team performed living donor liver transplantation using the right lobe graft with "
        "successful portal vein and hepatic artery anastomosis."
    ),
    (
        "The spine surgery team performed anterior cervical discectomy and fusion at C5 C6 and C6 C7 using allograft "
        "and anterior plate fixation for cervical myelopathy."
    ),
    (
        "The patient's acute respiratory distress syndrome required prone positioning, neuromuscular blockade with "
        "cisatracurium, and lung protective ventilation with low tidal volumes."
    ),
    (
        "The burn unit managed the thirty five percent total body surface area burn with early excision, split "
        "thickness skin grafting, and aggressive fluid resuscitation."
    ),
]
