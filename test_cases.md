# ✅ Test Cases – The Planet Website

---

## Page Load & Title – Test Cases

| TC ID   | Description                                                       | Expected Result                                                                 |
|---------|-------------------------------------------------------------------|---------------------------------------------------------------------------------|
| PL_01   | Verify the page loads completely within 3s                        | The page loads fully within the expected time limit                            |
| PL_02   | Verify all page elements are rendered correctly after loading     | All elements (text, images, buttons, menus) appear correctly without distortion |
| PL_03   | Verify the page title is correct                                  | The page title matches the expected title (shown in browser tab)              |
| PL_04   | Verify title is displayed in browser tab                          | The correct title appears in the browser tab                                   |
| PL_05   | Verify no 404 or 500 error during page load                       | Page opens successfully without errors                                         |
| PL_06   | Verify the favicon is displayed                                   | Favicon appears next to the page title                                         |
| PL_07   | Verify no broken images or links on load                          | All images and links are visible and working properly                          |
| PL_08   | Verify page title is SEO-friendly                                 | Title is concise and under 60 characters                                       |
| PL_09   | Verify page reloads properly                                      | Page reloads and all elements/functions work properly                          |
| PL_10   | Verify proper loading on multiple browsers                        | Page behaves consistently on Chrome, Firefox, Edge, Safari                     |
| PL_11   | Verify proper loading on multiple devices                         | Layout and title are preserved on desktop, tablet, and mobile                  |
| PL_12   | Verify the title tag is present in HTML                           | `<title>` tag exists in the `<head>` section                                   |
| PL_13   | Verify page behavior on slow connection                           | Page handles slow loading or shows a loading indicator                         |
| PL_15   | Verify meta title matches browser title                           | Meta title tag matches browser-displayed title                                 |

---

## Header Section – Test Cases

| TC ID     | Description                                               | Expected Result                                                   |
|-----------|-----------------------------------------------------------|-------------------------------------------------------------------|
| Header_01 | Verify logo is visible                                    | Logo is displayed correctly                                       |
| Header_02 | Click logo redirects to homepage                          | Redirects to homepage                                             |
| Header_03 | Navigation menu items are visible                         | All nav links (Blog, Courses, Books, Contact) are present         |
| Header_04 | Navigation links redirect correctly                        | Each link opens the correct page                                  |
| Header_05 | Menu items highlight on hover                             | Hover effect works (e.g., color or underline change)              |
| Header_06 | Header is responsive on mobile                            | Collapses into hamburger menu and opens correctly                 |
| Header_07 | All header elements are aligned and styled correctly      | No misalignment or layout issues                                  |

---

## Home Page – UI & Accessibility Test Cases

| TC ID   | Description                                                  | Expected Result                                                   |
|---------|--------------------------------------------------------------|-------------------------------------------------------------------|
| HP_01   | Main heading is visible                                      | Hero title text is displayed                                      |
| HP_02   | Font style and size are consistent                           | Typography is consistent across the site                          |
| HP_03   | Button styles are consistent                                 | Same shape, hover, and color styling for all buttons              |
| HP_04   | No spelling or grammatical errors                            | Text content is correct                                           |
| HP_05   | Verify favicon is present                                     | Icon appears in browser tab                                       |
| HP_06   | All images have alt tags                                     | Alt text is present for accessibility                             |
| HP_07   | Website displays correctly on mobile                         | No horizontal scroll, all content fits                            |
| HP_08   | Content stacks vertically on smaller screens                 | Cards, buttons, and menus adjust layout                           |
| HP_09   | Text and images scale correctly                              | No overlapping or zoom issues                                     |
| HP_10   | Website is navigable using keyboard only                     | Tab, Enter work across all links and buttons                      |
| HP_11   | Contrast ratio is readable                                   | Text meets WCAG accessibility standards                           |
| HP_12   | Screen readers can identify page regions                     | ARIA roles/tags are used correctly (nav, header, footer, etc.)    |
| HP_13   | Disconnect internet and reload page                          | Displays appropriate offline error message                        |
| HP_14   | Broken links show fallback or 404 page                       | Custom error page or fallback message is shown                    |
| HP_15   | Check for JavaScript errors on page load                     | No red error messages in browser console                          |
| HP_16   | Subheading or description is readable                        | Subtitle or intro paragraph is visible                            |
| HP_17   | CTA buttons are visible and styled correctly                 | "Start Learning" or similar CTA buttons are shown                 |
| HP_18   | Clicking CTA buttons redirects properly                      | User is navigated to correct section or page                      |
| HP_19   | Background/hero image loads properly                         | No distortion; hero image is sharp                                |

