# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import FailedSettlementReason1FormatChoice
from . import SecurityIdentification7
from . import UnitOrFaceAmount1Choice

class FailedMovement1(base_types._BaseFieldType):

	__slots__ = ["_CshAmt", "_Rsn", "_SctiesQty", "_SctyId"]
	@property
	def CshAmt(self):
		return self._CshAmt

	@CshAmt.setter
	def CshAmt(self, value):
		self._CshAmt = value if value is not None else base_types.UninitialisedField(self, 'CshAmt', ActiveCurrencyAndAmount, False)

	@CshAmt.deleter
	def CshAmt(self):
		del self._CshAmt
		self._CshAmt = base_types.UninitialisedField(self, 'CshAmt', ActiveCurrencyAndAmount, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', FailedSettlementReason1FormatChoice, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', FailedSettlementReason1FormatChoice, False)

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if value is not None else base_types.UninitialisedField(self, 'SctiesQty', UnitOrFaceAmount1Choice, False)

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = base_types.UninitialisedField(self, 'SctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification7, False)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rsn', type=FailedSettlementReason1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification7, min=0, max=1, mutex_group=None, array=False),
	))