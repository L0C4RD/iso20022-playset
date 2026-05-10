from . import base_types
from ._CorporateActionNotification002V15 import CorporateActionNotification002V15

class SEEV_031_002_15():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnNtfctn"]
		@property
		def CorpActnNtfctn(self):
			return self._CorpActnNtfctn

		@CorpActnNtfctn.setter
		def CorpActnNtfctn(self, value):
			self._CorpActnNtfctn = value if type(value) != base_types.auto else self.make_default("CorpActnNtfctn")

		@CorpActnNtfctn.deleter
		def CorpActnNtfctn(self):
			del self._CorpActnNtfctn
			self._CorpActnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnNtfctn', type=CorporateActionNotification002V15, min=1, max=1, mutex_group=None, array=False),
		))