---

## "Contact Us" Button (Homepage) – Test Cases

| TC ID   | Description                                                 | Expected Result                                                    |
|---------|-------------------------------------------------------------|--------------------------------------------------------------------|
| CUB01   | Verify "Contact Us" button is visible                       | Button is visible and readable                                     |
| CUB02   | Verify "Contact Us" button is clickable                     | Button is clickable                                                |
| CUB03   | Cursor changes to pointer on hover                          | Pointer icon appears                                               |
| CUB04   | Click "Contact Us" navigates to correct page                | Redirects to https://www.automatetheplanet.com/contact-us/         |
| CUB05   | Button is accessible via keyboard navigation                | Focusable and can be activated using Enter or Space                |
| CUB06   | Button styling and hover effect                             | Changes color or style on hover                                    |
| CUB07   | Button is responsive across screen sizes                    | Fully visible and usable on mobile, tablet, desktop                |

---

## Contact Page – Basic Load & Title Test Cases

| TC ID   | Description                                      | Expected Result                                                   |
|---------|--------------------------------------------------|-------------------------------------------------------------------|
| CP_01   | Verify contact page loads successfully           | Page loads with 200 status, no 404 or server error                |
| CP_02   | Verify page title and heading are correct        | Page title contains "Contact Us", and heading is visible          |

## Contact Us Form – Functional & Accessibility Test Cases

| TC ID   | Description                                                        | Expected Result                                                    |
|---------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| CP_03   | Verify the contact form is visible after the page loads           | Form and all its fields/buttons should appear properly             |
| CP_04   | Verify the form is centered/aligned as per design                 | Layout matches the design specification                            |
| CP_05   | Verify responsiveness of the form on mobile and tablet            | Form adapts and displays correctly on all screen sizes             |
| CP_06   | Verify all fields are present on the form                         | All form fields and submit button are visible                      |
| CP_07   | Verify Full Name accepts alphabetical characters                  | Should accept valid names only                                     |
| CP_08   | Verify Email field accepts valid email formats                    | Valid email is accepted (abc@domain.com)                           |
| CP_09   | Verify Email field rejects invalid formats                        | Invalid emails are rejected (e.g., abc@com, abc.com)               |
| CP_10   | Verify Phone Number field accepts only numeric input              | Only numbers should be accepted                                    |
| CP_11   | Verify Phone Number rejects alphabetic/special characters         | Validation message should appear                                   |
| CP_12   | Verify Message field allows long input (500-1000 characters)      | Can type and view long message                                     |
| CP_13   | Verify all fields are editable                                    | User can type and edit all fields                                  |
| CP_14   | Verify fields display placeholder text                            | Placeholder hints are shown correctly                              |
| CP_15   | Verify Submit button is disabled when required fields are empty   | Button should not be clickable or form should not submit           |
| CP_16   | Verify error message for missing Full Name                        | Displays “Full Name is required”                                   |
| CP_17   | Verify error message for missing Email                            | Displays “Email is required”                                       |
| CP_18   | Verify error message for missing Message                          | Displays “Message is required”                                     |
| CP_19   | Verify validation messages disappear after correction             | No errors shown after correcting inputs                            |
| CP_20   | Verify form submission with all valid inputs                      | Form submits and shows success confirmation                        |
| CP_21   | Verify form does not submit with invalid email                    | Error shown and submission blocked                                 |
| CP_22   | Verify form does not submit with empty fields                     | Error shown and submission blocked                                 |
| CP_23   | Verify success message or redirect after submission               | Message like “Thanks for contacting us” is shown                   |
| CP_25   | Verify Submit button is clickable only when required fields filled| Enabled only with valid inputs                                     |
| CP_26   | Verify error handling on server failure                           | Displays general error like “Something went wrong”                 |
| CP_27   | Verify form fields are properly labeled                           | Each input field has a corresponding label                         |
| CP_28   | Verify keyboard-only navigation through form                      | User can tab through and fill form without mouse                   |
| CP_29   | Verify screen reader reads form fields                            | Screen reader announces fields and placeholders/labels             |
| CP_30   | Verify Submit button has accessible name/ARIA label               | Screen reader reads “Submit” or similar label                      |

