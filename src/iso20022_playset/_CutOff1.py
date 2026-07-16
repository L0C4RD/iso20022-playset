# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import DateOffsetText
from . import ISOTime
from . import Max35Text

class CutOff1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CutOffTm", "_CutOffUpdId", "_ValDtOffset"]
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
	def CutOffTm(self):
		return self._CutOffTm

	@CutOffTm.setter
	def CutOffTm(self, value):
		self._CutOffTm = value if value is not None else base_types.UninitialisedField(self, 'CutOffTm', ISOTime, False)

	@CutOffTm.deleter
	def CutOffTm(self):
		del self._CutOffTm
		self._CutOffTm = base_types.UninitialisedField(self, 'CutOffTm', ISOTime, False)

	@property
	def CutOffUpdId(self):
		return self._CutOffUpdId

	@CutOffUpdId.setter
	def CutOffUpdId(self, value):
		self._CutOffUpdId = value if value is not None else base_types.UninitialisedField(self, 'CutOffUpdId', Max35Text, False)

	@CutOffUpdId.deleter
	def CutOffUpdId(self):
		del self._CutOffUpdId
		self._CutOffUpdId = base_types.UninitialisedField(self, 'CutOffUpdId', Max35Text, False)

	@property
	def ValDtOffset(self):
		return self._ValDtOffset

	@ValDtOffset.setter
	def ValDtOffset(self, value):
		self._ValDtOffset = value if value is not None else base_types.UninitialisedField(self, 'ValDtOffset', DateOffsetText, False)

	@ValDtOffset.deleter
	def ValDtOffset(self):
		del self._ValDtOffset
		self._ValDtOffset = base_types.UninitialisedField(self, 'ValDtOffset', DateOffsetText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CutOffTm', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CutOffUpdId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDtOffset', type=DateOffsetText, min=1, max=1, mutex_group=None, array=False),
	))