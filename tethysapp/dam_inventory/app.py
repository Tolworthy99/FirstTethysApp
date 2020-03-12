from tethys_sdk.base import TethysAppBase, url_map_maker


class DamInventory(TethysAppBase):
    """
    Tethys app class for Tolworthy App.
    """

    name = 'Tolworthy App'
    index = 'dam_inventory:home'
    icon = 'dam_inventory/images/icon.gif'
    package = 'dam_inventory'
    root_url = 'dam-inventory'
    color = '#8B0000'
    description = '"An App about me"'
    tags = '"CEEN514","FirstApp"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='dam-inventory',
                controller='dam_inventory.controllers.home'
            ),
            UrlMap(
                name = 'mappage',
                url='dam-inventory/mappage',
                controller='dam_inventory.controllers.mappage'
            ),
            UrlMap(
                name = 'form_page',
                url='dam-inventory/form_page',
                controller='dam_inventory.controllers.form_page'
            ),
            UrlMap(
                name = 'list_dams',
                url='dam-inventory/list_dams',
                controller='dam_inventory.controllers.list_dams'
            ),
            UrlMap(
                name = 'dam_map',
                url='dam-inventory/dam_map',
                controller='dam_inventory.controllers.dam_map'
            )
        )

        return url_maps
