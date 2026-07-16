# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestmentAccount76
from . import Max35Text

class AccountSelection3Choice(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_OthrAcctSelctnData"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def OthrAcctSelctnData(self):
		return self._OthrAcctSelctnData

	@OthrAcctSelctnData.setter
	def OthrAcctSelctnData(self, value):
		self._OthrAcctSelctnData = value if value is not None else base_types.UninitialisedField(self, 'OthrAcctSelctnData', InvestmentAccount76, False)

	@OthrAcctSelctnData.deleter
	def OthrAcctSelctnData(self):
		del self._OthrAcctSelctnData
		self._OthrAcctSelctnData = base_types.UninitialisedField(self, 'OthrAcctSelctnData', InvestmentAccount76, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrAcctSelctnData', type=InvestmentAccount76, min=0, max=1, mutex_group=1, array=False),
	))