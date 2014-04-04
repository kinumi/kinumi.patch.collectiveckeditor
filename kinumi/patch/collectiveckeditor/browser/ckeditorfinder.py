from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.ckeditor.browser.ckeditorfinder import CKFinder as Finder


class CKFinder(Finder):
    """
    Custom Finder class for CKEditor
    (patched)
        - change "self.allowimagesizeselection" to False.
        - remove "resolveuid" from "selectCKEditorItem" JS function.
        - override "finder.pt"
    """

    template = ViewPageTemplateFile('finder.pt')

    def __init__(self, context, request):
        super(CKFinder, self).__init__(context, request)
        self.allowimagesizeselection = False

    def __call__(self):
        super(CKFinder, self).__call__()
        return self.template()

    def get_jsaddons(self):
        request = aq_inner(self.request)
        session = request.get('SESSION', {})
        CKEditorFuncNum = session.get('CKEditorFuncNum', '')

        jsstring = """
selectCKEditorItem = function (selector, title, image_preview) {
 image_preview = (typeof image_preview != "undefined") ? image_preview : false;
 if (image_preview) selector = selector + '/image_preview' ;
 window.opener.CKEDITOR.tools.callFunction( %s, selector );
 window.close();
};
Browser.selectItem = selectCKEditorItem;
             """ % CKEditorFuncNum

        return jsstring
