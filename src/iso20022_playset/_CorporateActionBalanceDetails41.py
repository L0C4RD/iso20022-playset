from . import base_types
from ._BalanceFormat12Choice import BalanceFormat12Choice
from ._TotalEligibleBalanceFormat10 import TotalEligibleBalanceFormat10
from ._BalanceFormat11Choice import BalanceFormat11Choice

class CorporateActionBalanceDetails41(base_types._BaseFieldType):

	__slots__ = ["_BlckdBal", "_BrrwdBal", "_UafctdBal", "_OutForRegnBal", "_PdgRctBal", "_ConfdBal", "_AfctdBal", "_InTrnsShipmntBal", "_StrtPosBal", "_CollOutBal", "_OnLnBal", "_PdgDlvryBal", "_SttlmPosBal", "_TradDtPosBal", "_CollInBal", "_TtlElgblBal", "_RegdBal"]
	@property
	def BlckdBal(self):
		return self._BlckdBal

	@BlckdBal.setter
	def BlckdBal(self, value):
		self._BlckdBal = value if type(value) != base_types.auto else self.make_default("BlckdBal")

	@BlckdBal.deleter
	def BlckdBal(self):
		del self._BlckdBal
		self._BlckdBal = None

	@property
	def BrrwdBal(self):
		return self._BrrwdBal

	@BrrwdBal.setter
	def BrrwdBal(self, value):
		self._BrrwdBal = value if type(value) != base_types.auto else self.make_default("BrrwdBal")

	@BrrwdBal.deleter
	def BrrwdBal(self):
		del self._BrrwdBal
		self._BrrwdBal = None

	@property
	def UafctdBal(self):
		return self._UafctdBal

	@UafctdBal.setter
	def UafctdBal(self, value):
		self._UafctdBal = value if type(value) != base_types.auto else self.make_default("UafctdBal")

	@UafctdBal.deleter
	def UafctdBal(self):
		del self._UafctdBal
		self._UafctdBal = None

	@property
	def OutForRegnBal(self):
		return self._OutForRegnBal

	@OutForRegnBal.setter
	def OutForRegnBal(self, value):
		self._OutForRegnBal = value if type(value) != base_types.auto else self.make_default("OutForRegnBal")

	@OutForRegnBal.deleter
	def OutForRegnBal(self):
		del self._OutForRegnBal
		self._OutForRegnBal = None

	@property
	def PdgRctBal(self):
		return self._PdgRctBal

	@PdgRctBal.setter
	def PdgRctBal(self, value):
		self._PdgRctBal = value if type(value) != base_types.auto else self.make_default("PdgRctBal")

	@PdgRctBal.deleter
	def PdgRctBal(self):
		del self._PdgRctBal
		self._PdgRctBal = None

	@property
	def ConfdBal(self):
		return self._ConfdBal

	@ConfdBal.setter
	def ConfdBal(self, value):
		self._ConfdBal = value if type(value) != base_types.auto else self.make_default("ConfdBal")

	@ConfdBal.deleter
	def ConfdBal(self):
		del self._ConfdBal
		self._ConfdBal = None

	@property
	def AfctdBal(self):
		return self._AfctdBal

	@AfctdBal.setter
	def AfctdBal(self, value):
		self._AfctdBal = value if type(value) != base_types.auto else self.make_default("AfctdBal")

	@AfctdBal.deleter
	def AfctdBal(self):
		del self._AfctdBal
		self._AfctdBal = None

	@property
	def InTrnsShipmntBal(self):
		return self._InTrnsShipmntBal

	@InTrnsShipmntBal.setter
	def InTrnsShipmntBal(self, value):
		self._InTrnsShipmntBal = value if type(value) != base_types.auto else self.make_default("InTrnsShipmntBal")

	@InTrnsShipmntBal.deleter
	def InTrnsShipmntBal(self):
		del self._InTrnsShipmntBal
		self._InTrnsShipmntBal = None

	@property
	def StrtPosBal(self):
		return self._StrtPosBal

	@StrtPosBal.setter
	def StrtPosBal(self, value):
		self._StrtPosBal = value if type(value) != base_types.auto else self.make_default("StrtPosBal")

	@StrtPosBal.deleter
	def StrtPosBal(self):
		del self._StrtPosBal
		self._StrtPosBal = None

	@property
	def CollOutBal(self):
		return self._CollOutBal

	@CollOutBal.setter
	def CollOutBal(self, value):
		self._CollOutBal = value if type(value) != base_types.auto else self.make_default("CollOutBal")

	@CollOutBal.deleter
	def CollOutBal(self):
		del self._CollOutBal
		self._CollOutBal = None

	@property
	def OnLnBal(self):
		return self._OnLnBal

	@OnLnBal.setter
	def OnLnBal(self, value):
		self._OnLnBal = value if type(value) != base_types.auto else self.make_default("OnLnBal")

	@OnLnBal.deleter
	def OnLnBal(self):
		del self._OnLnBal
		self._OnLnBal = None

	@property
	def PdgDlvryBal(self):
		return self._PdgDlvryBal

	@PdgDlvryBal.setter
	def PdgDlvryBal(self, value):
		self._PdgDlvryBal = value if type(value) != base_types.auto else self.make_default("PdgDlvryBal")

	@PdgDlvryBal.deleter
	def PdgDlvryBal(self):
		del self._PdgDlvryBal
		self._PdgDlvryBal = None

	@property
	def SttlmPosBal(self):
		return self._SttlmPosBal

	@SttlmPosBal.setter
	def SttlmPosBal(self, value):
		self._SttlmPosBal = value if type(value) != base_types.auto else self.make_default("SttlmPosBal")

	@SttlmPosBal.deleter
	def SttlmPosBal(self):
		del self._SttlmPosBal
		self._SttlmPosBal = None

	@property
	def TradDtPosBal(self):
		return self._TradDtPosBal

	@TradDtPosBal.setter
	def TradDtPosBal(self, value):
		self._TradDtPosBal = value if type(value) != base_types.auto else self.make_default("TradDtPosBal")

	@TradDtPosBal.deleter
	def TradDtPosBal(self):
		del self._TradDtPosBal
		self._TradDtPosBal = None

	@property
	def CollInBal(self):
		return self._CollInBal

	@CollInBal.setter
	def CollInBal(self, value):
		self._CollInBal = value if type(value) != base_types.auto else self.make_default("CollInBal")

	@CollInBal.deleter
	def CollInBal(self):
		del self._CollInBal
		self._CollInBal = None

	@property
	def TtlElgblBal(self):
		return self._TtlElgblBal

	@TtlElgblBal.setter
	def TtlElgblBal(self, value):
		self._TtlElgblBal = value if type(value) != base_types.auto else self.make_default("TtlElgblBal")

	@TtlElgblBal.deleter
	def TtlElgblBal(self):
		del self._TtlElgblBal
		self._TtlElgblBal = None

	@property
	def RegdBal(self):
		return self._RegdBal

	@RegdBal.setter
	def RegdBal(self, value):
		self._RegdBal = value if type(value) != base_types.auto else self.make_default("RegdBal")

	@RegdBal.deleter
	def RegdBal(self):
		del self._RegdBal
		self._RegdBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UafctdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutForRegnBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgRctBal', type=BalanceFormat12Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfdBal', type=BalanceFormat11Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AfctdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InTrnsShipmntBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtPosBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollOutBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLnBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgDlvryBal', type=BalanceFormat12Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmPosBal', type=BalanceFormat12Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDtPosBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlElgblBal', type=TotalEligibleBalanceFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
	))

