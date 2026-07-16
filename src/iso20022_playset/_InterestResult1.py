# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CollateralBalance1
from . import ISODate
from . import InterestMethod1Code

class InterestResult1(base_types._BaseFieldType):

	__slots__ = ["_ClsgCollBal", "_IntrstDueToA", "_IntrstDueToB", "_IntrstMtd", "_OpngCollBal", "_ValDt"]
	@property
	def ClsgCollBal(self):
		return self._ClsgCollBal

	@ClsgCollBal.setter
	def ClsgCollBal(self, value):
		self._ClsgCollBal = value if value is not None else base_types.UninitialisedField(self, 'ClsgCollBal', CollateralBalance1, False)

	@ClsgCollBal.deleter
	def ClsgCollBal(self):
		del self._ClsgCollBal
		self._ClsgCollBal = base_types.UninitialisedField(self, 'ClsgCollBal', CollateralBalance1, False)

	@property
	def IntrstDueToA(self):
		return self._IntrstDueToA

	@IntrstDueToA.setter
	def IntrstDueToA(self, value):
		self._IntrstDueToA = value if value is not None else base_types.UninitialisedField(self, 'IntrstDueToA', ActiveCurrencyAndAmount, False)

	@IntrstDueToA.deleter
	def IntrstDueToA(self):
		del self._IntrstDueToA
		self._IntrstDueToA = base_types.UninitialisedField(self, 'IntrstDueToA', ActiveCurrencyAndAmount, False)

	@property
	def IntrstDueToB(self):
		return self._IntrstDueToB

	@IntrstDueToB.setter
	def IntrstDueToB(self, value):
		self._IntrstDueToB = value if value is not None else base_types.UninitialisedField(self, 'IntrstDueToB', ActiveCurrencyAndAmount, False)

	@IntrstDueToB.deleter
	def IntrstDueToB(self):
		del self._IntrstDueToB
		self._IntrstDueToB = base_types.UninitialisedField(self, 'IntrstDueToB', ActiveCurrencyAndAmount, False)

	@property
	def IntrstMtd(self):
		return self._IntrstMtd

	@IntrstMtd.setter
	def IntrstMtd(self, value):
		self._IntrstMtd = value if value is not None else base_types.UninitialisedField(self, 'IntrstMtd', InterestMethod1Code, False)

	@IntrstMtd.deleter
	def IntrstMtd(self):
		del self._IntrstMtd
		self._IntrstMtd = base_types.UninitialisedField(self, 'IntrstMtd', InterestMethod1Code, False)

	@property
	def OpngCollBal(self):
		return self._OpngCollBal

	@OpngCollBal.setter
	def OpngCollBal(self, value):
		self._OpngCollBal = value if value is not None else base_types.UninitialisedField(self, 'OpngCollBal', CollateralBalance1, False)

	@OpngCollBal.deleter
	def OpngCollBal(self):
		del self._OpngCollBal
		self._OpngCollBal = base_types.UninitialisedField(self, 'OpngCollBal', CollateralBalance1, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgCollBal', type=CollateralBalance1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstDueToA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstDueToB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstMtd', type=InterestMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngCollBal', type=CollateralBalance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))