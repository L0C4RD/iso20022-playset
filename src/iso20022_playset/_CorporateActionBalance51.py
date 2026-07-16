# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceFormat14Choice
from . import InstructedBalance21
from . import PendingBalance8
from . import Quantity80Choice
from . import SignedQuantityFormat13

class CorporateActionBalance51(base_types._BaseFieldType):

	__slots__ = ["_BlckdBal", "_BrrwdBal", "_CollInBal", "_CollOutBal", "_InTrnsShipmntBal", "_OblgtdBal", "_OnLnBal", "_OutForRegnBal", "_PdgDlvryBal", "_PdgRctBal", "_RegdBal", "_StrtPosBal", "_SttlmPosBal", "_TradDtPosBal", "_TtlElgblBal", "_TtlInstdBalDtls", "_UinstdBal"]
	@property
	def BlckdBal(self):
		return self._BlckdBal

	@BlckdBal.setter
	def BlckdBal(self, value):
		self._BlckdBal = value if value is not None else base_types.UninitialisedField(self, 'BlckdBal', SignedQuantityFormat13, False)

	@BlckdBal.deleter
	def BlckdBal(self):
		del self._BlckdBal
		self._BlckdBal = base_types.UninitialisedField(self, 'BlckdBal', SignedQuantityFormat13, False)

	@property
	def BrrwdBal(self):
		return self._BrrwdBal

	@BrrwdBal.setter
	def BrrwdBal(self, value):
		self._BrrwdBal = value if value is not None else base_types.UninitialisedField(self, 'BrrwdBal', SignedQuantityFormat13, False)

	@BrrwdBal.deleter
	def BrrwdBal(self):
		del self._BrrwdBal
		self._BrrwdBal = base_types.UninitialisedField(self, 'BrrwdBal', SignedQuantityFormat13, False)

	@property
	def CollInBal(self):
		return self._CollInBal

	@CollInBal.setter
	def CollInBal(self, value):
		self._CollInBal = value if value is not None else base_types.UninitialisedField(self, 'CollInBal', SignedQuantityFormat13, False)

	@CollInBal.deleter
	def CollInBal(self):
		del self._CollInBal
		self._CollInBal = base_types.UninitialisedField(self, 'CollInBal', SignedQuantityFormat13, False)

	@property
	def CollOutBal(self):
		return self._CollOutBal

	@CollOutBal.setter
	def CollOutBal(self, value):
		self._CollOutBal = value if value is not None else base_types.UninitialisedField(self, 'CollOutBal', SignedQuantityFormat13, False)

	@CollOutBal.deleter
	def CollOutBal(self):
		del self._CollOutBal
		self._CollOutBal = base_types.UninitialisedField(self, 'CollOutBal', SignedQuantityFormat13, False)

	@property
	def InTrnsShipmntBal(self):
		return self._InTrnsShipmntBal

	@InTrnsShipmntBal.setter
	def InTrnsShipmntBal(self, value):
		self._InTrnsShipmntBal = value if value is not None else base_types.UninitialisedField(self, 'InTrnsShipmntBal', SignedQuantityFormat13, False)

	@InTrnsShipmntBal.deleter
	def InTrnsShipmntBal(self):
		del self._InTrnsShipmntBal
		self._InTrnsShipmntBal = base_types.UninitialisedField(self, 'InTrnsShipmntBal', SignedQuantityFormat13, False)

	@property
	def OblgtdBal(self):
		return self._OblgtdBal

	@OblgtdBal.setter
	def OblgtdBal(self, value):
		self._OblgtdBal = value if value is not None else base_types.UninitialisedField(self, 'OblgtdBal', SignedQuantityFormat13, False)

	@OblgtdBal.deleter
	def OblgtdBal(self):
		del self._OblgtdBal
		self._OblgtdBal = base_types.UninitialisedField(self, 'OblgtdBal', SignedQuantityFormat13, False)

	@property
	def OnLnBal(self):
		return self._OnLnBal

	@OnLnBal.setter
	def OnLnBal(self, value):
		self._OnLnBal = value if value is not None else base_types.UninitialisedField(self, 'OnLnBal', SignedQuantityFormat13, False)

	@OnLnBal.deleter
	def OnLnBal(self):
		del self._OnLnBal
		self._OnLnBal = base_types.UninitialisedField(self, 'OnLnBal', SignedQuantityFormat13, False)

	@property
	def OutForRegnBal(self):
		return self._OutForRegnBal

	@OutForRegnBal.setter
	def OutForRegnBal(self, value):
		self._OutForRegnBal = value if value is not None else base_types.UninitialisedField(self, 'OutForRegnBal', SignedQuantityFormat13, False)

	@OutForRegnBal.deleter
	def OutForRegnBal(self):
		del self._OutForRegnBal
		self._OutForRegnBal = base_types.UninitialisedField(self, 'OutForRegnBal', SignedQuantityFormat13, False)

	@property
	def PdgDlvryBal(self):
		return self._PdgDlvryBal

	@PdgDlvryBal.setter
	def PdgDlvryBal(self, value):
		self._PdgDlvryBal = value if value is not None else base_types.UninitialisedField(self, 'PdgDlvryBal', PendingBalance8, True)

	@PdgDlvryBal.deleter
	def PdgDlvryBal(self):
		del self._PdgDlvryBal
		self._PdgDlvryBal = base_types.UninitialisedField(self, 'PdgDlvryBal', PendingBalance8, True)

	@property
	def PdgRctBal(self):
		return self._PdgRctBal

	@PdgRctBal.setter
	def PdgRctBal(self, value):
		self._PdgRctBal = value if value is not None else base_types.UninitialisedField(self, 'PdgRctBal', PendingBalance8, True)

	@PdgRctBal.deleter
	def PdgRctBal(self):
		del self._PdgRctBal
		self._PdgRctBal = base_types.UninitialisedField(self, 'PdgRctBal', PendingBalance8, True)

	@property
	def RegdBal(self):
		return self._RegdBal

	@RegdBal.setter
	def RegdBal(self, value):
		self._RegdBal = value if value is not None else base_types.UninitialisedField(self, 'RegdBal', SignedQuantityFormat13, False)

	@RegdBal.deleter
	def RegdBal(self):
		del self._RegdBal
		self._RegdBal = base_types.UninitialisedField(self, 'RegdBal', SignedQuantityFormat13, False)

	@property
	def StrtPosBal(self):
		return self._StrtPosBal

	@StrtPosBal.setter
	def StrtPosBal(self, value):
		self._StrtPosBal = value if value is not None else base_types.UninitialisedField(self, 'StrtPosBal', SignedQuantityFormat13, False)

	@StrtPosBal.deleter
	def StrtPosBal(self):
		del self._StrtPosBal
		self._StrtPosBal = base_types.UninitialisedField(self, 'StrtPosBal', SignedQuantityFormat13, False)

	@property
	def SttlmPosBal(self):
		return self._SttlmPosBal

	@SttlmPosBal.setter
	def SttlmPosBal(self, value):
		self._SttlmPosBal = value if value is not None else base_types.UninitialisedField(self, 'SttlmPosBal', SignedQuantityFormat13, False)

	@SttlmPosBal.deleter
	def SttlmPosBal(self):
		del self._SttlmPosBal
		self._SttlmPosBal = base_types.UninitialisedField(self, 'SttlmPosBal', SignedQuantityFormat13, False)

	@property
	def TradDtPosBal(self):
		return self._TradDtPosBal

	@TradDtPosBal.setter
	def TradDtPosBal(self, value):
		self._TradDtPosBal = value if value is not None else base_types.UninitialisedField(self, 'TradDtPosBal', SignedQuantityFormat13, False)

	@TradDtPosBal.deleter
	def TradDtPosBal(self):
		del self._TradDtPosBal
		self._TradDtPosBal = base_types.UninitialisedField(self, 'TradDtPosBal', SignedQuantityFormat13, False)

	@property
	def TtlElgblBal(self):
		return self._TtlElgblBal

	@TtlElgblBal.setter
	def TtlElgblBal(self, value):
		self._TtlElgblBal = value if value is not None else base_types.UninitialisedField(self, 'TtlElgblBal', Quantity80Choice, False)

	@TtlElgblBal.deleter
	def TtlElgblBal(self):
		del self._TtlElgblBal
		self._TtlElgblBal = base_types.UninitialisedField(self, 'TtlElgblBal', Quantity80Choice, False)

	@property
	def TtlInstdBalDtls(self):
		return self._TtlInstdBalDtls

	@TtlInstdBalDtls.setter
	def TtlInstdBalDtls(self, value):
		self._TtlInstdBalDtls = value if value is not None else base_types.UninitialisedField(self, 'TtlInstdBalDtls', InstructedBalance21, False)

	@TtlInstdBalDtls.deleter
	def TtlInstdBalDtls(self):
		del self._TtlInstdBalDtls
		self._TtlInstdBalDtls = base_types.UninitialisedField(self, 'TtlInstdBalDtls', InstructedBalance21, False)

	@property
	def UinstdBal(self):
		return self._UinstdBal

	@UinstdBal.setter
	def UinstdBal(self, value):
		self._UinstdBal = value if value is not None else base_types.UninitialisedField(self, 'UinstdBal', BalanceFormat14Choice, False)

	@UinstdBal.deleter
	def UinstdBal(self):
		del self._UinstdBal
		self._UinstdBal = base_types.UninitialisedField(self, 'UinstdBal', BalanceFormat14Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckdBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwdBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollOutBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InTrnsShipmntBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtdBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLnBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutForRegnBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgDlvryBal', type=PendingBalance8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdgRctBal', type=PendingBalance8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtPosBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPosBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtPosBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlElgblBal', type=Quantity80Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlInstdBalDtls', type=InstructedBalance21, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UinstdBal', type=BalanceFormat14Choice, min=1, max=1, mutex_group=None, array=False),
	))