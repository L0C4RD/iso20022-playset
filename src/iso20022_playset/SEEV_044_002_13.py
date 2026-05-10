import base_types
import CorporateActionMovementPreliminaryAdviceCancellationAdvice002V13

class SEEV_044_002_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnMvmntPrlimryAdvcCxlAdvc"]
		@property
		def CorpActnMvmntPrlimryAdvcCxlAdvc(self):
			return self._CorpActnMvmntPrlimryAdvcCxlAdvc

		@CorpActnMvmntPrlimryAdvcCxlAdvc.setter
		def CorpActnMvmntPrlimryAdvcCxlAdvc(self, value):
			self._CorpActnMvmntPrlimryAdvcCxlAdvc = value if type(value) != auto else self.make_default("CorpActnMvmntPrlimryAdvcCxlAdvc")

		@CorpActnMvmntPrlimryAdvcCxlAdvc.deleter
		def CorpActnMvmntPrlimryAdvcCxlAdvc(self):
			del self._CorpActnMvmntPrlimryAdvcCxlAdvc
			self._CorpActnMvmntPrlimryAdvcCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnMvmntPrlimryAdvcCxlAdvc', type=CorporateActionMovementPreliminaryAdviceCancellationAdvice002V13, min=1, max=1, mutex_group=None, array=False),
		))

