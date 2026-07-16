# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentificationFormatChoice
from . import InvestmentFundTransactionsByFund3
from . import YesNoIndicator

class SubAccountIdentification36(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_Id", "_TxOnSubAcct"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if value is not None else base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', AccountIdentificationFormatChoice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', AccountIdentificationFormatChoice, False)

	@property
	def TxOnSubAcct(self):
		return self._TxOnSubAcct

	@TxOnSubAcct.setter
	def TxOnSubAcct(self, value):
		self._TxOnSubAcct = value if value is not None else base_types.UninitialisedField(self, 'TxOnSubAcct', InvestmentFundTransactionsByFund3, True)

	@TxOnSubAcct.deleter
	def TxOnSubAcct(self):
		del self._TxOnSubAcct
		self._TxOnSubAcct = base_types.UninitialisedField(self, 'TxOnSubAcct', InvestmentFundTransactionsByFund3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AccountIdentificationFormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOnSubAcct', type=InvestmentFundTransactionsByFund3, min=0, max=None, mutex_group=None, array=True),
	))