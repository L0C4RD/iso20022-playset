import base_types
import ATMDepositCompletionAdviceV02

class CATP_014_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMDpstCmpltnAdvc"]
		@property
		def ATMDpstCmpltnAdvc(self):
			return self._ATMDpstCmpltnAdvc

		@ATMDpstCmpltnAdvc.setter
		def ATMDpstCmpltnAdvc(self, value):
			self._ATMDpstCmpltnAdvc = value if type(value) != auto else self.make_default("ATMDpstCmpltnAdvc")

		@ATMDpstCmpltnAdvc.deleter
		def ATMDpstCmpltnAdvc(self):
			del self._ATMDpstCmpltnAdvc
			self._ATMDpstCmpltnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDpstCmpltnAdvc', type=ATMDepositCompletionAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))

