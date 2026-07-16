# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod2
from . import PercentageRate
from . import YesNoIndicator

class MarketMakerProfile2(base_types._BaseFieldType):

	__slots__ = ["_Cmplc", "_CtrctPrd", "_Dscnt", "_MaxSprd"]
	@property
	def Cmplc(self):
		return self._Cmplc

	@Cmplc.setter
	def Cmplc(self, value):
		self._Cmplc = value if value is not None else base_types.UninitialisedField(self, 'Cmplc', YesNoIndicator, False)

	@Cmplc.deleter
	def Cmplc(self):
		del self._Cmplc
		self._Cmplc = base_types.UninitialisedField(self, 'Cmplc', YesNoIndicator, False)

	@property
	def CtrctPrd(self):
		return self._CtrctPrd

	@CtrctPrd.setter
	def CtrctPrd(self, value):
		self._CtrctPrd = value if value is not None else base_types.UninitialisedField(self, 'CtrctPrd', DateTimePeriod2, False)

	@CtrctPrd.deleter
	def CtrctPrd(self):
		del self._CtrctPrd
		self._CtrctPrd = base_types.UninitialisedField(self, 'CtrctPrd', DateTimePeriod2, False)

	@property
	def Dscnt(self):
		return self._Dscnt

	@Dscnt.setter
	def Dscnt(self, value):
		self._Dscnt = value if value is not None else base_types.UninitialisedField(self, 'Dscnt', PercentageRate, False)

	@Dscnt.deleter
	def Dscnt(self):
		del self._Dscnt
		self._Dscnt = base_types.UninitialisedField(self, 'Dscnt', PercentageRate, False)

	@property
	def MaxSprd(self):
		return self._MaxSprd

	@MaxSprd.setter
	def MaxSprd(self, value):
		self._MaxSprd = value if value is not None else base_types.UninitialisedField(self, 'MaxSprd', PercentageRate, False)

	@MaxSprd.deleter
	def MaxSprd(self):
		del self._MaxSprd
		self._MaxSprd = base_types.UninitialisedField(self, 'MaxSprd', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmplc', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctPrd', type=DateTimePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dscnt', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSprd', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))