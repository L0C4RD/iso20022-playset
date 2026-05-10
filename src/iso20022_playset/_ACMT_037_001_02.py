from . import base_types
from .AccountSwitchTechnicalRejectionV02 import AccountSwitchTechnicalRejectionV02

class ACMT_037_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctSwtchTechRjctn"]
		@property
		def AcctSwtchTechRjctn(self):
			return self._AcctSwtchTechRjctn

		@AcctSwtchTechRjctn.setter
		def AcctSwtchTechRjctn(self, value):
			self._AcctSwtchTechRjctn = value if type(value) != base_types.auto else self.make_default("AcctSwtchTechRjctn")

		@AcctSwtchTechRjctn.deleter
		def AcctSwtchTechRjctn(self):
			del self._AcctSwtchTechRjctn
			self._AcctSwtchTechRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchTechRjctn', type=AccountSwitchTechnicalRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))