---

## "Read Full Story" Button & Article Page Test Cases

| TC ID     | Description                                                    | Expected Result                                                                 |
|-----------|----------------------------------------------------------------|---------------------------------------------------------------------------------|
| RFSB_01   | Verify "Read Full Story" button is visible                     | Button is displayed clearly on the preview/featured story                       |
| RFSB_02   | Verify button text is correct                                  | Text shows exactly "Read Full Story"                                            |
| RFSB_03   | Verify button is clickable                                     | Button can be clicked                                                           |
| RFSB_04   | Verify cursor changes to pointer on hover                      | Cursor changes to pointer icon                                                  |
| RFSB_05   | Verify clicking button navigates to the full story             | Redirects to correct article page URL                                           |
| RFSB_06   | Verify button is accessible via keyboard                       | Button can be focused and activated using Tab + Enter                          |
| RFSB_07   | Verify button styling and hover effects                        | Button changes color/style on hover                                             |
| RFSB_08   | Verify button is responsive across devices                     | Button remains visible and usable on all screen sizes                           |
| RFSB_09   | Verify full story page loads successfully                      | Page loads with status 200, no errors                                           |
| RFSB_10   | Verify page title is correct                                   | Title reflects story content (e.g., "Transforming Testing Efficiency...")       |
| RFSB_11   | Verify main heading (story title) is visible                   | Story title is displayed prominently                                            |
| RFSB_12   | Verify article text content is displayed                       | Full article text loads and is readable                                         |
| RFSB_13   | Verify internal links within story work                        | Links navigate correctly                                                        |
| RFSB_14   | Verify social share buttons are visible/functional             | Social icons are displayed and clickable                                        |
| RFSB_15   | Verify related/suggested articles are visible                  | Related articles/cards appear at bottom or sidebar                              |
| RFSB_16   | Verify page footer is intact                                   | Footer loads correctly                                                          |
| RFSB_17   | Verify scroll works smoothly                                   | User can scroll through full page without glitches                              |
| RFSB_18   | Verify back button returns to homepage/previous page           | Browser back works correctly                                                    |
| RFSB_19   | Verify page works on all major browsers                        | No issues in Chrome, Firefox, Edge, Safari                                      |
| RFSB_20   | Verify all images in story have alt text                       | Images contain descriptive `alt` attributes                                     |
| RFSB_21   | Verify text contrast meets accessibility standards             | Readable text/background contrast                                               |
| RFSB_22   | Verify keyboard navigation through page                        | Tab/Shift+Tab work through links and buttons                                   |
| RFSB_23   | Verify screen reader reads headings and content                | Story content and headings are read properly by screen readers                  |

## "Read Full Story" Page – Additional Test Cases

| TC ID     | Description                                                | Expected Result                                                    |
|-----------|------------------------------------------------------------|--------------------------------------------------------------------|
| RFSB_24   | Verify no broken HTML or CSS on the page                  | No layout or style issues                                         |
| RFSB_25   | Load page with slow internet                               | Page shows loading indicators or loads eventually                  |
| RFSB_26   | Try to open the story URL directly                         | Page loads correctly without errors                                |
| RFSB_27   | Disable JavaScript and load the page                       | Basic content shows or fallback appears                            |
| RFSB_28   | Test with browser zoom in/out                              | Layout adapts without breaking                                     |

---

## "Read Full Article" Button – Test Cases

| TC ID     | Description                                                  | Expected Result                                                    |
|-----------|--------------------------------------------------------------|--------------------------------------------------------------------|
| RFA_01    | Verify "Read Full Article" button is visible                 | Button is visible and readable                                     |
| RFA_02    | Verify button text is exactly "Read Full Article"           | Text matches expected label                                        |
| RFA_03    | Verify button is clickable                                   | Button can be clicked                                              |
| RFA_04    | Verify cursor changes to pointer on hover                    | Cursor changes appropriately                                       |
| RFA_05    | Verify clicking button navigates to the full article        | User is redirected to the article page                             |
| RFA_06    | Verify button is keyboard accessible                         | Can be focused and activated with Enter/Space                      |
| RFA_07    | Verify button styling and hover effects                      | Button changes style/color on hover                                |
| RFA_08    | Verify button is responsive on different screen sizes        | Button remains usable across devices                               |

