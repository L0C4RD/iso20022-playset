import base_types
import CorporateActionCancellationAdvice002V13

class SEEV_039_002_13():

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
			base_types.FieldEntry(name='CorpActnCxlAdvc', type=CorporateActionCancellationAdvice002V13, min=1, max=1, mutex_group=None, array=False),
		))

