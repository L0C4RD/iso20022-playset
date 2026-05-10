from . import base_types
from .InstructedCorporateActionOption22 import InstructedCorporateActionOption22
from .SignedQuantityFormat13 import SignedQuantityFormat13
from .BalanceFormat14Choice import BalanceFormat14Choice

class InstructedBalance21(base_types._BaseFieldType):

	__slots__ = ["_TtlRjctdInstrBal", "_OptnDtls", "_TtlAccptdInstrBal", "_TtlPdgInstrBal", "_TtlInstdBal", "_TtlCancInstrBal", "_TtlPrtctInstrBal"]
	@property
	def TtlRjctdInstrBal(self):
		return self._TtlRjctdInstrBal

	@TtlRjctdInstrBal.setter
	def TtlRjctdInstrBal(self, value):
		self._TtlRjctdInstrBal = value if type(value) != auto else self.make_default("TtlRjctdInstrBal")

	@TtlRjctdInstrBal.deleter
	def TtlRjctdInstrBal(self):
		del self._TtlRjctdInstrBal
		self._TtlRjctdInstrBal = None

	@property
	def OptnDtls(self):
		return self._OptnDtls

	@OptnDtls.setter
	def OptnDtls(self, value):
		self._OptnDtls = value if type(value) != auto else self.make_default("OptnDtls")

	@OptnDtls.deleter
	def OptnDtls(self):
		del self._OptnDtls
		self._OptnDtls = None

	@property
	def TtlAccptdInstrBal(self):
		return self._TtlAccptdInstrBal

	@TtlAccptdInstrBal.setter
	def TtlAccptdInstrBal(self, value):
		self._TtlAccptdInstrBal = value if type(value) != auto else self.make_default("TtlAccptdInstrBal")

	@TtlAccptdInstrBal.deleter
	def TtlAccptdInstrBal(self):
		del self._TtlAccptdInstrBal
		self._TtlAccptdInstrBal = None

	@property
	def TtlPdgInstrBal(self):
		return self._TtlPdgInstrBal

	@TtlPdgInstrBal.setter
	def TtlPdgInstrBal(self, value):
		self._TtlPdgInstrBal = value if type(value) != auto else self.make_default("TtlPdgInstrBal")

	@TtlPdgInstrBal.deleter
	def TtlPdgInstrBal(self):
		del self._TtlPdgInstrBal
		self._TtlPdgInstrBal = None

	@property
	def TtlInstdBal(self):
		return self._TtlInstdBal

	@TtlInstdBal.setter
	def TtlInstdBal(self, value):
		self._TtlInstdBal = value if type(value) != auto else self.make_default("TtlInstdBal")

	@TtlInstdBal.deleter
	def TtlInstdBal(self):
		del self._TtlInstdBal
		self._TtlInstdBal = None

	@property
	def TtlCancInstrBal(self):
		return self._TtlCancInstrBal

	@TtlCancInstrBal.setter
	def TtlCancInstrBal(self, value):
		self._TtlCancInstrBal = value if type(value) != auto else self.make_default("TtlCancInstrBal")

	@TtlCancInstrBal.deleter
	def TtlCancInstrBal(self):
		del self._TtlCancInstrBal
		self._TtlCancInstrBal = None

	@property
	def TtlPrtctInstrBal(self):
		return self._TtlPrtctInstrBal

	@TtlPrtctInstrBal.setter
	def TtlPrtctInstrBal(self, value):
		self._TtlPrtctInstrBal = value if type(value) != auto else self.make_default("TtlPrtctInstrBal")

	@TtlPrtctInstrBal.deleter
	def TtlPrtctInstrBal(self):
		del self._TtlPrtctInstrBal
		self._TtlPrtctInstrBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlRjctdInstrBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnDtls', type=InstructedCorporateActionOption22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAccptdInstrBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgInstrBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlInstdBal', type=BalanceFormat14Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCancInstrBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPrtctInstrBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
	))

