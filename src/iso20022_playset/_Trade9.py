# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AnyBICDec2014Identifier
from . import ClearingMethod1Code
from . import ISODate
from . import InstrumentLeg7
from . import Max35Text
from . import Max70Text
from . import SecurityIdentification38Choice
from . import Trade10
from . import TradingMethodType1Code
from . import TradingModeType1Code
from . import UnderlyingProductIdentifier1Code

class Trade9(base_types._BaseFieldType):

	__slots__ = ["_AssoctdTradRef", "_ClrMtd", "_FXDtls", "_FXTradPdct", "_PdctId", "_PlcOfConf", "_SttlmCcy", "_SwpLeg", "_Symb", "_TradDt", "_TradId", "_TradgCcy", "_TradgMd", "_TradgMtd"]
	@property
	def AssoctdTradRef(self):
		return self._AssoctdTradRef

	@AssoctdTradRef.setter
	def AssoctdTradRef(self, value):
		self._AssoctdTradRef = value if value is not None else base_types.UninitialisedField(self, 'AssoctdTradRef', Max70Text, True)

	@AssoctdTradRef.deleter
	def AssoctdTradRef(self):
		del self._AssoctdTradRef
		self._AssoctdTradRef = base_types.UninitialisedField(self, 'AssoctdTradRef', Max70Text, True)

	@property
	def ClrMtd(self):
		return self._ClrMtd

	@ClrMtd.setter
	def ClrMtd(self, value):
		self._ClrMtd = value if value is not None else base_types.UninitialisedField(self, 'ClrMtd', ClearingMethod1Code, False)

	@ClrMtd.deleter
	def ClrMtd(self):
		del self._ClrMtd
		self._ClrMtd = base_types.UninitialisedField(self, 'ClrMtd', ClearingMethod1Code, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', Trade10, False)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', Trade10, False)

	@property
	def FXTradPdct(self):
		return self._FXTradPdct

	@FXTradPdct.setter
	def FXTradPdct(self, value):
		self._FXTradPdct = value if value is not None else base_types.UninitialisedField(self, 'FXTradPdct', UnderlyingProductIdentifier1Code, False)

	@FXTradPdct.deleter
	def FXTradPdct(self):
		del self._FXTradPdct
		self._FXTradPdct = base_types.UninitialisedField(self, 'FXTradPdct', UnderlyingProductIdentifier1Code, False)

	@property
	def PdctId(self):
		return self._PdctId

	@PdctId.setter
	def PdctId(self, value):
		self._PdctId = value if value is not None else base_types.UninitialisedField(self, 'PdctId', SecurityIdentification38Choice, False)

	@PdctId.deleter
	def PdctId(self):
		del self._PdctId
		self._PdctId = base_types.UninitialisedField(self, 'PdctId', SecurityIdentification38Choice, False)

	@property
	def PlcOfConf(self):
		return self._PlcOfConf

	@PlcOfConf.setter
	def PlcOfConf(self, value):
		self._PlcOfConf = value if value is not None else base_types.UninitialisedField(self, 'PlcOfConf', AnyBICDec2014Identifier, False)

	@PlcOfConf.deleter
	def PlcOfConf(self):
		del self._PlcOfConf
		self._PlcOfConf = base_types.UninitialisedField(self, 'PlcOfConf', AnyBICDec2014Identifier, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@property
	def SwpLeg(self):
		return self._SwpLeg

	@SwpLeg.setter
	def SwpLeg(self, value):
		self._SwpLeg = value if value is not None else base_types.UninitialisedField(self, 'SwpLeg', InstrumentLeg7, True)

	@SwpLeg.deleter
	def SwpLeg(self):
		del self._SwpLeg
		self._SwpLeg = base_types.UninitialisedField(self, 'SwpLeg', InstrumentLeg7, True)

	@property
	def Symb(self):
		return self._Symb

	@Symb.setter
	def Symb(self, value):
		self._Symb = value if value is not None else base_types.UninitialisedField(self, 'Symb', Max35Text, False)

	@Symb.deleter
	def Symb(self):
		del self._Symb
		self._Symb = base_types.UninitialisedField(self, 'Symb', Max35Text, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if value is not None else base_types.UninitialisedField(self, 'TradId', Max35Text, False)

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = base_types.UninitialisedField(self, 'TradId', Max35Text, False)

	@property
	def TradgCcy(self):
		return self._TradgCcy

	@TradgCcy.setter
	def TradgCcy(self, value):
		self._TradgCcy = value if value is not None else base_types.UninitialisedField(self, 'TradgCcy', ActiveCurrencyCode, False)

	@TradgCcy.deleter
	def TradgCcy(self):
		del self._TradgCcy
		self._TradgCcy = base_types.UninitialisedField(self, 'TradgCcy', ActiveCurrencyCode, False)

	@property
	def TradgMd(self):
		return self._TradgMd

	@TradgMd.setter
	def TradgMd(self, value):
		self._TradgMd = value if value is not None else base_types.UninitialisedField(self, 'TradgMd', TradingModeType1Code, False)

	@TradgMd.deleter
	def TradgMd(self):
		del self._TradgMd
		self._TradgMd = base_types.UninitialisedField(self, 'TradgMd', TradingModeType1Code, False)

	@property
	def TradgMtd(self):
		return self._TradgMtd

	@TradgMtd.setter
	def TradgMtd(self, value):
		self._TradgMtd = value if value is not None else base_types.UninitialisedField(self, 'TradgMtd', TradingMethodType1Code, False)

	@TradgMtd.deleter
	def TradgMtd(self):
		del self._TradgMtd
		self._TradgMtd = base_types.UninitialisedField(self, 'TradgMtd', TradingMethodType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssoctdTradRef', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrMtd', type=ClearingMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=Trade10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXTradPdct', type=UnderlyingProductIdentifier1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctId', type=SecurityIdentification38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfConf', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwpLeg', type=InstrumentLeg7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Symb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgMd', type=TradingModeType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgMtd', type=TradingMethodType1Code, min=0, max=1, mutex_group=None, array=False),
	))