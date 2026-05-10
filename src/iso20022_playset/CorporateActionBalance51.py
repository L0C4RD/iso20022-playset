from . import base_types
import Quantity80Choice
import PendingBalance8
import SignedQuantityFormat13
import BalanceFormat14Choice
import InstructedBalance21

class CorporateActionBalance51(base_types._BaseFieldType):

	__slots__ = ["_InTrnsShipmntBal", "_StrtPosBal", "_PdgDlvryBal", "_OutForRegnBal", "_SttlmPosBal", "_BlckdBal", "_RegdBal", "_PdgRctBal", "_CollOutBal", "_OblgtdBal", "_TradDtPosBal", "_TtlInstdBalDtls", "_OnLnBal", "_CollInBal", "_UinstdBal", "_TtlElgblBal", "_BrrwdBal"]
	@property
	def InTrnsShipmntBal(self):
		return self._InTrnsShipmntBal

	@InTrnsShipmntBal.setter
	def InTrnsShipmntBal(self, value):
		self._InTrnsShipmntBal = value if type(value) != auto else self.make_default("InTrnsShipmntBal")

	@InTrnsShipmntBal.deleter
	def InTrnsShipmntBal(self):
		del self._InTrnsShipmntBal
		self._InTrnsShipmntBal = None

	@property
	def StrtPosBal(self):
		return self._StrtPosBal

	@StrtPosBal.setter
	def StrtPosBal(self, value):
		self._StrtPosBal = value if type(value) != auto else self.make_default("StrtPosBal")

	@StrtPosBal.deleter
	def StrtPosBal(self):
		del self._StrtPosBal
		self._StrtPosBal = None

	@property
	def PdgDlvryBal(self):
		return self._PdgDlvryBal

	@PdgDlvryBal.setter
	def PdgDlvryBal(self, value):
		self._PdgDlvryBal = value if type(value) != auto else self.make_default("PdgDlvryBal")

	@PdgDlvryBal.deleter
	def PdgDlvryBal(self):
		del self._PdgDlvryBal
		self._PdgDlvryBal = None

	@property
	def OutForRegnBal(self):
		return self._OutForRegnBal

	@OutForRegnBal.setter
	def OutForRegnBal(self, value):
		self._OutForRegnBal = value if type(value) != auto else self.make_default("OutForRegnBal")

	@OutForRegnBal.deleter
	def OutForRegnBal(self):
		del self._OutForRegnBal
		self._OutForRegnBal = None

	@property
	def SttlmPosBal(self):
		return self._SttlmPosBal

	@SttlmPosBal.setter
	def SttlmPosBal(self, value):
		self._SttlmPosBal = value if type(value) != auto else self.make_default("SttlmPosBal")

	@SttlmPosBal.deleter
	def SttlmPosBal(self):
		del self._SttlmPosBal
		self._SttlmPosBal = None

	@property
	def BlckdBal(self):
		return self._BlckdBal

	@BlckdBal.setter
	def BlckdBal(self, value):
		self._BlckdBal = value if type(value) != auto else self.make_default("BlckdBal")

	@BlckdBal.deleter
	def BlckdBal(self):
		del self._BlckdBal
		self._BlckdBal = None

	@property
	def RegdBal(self):
		return self._RegdBal

	@RegdBal.setter
	def RegdBal(self, value):
		self._RegdBal = value if type(value) != auto else self.make_default("RegdBal")

	@RegdBal.deleter
	def RegdBal(self):
		del self._RegdBal
		self._RegdBal = None

	@property
	def PdgRctBal(self):
		return self._PdgRctBal

	@PdgRctBal.setter
	def PdgRctBal(self, value):
		self._PdgRctBal = value if type(value) != auto else self.make_default("PdgRctBal")

	@PdgRctBal.deleter
	def PdgRctBal(self):
		del self._PdgRctBal
		self._PdgRctBal = None

	@property
	def CollOutBal(self):
		return self._CollOutBal

	@CollOutBal.setter
	def CollOutBal(self, value):
		self._CollOutBal = value if type(value) != auto else self.make_default("CollOutBal")

	@CollOutBal.deleter
	def CollOutBal(self):
		del self._CollOutBal
		self._CollOutBal = None

	@property
	def OblgtdBal(self):
		return self._OblgtdBal

	@OblgtdBal.setter
	def OblgtdBal(self, value):
		self._OblgtdBal = value if type(value) != auto else self.make_default("OblgtdBal")

	@OblgtdBal.deleter
	def OblgtdBal(self):
		del self._OblgtdBal
		self._OblgtdBal = None

	@property
	def TradDtPosBal(self):
		return self._TradDtPosBal

	@TradDtPosBal.setter
	def TradDtPosBal(self, value):
		self._TradDtPosBal = value if type(value) != auto else self.make_default("TradDtPosBal")

	@TradDtPosBal.deleter
	def TradDtPosBal(self):
		del self._TradDtPosBal
		self._TradDtPosBal = None

	@property
	def TtlInstdBalDtls(self):
		return self._TtlInstdBalDtls

	@TtlInstdBalDtls.setter
	def TtlInstdBalDtls(self, value):
		self._TtlInstdBalDtls = value if type(value) != auto else self.make_default("TtlInstdBalDtls")

	@TtlInstdBalDtls.deleter
	def TtlInstdBalDtls(self):
		del self._TtlInstdBalDtls
		self._TtlInstdBalDtls = None

	@property
	def OnLnBal(self):
		return self._OnLnBal

	@OnLnBal.setter
	def OnLnBal(self, value):
		self._OnLnBal = value if type(value) != auto else self.make_default("OnLnBal")

	@OnLnBal.deleter
	def OnLnBal(self):
		del self._OnLnBal
		self._OnLnBal = None

	@property
	def CollInBal(self):
		return self._CollInBal

	@CollInBal.setter
	def CollInBal(self, value):
		self._CollInBal = value if type(value) != auto else self.make_default("CollInBal")

	@CollInBal.deleter
	def CollInBal(self):
		del self._CollInBal
		self._CollInBal = None

	@property
	def UinstdBal(self):
		return self._UinstdBal

	@UinstdBal.setter
	def UinstdBal(self, value):
		self._UinstdBal = value if type(value) != auto else self.make_default("UinstdBal")

	@UinstdBal.deleter
	def UinstdBal(self):
		del self._UinstdBal
		self._UinstdBal = None

	@property
	def TtlElgblBal(self):
		return self._TtlElgblBal

	@TtlElgblBal.setter
	def TtlElgblBal(self, value):
		self._TtlElgblBal = value if type(value) != auto else self.make_default("TtlElgblBal")

	@TtlElgblBal.deleter
	def TtlElgblBal(self):
		del self._TtlElgblBal
		self._TtlElgblBal = None

	@property
	def BrrwdBal(self):
		return self._BrrwdBal

	@BrrwdBal.setter
	def BrrwdBal(self, value):
		self._BrrwdBal = value if type(value) != auto else self.make_default("BrrwdBal")

	@BrrwdBal.deleter
	def BrrwdBal(self):
		del self._BrrwdBal
		self._BrrwdBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InTrnsShipmntBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtPosBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgDlvryBal', type=PendingBalance8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OutForRegnBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPosBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgRctBal', type=PendingBalance8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CollOutBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtdBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtPosBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlInstdBalDtls', type=InstructedBalance21, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLnBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UinstdBal', type=BalanceFormat14Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlElgblBal', type=Quantity80Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwdBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
	))

