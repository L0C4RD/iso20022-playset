from . import base_types
import Vehicle2
import PlainCardData17
import Max35NumericText
import TrueFalseIndicator
import DecimalNumber
import Max35Text
import CardDataReading5Code

class Vehicle1(base_types._BaseFieldType):

	__slots__ = ["_RefrHrs", "_AddtlVhclData", "_VhclNb", "_MntncId", "_UnitNb", "_VhclTag", "_TrlrHrs", "_TrlrNb", "_RplcmntCar", "_DrvrOrVhclCard", "_Hbmtr", "_VhclTagNtryMd", "_Odmtr"]
	@property
	def RefrHrs(self):
		return self._RefrHrs

	@RefrHrs.setter
	def RefrHrs(self, value):
		self._RefrHrs = value if type(value) != auto else self.make_default("RefrHrs")

	@RefrHrs.deleter
	def RefrHrs(self):
		del self._RefrHrs
		self._RefrHrs = None

	@property
	def AddtlVhclData(self):
		return self._AddtlVhclData

	@AddtlVhclData.setter
	def AddtlVhclData(self, value):
		self._AddtlVhclData = value if type(value) != auto else self.make_default("AddtlVhclData")

	@AddtlVhclData.deleter
	def AddtlVhclData(self):
		del self._AddtlVhclData
		self._AddtlVhclData = None

	@property
	def VhclNb(self):
		return self._VhclNb

	@VhclNb.setter
	def VhclNb(self, value):
		self._VhclNb = value if type(value) != auto else self.make_default("VhclNb")

	@VhclNb.deleter
	def VhclNb(self):
		del self._VhclNb
		self._VhclNb = None

	@property
	def MntncId(self):
		return self._MntncId

	@MntncId.setter
	def MntncId(self, value):
		self._MntncId = value if type(value) != auto else self.make_default("MntncId")

	@MntncId.deleter
	def MntncId(self):
		del self._MntncId
		self._MntncId = None

	@property
	def UnitNb(self):
		return self._UnitNb

	@UnitNb.setter
	def UnitNb(self, value):
		self._UnitNb = value if type(value) != auto else self.make_default("UnitNb")

	@UnitNb.deleter
	def UnitNb(self):
		del self._UnitNb
		self._UnitNb = None

	@property
	def VhclTag(self):
		return self._VhclTag

	@VhclTag.setter
	def VhclTag(self, value):
		self._VhclTag = value if type(value) != auto else self.make_default("VhclTag")

	@VhclTag.deleter
	def VhclTag(self):
		del self._VhclTag
		self._VhclTag = None

	@property
	def TrlrHrs(self):
		return self._TrlrHrs

	@TrlrHrs.setter
	def TrlrHrs(self, value):
		self._TrlrHrs = value if type(value) != auto else self.make_default("TrlrHrs")

	@TrlrHrs.deleter
	def TrlrHrs(self):
		del self._TrlrHrs
		self._TrlrHrs = None

	@property
	def TrlrNb(self):
		return self._TrlrNb

	@TrlrNb.setter
	def TrlrNb(self, value):
		self._TrlrNb = value if type(value) != auto else self.make_default("TrlrNb")

	@TrlrNb.deleter
	def TrlrNb(self):
		del self._TrlrNb
		self._TrlrNb = None

	@property
	def RplcmntCar(self):
		return self._RplcmntCar

	@RplcmntCar.setter
	def RplcmntCar(self, value):
		self._RplcmntCar = value if type(value) != auto else self.make_default("RplcmntCar")

	@RplcmntCar.deleter
	def RplcmntCar(self):
		del self._RplcmntCar
		self._RplcmntCar = None

	@property
	def DrvrOrVhclCard(self):
		return self._DrvrOrVhclCard

	@DrvrOrVhclCard.setter
	def DrvrOrVhclCard(self, value):
		self._DrvrOrVhclCard = value if type(value) != auto else self.make_default("DrvrOrVhclCard")

	@DrvrOrVhclCard.deleter
	def DrvrOrVhclCard(self):
		del self._DrvrOrVhclCard
		self._DrvrOrVhclCard = None

	@property
	def Hbmtr(self):
		return self._Hbmtr

	@Hbmtr.setter
	def Hbmtr(self, value):
		self._Hbmtr = value if type(value) != auto else self.make_default("Hbmtr")

	@Hbmtr.deleter
	def Hbmtr(self):
		del self._Hbmtr
		self._Hbmtr = None

	@property
	def VhclTagNtryMd(self):
		return self._VhclTagNtryMd

	@VhclTagNtryMd.setter
	def VhclTagNtryMd(self, value):
		self._VhclTagNtryMd = value if type(value) != auto else self.make_default("VhclTagNtryMd")

	@VhclTagNtryMd.deleter
	def VhclTagNtryMd(self):
		del self._VhclTagNtryMd
		self._VhclTagNtryMd = None

	@property
	def Odmtr(self):
		return self._Odmtr

	@Odmtr.setter
	def Odmtr(self, value):
		self._Odmtr = value if type(value) != auto else self.make_default("Odmtr")

	@Odmtr.deleter
	def Odmtr(self):
		del self._Odmtr
		self._Odmtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RefrHrs', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlVhclData', type=Vehicle2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VhclNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VhclTag', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrlrHrs', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrlrNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RplcmntCar', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrOrVhclCard', type=PlainCardData17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hbmtr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VhclTagNtryMd', type=CardDataReading5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Odmtr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

