from . import base_types
from ._InvestmentAccount76 import InvestmentAccount76
from ._Max35Text import Max35Text

class AccountSelection3Choice(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_OthrAcctSelctnData"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def OthrAcctSelctnData(self):
		return self._OthrAcctSelctnData

	@OthrAcctSelctnData.setter
	def OthrAcctSelctnData(self, value):
		self._OthrAcctSelctnData = value if type(value) != base_types.auto else self.make_default("OthrAcctSelctnData")

	@OthrAcctSelctnData.deleter
	def OthrAcctSelctnData(self):
		del self._OthrAcctSelctnData
		self._OthrAcctSelctnData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrAcctSelctnData', type=InvestmentAccount76, min=0, max=1, mutex_group=1, array=False),
	))

