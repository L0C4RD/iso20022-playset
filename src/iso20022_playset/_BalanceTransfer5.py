# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceTransferFundingLimit1
from . import BalanceTransferReference1
from . import SettlementMethod5Choice

class BalanceTransfer5(base_types._BaseFieldType):

	__slots__ = ["_BalTrfFndgLmt", "_BalTrfMtd", "_BalTrfRef"]
	@property
	def BalTrfFndgLmt(self):
		return self._BalTrfFndgLmt

	@BalTrfFndgLmt.setter
	def BalTrfFndgLmt(self, value):
		self._BalTrfFndgLmt = value if value is not None else base_types.UninitialisedField(self, 'BalTrfFndgLmt', BalanceTransferFundingLimit1, False)

	@BalTrfFndgLmt.deleter
	def BalTrfFndgLmt(self):
		del self._BalTrfFndgLmt
		self._BalTrfFndgLmt = base_types.UninitialisedField(self, 'BalTrfFndgLmt', BalanceTransferFundingLimit1, False)

	@property
	def BalTrfMtd(self):
		return self._BalTrfMtd

	@BalTrfMtd.setter
	def BalTrfMtd(self, value):
		self._BalTrfMtd = value if value is not None else base_types.UninitialisedField(self, 'BalTrfMtd', SettlementMethod5Choice, False)

	@BalTrfMtd.deleter
	def BalTrfMtd(self):
		del self._BalTrfMtd
		self._BalTrfMtd = base_types.UninitialisedField(self, 'BalTrfMtd', SettlementMethod5Choice, False)

	@property
	def BalTrfRef(self):
		return self._BalTrfRef

	@BalTrfRef.setter
	def BalTrfRef(self, value):
		self._BalTrfRef = value if value is not None else base_types.UninitialisedField(self, 'BalTrfRef', BalanceTransferReference1, False)

	@BalTrfRef.deleter
	def BalTrfRef(self):
		del self._BalTrfRef
		self._BalTrfRef = base_types.UninitialisedField(self, 'BalTrfRef', BalanceTransferReference1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTrfFndgLmt', type=BalanceTransferFundingLimit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTrfMtd', type=SettlementMethod5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTrfRef', type=BalanceTransferReference1, min=0, max=1, mutex_group=None, array=False),
	))