from . import base_types
import AccountSwitchInformationResponseV05

class ACMT_028_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctSwtchInfRspn"]
		@property
		def AcctSwtchInfRspn(self):
			return self._AcctSwtchInfRspn

		@AcctSwtchInfRspn.setter
		def AcctSwtchInfRspn(self, value):
			self._AcctSwtchInfRspn = value if type(value) != auto else self.make_default("AcctSwtchInfRspn")

		@AcctSwtchInfRspn.deleter
		def AcctSwtchInfRspn(self):
			del self._AcctSwtchInfRspn
			self._AcctSwtchInfRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchInfRspn', type=AccountSwitchInformationResponseV05, min=1, max=1, mutex_group=None, array=False),
		))