---

## "Start the Test" Button & Yes/No Form – Test Cases

| TC ID     | Description                                                        | Expected Result                                                    |
|-----------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| STTB_01   | Verify "Start the Test" button is visible                         | Button is displayed and readable                                   |
| STTB_02   | Verify button text is exactly "Start the Test"                   | Text matches expected label                                        |
| STTB_03   | Verify button is clickable                                         | Button can be clicked                                              |
| STTB_04   | Verify cursor changes to pointer on hover                         | Cursor changes appropriately                                       |
| STTB_05   | Verify clicking the button opens the test form                    | Form with Yes/No questions appears                                 |
| STTB_06   | Verify button is keyboard accessible                              | Focusable and can be activated using Enter/Space                   |
| STTB_07   | Verify button styling and hover effects                           | Button changes style/color on hover                                |
| STTB_08   | Verify button is responsive on different screen sizes             | Fully visible on mobile, tablet, desktop                           |
| STTB_09   | Verify test form appears upon click                               | Form is shown                                                      |
| STTB_10   | Verify each question has Yes/No options                           | Only Yes and No available                                          |
| STTB_11   | Verify questions are labeled clearly                              | Easy to read and understand                                        |
| STTB_12   | Verify form has a submit button                                   | Submit button is visible and enabled                               |
| STTB_13   | Verify form is responsive on all screen sizes                     | Layout adapts properly                                             |
| STTB_14   | Verify user can select either Yes or No                           | Selection works per question                                       |
| STTB_15   | Verify user can't select both Yes and No for same question        | Only one option selectable                                         |
| STTB_16   | Verify validation if submission attempted without all answers     | Prompt appears for missing responses                               |
| STTB_17   | Verify successful submission with all answers                     | Form submits without errors                                        |
| STTB_18   | Verify confirmation/result after submission                       | Result/confirmation message shown                                  |
| STTB_19   | Verify user can change answers before submit                      | Can update selection                                               |
| STTB_20   | Verify keyboard-only selection and submission                     | Tab and Space/Enter work                                           |
| STTB_21   | Verify form labels are linked to inputs                           | Screen readers announce correctly                                  |
| STTB_22   | Verify contrast of text and buttons                               | High enough contrast, readable                                     |
| STTB_23   | Verify screen reader reads all form elements                      | ARIA roles or proper HTML used                                     |
| STTB_24   | Verify behavior on page reload mid-form                           | Inputs are preserved or warning is shown                           |
| STTB_25   | Verify stability under rapid clicking                             | No crash or abnormal behavior                                      |
| STTB_26   | Verify network failure during submit                              | Error or retry message appears                                     |
| STTB_27   | Verify form handles unexpected input                              | No crashes or undefined behavior                                   |

---

## Book a Meeting Section – Functional Test Cases

