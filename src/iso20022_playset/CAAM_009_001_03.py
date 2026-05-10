import base_types
import ATMReconciliationAdviceV03

class CAAM_009_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMRcncltnAdvc"]
		@property
		def ATMRcncltnAdvc(self):
			return self._ATMRcncltnAdvc

		@ATMRcncltnAdvc.setter
		def ATMRcncltnAdvc(self, value):
			self._ATMRcncltnAdvc = value if type(value) != auto else self.make_default("ATMRcncltnAdvc")

		@ATMRcncltnAdvc.deleter
		def ATMRcncltnAdvc(self):
			del self._ATMRcncltnAdvc
			self._ATMRcncltnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRcncltnAdvc', type=ATMReconciliationAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))

