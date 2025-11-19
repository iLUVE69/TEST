'business_tax_return': {
                'keywords': ['form 1120', 'corporation income tax', 'business tax return', 'c-corp tax return', 's-corp tax return', 'form 1120s', '1120', 'btr'],
                'ai_prompt': 'Extract tax year and business name and extract the Business activity code number from the document',
                'format_template': 'BTR{tax_year}.{ext}',
                'required_fields': ['tax_year','business_name','Business_activity_code_number'],
                'priority': 10,
                'category': 'Tax Documents',
                'supported_types': ['pdf', 'jpg', 'tiff', 'tif'],
                'year_context': 'tax year, for the year ending, calendar year'
            },
            'Allonge': {
                'keywords': ['Allonge', 'Pay to the order', 'Attached to that certain', 'ALLONGE','Executed By'],
                'ai_prompt': 'Extract the recipient name and the provided name from the Allonge document',
                'format_template': 'Allonge_{Provider_Name}to{Recipient_Name}.{ext}',
                'required_fields': ['Recipient_Name','Provider_Name'],
                'priority': 10,
                'category': 'Allonge',
                'supported_types': ['pdf', 'jpg', 'tiff', 'tif'],
                'year_context': 'tax year, for the year ending, calendar year'
            },
            'Assignment of Leases and Rents': {
                'keywords': ['Assignment of leases and rents', 'ALR'],
                'ai_prompt': 'Extract the ASSIGNOR name and the ASSIGNEE name from the PARTIES Section in the document',
                'format_template': 'ALR_{ASSIGNOR_Name} to {ASSIGNEE_Name} - Recorded.{ext}',
                'required_fields': ['Assignor_Name','Assignee_Name'],
                'priority': 10,
                'category': 'ALR',
                'supported_types': ['pdf', 'jpg', 'tiff', 'tif'],
                'year_context': 'created date'
            },
            'Mortgage & Security Instrument': {
                'keywords': ['Mortgage', 'Mortgage Loan Agreement', 'Recorded', 'MORTGAGE','Recording and endorsement cover page'],
                'ai_prompt': '',
                'format_template': 'Mortgage - Recorded.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Mortgage',
                'supported_types': ['pdf', 'jpg', 'tiff', 'tif'],
                'year_context': 'created date'
            },
            'Promissory Note': {
                'keywords': ['Note', 'Mortgage Note', 'Prepayment', 'Promissory Note'],
                'ai_prompt': '',
                'format_template': 'Promissory Note.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Promissory Note',
                'supported_types': ['pdf', 'jpg', 'tiff', 'tif'],
                'year_context': 'created date'
            },
            'Title Policy - Final': {
                'keywords': ['Title Policy', 'Final Loan Policy', 'Loan Policy', 'Alta Policy Of Title Insurance', 'Alta Loan Policy'],
                'ai_prompt': '',
                'format_template': 'Title Policy.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Title Policy',
                'supported_types': ['pdf', 'jpg', 'tiff', 'tif'],
                'year_context': 'created date'
            },
            'personal_tax_return': {
                'keywords': ['form 1040', 'individual income tax', 'personal tax return', 'joint return', 'married filing jointly', '1040', 'ptr', 'U.S. Individual Income Tax Return'],
                'ai_prompt': 'Extract tax year',
                'format_template': 'PTR{tax_year}.{ext}',
                'required_fields': ['tax_year'],
                'priority': 10,
                'category': 'Tax Documents',
                'year_context': 'tax year, for the year ending, calendar year'
            },
            'tax_transcripts': {
                'keywords': ['tax transcript', 'irs transcript', 'tax record transcript', 'irs', 'internal revenue service'],
                'ai_prompt': 'Extract tax year and form type for tax transcript',
                'format_template': 'TaxTranscripts{tax_year}.{ext}',
                'required_fields': ['tax_year'],
                'priority': 10,
                'category': 'Tax Documents',
                'year_context': 'tax year, transcript year, record year'
            },
            'form_8821': {
                'keywords': ['form 8821', '8821', 'tax information authorization'],
                'ai_prompt': 'Extract the year and taxpayer name for Form 8821',
                'format_template': '8821.{ext}',
                'required_fields': ['Extract_year','Taxpayer_Name'],
                'priority': 10,
                'category': 'Tax Documents',
                'year_context': 'authorization year, form year'
            },
            '8821 Consent': {
                'keywords': ['IRS Form 8821', '8821', 'acknowledge, agree, and consent','IRS Form 4506-C or 8821'],
                'ai_prompt': 'Extract year',
                'format_template': '2202.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Tax Documents',
                'year_context': 'authorization year, form year'
            },
           'Tax Guard Liability': {
                'keywords': ['CLIENT NAME', 'TOTAL LIABILITY', 'INSTALLMENT AGREEMENT','UNFILED RETURNS'],
                'ai_prompt': 'Extract the date and total liability for Tax Guard Liability Report',
                'format_template': 'Tax Guard Liability Report_{date}.{ext}',
                'required_fields': ['date'],
                'priority': 10,
                'category': 'Tax Documents',
                'year_context': 'authorization year, form year'
            },

            # Loan Application Documents
            'terms_conditions': {
                'keywords': ['terms & conditions', 'terms and conditions', 'sba terms & conditions', 'sba terms and conditions', 't&c', 'sba terms'],
                'ai_prompt': 'Identify SBA Terms & Conditions document',
                'format_template': 'Terms & Conditions.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Application',
                'year_context': 'document date, effective date'
            },
            'terms_conditions_memo': {
                'keywords': ['terms & conditions memo', 'terms and conditions memo', 'sba terms & conditions memo', 't&c memo'],
                'ai_prompt': 'Identify SBA Terms & Conditions Memo',
                'format_template': 'Terms & Conditions Memo.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Application',
                'year_context': 'memo date, document date'
            },
            'lenders_loan_application': {
                'keywords': ['lenders loan application', 'downloaded from lender ai'],
                'ai_prompt': 'Identify Lenders Loan Application',
                'format_template': 'Application.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Application',
                'year_context': 'application date, submission date'
            },
            'form_1919': {
                'keywords': ['sba form 1919', '1919', '1919 - section i', '1919 - section ii', 'borrower information form'],
                'ai_prompt': 'Identify SBA Form 1919 and any section numbers',
                'format_template': '1919.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Application',
                'year_context': 'form date, submission date'
            },
            'form_1919_additional': {
                'keywords': ['sba 1919 additional', 'affiliate list', 'sba 1919 affiliate list', 'sba 1919 addendum a', '1919 addendum'],
                'ai_prompt': 'Identify SBA Form 1919 supporting documentation',
                'format_template': '1919 Supporting Documentation.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Application',
                'year_context': 'form date, addendum date'
            },
            'credit_memo': {
                'keywords': ['credit memo', 'cm', 'large balance credit memo', 'large balance cm'],
                'ai_prompt': 'identify credit memo',
                'format_template': 'Credit Memo.{ext}',
                'required_fields': [],
                'priority': 9,
                'category': 'Loan Application',
                'year_context': 'memo date, analysis date'
            },
            'credit_memo_amendment': {
                'keywords': ['credit memo amendment', 'credit amendment'],
                'ai_prompt': 'only identify credit amendment',
                'format_template': 'Credit Amendment.{ext}',
                'required_fields': [],
                'priority': 9,
                'category': 'Loan Application',
                'year_context': 'amendment date, revision date'
            },

            # Financial Statements
            'profit_loss': {
                'keywords': ['profit and loss', 'p&l', 'income statement', 'profit loss statement'],
                'ai_prompt': 'Extract period',
                'format_template': 'Profit & Loss - {date}.{ext}',
                'required_fields': ['date'],
                'priority': 9,
                'category': 'Financial Statements',
                'year_context': 'statement period, fiscal year, for the year ended'
            },
            'balance_sheet': {
                'keywords': ['balance sheet', 'ASSETS', 'Current Assets', 'Checking/Savings', 'Balance Sheet', 'Total Inventory ','Liabilities'],
                'ai_prompt': 'Extract date and business name from balance sheet',
                'format_template': 'Balance Sheet - {date}.{ext}',
                'required_fields': ['date'],
                'priority': 9,
                'category': 'Financial Statements',
                'year_context': 'as of date, statement date, fiscal year end'
            },
            'personal_financial_statement': {
                'keywords': ['personal financial statement', 'pfs', 'personal balance sheet', 'sba 413', 'form 413', 'sba form 413'],
                'ai_prompt': 'Extract individual name and date from personal financial statement',
                'format_template': 'PFS.{ext}',
                'required_fields': [],
                'priority': 9,
                'category': 'Financial Statements',
                'year_context': 'as of date, statement date'
            },
            'projections': {
                'keywords': ['projections', 'business plan'],
                'ai_prompt': 'Extract company name and projection year from projections',
                'format_template': 'Projections/ Business Plan.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Financial Statements',
                'year_context': 'projection year, forecast period'
            },
            'debt_schedule': {
                'keywords': ['debt schedule', 'bds', 'business debt schedule'],
                'ai_prompt': 'Extract business name from debt schedule',
                'format_template': 'Debt Schedule.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Financial Statements',
                'year_context': 'schedule date, as of date'
            },
            'bank_statements': {
                'keywords': ['bank statements', 'bnk stmt'],
                'ai_prompt': 'Extract account holder name and period from bank statements',
                'format_template': 'Bank Statement.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Financial Statements',
                'year_context': 'statement period, statement date'
            },
            'tax_return_extension': {
                'keywords': ['Application for Automatic Extension', 'business income tax'],
                'ai_prompt': 'Extract calender year',
                'format_template': 'BTR{tax_year}Extension.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Financial Statements',
                'year_context': 'statement period, statement date'
            },
            'tax_return_extension': {
                'keywords': ['Application for Automatic Extension', 'U.S. Individual Income Tax Return'],
                'ai_prompt': 'Extract calender year',
                'format_template': 'PTR{tax_year}Extension.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Financial Statements',
                'year_context': 'statement period, statement date'
            },

            # Credit Reports
            'credit_report_transunion': {
                'keywords': ['clear/tlo', 'tu', 'transunion'],
                'ai_prompt': 'Identify TransUnion credit report',
                'format_template': 'TU.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Credit Reports',
                'year_context': 'report date, as of date, pulled date'
            },
            'credit_report_experian': {
                'keywords': ['experian', 'experian credit report'],
                'ai_prompt': 'Identify Experian credit report',
                'format_template': 'Experian.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Credit Reports',
                'year_context': 'report date, as of date, pulled date'
            },
            'credit_report_equifax': {
                'keywords': ['equifax', 'equifax credit report'],
                'ai_prompt': 'Identify Equifax credit report',
                'format_template': 'Equifax.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Credit Reports',
                'year_context': 'report date, as of date, pulled date'
            },

            # Agreements and Legal Documents
            'purchase_agreement': {
                'keywords': ['psa', 'business purchase agreement', 'stock purchase agreement', 'real estate purchase agreement', 'asset purchase agreement'],
                'ai_prompt': 'Extract property address and purchase price from purchase agreement',
                'format_template': 'Purchase Agreement.{ext}',
                'required_fields': [],
                'priority': 9,
                'category': 'Legal Documents',
                'year_context': 'agreement date, closing date'
            },
            'bill_of_sale': {
                'keywords': ['bill of sale'],
                'ai_prompt': 'Extract buyer and seller names from bill of sale',
                'format_template': 'Bill of Sale.{ext}',
                'required_fields': [],
                'priority': 9,
                'category': 'Legal Documents',
                'year_context': 'sale date, transaction date'
            },
            'psa_amendment': {
                'keywords': ['psa addendum', 'psa amendment', 'purchase agreement addendum'],
                'ai_prompt': 'Extract property address from PSA amendment',
                'format_template': 'PSA Amendment.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Legal Documents',
                'year_context': 'amendment date, effective date'
            },
            'lease_agreement': {
                'keywords': ['lease agreement', 'commercial lease', 'rental agreement', 'lease contract', 'lease'],
                'ai_prompt': 'Extract property address and tenant name from lease agreement',
                'format_template': 'Lease Agreement.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Real Estate',
                'year_context': 'lease commencement date, lease term, effective date'
            },
            'landlord_waiver': {
                'keywords': ['landlord subordination', 'landlord waiver', 'landlord refusal', 'landlord consent'],
                'ai_prompt': 'Extract landlord name and property address from landlord waiver',
                'format_template': 'Landlord Waiver.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Real Estate',
                'year_context': 'waiver date, effective date'
            },
            'epc_oc_lease': {
                'keywords': ['epc-oc lease agreement'],
                'ai_prompt': 'Extract EPC and OC names from lease agreement',
                'format_template': 'EPC-OC Lease Agreement.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Real Estate',
                'year_context': 'lease date, effective date'
            },
            'landlord_subordination': {
                'keywords': ['subordination of lease', 'lease subordination'],
                'ai_prompt': 'Extract landlord name and property address from subordination',
                'format_template': 'Landlord Subordination.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Real Estate',
                'year_context': 'subordination date, effective date'
            },
            'assignment_lease_rents': {
                'keywords': ['assignment of lease and rents', 'tenant interest', 'lessee interest'],
                'ai_prompt': 'Extract property address from assignment of lease and rents',
                'format_template': 'Assignment of lease and rents (Tenant\'s Interest/Lessee\'s Interest).{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Real Estate',
                'year_context': 'assignment date, effective date'
            },
            'business_valuation': {
                'keywords': ['business valuations', 'business valuations report', 'bv'],
                'ai_prompt': 'Extract business address and valuation amount from business valuation',
                'format_template': 'Business Valuation Report.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Valuation',
                'year_context': 'valuation date, effective date'
            },
            'site_visit_report': {
                'keywords': ['site visit', 'inspection report', 'quick report'],
                'ai_prompt': 'Extract property address from site visit report',
                'format_template': 'Site Visit Report.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Reports',
                'year_context': 'visit date, inspection date'
            },
            'equipment_list': {
                'keywords': ['ff&e list', 'equipment list', 'm&e list', 'ffe list', 'furniture and fixture list'],
                'ai_prompt': 'Extract borrower name from equipment list',
                'format_template': 'Equipment List.{ext}',
                'required_fields': [],
                'priority': 7,
                'category': 'Collateral',
                'year_context': 'list date, effective date'
            },
            'collateral_schedule': {
                'keywords': ['collateral schedule', 'vehicle list', 'vehicle information owned checklist', 'vehicle information spreadsheet', 'fedex vehicle information list adi'],
                'ai_prompt': 'Extract vehicle information from collateral schedule',
                'format_template': 'Collateral Schedule.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Collateral',
                'year_context': 'schedule date, effective date'
            },

            # Loan Documents
            'note': {
                'keywords': ['note', 'promissory note','Note','NOTE'],
                'ai_prompt': '',
                'format_template': 'Note.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Documents',
                'year_context': 'note date, execution date'
            },
            'guaranty_agreement': {
                'keywords': ['guaranty agreement', 'sba unconditionally guaranty'],
                'ai_prompt': 'Extract guarantor name only',
                'format_template': 'Guaranty Agreement.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Documents',
                'year_context': 'agreement date, execution date'
            },
            'security_agreement': {
                'keywords': ['security agreement', 'SBA Form 1059','GRANT OF SECURITY INTEREST', 'This Agreement secures the payment'],
                'ai_prompt': 'Identify security agreement only',
                'format_template': 'Security Agreement.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Documents',
                'year_context': ''
            },
            'business_loan_agreement': {
                'keywords': ['business loan agreement', ' Business Loan Agreement (“Agreement”)'],
                'ai_prompt': '',
                'format_template': 'Business Loan Agreement.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Documents',
                'year_context': 'agreement date, execution date'
            },
            'sba loan agreement': {
                'keywords': ['sba loan agreement'],
                'ai_prompt': 'Identify sba loan agreement only',
                'format_template': 'SBA Loan Agreement.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Documents',
                'year_context': 'agreement date, execution date'
            },
           'Closing Instructions': {
                'keywords': ['closing instructions', 'loan documents enclosed'],
                'ai_prompt': '',
                'format_template': 'Closing Instruction Letter.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Documents',
                'year_context': 'agreement date, execution date'
            },
          'SBA Settlment Sheet': {
                'keywords': ['SBA Settlment Sheet'],
                'ai_prompt': 'Identify SBA Settlment Sheet',
                'format_template': 'Form 1050.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Loan Documents',
                'year_context': 'agreement date, execution date'
            },

            # SBA Forms
            'form_722': {
                'keywords': ['equal employment opportunity', 'sba 722'],
                'ai_prompt': 'Identify SBA Form 722',
                'format_template': '722.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'SBA Forms',
                'year_context': 'form date, submission date'
            },
            'borrower_certification': {
                'keywords': ['borrower and operating company certification', 'borrower certification'],
                'ai_prompt': '',
                'format_template': 'Borrowers Certification.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'SBA Forms',
                'year_context': 'certification date, execution date'
            },
            'form_601': {
                'keywords': ['agreement of compliance', 'sba form 601'],
                'ai_prompt': 'Identify SBA Form 601',
                'format_template': '601.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'SBA Forms',
                'year_context': 'form date, agreement date'
            },
            'form_159': {
                'keywords': ['159', 'compensation agreement', 'sba form 159'],
                'ai_prompt': 'Extract agent name and SBA loan number from Form 159',
                'format_template': '159.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'SBA Forms',
                'year_context': 'form date, agreement date'
            },
            'broker_invoice': {
                'keywords': ['referral fee invoice', 'broker fee invoice'],
                'ai_prompt': 'Extract agent name and broker fee from invoice',
                'format_template': 'Broker Invoice.{ext}',
                'required_fields': [],
                'priority': 7,
                'category': 'SBA Forms',
                'year_context': 'invoice date, service date'
            },
            'child_support_certification': {
                'keywords': ['child support certification', 'certificate of compliance with child support obligation'],
                'ai_prompt': 'Identify child support certification',
                'format_template': 'Child Support Certification.{ext}',
                'required_fields': [],
                'priority': 7,
                'category': 'Certifications',
                'year_context': 'certification date, effective date'
            },

            # Refinancing Documents
            'refinance_note': {
                'keywords': ['note being refinanced', 'refinance note'],
                'ai_prompt': 'Extract bank name and loan amount from refinance note',
                'format_template': 'Note - {bank_name}.{ext}',
                'required_fields': ['bank_name'],
                'priority': 8,
                'category': 'Refinancing',
                'year_context': 'note date, original date'
            },
            'payoff_statement': {
                'keywords': ['statements', 'payoff statements', 'stmts'],
                'ai_prompt': 'Extract lender name from payoff statement',
                'format_template': 'Payoff Statement.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Refinancing',
                'year_context': 'statement date, payoff date'
            },
            'debt_certification': {
                'keywords': ['debt certification'],
                'ai_prompt': 'Identify debt certification document',
                'format_template': 'Debt Refinance Certificate.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Refinancing',
                'year_context': 'certification date, effective date'
            },
            'seller_note': {
                'keywords': ['shareholder note', 'seller note', 'standby note', 'seller carry note'],
                'ai_prompt': 'Extract standby creditor name from seller note',
                'format_template': 'Seller Note.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Refinancing',
                'year_context': 'note date, execution date'
            },
            'standby_creditors_agreement': {
                'keywords': ['shareholder agreement', 'standby creditors agreement', 'standby agreement'],
                'ai_prompt': 'Extract standby creditor name from agreement',
                'format_template': 'Standby Creditors Agreement.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Refinancing',
                'year_context': 'agreement date, effective date'
            },
            'eidl_subordination': {
                'keywords': ['eidl subordination agreement'],
                'ai_prompt': 'Extract EIDL loan amount from subordination agreement',
                'format_template': 'EIDL Subordination Agreement.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Refinancing',
                'year_context': 'subordination date, effective date'
            },

            # Franchise Documents
            'franchise_agreement': {
                'keywords': ['franchise agreement'],
                'ai_prompt': 'Extract franchisor and franchisee names from franchise agreement',
                'format_template': 'Franchise Agreement.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Franchise',
                'year_context': 'agreement date, effective date'
            },
            'franchise_disclosure': {
                'keywords': ['fdd', 'franchise directory disclosure'],
                'ai_prompt': 'Extract franchise name from disclosure document',
                'format_template': 'Franchise Directory Disclosure.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Franchise',
                'year_context': 'disclosure date, effective date'
            },
            'fuel_agreement': {
                'keywords': ['fuel agreement', 'jobber agreement'],
                'ai_prompt': 'Extract business name and brand from fuel agreement',
                'format_template': 'Fuel Agreement.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Franchise',
                'year_context': 'agreement date, effective date'
            },

            # Real Estate Documents
            'real_estate_appraisal': {
                'keywords': ['cre appraisal report', 'cre appraisal', 'commercial real estate appraisal', 'property appraisal'],
                'ai_prompt': 'Extract property address and appraisal value from real estate appraisal',
                'format_template': 'CRE Appraisal Report - {address}.{ext}',
                'required_fields': ['address'],
                'priority': 9,
                'category': 'Real Estate',
                'year_context': 'appraisal date, inspection date, effective date'
            },
            'cre_appraisal_review': {
                'keywords': ['cre appraisal review report', 'cre review', 'review report'],
                'ai_prompt': 'Extract property address from CRE appraisal review',
                'format_template': 'CRE Appraisal Review Report - {address}.{ext}',
                'required_fields': ['address'],
                'priority': 9,
                'category': 'Real Estate',
                'year_context': 'review date, appraisal date'
            },
            'sfr_appraisal': {
                'keywords': ['sfr appraisal report', 'sfr report', 'appraisal', 'APPRAISAL OF', 'The purpose of this summary appraisal report','and adequately supported','opinion of the market value of the subject property'], 
                'ai_prompt': 'Extract property address from SFR appraisal',
                'format_template': 'SFR Appraisal Report - {address}.{ext}',
                'required_fields': ['address'],
                'priority': 10,
                'category': 'Real Estate',
                'year_context': 'appraisal date, inspection date'
            },
            'me_equipment_appraisal': {
                'keywords': ['m&e report', 'equipment appraisal'],
                'ai_prompt': 'Extract equipment details from M&E appraisal',
                'format_template': 'M&E Report.{ext}',
                'required_fields': [],
                'priority': 9,
                'category': 'Real Estate',
                'year_context': 'appraisal date, inspection date'
            },
            'phase_i_environmental': {
                'keywords': ['phase i environmental', 'phase 1 environmental', 'environmental site assessment', 'esa', 'phase i'],
                'ai_prompt': 'Extract property address from Phase I Environmental Assessment',
                'format_template': 'Phase I Report - {address}.{ext}',
                'required_fields': ['address'],
                'priority': 9,
                'category': 'Real Estate',
                'year_context': 'report date, assessment date, inspection date'
            },
            'phase_i_review': {
                'keywords': ['phase i review report'],
                'ai_prompt': 'Extract property address from Phase I review',
                'format_template': 'Phase I Review Report - {address}.{ext}',
                'required_fields': ['address'],
                'priority': 9,
                'category': 'Real Estate',
                'year_context': 'review date, report date'
            },
            'phase_ii_environmental': {
                'keywords': ['phase ii environmental', 'phase 2 environmental', 'phase ii'],
                'ai_prompt': 'Extract property address from Phase II Environmental Assessment',
                'format_template': 'Phase II Report - {address}.{ext}',
                'required_fields': ['address'],
                'priority': 9,
                'category': 'Real Estate',
                'year_context': 'report date, assessment date'
            },
            'environmental_questionnaire': {
                'keywords': ['environmental questionnaire', 'questionnaire'],
                'ai_prompt': 'Extract property address from environmental questionnaire',
                'format_template': 'Environmental Questionnaire.{ext}',
                'required_fields': [],
                'priority': 8,
                'category': 'Real Estate',
                'year_context': 'questionnaire date, completion date'
            },

            # Title and UCC Documents
            'ucc_pre_search': {
                'keywords': ['', 'Jurisdiction', 'Account Information', 'SEARCH SUMMARY'],
                'ai_prompt': 'Extract debtor name from UCC search only',
                'format_template': 'UCC Lien Search - {name}.{ext}',
                'required_fields': ['name'],
                'priority': 9,
                'category': 'Title/UCC',
                'year_context': 'search date, as of date'
            },
            'ucc_str': {
                'keywords': ['ucc str confirming lien position', 'str', 'search to reflect', 'post search', 'UCC Search Certificate', 'UCC Browse Results'],
                'ai_prompt': 'Extract name',
                'format_template': 'UCC- STR.{ext}',
                'required_fields': [],
                'priority': 9,
                'category': 'Title/UCC',
                'year_context': 'search date, filing date'
            },
            'ucc_filing': {
                'keywords': ['ucc-1', 'ucc filing', 'financing statement', 'ucc-1 financing statement', 'ucc 1', 'FILE', 'filling', 'Filing Numbe'],
                'ai_prompt': 'Extract only debtor name from UCC filing',
                'format_template': 'UCC 1.{ext}',
                'required_fields': [],
                'priority': 9,
                'category': 'Collateral',
                'year_context': 'filing date, effective date'
            },
            'alta_policy': {
                'keywords': ['alta policy', 'title policy', 'final policy', 'loan policy'],
                'ai_prompt': 'Extract property address and loan amount from ALTA policy',
                'format_template': 'ALTA Policy - {address}.{ext}',
                'required_fields': ['address'],
                'priority': 9,
                'category': 'Title/UCC',
                'year_context': 'policy date, effective date'
            },
            'recorded_deed_trust': {
                'keywords': ['recorded deed of trust', 'morgtages', 'dot', 'deed of trust', 'mortgage', 'grant deed', 'special warranty deed', 'warranty deed', 'wd'],
                'ai_prompt': 'Extract property address from recorded deed of trust',
                'format_template': 'Recorded Deed of Trust/ Mortgage - {address}.{ext}',
                'required_fields': ['address'],
                'priority': 10,
                'category': 'Title/UCC',
                'year_context': 'recording date, execution date'
            },
            'recorded_assignment_rents': {
                'keywords': ['recorded assignment of rents', 'ar', 'assignment of rent'],
                'ai_prompt': 'Extract property address from assignment of rents',
                'format_template': 'Recorded Assignment of Rent - {address}.{ext}',
                'required_fields': ['address'],
                'priority': 10,
                'category': 'Title/UCC',
                'year_context': 'recording date, execution date'
            },
            'vehicle_title': {
                'keywords': ['recorded vehicle title', 'title', 'vehicle title', 'certificate of title', 'car title', 'truck title', 'vin'],
                'ai_prompt': 'Extract VIN number (last 4 digits) and vehicle year/make/model from vehicle title',
                'format_template': 'Vehicle Title - VIN #{vin_last_4}.{ext}',
                'required_fields': ['vin_last_4'],
                'priority': 9,
                'category': 'Collateral',
                'year_context': 'title date, registration date, vehicle model year'
            },
            'certificate_good_standing': {
                'keywords': ['certificate of good standing', 'good standing certificate', 'certificate of existence'],
                'ai_prompt': 'Extract business name and state from certificate of good standing',
                'format_template': 'Certificate_of_Good_Standing.{ext}',
                'required_fields': [''],
                'priority': 9,
                'category': 'Corporate Documents',
                'year_context': 'certificate date, as of date, issued date'
            }, 
            'general_liability': {
                'keywords': ['general liability', 'coi', 'eoi', 'insurance - gl', 'ins', 'liability insurance'],
                'ai_prompt': 'borrower name',
                'format_template': 'Insurance - GL.{ext}',
                'required_fields': ['date', 'borrower_name'],
                'priority': 8,
                'category': 'Insurance Documents',
                'validation_context': 'date, address, borrower\'s name, rcl as certificate holder, signature, loan number'
            },
            'hazard_bpp': {
                'keywords': ['hazard', 'bpp', 'coi', 'eoi', 'insurance - bpp', 'ins', 'business personal property', 'EVIDENCE OF COMMERCIAL PROPERTY INSURANCE'],
                'ai_prompt': 'Extract borrower name',
                'format_template': 'Insurance_BPP_CRE.{ext}',
                'required_fields': ['date', 'borrower_name'],
                'priority': 8,
                'category': 'Insurance Documents',
                'validation_context': 'date, address, borrower\'s name, rcl as certificate holder, signature, loan number, 10 day cancellation, replacement cost'
            },
            'life_insurance': {
                'keywords': ['life insurance', 'life policy', 'life ins'],
                'ai_prompt': 'Extract date and policy holder name for life insurance policy',
                'format_template': 'Life_Insurance_Policy.{ext}',
                'required_fields': ['date', 'policy_holder_name'],
                'priority': 8,
                'category': 'Insurance Documents',
                'validation_context': 'date, policy holder\'s name, rcl as certificate holder'
            },
            'life_insurance_collateral_assignment_form': {
                'keywords': ['life insurance collateral assignment form', 'collateral assignment', 'life assignment form'],
                'ai_prompt': 'Extract policy holder name and date for life insurance collateral assignment form',
                'format_template': 'Life_Insurance_Collateral_Assignment_Form_{policy_holder}_{date}.{ext}',
                'required_fields': ['policy_holder_name'],
                'priority': 8,
                'category': 'Insurance Documents',
                'validation_context': 'life insurance collateral assignment form'
            },
            'life_insurance_collateral_assignment_letter': {
                'keywords': ['life insurance collateral assignment letter', 'collateral assignment letter', 'life assignment letter'],
                'ai_prompt': 'Extract policy holder name and date for life insurance collateral assignment letter',
                'format_template': 'Life_Insurance_Collateral_Assignment_Letter.{ext}',
                'required_fields': ['policy_holder_name'],
                'priority': 8,
                'category': 'Insurance Documents',
                'validation_context': 'life insurance collateral assignment letter'
            },
            'workers_compensation': {
                'keywords': ['workers compensation', 'worker compensation', 'work comp', 'wc', 'ins'],
                'ai_prompt': 'Extract date, borrower name, and loan number for workers compensation insurance',
                'format_template': 'Insurance_WC.{ext}',
                'required_fields': ['date', 'borrower_name'],
                'priority': 8,
                'category': 'Insurance Documents',
                'validation_context': 'date, address, borrower\'s name, rcl as certificate holder, signature, loan number'
            },
            'professional_liability': {
                'keywords': ['professional liability', 'coi', 'eoi', 'insurance - gl', 'ins', 'prof liability'],
                'ai_prompt': 'Extract date, borrower name, and loan number for professional liability insurance',
                'format_template': 'Insurance_Professional.{ext}',
                'required_fields': ['date', 'borrower_name'],
                'priority': 8,
                'category': 'Insurance Documents',
                'validation_context': 'date, address, borrower\'s name, rcl as certificate holder, signature, loan number'
            },
            'flood_determination': {
                'keywords': ['flood search', 'flood', 'flood certificate', 'flood cert', 'flood determination'],
                'ai_prompt': 'Extract address for flood determination',
                'format_template': 'Flood Determination.{ext}',
                'required_fields': ['address'],
                'priority': 7,
                'category': 'Property Documents',
                'validation_context': 'address, flood zone, determination question should be no if found yes look for flood insurance'
            },
            'articles_of_organization': {
                'keywords': ['articles of organization', 'articles of formation', 'articles', 'articles of inc'],
                'ai_prompt': 'Identify articles of organization',
                'format_template': 'Articles of Organization.{ext}',
                'required_fields': ['', ''],
                'priority': 9,
                'category': 'Corporate Documents',
                'validation_context': 'name, signature, formation date'
            },
            'operating_agreement': {
                'keywords': ['operating agreement', 'oa'],
                'ai_prompt': 'Identify only operating agreement',
                'format_template': 'Operating_Agreemen.{ext}',
                'required_fields': ['entity_name'],
                'priority': 9,
                'category': 'Corporate Documents',
                'validation_context': 'name, signature, ownership structure'
            },
            'certificate_of_good_standing': {
                'keywords': ['gs', 'cert. of gs', 'certificate of good standing', 'good standing'],
                'ai_prompt': '',
                'format_template': 'Certificate of Good Standing.{ext}',
                'required_fields': [''],
                'priority': 9,
                'category': 'Corporate Documents',
                'validation_context': 'name, signature'
            },
            'certificate_of_members': {
                'keywords': ['certificate of members', 'certificate of officer', 'cert of officers', 'member certificate'],
                'ai_prompt': '',
                'format_template': 'Certificate of Members.{ext}',
                'required_fields': ['', ''],
                'priority': 9,
                'category': 'Corporate Documents',
                'validation_context': 'name, signature, tin no., address, ownership structure'
            },
            'ss4': {
                'keywords': ['ss4', 'ein', 'ss-4', 'employer identification'],
                'ai_prompt': '',
                'format_template': 'SS-4.{ext}',
                'required_fields': ['entity_name', 'tin'],
                'priority': 9,
                'category': 'Corporate Documents',
                'validation_context': 'name, tin no., address'
            },
            'business_license': {
                'keywords': ['biz license', 'license', 'lic', 'business license'],
                'ai_prompt': 'Extract business name, license dates, and address for business license',
                'format_template': 'Business_License_{business_name}_{date}.{ext}',
                'required_fields': ['business_name'],
                'priority': 6,
                'category': 'Corporate Documents',
                'validation_context': 'name, dates, address'
            },
            'dba_filing': {
                'keywords': ['name filing', 'assumed name filing', 'dba filing', 'dba', 'doing business as'],
                'ai_prompt': 'Extract business names and signature date for DBA filing',
                'format_template': 'DBA_Filing_{business_name}_{date}.{ext}',
                'required_fields': ['business_name'],
                'priority': 9,
                'category': 'Corporate Documents',
                'validation_context': 'names, signature'
            },
            'bylaws': {
                'keywords': ['bylaws', 'by-laws', 'corporate bylaws'],
                'ai_prompt': 'Extract entity name, date, and address for bylaws document',
                'format_template': 'Bylaws_{entity_name}_{date}.{ext}',
                'required_fields': ['entity_name'],
                'priority': 9,
                'category': 'Corporate Documents',
                'validation_context': 'names, signature, date, address'
            },
            'caivrs': {
                'keywords': ['caivrs'],
                'ai_prompt': 'Extract TIN numbers for CAIVRS report',
                'format_template': 'CAIVRS_{tin}_{date}.{ext}',
                'required_fields': ['tin'],
                'priority': 10,
                'category': 'Compliance Documents',
                'validation_context': 'tin numbers'
            },
            'ofac': {
                'keywords': ['ofac', 'Sanctions List Search','Sanctions','OFAC','SDN', 'sanctions screening'],
                'ai_prompt': 'Extract searched name for OFAC screening',
                'format_template': 'OFAC.{ext}',
                'required_fields': [],
                'priority': 10,
                'category': 'Compliance Documents',
                'validation_context': 'name, your search has not returned any results, address, tin (if given)'
            },
            'photo_id': {
                'keywords': ['id', 'dl', 'driver license', 'passport', 'photo id'],
                'ai_prompt': 'Extract name, birth date, and expiration date for photo ID',
                'format_template': 'Photo_ID_{name}_{expiry_date}.{ext}',
                'required_fields': ['name', 'birth_date'],
                'priority': 6,
                'category': 'Identity Documents',
                'validation_context': 'name, birth date, expire date, address'
            },
            'etran_verification': {
                'keywords': ['plp transmittal', 'etran transmittal', 'etran verification'],
                'ai_prompt': 'Extract loan number, loan amount, and approval date for ETRAN verification',
                'format_template': 'Etran_Verification_{loan_number}_{approval_date}.{ext}',
                'required_fields': ['loan_number', 'loan_amount', 'approval_date'],
                'priority': 10,
                'category': 'SBA Documents',
                'validation_context': 'loan number, loan amount, approval date'
            },
            'etran_report': {
                'keywords': ['etran report', 'etran - origination', 'etran - servicing'],
                'ai_prompt': 'Extract comprehensive loan information including loan amount, approval date, and borrower details for ETRAN report',
                'format_template': 'ETRAN_{report_type}_{loan_number}_{date}.{ext}',
                'required_fields': ['loan_number', 'loan_amount', 'approval_date'],
                'priority': 10,
                'category': 'SBA Documents',
                'validation_context': 'loan amount, approval date, monthly payment amount, interest rates, referral name & fee, packaging fees, collateral, use of proceeds, borrower\'s information, guarantor\'s information, note date, maturity date, guaranty fee'
            },
            'ach_authorization': {
                'keywords': ['ach', 'ach authorization', 'ach form'],
                'ai_prompt': 'Extract loan number, borrower name, account number, and routing number for ACH authorization',
                'format_template': 'ACH_Authorization_{loan_number}_{borrower_name}.{ext}',
                'required_fields': ['loan_number', 'borrower_name', 'account_number', 'routing_number'],
                'priority': 9,
                'category': 'Banking Documents',
                'validation_context': 'loan number, borrower\'s name, signature, account number, routing number'
            },
            'voided_check': {
                'keywords': ['void check', 'cancel check', 'voided check'],
                'ai_prompt': 'Extract account number and routing number for voided check',
                'format_template': 'Void_Check_{account_number}_{date}.{ext}',
                'required_fields': ['account_number', 'routing_number'],
                'priority': 6,
                'category': 'Banking Documents',
                'validation_context': 'void, account number, routing number'
            },
            'transunion_report': {
                'keywords': ['tu', 'transunion', 'clear', 'tlo'],
                'ai_prompt': 'Extract name and TIN/SSN for TransUnion credit report',
                'format_template': 'TU_{name}_{tin_ssn}.{ext}',
                'required_fields': ['name', 'tin_ssn'],
                'priority': 8,
                'category': 'Credit Documents',
                'validation_context': 'name, tin/ssn'
            },
            
            'financial_statements': {
                'keywords': ['balance sheet', 'income statement', 'profit loss', 'financial statement', 'p&l'],
                'ai_prompt': 'Extract company name and period from financial statement',
                'format_template': 'FS_{company_name}_{period}.{ext}',
                'required_fields': ['company_name', 'period'],
                'priority': 9,
                'category': 'Financial Documents',
                'supported_types': ['pdf', 'xlsx', 'csv'],
                'year_context': 'period ending, as of date, fiscal year'
            },
            
            'bank_statements': {
                'keywords': ['bank statement', 'account statement', 'checking account', 'savings account'],
                'ai_prompt': 'Extract bank name, account number (last 4 digits), and statement period',
                'format_template': 'Bank_Statement_{bank_name}_{account_last4}_{period}.{ext}',
                'required_fields': ['bank_name', 'account_last4', 'period'],
                'priority': 8,
                'category': 'Banking Documents',
                'supported_types': ['pdf', 'csv'],
                'year_context': 'statement period, account period'
            },
            
            'voided_check': {
                'keywords': ['void check', 'cancel check', 'voided check'],
                'ai_prompt': 'Extract account number and routing number for voided check',
                'format_template': 'Void_Check_{account_number}_{date}.{ext}',
                'required_fields': ['account_number', 'routing_number'],
                'priority': 6,
                'category': 'Banking Documents',
                'supported_types': ['pdf', 'jpg', 'tiff', 'tif'],
                'validation_context': 'void, account number, routing number'
            }
        }
