"""Medical prompts of thirty to thirty-seven words about clinical cases."""

from __future__ import annotations

CASES: list[str] = [
    # ADDITIONAL LONG PROMPTS (30-37 WORDS)
    (
        "The patient presented with sudden onset of the worst headache of their life, and CT angiography confirmed a "
        "ruptured anterior communicating artery aneurysm requiring emergent coiling."
    ),
    (
        "Following the bone marrow transplant, the patient developed graft versus host disease affecting the skin, "
        "liver, and gastrointestinal tract, requiring high dose corticosteroids and tacrolimus."
    ),
    (
        "The multidisciplinary wound care team recommended negative pressure wound therapy for the complex diabetic "
        "foot ulcer with exposed tendon and signs of osteomyelitis."
    ),
    (
        "The patient's pulmonary hypertension has progressed despite dual oral therapy, and we're considering adding "
        "subcutaneous treprostinil or transitioning to intravenous epoprostenol."
    ),
    (
        "The transplant hepatologist recommended listing for liver transplantation given the hepatocellular carcinoma "
        "within Milan criteria and the underlying decompensated cirrhosis from hepatitis C."
    ),
    (
        "The pain management team performed a stellate ganglion block for the complex regional pain syndrome affecting "
        "the upper extremity with significant improvement in symptoms."
    ),
    (
        "The patient underwent successful endoscopic third ventriculostomy as an alternative to ventriculoperitoneal "
        "shunt placement for the obstructive hydrocephalus from aqueductal stenosis."
    ),
    (
        "The cystic fibrosis team initiated elexacaftor tezacaftor ivacaftor triple therapy, resulting in significant "
        "improvement in FEV1 and reduction in pulmonary exacerbations."
    ),
    (
        "The patient's refractory epilepsy is being evaluated for surgical management, with stereo EEG planned to "
        "localize the seizure onset zone before resection."
    ),
    (
        "The dermatology team diagnosed pemphigus vulgaris based on skin biopsy with direct immunofluorescence, "
        "initiating rituximab given the severity and extent of involvement."
    ),
    (
        "The patient developed tumor lysis syndrome following initiation of chemotherapy, requiring aggressive "
        "hydration, rasburicase, and temporary dialysis for the hyperuricemia and hyperkalemia."
    ),
    (
        "The interventional pulmonology team performed rigid bronchoscopy with mechanical debulking and stent "
        "placement for the malignant central airway obstruction causing respiratory failure."
    ),
    (
        "The patient's amyloidosis was confirmed as AL type on bone marrow biopsy, and the hematology team is planning "
        "daratumumab based chemotherapy followed by autologous stem cell transplant."
    ),
    (
        "The obstetric team managed the placenta accreta spectrum disorder with planned cesarean hysterectomy at "
        "thirty four weeks with interventional radiology on standby for balloon occlusion."
    ),
    (
        "The patient underwent successful Mohs micrographic surgery for the recurrent basal cell carcinoma on the nose "
        "with clear margins and subsequent reconstruction."
    ),
    (
        "The rheumatology team diagnosed antiphospholipid syndrome following the recurrent pregnancy losses and "
        "arterial thrombosis, initiating lifelong anticoagulation with warfarin."
    ),
    (
        "The patient's myasthenia gravis crisis required plasmapheresis, intravenous immunoglobulin, and temporary "
        "mechanical ventilation before stabilization and thymectomy planning."
    ),
    (
        "The pediatric surgery team performed laparoscopic Nissen fundoplication for the severe gastroesophageal "
        "reflux disease refractory to maximum medical therapy in the infant."
    ),
    (
        "The patient developed posterior reversible encephalopathy syndrome in the setting of severe hypertension, "
        "requiring aggressive blood pressure control and seizure prophylaxis."
    ),
    (
        "The colorectal surgery team performed total proctocolectomy with ileal pouch anal anastomosis for the "
        "ulcerative colitis refractory to biologic therapy."
    ),
    (
        "The patient's hereditary hemochromatosis was diagnosed after elevated transferrin saturation and ferritin, "
        "with HFE gene testing confirming C282Y homozygosity requiring phlebotomy."
    ),
    (
        "The ophthalmology team performed intravitreal anti VEGF injection with bevacizumab for the diabetic macular "
        "edema with significant improvement in visual acuity."
    ),
    (
        "The patient underwent cochlear implantation for the profound bilateral sensorineural hearing loss with "
        "successful activation and speech therapy initiation."
    ),
    (
        "The allergy team performed oral food challenge confirming peanut allergy, and the patient was started on "
        "peanut oral immunotherapy desensitization protocol."
    ),
    (
        "The sports medicine team diagnosed a stress fracture of the fifth metatarsal, recommending non weight bearing "
        "and bone stimulator therapy given the high risk location."
    ),
    (
        "The patient's paroxysmal nocturnal hemoglobinuria was treated with eculizumab, a complement inhibitor, with "
        "significant reduction in hemolysis and transfusion requirements."
    ),
    (
        "The otolaryngology team performed endoscopic sinus surgery with septoplasty and turbinate reduction for the "
        "chronic rhinosinusitis refractory to medical management."
    ),
    (
        "The patient developed immune thrombocytopenic purpura, and after failing corticosteroids and IVIG, underwent "
        "laparoscopic splenectomy with platelet count normalization."
    ),
    (
        "The plastic surgery team performed free flap reconstruction using the anterolateral thigh flap for the "
        "complex lower extremity defect following tumor resection."
    ),
    (
        "The patient's achalasia was treated with peroral endoscopic myotomy, with significant improvement in "
        "dysphagia symptoms and esophageal emptying on follow up studies."
    ),
    # MORE LONG PROMPTS (30-37 WORDS) - 125 MORE TO REACH 150 TOTAL
    (
        "The seventy four year old woman with a history of atrial fibrillation and chronic kidney disease stage four "
        "presented with melena and hemodynamic instability requiring emergent upper endoscopy and transfusion."
    ),
    (
        "The trauma surgery team performed damage control laparotomy with temporary abdominal closure for the grade "
        "five liver laceration, planning definitive repair after resuscitation and coagulopathy correction."
    ),
    (
        "The patient's severe aortic stenosis with syncope and heart failure symptoms meets criteria for urgent "
        "surgical aortic valve replacement given the prohibitive surgical risk score."
    ),
    (
        "The neurology team initiated natalizumab infusion for the aggressive relapsing remitting multiple sclerosis "
        "after discussion of the JC virus risk and PML monitoring protocol."
    ),
    (
        "The patient underwent successful liver kidney transplant for the combined hepatorenal syndrome secondary to "
        "autosomal dominant polycystic kidney and liver disease with good early graft function."
    ),
    (
        "The cardiology team performed alcohol septal ablation for the symptomatic hypertrophic obstructive "
        "cardiomyopathy with significant gradient reduction and improvement in exercise tolerance post procedure."
    ),
    (
        "The patient's refractory chronic lymphocytic leukemia is being treated with venetoclax and obinutuzumab "
        "combination therapy following progression on ibrutinib and multiple prior lines."
    ),
    (
        "The surgical oncology team performed cytoreductive surgery with hyperthermic intraperitoneal chemotherapy "
        "using mitomycin C for the appendiceal mucinous neoplasm with peritoneal dissemination."
    ),
    (
        "The patient developed immune checkpoint inhibitor induced pneumonitis on pembrolizumab, requiring high dose "
        "corticosteroids, temporary immunotherapy hold, and pulmonology co management for recovery."
    ),
    (
        "The interventional neuroradiology team performed successful flow diversion with the Pipeline embolization "
        "device for the giant unruptured internal carotid artery aneurysm."
    ),
    (
        "The patient's Addison's disease was confirmed with low morning cortisol and elevated ACTH, requiring lifelong "
        "glucocorticoid and mineralocorticoid replacement therapy with stress dosing education."
    ),
    (
        "The bariatric surgery team performed sleeve gastrectomy for the morbidly obese patient with BMI of fifty two "
        "and multiple obesity related comorbidities including type two diabetes."
    ),
    (
        "The patient underwent successful bilateral lung transplantation for end stage idiopathic pulmonary fibrosis "
        "with good early graft function and initiation of tacrolimus based immunosuppression."
    ),
    (
        "The neuro oncology team recommended temozolomide and radiation therapy following maximal safe resection of "
        "the IDH mutant, MGMT methylated glioblastoma with plan for tumor treating fields."
    ),
    (
        "The patient's severe combined immunodeficiency was diagnosed on newborn screening, and the immunology team is "
        "planning haploidentical stem cell transplant from the mother."
    ),
    (
        "The cardiac surgery team performed the Ross procedure for the young patient with severe aortic regurgitation, "
        "using the pulmonary autograft to avoid lifelong anticoagulation."
    ),
    (
        "The patient developed acute cellular rejection of the transplanted heart on routine endomyocardial biopsy, "
        "requiring pulse dose methylprednisolone and adjustment of maintenance immunosuppression."
    ),
    (
        "The hepatology team initiated sofosbuvir velpatasvir combination therapy for the genotype three hepatitis C "
        "infection, achieving sustained virologic response at twelve weeks post treatment."
    ),
    (
        "The patient underwent successful transcatheter mitral valve repair with the MitraClip device for severe "
        "functional mitral regurgitation with improvement in heart failure symptoms."
    ),
    (
        "The pediatric oncology team initiated vincristine, dactinomycin, and cyclophosphamide chemotherapy for the "
        "newly diagnosed Wilms tumor following nephrectomy with favorable histology."
    ),
]
