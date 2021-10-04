import pytest
from yossi_mongo_object import YossiMongoObject as OBJ
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('.\mongo_steps.feature', 'changing the data')
def test_changing_the_data():
    pass

@pytest.fixture(scope='function')
def context():
    return {}


@given('the mail is yossigoldberg2@gmail.com')
def the_mail_is_garygmailcom(context):
    """the mail is yossigoldberg2@gmail.com."""
    context['obj'] = OBJ()
    context['obj'].edit_mongo_mail("yossigoldberg2@gmail.com")

@when('I change mail to yossiyossi@gmail')
def i_change_mail_to_garygarygmail(context):
    """I change mail to yossiyossi@gmail."""
    context["obj"].edit_mongo_mail("yossiyossi@gmail")


@then('mongoDB mail also is updated')
def mongodb_mail_also_is_updated(context):
    context["obj"].navigate_to_mongo_express_mail()
    assert (context["obj"].get_mongo_express_mail() == 'yossiyossi@gmail')