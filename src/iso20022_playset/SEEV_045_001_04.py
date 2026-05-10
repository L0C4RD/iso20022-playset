from . import base_types
from .ShareholdersIdentificationDisclosureRequestV04 import ShareholdersIdentificationDisclosureRequestV04

class SEEV_045_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ShrhldrsIdDsclsrReq"]
		@property
		def ShrhldrsIdDsclsrReq(self):
			return self._ShrhldrsIdDsclsrReq

		@ShrhldrsIdDsclsrReq.setter
		def ShrhldrsIdDsclsrReq(self, value):
			self._ShrhldrsIdDsclsrReq = value if type(value) != auto else self.make_default("ShrhldrsIdDsclsrReq")

		@ShrhldrsIdDsclsrReq.deleter
		def ShrhldrsIdDsclsrReq(self):
			del self._ShrhldrsIdDsclsrReq
			self._ShrhldrsIdDsclsrReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrsIdDsclsrReq', type=ShareholdersIdentificationDisclosureRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

