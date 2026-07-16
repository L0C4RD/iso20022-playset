# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ClosingType1Code
from . import DeliveryType2Code
from . import ISODateTime
from . import Max350Text
from . import PercentageRate

class Agreement5(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_ClsgTp", "_Desc", "_DlvryTp", "_Dt", "_MrgnRatio", "_StartDt"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def ClsgTp(self):
		return self._ClsgTp

	@ClsgTp.setter
	def ClsgTp(self, value):
		self._ClsgTp = value if value is not None else base_types.UninitialisedField(self, 'ClsgTp', ClosingType1Code, False)

	@ClsgTp.deleter
	def ClsgTp(self):
		del self._ClsgTp
		self._ClsgTp = base_types.UninitialisedField(self, 'ClsgTp', ClosingType1Code, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@property
	def DlvryTp(self):
		return self._DlvryTp

	@DlvryTp.setter
	def DlvryTp(self, value):
		self._DlvryTp = value if value is not None else base_types.UninitialisedField(self, 'DlvryTp', DeliveryType2Code, False)

	@DlvryTp.deleter
	def DlvryTp(self):
		del self._DlvryTp
		self._DlvryTp = base_types.UninitialisedField(self, 'DlvryTp', DeliveryType2Code, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODateTime, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODateTime, False)

	@property
	def MrgnRatio(self):
		return self._MrgnRatio

	@MrgnRatio.setter
	def MrgnRatio(self, value):
		self._MrgnRatio = value if value is not None else base_types.UninitialisedField(self, 'MrgnRatio', PercentageRate, False)

	@MrgnRatio.deleter
	def MrgnRatio(self):
		del self._MrgnRatio
		self._MrgnRatio = base_types.UninitialisedField(self, 'MrgnRatio', PercentageRate, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODateTime, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgTp', type=ClosingType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryTp', type=DeliveryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRatio', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))