from . import base_types
from .ShareholdersIdentificationDisclosureRequestCancellationAdviceV01 import ShareholdersIdentificationDisclosureRequestCancellationAdviceV01

class SEEV_046_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ShrhldrsIdDsclsrReqCxlAdvc"]
		@property
		def ShrhldrsIdDsclsrReqCxlAdvc(self):
			return self._ShrhldrsIdDsclsrReqCxlAdvc

		@ShrhldrsIdDsclsrReqCxlAdvc.setter
		def ShrhldrsIdDsclsrReqCxlAdvc(self, value):
			self._ShrhldrsIdDsclsrReqCxlAdvc = value if type(value) != base_types.auto else self.make_default("ShrhldrsIdDsclsrReqCxlAdvc")

		@ShrhldrsIdDsclsrReqCxlAdvc.deleter
		def ShrhldrsIdDsclsrReqCxlAdvc(self):
			del self._ShrhldrsIdDsclsrReqCxlAdvc
			self._ShrhldrsIdDsclsrReqCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrsIdDsclsrReqCxlAdvc', type=ShareholdersIdentificationDisclosureRequestCancellationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

