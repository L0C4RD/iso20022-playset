from . import base_types
from .CorporateActionNarrativeV09 import CorporateActionNarrativeV09

class SEEV_038_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnNrrtv"]
		@property
		def CorpActnNrrtv(self):
			return self._CorpActnNrrtv

		@CorpActnNrrtv.setter
		def CorpActnNrrtv(self, value):
			self._CorpActnNrrtv = value if type(value) != auto else self.make_default("CorpActnNrrtv")

		@CorpActnNrrtv.deleter
		def CorpActnNrrtv(self):
			del self._CorpActnNrrtv
			self._CorpActnNrrtv = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnNrrtv', type=CorporateActionNarrativeV09, min=1, max=1, mutex_group=None, array=False),
		))