| TC ID     | Description                                                  | Expected Result                                                    |
|-----------|--------------------------------------------------------------|--------------------------------------------------------------------|
| BAMB01    | Verify "Book a Meeting" section is visible                   | Section is displayed and labeled clearly                           |
| BAMB02    | Verify responsiveness of booking section                     | Layout adapts on desktop, tablet, and mobile                       |
| BAMB03    | Verify date picker blocks past dates                         | Past dates cannot be selected                                      |
| BAMB04    | Verify time picker restricts invalid times                   | Only valid meeting times selectable                                |
| BAMB05    | Verify user can pick valid meeting slot                      | No conflicts; valid slot is picked                                 |
| BAMB06    | Verify "Edit" icon appears after selecting date/time         | Edit icon is visible after selection                               |
| BAMB07    | Clicking "Edit" scrolls to booking form top                  | Smooth scroll back to start of form                                |
| BAMB08    | User can re-select different date/time after clicking Edit   | User can change previous selection                                 |
| BAMB09    | All booking input fields are visible                         | Fields like Name, Email, Date, Time are shown                      |
| BAMB10    | Placeholder text/hints are present in fields                 | Helpful placeholder text appears                                   |
| BAMB11    | Verify form fields/buttons are accessible via keyboard              | User can tab through inputs and activate buttons                  |
| BAMB12    | Verify name fields accept valid characters                          | Letters, spaces, punctuation accepted                             |
| BAMB13    | Verify email field accepts only valid formats                       | Invalid email shows error message                                 |
| BAMB15    | Verify input fields have max character limits                       | Limit enforced or warning shown                                   |
| BAMB16    | Verify required fields must be filled before submission             | Error shown or submit disabled if empty                           |
| BAMB17    | Verify handling of unusual characters                               | No crash or error                                                 |
| BAMB18    | Verify "Request" button is visible                                  | Button is clearly displayed and enabled                           |
| BAMB19    | Verify successful form submission with valid inputs                 | Form submits and processes correctly                              |
| BAMB20    | Verify confirmation message after successful booking                | Confirmation or success notification shown                        |
| BAMB21    | Verify form blocks invalid/incomplete submissions                   | Validation prevents form submit                                   |
| BAMB22    | Verify correct data sent to backend                                 | Backend receives correct data                                     |
| BAMB23    | Verify form clears after submission                                 | Inputs reset or cleared                                           |
| BAMB24    | Verify accessibility contrast of inputs and labels                  | Text/buttons visible and readable                                 |
| BAMB25    | Verify error messages are helpful                                   | Error explains what went wrong                                    |
| BAMB26    | Verify screen reader compatibility                                  | Reader announces form elements                                    |
| BAMB27    | Verify submission with internet loss                                | Retry or error shown                                              |
| BAMB28    | Verify form handles rapid multiple submissions                      | Duplicate booking prevented                                       |
| BAMB29    | Verify refresh during filling form                                  | Inputs preserved or warning shown                                 |
| BAMB30    | Verify booking restricted on weekends/holidays                      | Calendar blocks those days                                        |

---

## Footer Section – Test Cases

| TC ID       | Description                                                  | Expected Result                                                    |
|-------------|--------------------------------------------------------------|--------------------------------------------------------------------|
| FOOTER_01   | Footer is visible on all pages                               | Displayed consistently                                             |
| FOOTER_02   | All expected footer elements are present                      | Icons, links, and text are visible                                |
| FOOTER_03   | Footer text content is correct                                | Matches specified content                                         |
| FOOTER_04   | Font styling is consistent                                    | Matches branding                                                  |
| FOOTER_05   | Footer background color is correct                            | Matches design                                                    |
| FOOTER_06   | Footer layout is aligned properly                             | No misalignment                                                   |
| FOOTER_07   | All footer links are visible                                  | Links appear clearly                                              |
| FOOTER_08   | Footer links are clickable                                    | Links open as expected                                            |
| FOOTER_09   | Links navigate to correct pages                               | Target pages open correctly                                       |
| FOOTER_10   | Link behavior matches spec (new tab/same tab)                 | Opens as intended                                                 |
| FOOTER_11   | Hover effects on links work                                   | Color or style changes on hover                                   |
| FOOTER_12   | Footer links are keyboard accessible                          | Can tab through and activate links                                |
| FOOTER_13   | Social icons are visible                                      | All expected social icons shown                                   |
| FOOTER_14   | Social icons are clickable                                    | Icons open links                                                  |
| FOOTER_15   | Social icons link to correct social pages                     | Correct social accounts open                                      |
| FOOTER_16   | Social icons open in new tab                                  | Does not navigate away from site                                  |
| FOOTER_17   | Hover effect on social icons                                  | Icons change color or style                                       |
| FOOTER_18   | Icons are keyboard accessible                                 | Can be focused and activated                                     |
| FOOTER_19   | Footer responsive on all screen sizes                         | Layout adjusts for mobile/tablet                                  |
| FOOTER_20   | Text and layout do not break on small screens                 | Readable and accessible                                           |
| FOOTER_21   | Footer works on all browsers                                  | Chrome, Firefox, Safari, Edge                                     |
| FOOTER_22   | Footer text contrast meets accessibility standards            | Text is readable                                                  |
| FOOTER_23   | Footer links have aria-labels                                 | Announced by screen reader properly                               |
| FOOTER_24   | Keyboard navigation within footer works                       | Tab moves between all links/icons                                 |
| FOOTER_25   | Footer content is readable by screen readers                  | All elements are announced                                        |
| FOOTER_26   | Footer copyright year is updated                              | Year is current (e.g., 2025)                                      |
| FOOTER_27   | No broken links in footer                                     | All return 200 OK                                                 |
| FOOTER_28   | Footer doesn't overlap page content                           | Footer stays at bottom                                           |
| FOOTER_29   | Privacy/Contact links work properly                           | Navigate to correct pages                                         |
| FOOTER_30   | Copyright text is present                                     | Correct year and company shown                                   |

