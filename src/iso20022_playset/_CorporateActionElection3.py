# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionCashMovements2
from . import CorporateActionOption1FormatChoice
from . import CorporateActionSecuritiesMovement2
from . import Exact3NumericText
from . import PercentageRate
from . import SecuritiesAccount7
from . import UnitOrFaceAmount1Choice

class CorporateActionElection3(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_CshMvmntDtls", "_InstdSctiesQtyToRcv", "_InstdUndrlygSctiesQty", "_OptnNb", "_OptnTp", "_PropsdRate", "_SctiesMvmntDtls"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', SecuritiesAccount7, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', SecuritiesAccount7, False)

	@property
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'CshMvmntDtls', CorporateActionCashMovements2, True)

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = base_types.UninitialisedField(self, 'CshMvmntDtls', CorporateActionCashMovements2, True)

	@property
	def InstdSctiesQtyToRcv(self):
		return self._InstdSctiesQtyToRcv

	@InstdSctiesQtyToRcv.setter
	def InstdSctiesQtyToRcv(self, value):
		self._InstdSctiesQtyToRcv = value if value is not None else base_types.UninitialisedField(self, 'InstdSctiesQtyToRcv', UnitOrFaceAmount1Choice, False)

	@InstdSctiesQtyToRcv.deleter
	def InstdSctiesQtyToRcv(self):
		del self._InstdSctiesQtyToRcv
		self._InstdSctiesQtyToRcv = base_types.UninitialisedField(self, 'InstdSctiesQtyToRcv', UnitOrFaceAmount1Choice, False)

	@property
	def InstdUndrlygSctiesQty(self):
		return self._InstdUndrlygSctiesQty

	@InstdUndrlygSctiesQty.setter
	def InstdUndrlygSctiesQty(self, value):
		self._InstdUndrlygSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'InstdUndrlygSctiesQty', UnitOrFaceAmount1Choice, False)

	@InstdUndrlygSctiesQty.deleter
	def InstdUndrlygSctiesQty(self):
		del self._InstdUndrlygSctiesQty
		self._InstdUndrlygSctiesQty = base_types.UninitialisedField(self, 'InstdUndrlygSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@property
	def PropsdRate(self):
		return self._PropsdRate

	@PropsdRate.setter
	def PropsdRate(self, value):
		self._PropsdRate = value if value is not None else base_types.UninitialisedField(self, 'PropsdRate', PercentageRate, False)

	@PropsdRate.deleter
	def PropsdRate(self):
		del self._PropsdRate
		self._PropsdRate = base_types.UninitialisedField(self, 'PropsdRate', PercentageRate, False)

	@property
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntDtls', CorporateActionSecuritiesMovement2, True)

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = base_types.UninitialisedField(self, 'SctiesMvmntDtls', CorporateActionSecuritiesMovement2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmntDtls', type=CorporateActionCashMovements2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstdSctiesQtyToRcv', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdUndrlygSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=CorporateActionSecuritiesMovement2, min=0, max=None, mutex_group=None, array=True),
	))