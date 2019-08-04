class SFClssicLocators:

    ## Common locators
    str_user = "username"
    str_password = "password"
    str_submit = "Login"
    str_menu_bar_parent = "ID=tabBar"
    str_tab= "// li[ @ id = '<<text_replace>>'] / a"
    str_main_menu_bar = "xpath=//a[contains(text(),'<<text_replace>>')]"
    str_create_new_object = "xpath=//input[contains(@value,'New')]"
    str_continue = "xpath=//input[contains(@value,'Continue')]"
    str_new_record_type = "xpath=//div[@class='requiredInput']/select"
    str_common_input = "//label[text()='<<text_replace>>']/ancestor::td/following-sibling::td[1]//input[@type ='text']" #"xpath=//label[text()='<<text_replace>>']/ancestor::td[1]/following-sibling::td[1]//input"
    str_common_textarea = "//label[text()='<<text_replace>>']/ancestor::td[1]/following-sibling::td[1]//textarea[@type='text']"
    str_common_dropdown = "//label[text()='<<text_replace>>']/ancestor::td[1]/following-sibling::td[1]//select"
    str_common_dropdown_th = "xpath=//label[text()='Override Single Quote Reason']/ancestor::th[1]/following-sibling::td[1]/select"
    str_common_checkbox = "xpath=//label[text()='<<text_replace>>']/ancestor::td[1]/following-sibling::td[1]//input[@type='checkbox']"
    str_common_checkbox_th = "xpath=//label[text()='<<text_replace>>']/ancestor::th[1]/following-sibling::td[1]/input[@type='checkbox']"
    str_header_buttons = "//div[@class='pbHeader']//input[@title='<<text_replace>>' or @value='<<text_replace>>']"  #"xpath=//div[@class='pbHeader']//input[@title='<<text_replace>>']"
    str_common_input_btn = "xpath=//input[@value='<<text_replace>>']"
    str_common_button_btn = "xpath=//button[text()='<<text_replace>>']"
    str_common_input_lookup = "xpath=//label[text()='<<text_replace>>']/ancestor::td/following::td[1]//span/input[@type='text']"
    str_setup_link="xpath=//a[text()='Setup' and @title='Setup']"


    #Opportunities Page
    str_new_opportunity="xpath=//input[@value=' New ' and @type='button']"


    # str_searchllookup ="xpath=//input[@id='lksrch']"
    str_lookup_icon = "//label[text()='<<text_replace>>']/ancestor::td[1]/following-sibling::td[1]//a"
    str_lookup_go = "xpath=//input[contains(@value,'Go')]"
    str_lookup_search_result = "xpath=//div[text()='Search Results']/parent::div//a[text()='<<text_replace>>']"
    str_bottom_buttons = "xpath=//div[@class='pbBottomButtons']//input[@title='Cancel']"

    ## contacts page Locators
    str_err_duplicate_accounts = "xpath=//div[@class='pbError' and contains(text(), 'Possible Duplicate Records Found')]"
    str_err_invalid_data = "xpath=//div[@class='pbError' and contains(text(), 'Error: Invalid Data')]"
    str_name_click = "xpath=//a[@id='globalHeaderNameMink']/span"
    str_light_click = "xpath=//li/a[text()='Switch to Lightning Experience']"
    str_image_click = "xpath=//span[@class='photoContainer forceSocialPhoto']"
    str_classic_click = "xpath=//a[text()='Switch to Salesforce Classic']"
    str_create_new_quote_button = "xpath=//div[@class='pbHeader']//input[@value='<<text_replace>>']"
    str_new_record_type = "xpath=//div[@class='requiredInput']/select"
    str_continue = "xpath=//input[contains(@value,'Continue')]"

    ## Accounts page Locators
    str_common_quote_look_up_icon = "xpath=//label[contains(text(),'<<text_replace>>')]/parent::th[1]/following-sibling::td[1]//img[@title='Lookup']"
    str_common_quote_search_textbox = "xpath=//input[@value='<<text_replace>>']/preceding-sibling::input[@type='text']"
    str_common_quote_search_button = "xpath=//input[@value='Search']"
    str_common_quote_choose_link = "xpath=//a[text()='<<text_replace>>']"
    str_tab_details = "xpath=//span[text()='Details']"
    str_new_opportunity_button = "xpath=//input[@value='<<text_replace>>']"
    str_classic_select_account = "xpath=//div[@class='hotListElement']//tr[2]//a"
    str_new_account_btn ='//*[@id="hotlist"]/table/tbody/tr/td[2]/input'

    # Search Results Page
    str_search_item_link = "xpath=(//table[@class='list']/descendant::a[contains(text(),'<<text_replace>>')])[1]"

    ## Quotes Page Locators
    str_quote_common_drop_down = "xpath=//label[text()='<<text_replace>>']/ancestor::th[1]/following-sibling::td[1]//select"
    str_quote_common_check_box = "xpath=//label[text()='<<text_replace>>']/ancestor::th[1]/following-sibling::td[1]//input[@type='checkbox']"
    str_show = "xpath=//div[@id='PRPTable_length']/label/select"
    str_sold_to_contact_name = "xpath=//table[@id='listComponent:innerTable']//tbody/tr[1]/td[1]/a"
    str_Bill_to_Contact_name = "xpath=//table[@id='listComponent:innerTable']//tbody/tr[1]/td[1]/a"
    str_quote_next_button = "xpath=//div[@class='pbHeader']//input[@value='<<text_replace>>']"
    str_quote_select_entity = "xpath=//div[@class='opportunityBlock']//label[contains(text(),'<<text_replace>>')]/preceding-sibling::input"
    str_quote_billing_accounts = "xpath=//label[text()=' billing account']//strong[contains(text(),'new')]"
    str_quote_new_quote_type = "xpath=(//h3[contains(text(),'Choose Quote Type')]/following::input[@type='radio' and @value='new'])[2]"
    str_quote_amend_quote_type = "xpath=//div[@data-id='selectQuoteTypeSection']//label[text()=' subscription for this billing account']/strong[contains(text(),'amend existing')]/ancestor::td[1]/input[@type='radio']"
    str_quote_renew_quote_type = "xpath=//div[@data-id='selectQuoteTypeSection']//label[text()=' subscription for this billing account']/strong[contains(text(),'renew existing')]/ancestor::td[1]/input[@type='radio']"
    str_quote_cancel_quote_type = "xpath=//div[@data-id='selectQuoteTypeSection']//label[text()=' subscription for this billing account']/strong[contains(text(),'cancel existing')]/ancestor::td[1]/input[@type='radio']"
    str_new_quotes_flow = "xpath=//span[text()='New Quote Flow']/following-sibling::span[contains(@class,'MenuButton')]"
    str_new_quotes_add_products = "xpath=//div[text()='Select a Step to Begin']/following-sibling::div/span[text()='Add Products']"
    str_add_product_table = "xpath=//table[@id='bundleProductTable']"
    str_rate_plan_charge_table = "xpath=//div[contains(@id, 'ratePlanChargeTable')]//table[contains(@id,'ratePlanChargeTable')]"
    str_existingbillingaccounts = "xpath=//table[@id='table-billingAccounts']/descendant::input[@type='radio']"
    str_amendexisting_subscription = "xpath=//input[@type='radio' and @value='amend']"
    str_table_existing_subscriptionNames = "xpath=//table[@id='table-subscriptions']/tbody/tr/td[2]"
    str_table_existing_specific_subscriptionName = "xpath=(//table[@id='table-subscriptions']/tbody/tr/td[2])[<<text_replace>>]"
    str_table_subscriptions = "xpath=//table[@id='table-subscriptions']"
    str_table_subscriptions_radio = "xpath=(//table[@id='table-subscriptions']/descendant::input[@type='radio'])[<<text_replace>>]"
    str_account_link="xpath=(//table[@class='detailList']/tbody/tr/td[text()='Account']/following::a)[1]"
    str_next_button_cancel_quote="xpath=(//input[@value='Next'])[2]"



    str_quote_label = "xpath=//table[@class='detailList']/tbody/tr/td[text()='<<text_replace>>']/following::td[1]"
    str_h3_heading = "xpath=//td[@class='pbTitle']/h3[contains(text(),'<<text_replace>>')]"
    str_product_user_numbers = "xpath=//table[@class='list']/tbody/tr[@class='headerRow']/th[contains(text(),'Product User No')]/parent::tr/following-sibling::tr/th"
    str_quote_action_button = "xpath=(//input[@value='<<text_replace>>'])[1]"
    str_confirmation_OK = "xpath="
    str_gotolist_productusers = "xpath=//h3[contains(text(),'Product Users')]/ancestor::div[@class='bPageBlock brandSecondaryBrd secondaryPalette']/descendant::div[@class='pShowMore']/a[contains(text(),'Go to list')]"
    str_product_user_gotolist = "xpath=//table[@class='list']/tbody/tr[contains(@class,'dataRow')]/th"

    str_quote_ready = "xpath=//div[@id='status' and text()='Quote is Ready.']"
    str_quote_label2 = "xpath=//table[@class='detailList']/tbody/tr/td[@class='labelCol']/following::span[text()='<<text_replace>>']/parent::td/following-sibling::td[1]"
    str_quote_label2_select="xpath=//table[@class='detailList']/tbody/tr/td[@class='labelCol']/following::span[text()='<<text_replace>>']/parent::td/following-sibling::td[1]/div/span/select"
    str_quote_status_div = "xpath=//div[@id='status']"
    str_quote_ready_frame = "xpath=//iframe[@name='0660Q0000004foB']"
    str_CreateNewQuote_click = "xpath=//span[contains(.,'Create New Quote')]"
    str_remove_image="xpath=//img[contains(@src,'remove12')]"
    str_next_product_location_information="xpath=//a[contains(@class,'paginate')]/parent::span/following-sibling::a[contains(text(),'Next')]"
    str_productinfo_frame="xpath=//iframe[@id='0660Q0000004foC']"
    str_product_info_table="xpath=//table[@id='example']"
    str_expand_product_row="xpath=//table[@id='example']/tbody/tr[<<text_replace>>]/td[1]/i"
    str_product_name_rows="xpath=//table[@id='example']/tbody/tr"
    str_product_name="xpath=//table[@id='example']/tbody/tr[<<text__replace>>]/td[2]"
    str_image_name="xpath=//table[@id='example']/tbody/tr[<<text__replace>>]/td[9]/img"
    str_quotestatus_dropdown="xpath=//table[@class='detailList']/tbody/tr/td[text()='Quote Status']/following::div[2]/span/select"


    # Product User Detail Page
    str_product_user_detail_label = "xpath=//table[@class='detailList']/tbody/tr/td[text()='<<text_replace>>']/following::td[1]"
    str_product_user_detail_label_select_dropdown = "xpath=//table[@class='detailList']/tbody/tr/td[text()='<<text_replace>>']/following::select[1]"
    str_save_product_user_detail = "xpath=(//input[@value=' Save ' and @class='btn' ])[1]"
    str_product_user_entitlements = "xpath=//table[@class='list']/tbody/tr[@class='headerRow']/th[contains(text(),'Entitlement Number')]/parent::tr/following-sibling::tr/th"
    str_product_user_entitlement_link = "xpath=//span[@class='listTitle' and contains(text(),'Product User Entitlements')]"
    str_gotolist_productusersentitlements = "xpath=//h3[contains(text(),'Product User Entitlements')]/ancestor::div[@class='bPageBlock brandSecondaryBrd secondaryPalette']/descendant::div[@class='pShowMore']/a[contains(text(),'Go to list')]"
    str_product_user_entitlements_gotolist = "xpath=//table[@class='list']/tbody/tr[contains(@class,'dataRow')]/th"
    str_h1_tabNavigation="xpath=//h1[contains(text(),'Tab Navigation')]"


    # Product User Entititlement Detail Page
    str_product_user_e_detail_label = "xpath=//table[@class='detailList']/tbody/tr/td[text()='<<text_replace>>']/following::td[1]"
    str_product_user_e_detail_label_select_dropdown = "xpath=//table[@class='detailList']/tbody/tr/td[text()='<<text_replace>>']/following::select[1]"
    str_save_product_user_e_detail = "xpath=(//input[@value=' Save ' and @class='btn' ])[1]"
    str_edit_product_user_e_detail="xpath=(//input[@value=' Edit ' and @class='btn' ])[1]"
    str_entitlement_section="xpath=//a[@class='linklet']/span[contains(text(),'Product User Entitlement')]"
    str_h2_quote="xpath=//h2[@class='pageDescription' and contains(text(),'Quote')]"

    # Product User Entititlement Detail Page
    str_product_user_e_detail_label = "xpath=//table[@class='detailList']/tbody/tr/td[text()='<<text_replace>>']/following::td[1]"
    str_product_user_e_detail_label_select_dropdown = "xpath=//table[@class='detailList']/tbody/tr/td[text()='<<text_replace>>']/following::select[1]"
    str_save_product_user_e_detail = "xpath=(//input[@value=' Save ' and @class='btn' ])[1]"



    # select product and office locations
    str_search_input = "xpath=//input[@id='search_bar']"
    str_search_button = "xpath=//input[@id='search_bar']/following-sibling::span[@class='searchButton']"
    str_select_all_button = "xpath=//button[text()='Select All']"
    str_select_first_button = "xpath=//tbody[@id='search_results_tbody']/tr[1]/td[6]/button[@type='button']"
    str_add_products_button = "xpath=//span[text()='Add Products']"
    str_add_products_and_close_button = "xpath=//span[text()='Add Products and Close']"
    str_next_button = "xpath=//button[contains(text(),'Next')]"
    str_select_product="xpath=//table[@id='search_results_table']/tbody/tr[<<text__replace>>]/td[4]"
    str_more_products="xpath=//span[text()='More Results']"
    str_saving_pleasewait="xpath=//*[@id='save_text']"

    ##select office loactions
    str_add_locations_and_close_button = "xpath=//span[text()='Add Locations and Close']"
    str_save_product_button = "xpath=//button[contains(text(),'Save')]"
    str_office_check_box = "xpath=//div[@class='DTFC_LeftBodyLiner']//tr[@role='row']/td[@class=' dt-checkboxes-cell']/input"
    str_Copy_Products_button = "xpath=//button[text()='Copy Products']"
    str_copy_products_inside_button = "xpath=//span[text()='Copy Products']"
    str_ok_button = "xpath=//div[@id='success']//button[text()='OK']"
    str_checkbox_all = "xpath=(//th[@class='dt-checkboxes-cell dt-checkboxes-select-all sorting_disabled']/input)[1]"
    str_officelocations_next = "xpath=//button[text()=' Next ']"
    str_copy_all_products_checkbox="xpath=//*[@id='products_table']/thead/tr/th[1]/input"
    str_no_office_locations = "xpath=//table[@id='QOL_table']/tbody/tr"
    str_office_locations_link="xpath=//table[@id='QOL_table']/tbody/tr[<<text__replace>>]/td[3]/a"
    str_copying_products="xpath=//div[@id='loaderText' and contains(text(),'Copying Products')]"

    #specific office location
    str_numberof_rows_one_location="xpath=//div[@class='DTFC_LeftBodyLiner']/table/tbody/tr"
    str_product_name_in_officelocation="xpath=//div[@class='DTFC_LeftBodyLiner']/table/tbody/tr[<<text__replace>>]/td[3]"
    str_delete_product_name_button="xpath=//div[@class='DTFC_LeftBodyLiner']/table/tbody/tr[<<text__replace>>]/td[2]/button"
    str_checkbox_product_name="xpath=//div[@class='DTFC_LeftBodyLiner']/table/tbody/tr[<<text__replace>>]/td[1]/input"
    str_quote_summary_link="xpath=//a[text()='Quote Summary']"
    str_checkbox_delete_products="xpath=//div[@class='DTFC_LeftHeadWrapper']/table/thead/tr[1]/th[2]/button"
    str_delete_product_yes_no="xpath=//div[@class='ui-dialog-buttonset']/following::span[text()='<<text__replace>>']"
    str_submit_button="xpath=//button[contains(text(),'Submit')]"


    ##manage components and product users
    str_manage_components = "xpath=//table[@id='PRPTable']//tbody/tr['<<text_replace>>']/td[9]//input[@value='Manage Components']"
    str_save_button = "xpath=//input[@value='Save']"
    str_quick_save = "xpath=//input[@value='Quick Save']"
    str_manage_users = "xpath=//table[@id='PRPTable']//tbody/tr['<<text_replace>>']/td[10]//input[@value='Manage Users']"
    str_contact_img = "xpath=//table[@id='new-contacts-table']//img[@class='custom-lookup-icon']"
    str_first_contact = "xpath=//table[@id='DataTables_Table_0']//tbody/tr[1]/td[1]/span"
    str_save_product_users = "xpath=//input[@value='Save Product Users']"
    str_Go_back_to_manage_components_and_productusers = "xpath=//input[@value='Go Back To Manage Components & Product Users']"
    str_go_to_quote = "xpath=//input[@value='Go to Quote']"
    str_summary_list = "xpath=//table[@id='PRPTable']//tr"
    str_input_btn = "xpath=//input[@id='phSearchInput']"
    str_search_btn = "xpath=//input[@id='phSearchButton']"
    str_first_quote_selection = "xpath=//a[text()='Quote for Techonomy_Opty_17th_May']"
    str_add_components = "xpath=//input[@value='Add Components']"
    str_selected_user = "xpath=//table[@id='PRPTable']//tbody/tr[<<text_replace>>]/td[10]/span"
    str_selected_component = "xpath=//table[@id='PRPTable']//tbody/tr[<<text_replace>>]/td[9]/span"
    str_show_entries_components="xpath=//*[@id='enterpriseAvlbCompTbl_length']/label/select"
    str_number_of_components="xpath=//table[@id='enterpriseAvlbCompTbl']/tbody/tr"
    str_first_contact_checkbox="xpath=(//input[@type='checkbox'])[1]"



    ##large quote fields
    str_opportunity_link = "xpath=//a[text()='HK_Techonomy_Opty_04_June_6']"
    str_new_contact_role = "xpath=//input[@name='newRole']"
    str_primary_contact_radio = "xpath=//input[@type='radio' and @value='0']"
    str_primary_contact_role = "xpath=//select[@id='role0']"
    str_save_button_contact_role = "xpath=//td[@class='pbButton']/input[@name='save']"
    str_reason_win_or_lost = "xpath=//span[text()='Reason Won/Lost']/parent::td[1]/following-sibling::td[1]/div"
    str_quote_business_type = "xpath=//td[text()='Quote Business Type']/parent::tr[1]//select"
    str_reason_dd_win_or_lost = "xpath=//td[text()='Reason Won/Lost']/parent::tr[1]//select"
    str_ok_dependent_fields = "xpath=//input[@value='OK']"
    str_save_button_large_quote_page = "xpath=//td[@class='pbButton']/input[@title='Save']"
    str_table_officelocations = "xpath=//table[@class='stripe row-border order-column nowrap dashedLine dataTable no-footer DTFC_Cloned']"

    ##Quote Line Confirmation
    str_quote_Line_Confir_text = "xpath=//p[text()='Will you be adding more than 90.0 products?']"
    str_quote_line_confirm_yes_or_no = "xpath=//span[text()='Yes']"

   #switching lightning - classic locators
    str_name_click = "xpath=//a[@id='globalHeaderNameMink']/span"
    str_light_click = "xpath=//li/a[text()='Switch to Lightning Experience']"
    str_image_click = "xpath=//span[@class='photoContainer forceSocialPhoto']"
    str_classic_click = "xpath=//a[text()='Switch to Salesforce Classic']"

    str_search_text = "xpath=//div[@class='searchBoxClearContainer']/input[@id='phSearchInput']"
    str_search_button_search = "xpath=//div[@id='searchButtonContainer']"
    # Search Results Page
    str_search_item_link = "xpath=(//table[@class='list']/descendant::a[contains(text(),'<<text_replace>>')])[1]"
    str_quote_detail_button = "xpath=//td[@id='topButtonRow']/input[@title='<<text_replace>>']"
    str_feedback_input = "xpath=//textarea[@name='lightningFeedbackPage:feedbackForm:commentText']"
    str_classic_selectopportunities = "xpath=//div[@class='hotListElement']//tr[2]//a"
    str_classic_selectplussign = "xpath=//img[contains(@alt,'All Tabs')]"
    # str_classic_selectquote = "xpath=//*[@id='bodyCell']/div[3]/div[2]/table/tbody/tr[57]/td[2]/a"
    str_classic_selectquote = "xpath=(//a[contains(.,'Quotes')])[2]"
    str_classic_selectrecentquote = "xpath=//*[@id='bodyCell']/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/th/a"
    str_classic_inputtext = "xpath=//div[@id='00N1W0000039lzX_ileinner']"
    str_classic_cancelquote = "xpath=//input[@value='Cancel']"

    str_classic_menuitem = "xpath=//*[@id='globalHeaderNameMink']/b"
    str_classic_setup = "xpath=//li/a[text()='Setup']"
    str_classic_manageusers = "xpath=//a[contains(.,'Manage Users')]"
    str_classic_profiles = "xpath=//*[@id='EnhancedProfiles_font']"
    str_classic_profilename = "xpath=//*[@id='00e1W000001BhcQ_ProfileName']/a/span"
    str_classic_assignedusers = "xpath=//*[@id='page:console:j_id78:j_id79:overview_header:j_id80:button_assigned_users']"
    str_classic_userinrelatedprofile = "xpath=//a[contains(@title,'Login - Record 1 - Olushi, Wale')]"