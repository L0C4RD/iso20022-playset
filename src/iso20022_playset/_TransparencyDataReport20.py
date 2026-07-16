# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InstrumentOrSubClassIdentification2Choice
from . import MICIdentifier
from . import Max350Text
from . import Max35Text
from . import Period4Choice
from . import StatisticsTransparency2
from . import TonsOrCurrency2Choice
from . import TrueFalseIndicator

class TransparencyDataReport20(base_types._BaseFieldType):

	__slots__ = ["_FullNm", "_Id", "_Lqdty", "_PreTradInstrmSzSpcfcThrshld", "_PreTradLrgInScaleThrshld", "_PstTradInstrmSzSpcfcThrshld", "_PstTradLrgInScaleThrshld", "_RptgPrd", "_Sttstcs", "_TechRcrdId", "_TradgVn"]
	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if value is not None else base_types.UninitialisedField(self, 'FullNm', Max350Text, False)

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = base_types.UninitialisedField(self, 'FullNm', Max350Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', InstrumentOrSubClassIdentification2Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', InstrumentOrSubClassIdentification2Choice, False)

	@property
	def Lqdty(self):
		return self._Lqdty

	@Lqdty.setter
	def Lqdty(self, value):
		self._Lqdty = value if value is not None else base_types.UninitialisedField(self, 'Lqdty', TrueFalseIndicator, False)

	@Lqdty.deleter
	def Lqdty(self):
		del self._Lqdty
		self._Lqdty = base_types.UninitialisedField(self, 'Lqdty', TrueFalseIndicator, False)

	@property
	def PreTradInstrmSzSpcfcThrshld(self):
		return self._PreTradInstrmSzSpcfcThrshld

	@PreTradInstrmSzSpcfcThrshld.setter
	def PreTradInstrmSzSpcfcThrshld(self, value):
		self._PreTradInstrmSzSpcfcThrshld = value if value is not None else base_types.UninitialisedField(self, 'PreTradInstrmSzSpcfcThrshld', TonsOrCurrency2Choice, False)

	@PreTradInstrmSzSpcfcThrshld.deleter
	def PreTradInstrmSzSpcfcThrshld(self):
		del self._PreTradInstrmSzSpcfcThrshld
		self._PreTradInstrmSzSpcfcThrshld = base_types.UninitialisedField(self, 'PreTradInstrmSzSpcfcThrshld', TonsOrCurrency2Choice, False)

	@property
	def PreTradLrgInScaleThrshld(self):
		return self._PreTradLrgInScaleThrshld

	@PreTradLrgInScaleThrshld.setter
	def PreTradLrgInScaleThrshld(self, value):
		self._PreTradLrgInScaleThrshld = value if value is not None else base_types.UninitialisedField(self, 'PreTradLrgInScaleThrshld', TonsOrCurrency2Choice, False)

	@PreTradLrgInScaleThrshld.deleter
	def PreTradLrgInScaleThrshld(self):
		del self._PreTradLrgInScaleThrshld
		self._PreTradLrgInScaleThrshld = base_types.UninitialisedField(self, 'PreTradLrgInScaleThrshld', TonsOrCurrency2Choice, False)

	@property
	def PstTradInstrmSzSpcfcThrshld(self):
		return self._PstTradInstrmSzSpcfcThrshld

	@PstTradInstrmSzSpcfcThrshld.setter
	def PstTradInstrmSzSpcfcThrshld(self, value):
		self._PstTradInstrmSzSpcfcThrshld = value if value is not None else base_types.UninitialisedField(self, 'PstTradInstrmSzSpcfcThrshld', TonsOrCurrency2Choice, False)

	@PstTradInstrmSzSpcfcThrshld.deleter
	def PstTradInstrmSzSpcfcThrshld(self):
		del self._PstTradInstrmSzSpcfcThrshld
		self._PstTradInstrmSzSpcfcThrshld = base_types.UninitialisedField(self, 'PstTradInstrmSzSpcfcThrshld', TonsOrCurrency2Choice, False)

	@property
	def PstTradLrgInScaleThrshld(self):
		return self._PstTradLrgInScaleThrshld

	@PstTradLrgInScaleThrshld.setter
	def PstTradLrgInScaleThrshld(self, value):
		self._PstTradLrgInScaleThrshld = value if value is not None else base_types.UninitialisedField(self, 'PstTradLrgInScaleThrshld', TonsOrCurrency2Choice, False)

	@PstTradLrgInScaleThrshld.deleter
	def PstTradLrgInScaleThrshld(self):
		del self._PstTradLrgInScaleThrshld
		self._PstTradLrgInScaleThrshld = base_types.UninitialisedField(self, 'PstTradLrgInScaleThrshld', TonsOrCurrency2Choice, False)

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if value is not None else base_types.UninitialisedField(self, 'RptgPrd', Period4Choice, False)

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = base_types.UninitialisedField(self, 'RptgPrd', Period4Choice, False)

	@property
	def Sttstcs(self):
		return self._Sttstcs

	@Sttstcs.setter
	def Sttstcs(self, value):
		self._Sttstcs = value if value is not None else base_types.UninitialisedField(self, 'Sttstcs', StatisticsTransparency2, False)

	@Sttstcs.deleter
	def Sttstcs(self):
		del self._Sttstcs
		self._Sttstcs = base_types.UninitialisedField(self, 'Sttstcs', StatisticsTransparency2, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=InstrumentOrSubClassIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lqdty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreTradInstrmSzSpcfcThrshld', type=TonsOrCurrency2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreTradLrgInScaleThrshld', type=TonsOrCurrency2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradInstrmSzSpcfcThrshld', type=TonsOrCurrency2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradLrgInScaleThrshld', type=TonsOrCurrency2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttstcs', type=StatisticsTransparency2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
	))