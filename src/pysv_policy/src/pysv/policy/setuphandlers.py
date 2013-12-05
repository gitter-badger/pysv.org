# -*- coding: iso-8859-1 -*-
"""
pysv_policy setup handlers

@copyright: 2013 ReimarBauer
@license:  GPL
"""
from plone.app.controlpanel.security import ISecuritySchema


def importVarious(context):
    """Miscellanous steps import handle
    """
    # We check from our GenericSetup context whether we are running
    if context.readDataFile('pysv.policy_various.txt') is None:
        return  # Not this add-on

    portal = context.getSite()

    # Fetch the adapter
    security_adapter = ISecuritySchema(portal)
    security_adapter.set_enable_user_folders(True)
