import base_types
import ATMCompletionAdviceV03

class CATP_008_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMCmpltnAdvc"]
		@property
		def ATMCmpltnAdvc(self):
			return self._ATMCmpltnAdvc

		@ATMCmpltnAdvc.setter
		def ATMCmpltnAdvc(self, value):
			self._ATMCmpltnAdvc = value if type(value) != auto else self.make_default("ATMCmpltnAdvc")

		@ATMCmpltnAdvc.deleter
		def ATMCmpltnAdvc(self):
			del self._ATMCmpltnAdvc
			self._ATMCmpltnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMCmpltnAdvc', type=ATMCompletionAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))

