import base_types
import CorporateActionMovementReversalAdvice002V16

class SEEV_037_002_16():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnMvmntRvslAdvc"]
		@property
		def CorpActnMvmntRvslAdvc(self):
			return self._CorpActnMvmntRvslAdvc

		@CorpActnMvmntRvslAdvc.setter
		def CorpActnMvmntRvslAdvc(self, value):
			self._CorpActnMvmntRvslAdvc = value if type(value) != auto else self.make_default("CorpActnMvmntRvslAdvc")

		@CorpActnMvmntRvslAdvc.deleter
		def CorpActnMvmntRvslAdvc(self):
			del self._CorpActnMvmntRvslAdvc
			self._CorpActnMvmntRvslAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnMvmntRvslAdvc', type=CorporateActionMovementReversalAdvice002V16, min=1, max=1, mutex_group=None, array=False),
		))

