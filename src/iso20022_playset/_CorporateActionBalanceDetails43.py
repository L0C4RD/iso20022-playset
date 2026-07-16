# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceFormat11Choice
from . import BalanceFormat12Choice
from . import TotalEligibleBalanceFormat10

class CorporateActionBalanceDetails43(base_types._BaseFieldType):

	__slots__ = ["_AfctdBal", "_BlckdBal", "_BrrwdBal", "_CollInBal", "_CollOutBal", "_InTrnsShipmntBal", "_InstdBal", "_OblgtdBal", "_OnLnBal", "_OutForRegnBal", "_PdgDlvryBal", "_PdgRctBal", "_RegdBal", "_StrtPosBal", "_SttlmPosBal", "_TradDtPosBal", "_TtlElgblBal", "_UafctdBal", "_UinstdBal"]
	@property
	def AfctdBal(self):
		return self._AfctdBal

	@AfctdBal.setter
	def AfctdBal(self, value):
		self._AfctdBal = value if value is not None else base_types.UninitialisedField(self, 'AfctdBal', BalanceFormat11Choice, False)

	@AfctdBal.deleter
	def AfctdBal(self):
		del self._AfctdBal
		self._AfctdBal = base_types.UninitialisedField(self, 'AfctdBal', BalanceFormat11Choice, False)

	@property
	def BlckdBal(self):
		return self._BlckdBal

	@BlckdBal.setter
	def BlckdBal(self, value):
		self._BlckdBal = value if value is not None else base_types.UninitialisedField(self, 'BlckdBal', BalanceFormat11Choice, False)

	@BlckdBal.deleter
	def BlckdBal(self):
		del self._BlckdBal
		self._BlckdBal = base_types.UninitialisedField(self, 'BlckdBal', BalanceFormat11Choice, False)

	@property
	def BrrwdBal(self):
		return self._BrrwdBal

	@BrrwdBal.setter
	def BrrwdBal(self, value):
		self._BrrwdBal = value if value is not None else base_types.UninitialisedField(self, 'BrrwdBal', BalanceFormat11Choice, False)

	@BrrwdBal.deleter
	def BrrwdBal(self):
		del self._BrrwdBal
		self._BrrwdBal = base_types.UninitialisedField(self, 'BrrwdBal', BalanceFormat11Choice, False)

	@property
	def CollInBal(self):
		return self._CollInBal

	@CollInBal.setter
	def CollInBal(self, value):
		self._CollInBal = value if value is not None else base_types.UninitialisedField(self, 'CollInBal', BalanceFormat11Choice, False)

	@CollInBal.deleter
	def CollInBal(self):
		del self._CollInBal
		self._CollInBal = base_types.UninitialisedField(self, 'CollInBal', BalanceFormat11Choice, False)

	@property
	def CollOutBal(self):
		return self._CollOutBal

	@CollOutBal.setter
	def CollOutBal(self, value):
		self._CollOutBal = value if value is not None else base_types.UninitialisedField(self, 'CollOutBal', BalanceFormat11Choice, False)

	@CollOutBal.deleter
	def CollOutBal(self):
		del self._CollOutBal
		self._CollOutBal = base_types.UninitialisedField(self, 'CollOutBal', BalanceFormat11Choice, False)

	@property
	def InTrnsShipmntBal(self):
		return self._InTrnsShipmntBal

	@InTrnsShipmntBal.setter
	def InTrnsShipmntBal(self, value):
		self._InTrnsShipmntBal = value if value is not None else base_types.UninitialisedField(self, 'InTrnsShipmntBal', BalanceFormat11Choice, False)

	@InTrnsShipmntBal.deleter
	def InTrnsShipmntBal(self):
		del self._InTrnsShipmntBal
		self._InTrnsShipmntBal = base_types.UninitialisedField(self, 'InTrnsShipmntBal', BalanceFormat11Choice, False)

	@property
	def InstdBal(self):
		return self._InstdBal

	@InstdBal.setter
	def InstdBal(self, value):
		self._InstdBal = value if value is not None else base_types.UninitialisedField(self, 'InstdBal', BalanceFormat11Choice, False)

	@InstdBal.deleter
	def InstdBal(self):
		del self._InstdBal
		self._InstdBal = base_types.UninitialisedField(self, 'InstdBal', BalanceFormat11Choice, False)

	@property
	def OblgtdBal(self):
		return self._OblgtdBal

	@OblgtdBal.setter
	def OblgtdBal(self, value):
		self._OblgtdBal = value if value is not None else base_types.UninitialisedField(self, 'OblgtdBal', BalanceFormat11Choice, False)

	@OblgtdBal.deleter
	def OblgtdBal(self):
		del self._OblgtdBal
		self._OblgtdBal = base_types.UninitialisedField(self, 'OblgtdBal', BalanceFormat11Choice, False)

	@property
	def OnLnBal(self):
		return self._OnLnBal

	@OnLnBal.setter
	def OnLnBal(self, value):
		self._OnLnBal = value if value is not None else base_types.UninitialisedField(self, 'OnLnBal', BalanceFormat11Choice, False)

	@OnLnBal.deleter
	def OnLnBal(self):
		del self._OnLnBal
		self._OnLnBal = base_types.UninitialisedField(self, 'OnLnBal', BalanceFormat11Choice, False)

	@property
	def OutForRegnBal(self):
		return self._OutForRegnBal

	@OutForRegnBal.setter
	def OutForRegnBal(self, value):
		self._OutForRegnBal = value if value is not None else base_types.UninitialisedField(self, 'OutForRegnBal', BalanceFormat11Choice, False)

	@OutForRegnBal.deleter
	def OutForRegnBal(self):
		del self._OutForRegnBal
		self._OutForRegnBal = base_types.UninitialisedField(self, 'OutForRegnBal', BalanceFormat11Choice, False)

	@property
	def PdgDlvryBal(self):
		return self._PdgDlvryBal

	@PdgDlvryBal.setter
	def PdgDlvryBal(self, value):
		self._PdgDlvryBal = value if value is not None else base_types.UninitialisedField(self, 'PdgDlvryBal', BalanceFormat12Choice, True)

	@PdgDlvryBal.deleter
	def PdgDlvryBal(self):
		del self._PdgDlvryBal
		self._PdgDlvryBal = base_types.UninitialisedField(self, 'PdgDlvryBal', BalanceFormat12Choice, True)

	@property
	def PdgRctBal(self):
		return self._PdgRctBal

	@PdgRctBal.setter
	def PdgRctBal(self, value):
		self._PdgRctBal = value if value is not None else base_types.UninitialisedField(self, 'PdgRctBal', BalanceFormat12Choice, True)

	@PdgRctBal.deleter
	def PdgRctBal(self):
		del self._PdgRctBal
		self._PdgRctBal = base_types.UninitialisedField(self, 'PdgRctBal', BalanceFormat12Choice, True)

	@property
	def RegdBal(self):
		return self._RegdBal

	@RegdBal.setter
	def RegdBal(self, value):
		self._RegdBal = value if value is not None else base_types.UninitialisedField(self, 'RegdBal', BalanceFormat11Choice, False)

	@RegdBal.deleter
	def RegdBal(self):
		del self._RegdBal
		self._RegdBal = base_types.UninitialisedField(self, 'RegdBal', BalanceFormat11Choice, False)

	@property
	def StrtPosBal(self):
		return self._StrtPosBal

	@StrtPosBal.setter
	def StrtPosBal(self, value):
		self._StrtPosBal = value if value is not None else base_types.UninitialisedField(self, 'StrtPosBal', BalanceFormat11Choice, False)

	@StrtPosBal.deleter
	def StrtPosBal(self):
		del self._StrtPosBal
		self._StrtPosBal = base_types.UninitialisedField(self, 'StrtPosBal', BalanceFormat11Choice, False)

	@property
	def SttlmPosBal(self):
		return self._SttlmPosBal

	@SttlmPosBal.setter
	def SttlmPosBal(self, value):
		self._SttlmPosBal = value if value is not None else base_types.UninitialisedField(self, 'SttlmPosBal', BalanceFormat12Choice, True)

	@SttlmPosBal.deleter
	def SttlmPosBal(self):
		del self._SttlmPosBal
		self._SttlmPosBal = base_types.UninitialisedField(self, 'SttlmPosBal', BalanceFormat12Choice, True)

	@property
	def TradDtPosBal(self):
		return self._TradDtPosBal

	@TradDtPosBal.setter
	def TradDtPosBal(self, value):
		self._TradDtPosBal = value if value is not None else base_types.UninitialisedField(self, 'TradDtPosBal', BalanceFormat11Choice, False)

	@TradDtPosBal.deleter
	def TradDtPosBal(self):
		del self._TradDtPosBal
		self._TradDtPosBal = base_types.UninitialisedField(self, 'TradDtPosBal', BalanceFormat11Choice, False)

	@property
	def TtlElgblBal(self):
		return self._TtlElgblBal

	@TtlElgblBal.setter
	def TtlElgblBal(self, value):
		self._TtlElgblBal = value if value is not None else base_types.UninitialisedField(self, 'TtlElgblBal', TotalEligibleBalanceFormat10, False)

	@TtlElgblBal.deleter
	def TtlElgblBal(self):
		del self._TtlElgblBal
		self._TtlElgblBal = base_types.UninitialisedField(self, 'TtlElgblBal', TotalEligibleBalanceFormat10, False)

	@property
	def UafctdBal(self):
		return self._UafctdBal

	@UafctdBal.setter
	def UafctdBal(self, value):
		self._UafctdBal = value if value is not None else base_types.UninitialisedField(self, 'UafctdBal', BalanceFormat11Choice, False)

	@UafctdBal.deleter
	def UafctdBal(self):
		del self._UafctdBal
		self._UafctdBal = base_types.UninitialisedField(self, 'UafctdBal', BalanceFormat11Choice, False)

	@property
	def UinstdBal(self):
		return self._UinstdBal

	@UinstdBal.setter
	def UinstdBal(self, value):
		self._UinstdBal = value if value is not None else base_types.UninitialisedField(self, 'UinstdBal', BalanceFormat11Choice, False)

	@UinstdBal.deleter
	def UinstdBal(self):
		del self._UinstdBal
		self._UinstdBal = base_types.UninitialisedField(self, 'UinstdBal', BalanceFormat11Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AfctdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollOutBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InTrnsShipmntBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLnBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutForRegnBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgDlvryBal', type=BalanceFormat12Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdgRctBal', type=BalanceFormat12Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtPosBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPosBal', type=BalanceFormat12Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDtPosBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlElgblBal', type=TotalEligibleBalanceFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UafctdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UinstdBal', type=BalanceFormat11Choice, min=0, max=1, mutex_group=None, array=False),
	))