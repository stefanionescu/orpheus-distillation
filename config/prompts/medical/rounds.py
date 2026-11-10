"""Medical prompts of thirty to thirty-seven words about procedures and rare conditions."""

from __future__ import annotations

ROUNDS: list[str] = [
    (
        "The patient developed acute intermittent porphyria attack with severe abdominal pain, requiring hemin "
        "infusion, glucose loading, and avoidance of precipitating medications."
    ),
    (
        "The neurology team diagnosed Lambert Eaton myasthenic syndrome with positive voltage gated calcium channel "
        "antibodies, initiating 3,4-diaminopyridine and screening for small cell lung cancer."
    ),
    (
        "The patient underwent successful deep anterior lamellar keratoplasty for the corneal scar, preserving the "
        "host endothelium and reducing rejection risk."
    ),
    (
        "The hematology team initiated bispecific T cell engager therapy with blinatumomab for the relapsed B cell "
        "acute lymphoblastic leukemia after allogeneic transplant failure."
    ),
    (
        "The patient's eosinophilic esophagitis was diagnosed on esophageal biopsy showing greater than fifteen "
        "eosinophils per high power field, initiating swallowed fluticasone therapy."
    ),
    (
        "The surgical team performed total thyroidectomy with central neck dissection for the papillary thyroid "
        "carcinoma with nodal metastases, followed by radioactive iodine ablation."
    ),
    (
        "The patient developed cerebral salt wasting following subarachnoid hemorrhage, requiring aggressive sodium "
        "and fluid replacement to maintain euvolemia and prevent vasospasm."
    ),
    (
        "The interventional pulmonology team performed electromagnetic navigation bronchoscopy with biopsy of the "
        "peripheral lung nodule, confirming adenocarcinoma for staging workup."
    ),
    (
        "The patient's cold agglutinin disease was diagnosed with positive direct Coombs test and cold agglutinin "
        "titer, initiating rituximab for the symptomatic hemolytic anemia."
    ),
    (
        "The cardiac surgery team performed surgical ventricular restoration for the ischemic cardiomyopathy with "
        "large anterior aneurysm, achieving improved ejection fraction post operatively."
    ),
    (
        "The patient underwent successful limbal stem cell transplant for the severe ocular surface disease from "
        "chemical burn, with epithelial healing and vision improvement."
    ),
    (
        "The oncology team initiated entrectinib for the ROS1 rearranged non small cell lung cancer with brain "
        "metastases, achieving intracranial and systemic disease control."
    ),
    (
        "The patient's stiff person syndrome was diagnosed with positive anti GAD antibodies and characteristic EMG "
        "findings, initiating diazepam and IVIG with physical therapy."
    ),
    (
        "The transplant team performed ABO incompatible kidney transplant after desensitization with plasmapheresis "
        "and rituximab, achieving good graft function with protocol surveillance biopsies."
    ),
    (
        "The patient developed posterior circulation stroke from vertebral artery dissection, requiring "
        "anticoagulation and close monitoring for extension or recurrence."
    ),
    (
        "The surgical team performed laparoscopic splenectomy for the hereditary spherocytosis with severe hemolytic "
        "anemia, with preoperative vaccination and post splenectomy antibiotic prophylaxis."
    ),
    (
        "The patient's neuromyelitis optica spectrum disorder was diagnosed with positive aquaporin 4 antibodies, "
        "initiating eculizumab for attack prevention and relapse reduction."
    ),
    (
        "The interventional cardiology team performed left atrial appendage occlusion with the Watchman device for "
        "atrial fibrillation with contraindication to long term anticoagulation."
    ),
    (
        "The patient underwent successful multivisceral transplant including stomach, small bowel, and liver for the "
        "diffuse intestinal ganglioneuromatosis with liver failure."
    ),
    (
        "The rheumatology team diagnosed eosinophilic granulomatosis with polyangiitis with asthma, eosinophilia, and "
        "mononeuritis multiplex, initiating high dose corticosteroids and mepolizumab."
    ),
    (
        "The patient developed thrombotic storm with multiple arterial and venous thromboses, requiring therapeutic "
        "anticoagulation, aspirin, and evaluation for underlying malignancy."
    ),
    (
        "The surgical oncology team performed total pelvic exenteration for the recurrent cervical cancer involving "
        "bladder and rectum, with ileal conduit and colostomy creation."
    ),
    (
        "The patient's Langerhans cell histiocytosis was diagnosed on skin biopsy showing CD1a positive cells, "
        "initiating vinblastine and prednisone for the multisystem disease."
    ),
    (
        "The neurosurgery team performed corpus callosotomy for the medically refractory drop attacks from Lennox "
        "Gastaut syndrome, achieving significant reduction in atonic seizures."
    ),
    (
        "The patient developed catastrophic antiphospholipid syndrome with multiorgan failure, requiring "
        "anticoagulation, plasma exchange, corticosteroids, and IVIG in the intensive care unit."
    ),
    (
        "The cardiac surgery team performed the arterial switch operation for the neonate with transposition of the "
        "great arteries, achieving successful coronary transfer."
    ),
    (
        "The patient's chronic inflammatory demyelinating polyneuropathy was diagnosed with nerve conduction studies "
        "and CSF albuminocytologic dissociation, initiating IVIG therapy."
    ),
    (
        "The interventional radiology team performed portal vein embolization to induce contralateral liver "
        "hypertrophy before major hepatectomy for the colorectal liver metastases."
    ),
    (
        "The patient underwent successful face transplant for the severe facial disfigurement from trauma, requiring "
        "lifelong immunosuppression and extensive rehabilitation."
    ),
    (
        "The oncology team initiated lorlatinib for the ALK rearranged non small cell lung cancer with progression on "
        "second generation ALK inhibitor and CNS involvement."
    ),
    (
        "The patient's hemolytic uremic syndrome was diagnosed with microangiopathic hemolytic anemia, "
        "thrombocytopenia, and acute kidney injury, initiating eculizumab for atypical HUS."
    ),
    (
        "The surgical team performed total artificial heart implantation as bridge to transplant for the patient with "
        "biventricular failure not suitable for LVAD alone."
    ),
    (
        "The patient developed acute graft versus host disease of the gut following allogeneic transplant, requiring "
        "high dose steroids and ruxolitinib for steroid refractory disease."
    ),
    (
        "The neurology team diagnosed superficial siderosis with progressive hearing loss and ataxia, identifying "
        "dural defect on imaging and planning surgical repair."
    ),
    (
        "The patient underwent successful hand transplant for the bilateral hand amputation, requiring lifelong "
        "immunosuppression and intensive occupational therapy for functional recovery."
    ),
    (
        "The hematology team initiated gene therapy with betibeglogene autotemcel for the transfusion dependent beta "
        "thalassemia, achieving transfusion independence post treatment."
    ),
    (
        "The patient's Whipple disease was diagnosed on small bowel biopsy with PAS positive macrophages, initiating "
        "prolonged antibiotic therapy with ceftriaxone followed by trimethoprim sulfamethoxazole."
    ),
    (
        "The cardiac surgery team performed the Fontan procedure for the single ventricle physiology, completing the "
        "staged palliation with total cavopulmonary connection."
    ),
    (
        "The patient developed progressive multifocal leukoencephalopathy on natalizumab, requiring drug cessation, "
        "plasma exchange, and immune reconstitution inflammatory syndrome management."
    ),
    (
        "The surgical team performed ex vivo liver resection and autotransplantation for the complex hepatic alveolar "
        "echinococcosis involving all hepatic veins and the IVC."
    ),
    (
        "The patient's POEMS syndrome was diagnosed with polyneuropathy, organomegaly, endocrinopathy, M protein, and "
        "skin changes, initiating autologous stem cell transplant."
    ),
    (
        "The interventional neuroradiology team performed Wada test to lateralize language and memory function before "
        "temporal lobectomy for the medically refractory temporal lobe epilepsy."
    ),
    (
        "The patient underwent successful uterus transplant for the absolute uterine factor infertility, with embryo "
        "transfer planned after graft stabilization and optimization."
    ),
    (
        "The oncology team initiated trastuzumab deruxtecan for the HER2 low metastatic breast cancer progressing on "
        "prior therapies, achieving significant tumor response."
    ),
    (
        "The patient's hereditary transthyretin amyloidosis was diagnosed with genetic testing confirming val 30 met "
        "mutation, initiating patisiran RNA interference therapy."
    ),
    (
        "The surgical team performed simultaneous liver kidney transplant for the primary hyperoxaluria type one with "
        "end stage renal disease and hepatic oxalate overproduction."
    ),
    (
        "The patient developed immune effector cell associated neurotoxicity syndrome following CAR T cell therapy, "
        "requiring tocilizumab and dexamethasone with close neurologic monitoring."
    ),
    (
        "The neurosurgery team performed responsive neurostimulation device implantation for the medically refractory "
        "focal epilepsy with seizure onset in eloquent cortex."
    ),
]
