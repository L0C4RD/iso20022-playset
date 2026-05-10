from . import base_types
import CorporateActionCancellationAdviceV13

class SEEV_039_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnCxlAdvc"]
		@property
		def CorpActnCxlAdvc(self):
			return self._CorpActnCxlAdvc

		@CorpActnCxlAdvc.setter
		def CorpActnCxlAdvc(self, value):
			self._CorpActnCxlAdvc = value if type(value) != auto else self.make_default("CorpActnCxlAdvc")

		@CorpActnCxlAdvc.deleter
		def CorpActnCxlAdvc(self):
			del self._CorpActnCxlAdvc
			self._CorpActnCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnCxlAdvc', type=CorporateActionCancellationAdviceV13, min=1, max=1, mutex_group=None, array=False),
		))

