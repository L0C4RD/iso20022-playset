# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Clearing8
from . import PartyIdentification253Choice
from . import PartyIdentificationAndAccount227
from . import SecuritiesAccount18
from . import SecuritiesAccount19
from . import Settlement2
from . import SupplementaryData1
from . import TradeLeg14

class TradeLegNotificationV05(base_types._BaseFieldType):

	__slots__ = ["_ClrAcct", "_ClrDtls", "_ClrMmb", "_DlvryAcct", "_NonClrMmb", "_SplmtryData", "_SttlmDtls", "_TradLegDtls"]
	@property
	def ClrAcct(self):
		return self._ClrAcct

	@ClrAcct.setter
	def ClrAcct(self, value):
		self._ClrAcct = value if value is not None else base_types.UninitialisedField(self, 'ClrAcct', SecuritiesAccount18, False)

	@ClrAcct.deleter
	def ClrAcct(self):
		del self._ClrAcct
		self._ClrAcct = base_types.UninitialisedField(self, 'ClrAcct', SecuritiesAccount18, False)

	@property
	def ClrDtls(self):
		return self._ClrDtls

	@ClrDtls.setter
	def ClrDtls(self, value):
		self._ClrDtls = value if value is not None else base_types.UninitialisedField(self, 'ClrDtls', Clearing8, False)

	@ClrDtls.deleter
	def ClrDtls(self):
		del self._ClrDtls
		self._ClrDtls = base_types.UninitialisedField(self, 'ClrDtls', Clearing8, False)

	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if value is not None else base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification253Choice, False)

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification253Choice, False)

	@property
	def DlvryAcct(self):
		return self._DlvryAcct

	@DlvryAcct.setter
	def DlvryAcct(self, value):
		self._DlvryAcct = value if value is not None else base_types.UninitialisedField(self, 'DlvryAcct', SecuritiesAccount19, False)

	@DlvryAcct.deleter
	def DlvryAcct(self):
		del self._DlvryAcct
		self._DlvryAcct = base_types.UninitialisedField(self, 'DlvryAcct', SecuritiesAccount19, False)

	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if value is not None else base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount227, False)

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount227, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def SttlmDtls(self):
		return self._SttlmDtls

	@SttlmDtls.setter
	def SttlmDtls(self, value):
		self._SttlmDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmDtls', Settlement2, False)

	@SttlmDtls.deleter
	def SttlmDtls(self):
		del self._SttlmDtls
		self._SttlmDtls = base_types.UninitialisedField(self, 'SttlmDtls', Settlement2, False)

	@property
	def TradLegDtls(self):
		return self._TradLegDtls

	@TradLegDtls.setter
	def TradLegDtls(self, value):
		self._TradLegDtls = value if value is not None else base_types.UninitialisedField(self, 'TradLegDtls', TradeLeg14, False)

	@TradLegDtls.deleter
	def TradLegDtls(self):
		del self._TradLegDtls
		self._TradLegDtls = base_types.UninitialisedField(self, 'TradLegDtls', TradeLeg14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrAcct', type=SecuritiesAccount18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrDtls', type=Clearing8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification253Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount227, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmDtls', type=Settlement2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLegDtls', type=TradeLeg14, min=1, max=1, mutex_group=None, array=False),
	))