---

## Web Automation Page – Test Cases

| TC ID   | Description                                                     | Expected Result                                              |
|---------|-----------------------------------------------------------------|--------------------------------------------------------------|
| WP_01   | Verify page loads successfully without errors                   | Page loads fully with no broken elements                     |
| WP_02   | Verify page title is correct and matches content                | Title reflects "Web Automation Services"                     |
| WP_03   | Verify header section is visible and contains logo/nav         | Header is displayed correctly                                |
| WP_04   | Verify main heading (H1) is visible                             | Heading is prominent and accurate                            |
| WP_05   | Verify textual content is readable and error-free               | Clear, legible, no spelling mistakes                         |
| WP_06   | Verify images/icons related to web automation are present       | Images/icons load correctly                                  |
| WP_07   | Verify presence of CTA buttons like “Contact Us”, “Book…”       | Buttons visible and labeled appropriately                    |
| WP_08   | Verify layout/spacing consistency                               | No overlaps, proper spacing                                  |
| WP_11   | Verify “Contact Us” button navigates to contact page            | Redirects to contact form/page                               |
| WP_12   | Verify CTA buttons respond to clicks                            | Buttons perform expected actions                             |
| WP_13   | Verify internal links navigate correctly                        | Links open correct pages                                     |
| WP_14   | Verify external links open in new tabs                          | Opens in new browser tab                                     |
| WP_15   | Verify current page is highlighted in menu                      | Menu highlights current page                                 |
| WP_16   | Verify footer links work from this page                         | All links navigate correctly                                 |
| WP_17   | Verify interactive elements (accordion/tabs) work properly      | Expand/collapse or switch content works                      |
| WP_18   | Verify layout adjusts across screen sizes                       | Responsive layout maintained                                 |
| WP_19   | Verify text/images/buttons resize or reposition properly        | No overlapping, everything accessible                        |
| WP_20   | Verify navigation collapses into hamburger menu                 | Hamburger menu visible/functional on small screens           |
| WP_21   | Verify semantic HTML tags used correctly                        | Logical, accessible structure                                |
| WP_22   | Verify text/button color contrast meets accessibility standards | Text/buttons are clearly visible                             |
| WP_23   | Verify all images have descriptive alt text                     | alt attributes are present                                   |
| WP_24   | Verify keyboard accessibility of interactive elements           | All links/buttons usable via keyboard                        |
| WP_25   | Verify screen reader can read content correctly                 | Content announced accurately by screen readers               |

---

## Automated Testing Unleashed Page (ATUP) – Test Cases

