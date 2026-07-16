# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceFormat14Choice
from . import Quantity80Choice

class CorporateActionBalanceDetails44(base_types._BaseFieldType):

	__slots__ = ["_BlckdBal", "_BrrwdBal", "_CollInBal", "_CollOutBal", "_InTrnsShipmntBal", "_OnLnBal", "_OutForRegnBal", "_PdgDlvryBal", "_PdgRctBal", "_RegdBal", "_StrtPosBal", "_SttlmPosBal", "_TradDtPosBal", "_TtlElgblBal"]
	@property
	def BlckdBal(self):
		return self._BlckdBal

	@BlckdBal.setter
	def BlckdBal(self, value):
		self._BlckdBal = value if value is not None else base_types.UninitialisedField(self, 'BlckdBal', BalanceFormat14Choice, False)

	@BlckdBal.deleter
	def BlckdBal(self):
		del self._BlckdBal
		self._BlckdBal = base_types.UninitialisedField(self, 'BlckdBal', BalanceFormat14Choice, False)

	@property
	def BrrwdBal(self):
		return self._BrrwdBal

	@BrrwdBal.setter
	def BrrwdBal(self, value):
		self._BrrwdBal = value if value is not None else base_types.UninitialisedField(self, 'BrrwdBal', BalanceFormat14Choice, False)

	@BrrwdBal.deleter
	def BrrwdBal(self):
		del self._BrrwdBal
		self._BrrwdBal = base_types.UninitialisedField(self, 'BrrwdBal', BalanceFormat14Choice, False)

	@property
	def CollInBal(self):
		return self._CollInBal

	@CollInBal.setter
	def CollInBal(self, value):
		self._CollInBal = value if value is not None else base_types.UninitialisedField(self, 'CollInBal', BalanceFormat14Choice, False)

	@CollInBal.deleter
	def CollInBal(self):
		del self._CollInBal
		self._CollInBal = base_types.UninitialisedField(self, 'CollInBal', BalanceFormat14Choice, False)

	@property
	def CollOutBal(self):
		return self._CollOutBal

	@CollOutBal.setter
	def CollOutBal(self, value):
		self._CollOutBal = value if value is not None else base_types.UninitialisedField(self, 'CollOutBal', BalanceFormat14Choice, False)

	@CollOutBal.deleter
	def CollOutBal(self):
		del self._CollOutBal
		self._CollOutBal = base_types.UninitialisedField(self, 'CollOutBal', BalanceFormat14Choice, False)

	@property
	def InTrnsShipmntBal(self):
		return self._InTrnsShipmntBal

	@InTrnsShipmntBal.setter
	def InTrnsShipmntBal(self, value):
		self._InTrnsShipmntBal = value if value is not None else base_types.UninitialisedField(self, 'InTrnsShipmntBal', BalanceFormat14Choice, False)

	@InTrnsShipmntBal.deleter
	def InTrnsShipmntBal(self):
		del self._InTrnsShipmntBal
		self._InTrnsShipmntBal = base_types.UninitialisedField(self, 'InTrnsShipmntBal', BalanceFormat14Choice, False)

	@property
	def OnLnBal(self):
		return self._OnLnBal

	@OnLnBal.setter
	def OnLnBal(self, value):
		self._OnLnBal = value if value is not None else base_types.UninitialisedField(self, 'OnLnBal', BalanceFormat14Choice, False)

	@OnLnBal.deleter
	def OnLnBal(self):
		del self._OnLnBal
		self._OnLnBal = base_types.UninitialisedField(self, 'OnLnBal', BalanceFormat14Choice, False)

	@property
	def OutForRegnBal(self):
		return self._OutForRegnBal

	@OutForRegnBal.setter
	def OutForRegnBal(self, value):
		self._OutForRegnBal = value if value is not None else base_types.UninitialisedField(self, 'OutForRegnBal', BalanceFormat14Choice, False)

	@OutForRegnBal.deleter
	def OutForRegnBal(self):
		del self._OutForRegnBal
		self._OutForRegnBal = base_types.UninitialisedField(self, 'OutForRegnBal', BalanceFormat14Choice, False)

	@property
	def PdgDlvryBal(self):
		return self._PdgDlvryBal

	@PdgDlvryBal.setter
	def PdgDlvryBal(self, value):
		self._PdgDlvryBal = value if value is not None else base_types.UninitialisedField(self, 'PdgDlvryBal', BalanceFormat14Choice, True)

	@PdgDlvryBal.deleter
	def PdgDlvryBal(self):
		del self._PdgDlvryBal
		self._PdgDlvryBal = base_types.UninitialisedField(self, 'PdgDlvryBal', BalanceFormat14Choice, True)

	@property
	def PdgRctBal(self):
		return self._PdgRctBal

	@PdgRctBal.setter
	def PdgRctBal(self, value):
		self._PdgRctBal = value if value is not None else base_types.UninitialisedField(self, 'PdgRctBal', BalanceFormat14Choice, True)

	@PdgRctBal.deleter
	def PdgRctBal(self):
		del self._PdgRctBal
		self._PdgRctBal = base_types.UninitialisedField(self, 'PdgRctBal', BalanceFormat14Choice, True)

	@property
	def RegdBal(self):
		return self._RegdBal

	@RegdBal.setter
	def RegdBal(self, value):
		self._RegdBal = value if value is not None else base_types.UninitialisedField(self, 'RegdBal', BalanceFormat14Choice, False)

	@RegdBal.deleter
	def RegdBal(self):
		del self._RegdBal
		self._RegdBal = base_types.UninitialisedField(self, 'RegdBal', BalanceFormat14Choice, False)

	@property
	def StrtPosBal(self):
		return self._StrtPosBal

	@StrtPosBal.setter
	def StrtPosBal(self, value):
		self._StrtPosBal = value if value is not None else base_types.UninitialisedField(self, 'StrtPosBal', BalanceFormat14Choice, False)

	@StrtPosBal.deleter
	def StrtPosBal(self):
		del self._StrtPosBal
		self._StrtPosBal = base_types.UninitialisedField(self, 'StrtPosBal', BalanceFormat14Choice, False)

	@property
	def SttlmPosBal(self):
		return self._SttlmPosBal

	@SttlmPosBal.setter
	def SttlmPosBal(self, value):
		self._SttlmPosBal = value if value is not None else base_types.UninitialisedField(self, 'SttlmPosBal', BalanceFormat14Choice, False)

	@SttlmPosBal.deleter
	def SttlmPosBal(self):
		del self._SttlmPosBal
		self._SttlmPosBal = base_types.UninitialisedField(self, 'SttlmPosBal', BalanceFormat14Choice, False)

	@property
	def TradDtPosBal(self):
		return self._TradDtPosBal

	@TradDtPosBal.setter
	def TradDtPosBal(self, value):
		self._TradDtPosBal = value if value is not None else base_types.UninitialisedField(self, 'TradDtPosBal', BalanceFormat14Choice, False)

	@TradDtPosBal.deleter
	def TradDtPosBal(self):
		del self._TradDtPosBal
		self._TradDtPosBal = base_types.UninitialisedField(self, 'TradDtPosBal', BalanceFormat14Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollOutBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InTrnsShipmntBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLnBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutForRegnBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgDlvryBal', type=BalanceFormat14Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdgRctBal', type=BalanceFormat14Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtPosBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPosBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtPosBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlElgblBal', type=Quantity80Choice, min=0, max=1, mutex_group=None, array=False),
	))