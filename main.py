import site_navigation



# create the main function 

def main():
    site_navigation.navigate_site()
    indicies  = site_navigation.search_string_text_file('libs-ui-src-ProductCard__title--LgNam')
    items = site_navigation.menu_items(indicies)
    


