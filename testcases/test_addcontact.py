from page.app import App


class TestAddContact:

    def setup(self):
        self.app = App()
        # self.app.start()
        self.main = self.app.start().main()

    def teardown(self):
        pass


    def test_addcontact(self):
        toast_info = self.main.goto_contacts().goto_add_member().goto_contactadd().send_message().click_save()
        assert '成功' in toast_info.get_toast()