#& Learning about selectors => 

'''
ID Locator → By.ID, "id_value"

Name Locator → By.NAME, "name_value"

Link Text Locator → By.LINK_TEXT, "Exact Link Text"

Partial Link Text Locator → By.PARTIAL_LINK_TEXT, "Partial Text"

CSS – Tag and ID → tag#id

CSS – Tag and Class → tag.class

CSS – Tag and Attribute → tag[attribute='value']

CSS – Tag, Class, and Attribute → tag.class[attribute='value']

CSS – Inner Text (Contains) → tag:contains("innertext")

XPath – Relative XPath → //tag[@attributename='attributevalue']

XPath – Absolute XPath → /html/body/.../tag 

'''

'''🚀 Selenium Locators – Quick Revision
1️⃣ ID Locator

👉 By.ID, "id_value"

2️⃣ Name Locator

👉 By.NAME, "name_value"

3️⃣ Link Text

👉 By.LINK_TEXT, "Exact Link Text"

4️⃣ Partial Link Text

👉 By.PARTIAL_LINK_TEXT, "Partial Text"

🎯 CSS Selectors
5️⃣ Tag and ID

👉 tag#id

Example:
input#username

6️⃣ Tag and Class

👉 tag.class

Example:
input.form-control

7️⃣ Tag and Attribute

👉 tag[attribute='value']

Example:
input[type='text']

8️⃣ Tag + Class + Attribute

👉 tag.class[attribute='value']

Example:
input.form-control[type='text']

9️⃣ Inner Text (CSS – jQuery style)

👉 tag:contains("innertext")

⚠ Not supported directly in Selenium CSS

🔎 XPath
🔟 Relative XPath (Recommended)

👉 //tag[@attributename='attributevalue']

Example:
//input[@id='username']

1️⃣1️⃣ Absolute XPath (Avoid)

👉 /html/body/.../tag

'''