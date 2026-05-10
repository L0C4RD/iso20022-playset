from . import base_types
import PercentageRate
import CorporateActionOption1FormatChoice
import UnitOrFaceAmount1Choice
import Exact3NumericText
import CorporateActionCashMovements2
import CorporateActionSecuritiesMovement2
import SecuritiesAccount7

class CorporateActionElection3(base_types._BaseFieldType):

	__slots__ = ["_CshMvmntDtls", "_InstdSctiesQtyToRcv", "_OptnNb", "_AcctDtls", "_OptnTp", "_InstdUndrlygSctiesQty", "_PropsdRate", "_SctiesMvmntDtls"]
	@property
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if type(value) != auto else self.make_default("CshMvmntDtls")

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = None

	@property
	def InstdSctiesQtyToRcv(self):
		return self._InstdSctiesQtyToRcv

	@InstdSctiesQtyToRcv.setter
	def InstdSctiesQtyToRcv(self, value):
		self._InstdSctiesQtyToRcv = value if type(value) != auto else self.make_default("InstdSctiesQtyToRcv")

	@InstdSctiesQtyToRcv.deleter
	def InstdSctiesQtyToRcv(self):
		del self._InstdSctiesQtyToRcv
		self._InstdSctiesQtyToRcv = None

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def InstdUndrlygSctiesQty(self):
		return self._InstdUndrlygSctiesQty

	@InstdUndrlygSctiesQty.setter
	def InstdUndrlygSctiesQty(self, value):
		self._InstdUndrlygSctiesQty = value if type(value) != auto else self.make_default("InstdUndrlygSctiesQty")

	@InstdUndrlygSctiesQty.deleter
	def InstdUndrlygSctiesQty(self):
		del self._InstdUndrlygSctiesQty
		self._InstdUndrlygSctiesQty = None

	@property
	def PropsdRate(self):
		return self._PropsdRate

	@PropsdRate.setter
	def PropsdRate(self, value):
		self._PropsdRate = value if type(value) != auto else self.make_default("PropsdRate")

	@PropsdRate.deleter
	def PropsdRate(self):
		del self._PropsdRate
		self._PropsdRate = None

	@property
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if type(value) != auto else self.make_default("SctiesMvmntDtls")

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshMvmntDtls', type=CorporateActionCashMovements2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstdSctiesQtyToRcv', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdUndrlygSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=CorporateActionSecuritiesMovement2, min=0, max=None, mutex_group=None, array=True),
	))

