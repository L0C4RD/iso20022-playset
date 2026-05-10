import base_types
import InvestmentFundTransactionsByFund3
import YesNoIndicator
import AccountIdentificationFormatChoice

class SubAccountIdentification36(base_types._BaseFieldType):

	__slots__ = ["_TxOnSubAcct", "_Id", "_ActvtyInd"]
	@property
	def TxOnSubAcct(self):
		return self._TxOnSubAcct

	@TxOnSubAcct.setter
	def TxOnSubAcct(self, value):
		self._TxOnSubAcct = value if type(value) != auto else self.make_default("TxOnSubAcct")

	@TxOnSubAcct.deleter
	def TxOnSubAcct(self):
		del self._TxOnSubAcct
		self._TxOnSubAcct = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxOnSubAcct', type=InvestmentFundTransactionsByFund3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=AccountIdentificationFormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

