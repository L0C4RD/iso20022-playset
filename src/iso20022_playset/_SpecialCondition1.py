# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class SpecialCondition1(base_types._BaseFieldType):

	__slots__ = ["_IncmgAmt", "_IncmgAmtToOthrAcct", "_OutgngAmt", "_PmtFrOthrAcct"]
	@property
	def IncmgAmt(self):
		return self._IncmgAmt

	@IncmgAmt.setter
	def IncmgAmt(self, value):
		self._IncmgAmt = value if value is not None else base_types.UninitialisedField(self, 'IncmgAmt', ActiveCurrencyAndAmount, False)

	@IncmgAmt.deleter
	def IncmgAmt(self):
		del self._IncmgAmt
		self._IncmgAmt = base_types.UninitialisedField(self, 'IncmgAmt', ActiveCurrencyAndAmount, False)

	@property
	def IncmgAmtToOthrAcct(self):
		return self._IncmgAmtToOthrAcct

	@IncmgAmtToOthrAcct.setter
	def IncmgAmtToOthrAcct(self, value):
		self._IncmgAmtToOthrAcct = value if value is not None else base_types.UninitialisedField(self, 'IncmgAmtToOthrAcct', ActiveCurrencyAndAmount, False)

	@IncmgAmtToOthrAcct.deleter
	def IncmgAmtToOthrAcct(self):
		del self._IncmgAmtToOthrAcct
		self._IncmgAmtToOthrAcct = base_types.UninitialisedField(self, 'IncmgAmtToOthrAcct', ActiveCurrencyAndAmount, False)

	@property
	def OutgngAmt(self):
		return self._OutgngAmt

	@OutgngAmt.setter
	def OutgngAmt(self, value):
		self._OutgngAmt = value if value is not None else base_types.UninitialisedField(self, 'OutgngAmt', ActiveCurrencyAndAmount, False)

	@OutgngAmt.deleter
	def OutgngAmt(self):
		del self._OutgngAmt
		self._OutgngAmt = base_types.UninitialisedField(self, 'OutgngAmt', ActiveCurrencyAndAmount, False)

	@property
	def PmtFrOthrAcct(self):
		return self._PmtFrOthrAcct

	@PmtFrOthrAcct.setter
	def PmtFrOthrAcct(self, value):
		self._PmtFrOthrAcct = value if value is not None else base_types.UninitialisedField(self, 'PmtFrOthrAcct', ActiveCurrencyAndAmount, False)

	@PmtFrOthrAcct.deleter
	def PmtFrOthrAcct(self):
		del self._PmtFrOthrAcct
		self._PmtFrOthrAcct = base_types.UninitialisedField(self, 'PmtFrOthrAcct', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncmgAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmgAmtToOthrAcct', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutgngAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrOthrAcct', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))