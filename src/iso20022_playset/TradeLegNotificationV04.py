from . import base_types
from .TradeLeg11 import TradeLeg11
from .SupplementaryData1 import SupplementaryData1
from .PartyIdentificationAndAccount227 import PartyIdentificationAndAccount227
from .Settlement2 import Settlement2
from .SecuritiesAccount18 import SecuritiesAccount18
from .PartyIdentification253Choice import PartyIdentification253Choice
from .Clearing7 import Clearing7
from .SecuritiesAccount19 import SecuritiesAccount19

class TradeLegNotificationV04(base_types._BaseFieldType):

	__slots__ = ["_NonClrMmb", "_ClrDtls", "_SplmtryData", "_DlvryAcct", "_ClrMmb", "_SttlmDtls", "_TradLegDtls", "_ClrAcct"]
	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if type(value) != base_types.auto else self.make_default("NonClrMmb")

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = None

	@property
	def ClrDtls(self):
		return self._ClrDtls

	@ClrDtls.setter
	def ClrDtls(self, value):
		self._ClrDtls = value if type(value) != base_types.auto else self.make_default("ClrDtls")

	@ClrDtls.deleter
	def ClrDtls(self):
		del self._ClrDtls
		self._ClrDtls = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def DlvryAcct(self):
		return self._DlvryAcct

	@DlvryAcct.setter
	def DlvryAcct(self, value):
		self._DlvryAcct = value if type(value) != base_types.auto else self.make_default("DlvryAcct")

	@DlvryAcct.deleter
	def DlvryAcct(self):
		del self._DlvryAcct
		self._DlvryAcct = None

	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if type(value) != base_types.auto else self.make_default("ClrMmb")

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = None

	@property
	def SttlmDtls(self):
		return self._SttlmDtls

	@SttlmDtls.setter
	def SttlmDtls(self, value):
		self._SttlmDtls = value if type(value) != base_types.auto else self.make_default("SttlmDtls")

	@SttlmDtls.deleter
	def SttlmDtls(self):
		del self._SttlmDtls
		self._SttlmDtls = None

	@property
	def TradLegDtls(self):
		return self._TradLegDtls

	@TradLegDtls.setter
	def TradLegDtls(self, value):
		self._TradLegDtls = value if type(value) != base_types.auto else self.make_default("TradLegDtls")

	@TradLegDtls.deleter
	def TradLegDtls(self):
		del self._TradLegDtls
		self._TradLegDtls = None

	@property
	def ClrAcct(self):
		return self._ClrAcct

	@ClrAcct.setter
	def ClrAcct(self, value):
		self._ClrAcct = value if type(value) != base_types.auto else self.make_default("ClrAcct")

	@ClrAcct.deleter
	def ClrAcct(self):
		del self._ClrAcct
		self._ClrAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount227, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrDtls', type=Clearing7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvryAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification253Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDtls', type=Settlement2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLegDtls', type=TradeLeg11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAcct', type=SecuritiesAccount18, min=1, max=1, mutex_group=None, array=False),
	))

