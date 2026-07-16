# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Max3NumericText
from . import Max70Text

class LodgingRoom2(base_types._BaseFieldType):

	__slots__ = ["_Adlts", "_BedTp", "_Chldrn", "_DalyRate", "_Gsts", "_Lctn", "_Tp"]
	@property
	def Adlts(self):
		return self._Adlts

	@Adlts.setter
	def Adlts(self, value):
		self._Adlts = value if value is not None else base_types.UninitialisedField(self, 'Adlts', Max3NumericText, False)

	@Adlts.deleter
	def Adlts(self):
		del self._Adlts
		self._Adlts = base_types.UninitialisedField(self, 'Adlts', Max3NumericText, False)

	@property
	def BedTp(self):
		return self._BedTp

	@BedTp.setter
	def BedTp(self, value):
		self._BedTp = value if value is not None else base_types.UninitialisedField(self, 'BedTp', Max70Text, False)

	@BedTp.deleter
	def BedTp(self):
		del self._BedTp
		self._BedTp = base_types.UninitialisedField(self, 'BedTp', Max70Text, False)

	@property
	def Chldrn(self):
		return self._Chldrn

	@Chldrn.setter
	def Chldrn(self, value):
		self._Chldrn = value if value is not None else base_types.UninitialisedField(self, 'Chldrn', Max3NumericText, False)

	@Chldrn.deleter
	def Chldrn(self):
		del self._Chldrn
		self._Chldrn = base_types.UninitialisedField(self, 'Chldrn', Max3NumericText, False)

	@property
	def DalyRate(self):
		return self._DalyRate

	@DalyRate.setter
	def DalyRate(self, value):
		self._DalyRate = value if value is not None else base_types.UninitialisedField(self, 'DalyRate', ImpliedCurrencyAndAmount, False)

	@DalyRate.deleter
	def DalyRate(self):
		del self._DalyRate
		self._DalyRate = base_types.UninitialisedField(self, 'DalyRate', ImpliedCurrencyAndAmount, False)

	@property
	def Gsts(self):
		return self._Gsts

	@Gsts.setter
	def Gsts(self, value):
		self._Gsts = value if value is not None else base_types.UninitialisedField(self, 'Gsts', Max3NumericText, False)

	@Gsts.deleter
	def Gsts(self):
		del self._Gsts
		self._Gsts = base_types.UninitialisedField(self, 'Gsts', Max3NumericText, False)

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if value is not None else base_types.UninitialisedField(self, 'Lctn', Max35Text, False)

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = base_types.UninitialisedField(self, 'Lctn', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adlts', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BedTp', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chldrn', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DalyRate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Gsts', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))