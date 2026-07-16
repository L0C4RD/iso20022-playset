# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Fee12
from . import FinancialInstrument107
from . import InvestmentAccount81
from . import LegIdentification1Choice
from . import Max350Text

class SwitchLegReferences3(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmDtls", "_InvstmtAcctDtls", "_LegId", "_LegRjctnRsn", "_RprdFee"]
	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument107, False)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument107, False)

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount81, False)

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount81, False)

	@property
	def LegId(self):
		return self._LegId

	@LegId.setter
	def LegId(self, value):
		self._LegId = value if value is not None else base_types.UninitialisedField(self, 'LegId', LegIdentification1Choice, False)

	@LegId.deleter
	def LegId(self):
		del self._LegId
		self._LegId = base_types.UninitialisedField(self, 'LegId', LegIdentification1Choice, False)

	@property
	def LegRjctnRsn(self):
		return self._LegRjctnRsn

	@LegRjctnRsn.setter
	def LegRjctnRsn(self, value):
		self._LegRjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'LegRjctnRsn', Max350Text, False)

	@LegRjctnRsn.deleter
	def LegRjctnRsn(self):
		del self._LegRjctnRsn
		self._LegRjctnRsn = base_types.UninitialisedField(self, 'LegRjctnRsn', Max350Text, False)

	@property
	def RprdFee(self):
		return self._RprdFee

	@RprdFee.setter
	def RprdFee(self, value):
		self._RprdFee = value if value is not None else base_types.UninitialisedField(self, 'RprdFee', Fee12, True)

	@RprdFee.deleter
	def RprdFee(self):
		del self._RprdFee
		self._RprdFee = base_types.UninitialisedField(self, 'RprdFee', Fee12, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument107, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegId', type=LegIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegRjctnRsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdFee', type=Fee12, min=0, max=10, mutex_group=None, array=True),
	))