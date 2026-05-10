import base_types
import ATMWithdrawalCompletionAdviceV03

class CATP_003_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMWdrwlCmpltnAdvc"]
		@property
		def ATMWdrwlCmpltnAdvc(self):
			return self._ATMWdrwlCmpltnAdvc

		@ATMWdrwlCmpltnAdvc.setter
		def ATMWdrwlCmpltnAdvc(self, value):
			self._ATMWdrwlCmpltnAdvc = value if type(value) != auto else self.make_default("ATMWdrwlCmpltnAdvc")

		@ATMWdrwlCmpltnAdvc.deleter
		def ATMWdrwlCmpltnAdvc(self):
			del self._ATMWdrwlCmpltnAdvc
			self._ATMWdrwlCmpltnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMWdrwlCmpltnAdvc', type=ATMWithdrawalCompletionAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))

