from . import base_types
import ShareholdersIdentificationDisclosureResponseV03

class SEEV_047_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ShrhldrsIdDsclsrRspn"]
		@property
		def ShrhldrsIdDsclsrRspn(self):
			return self._ShrhldrsIdDsclsrRspn

		@ShrhldrsIdDsclsrRspn.setter
		def ShrhldrsIdDsclsrRspn(self, value):
			self._ShrhldrsIdDsclsrRspn = value if type(value) != auto else self.make_default("ShrhldrsIdDsclsrRspn")

		@ShrhldrsIdDsclsrRspn.deleter
		def ShrhldrsIdDsclsrRspn(self):
			del self._ShrhldrsIdDsclsrRspn
			self._ShrhldrsIdDsclsrRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrsIdDsclsrRspn', type=ShareholdersIdentificationDisclosureResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

