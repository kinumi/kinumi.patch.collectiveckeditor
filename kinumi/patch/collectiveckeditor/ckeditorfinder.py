from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from collective.ckeditor.browser.ckeditorfinder import CKFinder as Finder

class CKFinder(Finder):
    """
    Custom Finder class for CKEditor
    """
    
    def get_jsaddons(self):
        """
        redefine selectItem method
        in js string
        """
        request = aq_inner(self.request)
        session = request.get('SESSION', {})
        CKEditorFuncNum = session.get('CKEditorFuncNum', '')

        jsstring = """
selectCKEditorItem = function (selector, title, image_preview) {
 image_preview = (typeof image_preview != "undefined") ? image_preview : false;
 if (image_preview) selector = selector + '/image_preview' ;
 window.opener.CKEDITOR.tools.callFunction( %s, 'resolveuid/' + selector );
 window.close();
};
Browser.selectItem = selectCKEditorItem;
             """ % CKEditorFuncNum

        return jsstring
