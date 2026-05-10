import base_types
import Max70Text
import InstrumentLeg7
import SecurityIdentification38Choice
import ActiveCurrencyCode
import TradingMethodType1Code
import ClearingMethod1Code
import ISODate
import TradingModeType1Code
import Max35Text
import Trade10
import UnderlyingProductIdentifier1Code
import AnyBICDec2014Identifier

class Trade9(base_types._BaseFieldType):

	__slots__ = ["_SwpLeg", "_SttlmCcy", "_ClrMtd", "_Symb", "_PdctId", "_TradgMtd", "_TradDt", "_FXDtls", "_AssoctdTradRef", "_TradgCcy", "_TradgMd", "_FXTradPdct", "_PlcOfConf", "_TradId"]
	@property
	def SwpLeg(self):
		return self._SwpLeg

	@SwpLeg.setter
	def SwpLeg(self, value):
		self._SwpLeg = value if type(value) != auto else self.make_default("SwpLeg")

	@SwpLeg.deleter
	def SwpLeg(self):
		del self._SwpLeg
		self._SwpLeg = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def ClrMtd(self):
		return self._ClrMtd

	@ClrMtd.setter
	def ClrMtd(self, value):
		self._ClrMtd = value if type(value) != auto else self.make_default("ClrMtd")

	@ClrMtd.deleter
	def ClrMtd(self):
		del self._ClrMtd
		self._ClrMtd = None

	@property
	def Symb(self):
		return self._Symb

	@Symb.setter
	def Symb(self, value):
		self._Symb = value if type(value) != auto else self.make_default("Symb")

	@Symb.deleter
	def Symb(self):
		del self._Symb
		self._Symb = None

	@property
	def PdctId(self):
		return self._PdctId

	@PdctId.setter
	def PdctId(self, value):
		self._PdctId = value if type(value) != auto else self.make_default("PdctId")

	@PdctId.deleter
	def PdctId(self):
		del self._PdctId
		self._PdctId = None

	@property
	def TradgMtd(self):
		return self._TradgMtd

	@TradgMtd.setter
	def TradgMtd(self, value):
		self._TradgMtd = value if type(value) != auto else self.make_default("TradgMtd")

	@TradgMtd.deleter
	def TradgMtd(self):
		del self._TradgMtd
		self._TradgMtd = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if type(value) != auto else self.make_default("FXDtls")

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = None

	@property
	def AssoctdTradRef(self):
		return self._AssoctdTradRef

	@AssoctdTradRef.setter
	def AssoctdTradRef(self, value):
		self._AssoctdTradRef = value if type(value) != auto else self.make_default("AssoctdTradRef")

	@AssoctdTradRef.deleter
	def AssoctdTradRef(self):
		del self._AssoctdTradRef
		self._AssoctdTradRef = None

	@property
	def TradgCcy(self):
		return self._TradgCcy

	@TradgCcy.setter
	def TradgCcy(self, value):
		self._TradgCcy = value if type(value) != auto else self.make_default("TradgCcy")

	@TradgCcy.deleter
	def TradgCcy(self):
		del self._TradgCcy
		self._TradgCcy = None

	@property
	def TradgMd(self):
		return self._TradgMd

	@TradgMd.setter
	def TradgMd(self, value):
		self._TradgMd = value if type(value) != auto else self.make_default("TradgMd")

	@TradgMd.deleter
	def TradgMd(self):
		del self._TradgMd
		self._TradgMd = None

	@property
	def FXTradPdct(self):
		return self._FXTradPdct

	@FXTradPdct.setter
	def FXTradPdct(self, value):
		self._FXTradPdct = value if type(value) != auto else self.make_default("FXTradPdct")

	@FXTradPdct.deleter
	def FXTradPdct(self):
		del self._FXTradPdct
		self._FXTradPdct = None

	@property
	def PlcOfConf(self):
		return self._PlcOfConf

	@PlcOfConf.setter
	def PlcOfConf(self, value):
		self._PlcOfConf = value if type(value) != auto else self.make_default("PlcOfConf")

	@PlcOfConf.deleter
	def PlcOfConf(self):
		del self._PlcOfConf
		self._PlcOfConf = None

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if type(value) != auto else self.make_default("TradId")

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SwpLeg', type=InstrumentLeg7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMtd', type=ClearingMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Symb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctId', type=SecurityIdentification38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgMtd', type=TradingMethodType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=Trade10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdTradRef', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradgCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgMd', type=TradingModeType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXTradPdct', type=UnderlyingProductIdentifier1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfConf', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