| TC ID     | Description                                                   | Expected Result                                                  |
|-----------|---------------------------------------------------------------|------------------------------------------------------------------|
| ATUP_01   | Verify page load time is under 3s                             | Loads quickly                                                    |
| ATUP_02   | Verify media is optimized                                     | Images/media load fast                                           |
| ATUP_03   | Verify meta title/description are correct                     | SEO tags are correct                                             |
| ATUP_04   | Verify SEO-friendly heading structure                         | H1, H2 structured logically                                      |
| ATUP_05   | Verify URL is SEO-friendly                                    | URL is clean, descriptive                                        |
| ATUP_06   | Verify page loads over HTTPS                                  | URL begins with https://                                         |
| ATUP_07   | Verify no sensitive info is exposed                           | No security risks present                                        |
| ATUP_08   | Verify page loads fully without errors                        | No missing images/scripts                                        |
| ATUP_09   | Verify title matches resource/book title                      | Title is accurate and relevant                                   |
| ATUP_10   | Verify header/footer are present                              | Both load correctly                                              |
| ATUP_11   | Verify main heading (H1) is visible                           | H1 is prominent                                                  |
| ATUP_12   | Verify text is readable and formatted                         | Text is clear and styled properly                               |
| ATUP_13   | Verify images/book covers load correctly                      | Images are visible and relevant                                 |
| ATUP_14   | Verify font style and size is consistent                      | Matches website design                                           |
| ATUP_15   | Verify internal links work properly                           | Correct navigation                                               |
| ATUP_16   | Verify external links open in new tab                         | Opens in new tab                                                 |
| ATUP_17   | Verify “Purchase EN Books” buttons redirect correctly         | Buttons navigate to correct pages                               |
| ATUP_20   | Verify purchase button goes to order page                     | Opens purchase/checkout page                                    |
| ATUP_29   | Verify images have alt attributes                             | Descriptive alt text present                                    |
| ATUP_30   | Verify contrast meets WCAG standards                          | Text and button contrast accessible                             |
| ATUP_31   | Verify keyboard navigability of all elements                  | Keyboard usable for all links/buttons                           |
| ATUP_32   | Verify screen reader compatibility                            | All content is readable via screen readers                      |
| ATUP_33   | Verify page load time under 3s                                | Loads quickly                                                    |
| ATUP_34   | Verify media is optimized                                     | Media loads promptly                                             |
| ATUP_35   | Verify meta title/desc tags are set properly                  | Meta tags exist and match content                               |
| ATUP_36   | Verify heading hierarchy is logical                           | Proper nesting (H1 > H2 > H3...)                                |
| ATUP_37   | Verify URL is SEO-friendly                                    | Clean and keyword-rich                                           |
| ATUP_38   | Verify HTTPS is used                                          | URL begins with https://                                         |
| ATUP_39   | Verify no insecure data exposed                               | Payment/personal info protected                                 |
| ATUP_40   | Verify all links/images load correctly                        | No 404 or broken elements                                       |
| ATUP_41   | Verify content is up to date                                  | Latest version shown                                             |
| ATUP_42   | Verify social share buttons function                          | Sharing works as expected                                       |

---

## Resources Page – Test Cases

| TC ID     | Description                                                   | Expected Result                                                  |
|-----------|---------------------------------------------------------------|------------------------------------------------------------------|
| RP_01     | Verify page loads without errors                              | Page loads fully                                                 |
| RP_02     | Verify page title is "Resources"                              | Title matches                                                    |
| RP_03     | Verify header/footer are present                              | Displayed correctly                                               |
| RP_04     | Verify H1 heading is visible                                  | Heading “Resources” is clear                                     |
| RP_05     | Verify intro text and descriptions are readable               | No typos, all content visible                                    |
| RP_06     | Verify images/icons load correctly                            | No broken images                                                 |
| RP_07     | Verify font styles are consistent                             | Matches brand style guide                                        |
| RP_08     | Verify search filters resources properly                      | Results update dynamically                                       |
| RP_09     | Verify all resource links work                                | Navigates to correct pages                                       |
| RP_10     | Verify nav menu links work                                    | Opens correct sections                                           |
| RP_11     | Verify "Learn More" buttons work                              | Navigates to correct resource page                               |
| RP_12     | Verify “Download this paper” button works                     | Downloads without error                                          |
| RP_13     | Verify downloadable content starts download                   | File starts downloading                                          |
| RP_14     | Verify “Download Cheat Sheet” works                           | File downloads or opens                                          |
| RP_15     | Verify external links open in new tab                         | Does not replace current tab                                     |
| RP_16     | Verify layout adapts across screen sizes                      | Responsive design confirmed                                      |
| RP_17     | Verify resource layout adjusts on smaller screens             | No overlap, clean layout                                         |
| RP_18     | Verify images have descriptive alt text                       | All images tagged appropriately                                  |
| RP_19     | Verify contrast for text and buttons is sufficient            | Readable by visually impaired users                              |
| RP_20     | Verify keyboard navigation across all links/buttons           | Tab/Enter works throughout                                       |
| RP_21     | Verify screen reader can read page content                    | All elements announced                                           |
| RP_22     | Verify acceptable page load time (< 3s)                       | Quick and complete load                                          |
| RP_23     | Verify media/scripts optimized for performance                | Smooth page performance                                          |
| RP_24     | Verify meta tags are present                                  | Meta title and description relevant                             |
| RP_25     | Verify heading tags used in logical order                     | H1, H2, H3 nesting is correct                                    |
| RP_26     | Verify URL is SEO-friendly                                    | Clean and keyword rich                                           |
| RP_27     | Verify HTTPS is used                                          | Secure page access                                               |
| RP_28     | Verify no sensitive info exposed                              | Safe from data leaks                                             |
| RP_29     | Verify no broken links/images                                 | All elements work correctly                                      |
