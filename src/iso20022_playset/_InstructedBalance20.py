# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceFormat11Choice
from . import InstructedCorporateActionOption21
from . import SignedQuantityFormat10

class InstructedBalance20(base_types._BaseFieldType):

	__slots__ = ["_OptnDtls", "_TtlAccptdInstrBal", "_TtlCancInstrBal", "_TtlInstdBal", "_TtlPdgInstrBal", "_TtlPrtctInstrBal", "_TtlRjctdInstrBal"]
	@property
	def OptnDtls(self):
		return self._OptnDtls

	@OptnDtls.setter
	def OptnDtls(self, value):
		self._OptnDtls = value if value is not None else base_types.UninitialisedField(self, 'OptnDtls', InstructedCorporateActionOption21, True)

	@OptnDtls.deleter
	def OptnDtls(self):
		del self._OptnDtls
		self._OptnDtls = base_types.UninitialisedField(self, 'OptnDtls', InstructedCorporateActionOption21, True)

	@property
	def TtlAccptdInstrBal(self):
		return self._TtlAccptdInstrBal

	@TtlAccptdInstrBal.setter
	def TtlAccptdInstrBal(self, value):
		self._TtlAccptdInstrBal = value if value is not None else base_types.UninitialisedField(self, 'TtlAccptdInstrBal', SignedQuantityFormat10, False)

	@TtlAccptdInstrBal.deleter
	def TtlAccptdInstrBal(self):
		del self._TtlAccptdInstrBal
		self._TtlAccptdInstrBal = base_types.UninitialisedField(self, 'TtlAccptdInstrBal', SignedQuantityFormat10, False)

	@property
	def TtlCancInstrBal(self):
		return self._TtlCancInstrBal

	@TtlCancInstrBal.setter
	def TtlCancInstrBal(self, value):
		self._TtlCancInstrBal = value if value is not None else base_types.UninitialisedField(self, 'TtlCancInstrBal', SignedQuantityFormat10, False)

	@TtlCancInstrBal.deleter
	def TtlCancInstrBal(self):
		del self._TtlCancInstrBal
		self._TtlCancInstrBal = base_types.UninitialisedField(self, 'TtlCancInstrBal', SignedQuantityFormat10, False)

	@property
	def TtlInstdBal(self):
		return self._TtlInstdBal

	@TtlInstdBal.setter
	def TtlInstdBal(self, value):
		self._TtlInstdBal = value if value is not None else base_types.UninitialisedField(self, 'TtlInstdBal', BalanceFormat11Choice, False)

	@TtlInstdBal.deleter
	def TtlInstdBal(self):
		del self._TtlInstdBal
		self._TtlInstdBal = base_types.UninitialisedField(self, 'TtlInstdBal', BalanceFormat11Choice, False)

	@property
	def TtlPdgInstrBal(self):
		return self._TtlPdgInstrBal

	@TtlPdgInstrBal.setter
	def TtlPdgInstrBal(self, value):
		self._TtlPdgInstrBal = value if value is not None else base_types.UninitialisedField(self, 'TtlPdgInstrBal', SignedQuantityFormat10, False)

	@TtlPdgInstrBal.deleter
	def TtlPdgInstrBal(self):
		del self._TtlPdgInstrBal
		self._TtlPdgInstrBal = base_types.UninitialisedField(self, 'TtlPdgInstrBal', SignedQuantityFormat10, False)

	@property
	def TtlPrtctInstrBal(self):
		return self._TtlPrtctInstrBal

	@TtlPrtctInstrBal.setter
	def TtlPrtctInstrBal(self, value):
		self._TtlPrtctInstrBal = value if value is not None else base_types.UninitialisedField(self, 'TtlPrtctInstrBal', SignedQuantityFormat10, False)

	@TtlPrtctInstrBal.deleter
	def TtlPrtctInstrBal(self):
		del self._TtlPrtctInstrBal
		self._TtlPrtctInstrBal = base_types.UninitialisedField(self, 'TtlPrtctInstrBal', SignedQuantityFormat10, False)

	@property
	def TtlRjctdInstrBal(self):
		return self._TtlRjctdInstrBal

	@TtlRjctdInstrBal.setter
	def TtlRjctdInstrBal(self, value):
		self._TtlRjctdInstrBal = value if value is not None else base_types.UninitialisedField(self, 'TtlRjctdInstrBal', SignedQuantityFormat10, False)

	@TtlRjctdInstrBal.deleter
	def TtlRjctdInstrBal(self):
		del self._TtlRjctdInstrBal
		self._TtlRjctdInstrBal = base_types.UninitialisedField(self, 'TtlRjctdInstrBal', SignedQuantityFormat10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OptnDtls', type=InstructedCorporateActionOption21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAccptdInstrBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCancInstrBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlInstdBal', type=BalanceFormat11Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgInstrBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPrtctInstrBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlRjctdInstrBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
	))