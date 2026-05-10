import base_types
import Max256Text
import ATMMediaType4Code
import Number
import ATMMediaType1Code
import CardDataReading4Code
import TrueFalseIndicator
import DisplayCapabilities5
import CardholderVerificationCapability3Code

class PointOfInteractionCapabilities10(base_types._BaseFieldType):

	__slots__ = ["_MxScrptLngth", "_IntractvTxs", "_MsgCpblties", "_RctPrtg", "_CardCaptrCpbl", "_ApprvlCdLngth", "_PINLngthCpblties", "_Authntcn", "_WdrwlMdia", "_CardWrtData", "_CardRdData", "_DpstdMdia"]
	@property
	def MxScrptLngth(self):
		return self._MxScrptLngth

	@MxScrptLngth.setter
	def MxScrptLngth(self, value):
		self._MxScrptLngth = value if type(value) != auto else self.make_default("MxScrptLngth")

	@MxScrptLngth.deleter
	def MxScrptLngth(self):
		del self._MxScrptLngth
		self._MxScrptLngth = None

	@property
	def IntractvTxs(self):
		return self._IntractvTxs

	@IntractvTxs.setter
	def IntractvTxs(self, value):
		self._IntractvTxs = value if type(value) != auto else self.make_default("IntractvTxs")

	@IntractvTxs.deleter
	def IntractvTxs(self):
		del self._IntractvTxs
		self._IntractvTxs = None

	@property
	def MsgCpblties(self):
		return self._MsgCpblties

	@MsgCpblties.setter
	def MsgCpblties(self, value):
		self._MsgCpblties = value if type(value) != auto else self.make_default("MsgCpblties")

	@MsgCpblties.deleter
	def MsgCpblties(self):
		del self._MsgCpblties
		self._MsgCpblties = None

	@property
	def RctPrtg(self):
		return self._RctPrtg

	@RctPrtg.setter
	def RctPrtg(self, value):
		self._RctPrtg = value if type(value) != auto else self.make_default("RctPrtg")

	@RctPrtg.deleter
	def RctPrtg(self):
		del self._RctPrtg
		self._RctPrtg = None

	@property
	def CardCaptrCpbl(self):
		return self._CardCaptrCpbl

	@CardCaptrCpbl.setter
	def CardCaptrCpbl(self, value):
		self._CardCaptrCpbl = value if type(value) != auto else self.make_default("CardCaptrCpbl")

	@CardCaptrCpbl.deleter
	def CardCaptrCpbl(self):
		del self._CardCaptrCpbl
		self._CardCaptrCpbl = None

	@property
	def ApprvlCdLngth(self):
		return self._ApprvlCdLngth

	@ApprvlCdLngth.setter
	def ApprvlCdLngth(self, value):
		self._ApprvlCdLngth = value if type(value) != auto else self.make_default("ApprvlCdLngth")

	@ApprvlCdLngth.deleter
	def ApprvlCdLngth(self):
		del self._ApprvlCdLngth
		self._ApprvlCdLngth = None

	@property
	def PINLngthCpblties(self):
		return self._PINLngthCpblties

	@PINLngthCpblties.setter
	def PINLngthCpblties(self, value):
		self._PINLngthCpblties = value if type(value) != auto else self.make_default("PINLngthCpblties")

	@PINLngthCpblties.deleter
	def PINLngthCpblties(self):
		del self._PINLngthCpblties
		self._PINLngthCpblties = None

	@property
	def Authntcn(self):
		return self._Authntcn

	@Authntcn.setter
	def Authntcn(self, value):
		self._Authntcn = value if type(value) != auto else self.make_default("Authntcn")

	@Authntcn.deleter
	def Authntcn(self):
		del self._Authntcn
		self._Authntcn = None

	@property
	def WdrwlMdia(self):
		return self._WdrwlMdia

	@WdrwlMdia.setter
	def WdrwlMdia(self, value):
		self._WdrwlMdia = value if type(value) != auto else self.make_default("WdrwlMdia")

	@WdrwlMdia.deleter
	def WdrwlMdia(self):
		del self._WdrwlMdia
		self._WdrwlMdia = None

	@property
	def CardWrtData(self):
		return self._CardWrtData

	@CardWrtData.setter
	def CardWrtData(self, value):
		self._CardWrtData = value if type(value) != auto else self.make_default("CardWrtData")

	@CardWrtData.deleter
	def CardWrtData(self):
		del self._CardWrtData
		self._CardWrtData = None

	@property
	def CardRdData(self):
		return self._CardRdData

	@CardRdData.setter
	def CardRdData(self, value):
		self._CardRdData = value if type(value) != auto else self.make_default("CardRdData")

	@CardRdData.deleter
	def CardRdData(self):
		del self._CardRdData
		self._CardRdData = None

	@property
	def DpstdMdia(self):
		return self._DpstdMdia

	@DpstdMdia.setter
	def DpstdMdia(self, value):
		self._DpstdMdia = value if type(value) != auto else self.make_default("DpstdMdia")

	@DpstdMdia.deleter
	def DpstdMdia(self):
		del self._DpstdMdia
		self._DpstdMdia = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MxScrptLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntractvTxs', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgCpblties', type=DisplayCapabilities5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RctPrtg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCaptrCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApprvlCdLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINLngthCpblties', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Authntcn', type=CardholderVerificationCapability3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WdrwlMdia', type=ATMMediaType1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardWrtData', type=CardDataReading4Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardRdData', type=CardDataReading4Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DpstdMdia', type=ATMMediaType4Code, min=0, max=None, mutex_group=None, array=True),
	))

