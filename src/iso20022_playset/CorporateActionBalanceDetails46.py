import base_types
import BalanceFormat16Choice
import BalanceFormat14Choice
import TotalEligibleBalanceFormat11

class CorporateActionBalanceDetails46(base_types._BaseFieldType):

	__slots__ = ["_InstdBal", "_OblgtdBal", "_PdgRctBal", "_RegdBal", "_BrrwdBal", "_OnLnBal", "_TradDtPosBal", "_CollOutBal", "_AfctdBal", "_UinstdBal", "_InTrnsShipmntBal", "_BlckdBal", "_OutForRegnBal", "_TtlElgblBal", "_SttlmPosBal", "_StrtPosBal", "_PdgDlvryBal", "_UafctdBal", "_CollInBal"]
	@property
	def InstdBal(self):
		return self._InstdBal

	@InstdBal.setter
	def InstdBal(self, value):
		self._InstdBal = value if type(value) != auto else self.make_default("InstdBal")

	@InstdBal.deleter
	def InstdBal(self):
		del self._InstdBal
		self._InstdBal = None

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
	def BrrwdBal(self):
		return self._BrrwdBal

	@BrrwdBal.setter
	def BrrwdBal(self, value):
		self._BrrwdBal = value if type(value) != auto else self.make_default("BrrwdBal")

	@BrrwdBal.deleter
	def BrrwdBal(self):
		del self._BrrwdBal
		self._BrrwdBal = None

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
	def AfctdBal(self):
		return self._AfctdBal

	@AfctdBal.setter
	def AfctdBal(self, value):
		self._AfctdBal = value if type(value) != auto else self.make_default("AfctdBal")

	@AfctdBal.deleter
	def AfctdBal(self):
		del self._AfctdBal
		self._AfctdBal = None

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
	def UafctdBal(self):
		return self._UafctdBal

	@UafctdBal.setter
	def UafctdBal(self, value):
		self._UafctdBal = value if type(value) != auto else self.make_default("UafctdBal")

	@UafctdBal.deleter
	def UafctdBal(self):
		del self._UafctdBal
		self._UafctdBal = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgRctBal', type=BalanceFormat16Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLnBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtPosBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollOutBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AfctdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UinstdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InTrnsShipmntBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutForRegnBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlElgblBal', type=TotalEligibleBalanceFormat11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPosBal', type=BalanceFormat16Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StrtPosBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgDlvryBal', type=BalanceFormat16Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UafctdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
	))

