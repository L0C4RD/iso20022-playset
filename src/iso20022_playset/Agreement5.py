import base_types
import ISODateTime
import PercentageRate
import Max350Text
import ClosingType1Code
import ActiveCurrencyCode
import DeliveryType2Code

class Agreement5(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_MrgnRatio", "_ClsgTp", "_Dt", "_DlvryTp", "_Ccy", "_StartDt"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def MrgnRatio(self):
		return self._MrgnRatio

	@MrgnRatio.setter
	def MrgnRatio(self, value):
		self._MrgnRatio = value if type(value) != auto else self.make_default("MrgnRatio")

	@MrgnRatio.deleter
	def MrgnRatio(self):
		del self._MrgnRatio
		self._MrgnRatio = None

	@property
	def ClsgTp(self):
		return self._ClsgTp

	@ClsgTp.setter
	def ClsgTp(self, value):
		self._ClsgTp = value if type(value) != auto else self.make_default("ClsgTp")

	@ClsgTp.deleter
	def ClsgTp(self):
		del self._ClsgTp
		self._ClsgTp = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def DlvryTp(self):
		return self._DlvryTp

	@DlvryTp.setter
	def DlvryTp(self, value):
		self._DlvryTp = value if type(value) != auto else self.make_default("DlvryTp")

	@DlvryTp.deleter
	def DlvryTp(self):
		del self._DlvryTp
		self._DlvryTp = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRatio', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgTp', type=ClosingType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryTp', type=DeliveryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

