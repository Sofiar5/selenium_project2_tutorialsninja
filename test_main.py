import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.regression
@pytest.mark.smoke
@allure.feature("Menu Items")
@allure.story("Test main menu items")
def test_menu_item(driver):
    with allure.step("Open the demo page"):
        driver.get("https://tutorialsninja.com/demo/")

    expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs", "Cameras", "MP3 Players"]

    with allure.step(f"Click on menu item: {expected_menu_items[0]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_item1.click()

    with allure.step(f"Click on menu item: {expected_menu_items[1]}"):
        menu_item2 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_item2.click()

    with allure.step(f"Click on menu item: {expected_menu_items[2]}"):
        menu_item3 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_item3.click()

    with allure.step(f"Click on menu item: {expected_menu_items[3]} and verify header"):
        menu_item4 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_item4.click()
        assert driver.find_element(By.TAG_NAME, "h2").text == expected_menu_items[3]

    with allure.step(f"Click on menu item: {expected_menu_items[4]} and verify header"):
        menu_item5 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
        menu_item5.click()
        assert driver.find_element(By.TAG_NAME, "h2").text == expected_menu_items[4]

    with allure.step(f"Click on menu item: {expected_menu_items[5]} and verify header"):
        menu_item6 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
        menu_item6.click()
        assert driver.find_element(By.TAG_NAME, "h2").text == expected_menu_items[5]

    with allure.step(f"Click on menu item: {expected_menu_items[6]} and verify header"):
        menu_item7 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_item7.click()
        assert driver.find_element(By.TAG_NAME, "h2").text == expected_menu_items[6]

    with allure.step(f"Click on menu item: {expected_menu_items[7]}"):
        menu_item8 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
        menu_item8.click()

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize("menu_locator, submenu_locator, result_text",[
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH,'//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            'PC'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH,'//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            'Mac'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH,'//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            'Macs'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH,'//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            'Windows'
    )
])
@allure.feature("Nested Menu")
@allure.story("Test nested menus")
def test_nested_menu(driver,menu_locator, submenu_locator, result_text):
    with allure.step("Open the demo page"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step(f"Hover and select submenu: {result_text}"):
        menu = driver.find_element(*menu_locator)
        submenu = driver.find_element(*submenu_locator)
        ActionChains(driver).move_to_element(menu).click(submenu).perform()

    with allure.step(f"Verify text: {result_text}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == result_text

@pytest.mark.smoke
@allure.feature("Search Product")
@allure.story("Search for a product")
def test_search_product(driver):
    with allure.step("Open the demo page"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Search for 'MacBook'"):
        search = driver.find_element(By.NAME, "search")
        search.send_keys('MacBook')
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
        button.click()

    with allure.step("Verify search results"):
        products = driver.find_elements(By.TAG_NAME, 'h4')
        new_list = [elem.text for elem in products if "MacBook" in elem.text]
        assert len(products) == len(new_list)

@pytest.mark.regression
@pytest.mark.smoke
@allure.feature("Cart")
@allure.story("Add to cart")
def test_add_to_cart(driver):
    with allure.step("Open the demo page"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Add product to cart"):
        product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        product.click()

    with allure.step("Wait for success message"):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.alert.alert-success'))
        )
        assert "Success: You have added" in success_message.text

    with allure.step("Verify cart is updated"):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "1 item(s)")
        )
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cart"))
        )
        cart_button.click()

    with allure.step("Wait for cart dropdown to load and verify contents"):
        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.pull-right"))
        )
        assert "MacBook" in cart_contents.text, "Expected 'MacBook' in cart, but got"

@pytest.mark.regression
@pytest.mark.smoke
@allure.feature("Slider")
@allure.story("Test slider functionality")
def test_slider_functionality(driver):
    with allure.step("Open the demo page"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Locate the slider element"):
        slider = driver.find_element(By.CLASS_NAME, "swiper-container")
        assert slider.is_displayed(), "Slider is not visible on the page"

    with allure.step("Locate the first active slide"):
        first_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        first_slide_src = first_slide.get_attribute("src")

    with allure.step("Interact with the slider (right arrow)"):
        next_arrow = driver.find_element(By.CLASS_NAME, "swiper-button-next")
        ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

    with allure.step("Wait for the slider to change"):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(first_slide)
        )

    with allure.step("Locate the new active slide and verify that it has changed"):
        new_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        new_slide_src = new_slide.get_attribute("src")
        assert first_slide_src != new_slide_src, "Slider did not move to the next image"

    with allure.step("Test the left arrow to return to the first slide"):
        prev_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-prev')
        prev_arrow.click()

    with allure.step("Wait for the slider to return to the first slide"):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(new_slide)
        )

    with allure.step("Verify that the slider returned to the first image"):
        reverted_slide_src = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img").get_attribute("src")
        assert reverted_slide_src == first_slide_src, "Slider did not return to the first image"

@pytest.mark.regression
@pytest.mark.smoke
@allure.feature("Wishlist")
@allure.story("Add to Wishlist")
def test_wish_list(driver,login):
    with allure.step("Open the demo page"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Add a product to the wishlist"):
        wishlist_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]/i')
        wishlist_button.click()

    with allure.step("Navigate to the wishlist page"):
        wishlist_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist-total"]'))
        )
        wishlist_link.click()

    with allure.step("Wait for the wishlist page to load and check for the product"):
        wishlist_contents = driver.find_element(By.LINK_TEXT, 'MacBook')
        assert "MacBook" in wishlist_contents.text, "MacBook not found in wishlist"

@pytest.mark.regression
@pytest.mark.smoke
@allure.feature("Bottom Menu")
@allure.story("Verify bottom menu links")
def test_bottom_menu(driver):
    with allure.step("Open the demo page"):
        driver.get("https://tutorialsninja.com/demo/")

    expected_menu_items = ["About Us", "Delivery Information", "Privacy Policy", "Terms & Conditions",
                           "Contact Us","Returns", "Site Map","Brands","Gift Certificates","Affiliate",
                           "Specials","Order History", "Wish List", "Newsletter"]

    for el in expected_menu_items:
        with allure.step(f"Click on menu item: {el}"):
            menu_item = driver.find_element(By.LINK_TEXT, el)
            menu_item.click()

        with allure.step(f"Verify page content for {el}"):
            h_text = driver.find_element(By.ID, "content").text

            if el not in ["Brands", "Gift Certificates", "Specials"]:
                assert el in h_text, f"Expected {el} in page header, but got {h_text}"
            else:
                assert el[:-1] in h_text, f"Expected {el} in page header, but got {h_text}"

@pytest.mark.regression
@pytest.mark.smoke
@allure.feature("Bottom Menu")
@allure.story("Verify 'My Account' from bottom menu")
def test_bottom_menu_my_account(driver):
    with allure.step("Open the demo page"):
        driver.get("https://tutorialsninja.com/demo/")

    expected_menu_item = "My Account"

    with allure.step("Click on the 'My Account' menu item"):
        menu_item = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[4]/ul/li[1]/a')
        menu_item.click()

    with allure.step("Verify 'My Account' page content"):
        h_text = driver.find_element(By.ID, "content").text
        assert expected_menu_item in h_text, f"Expected {expected_menu_item} in page header, but got {h_text}"
