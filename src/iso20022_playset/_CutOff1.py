# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._DateOffsetText import DateOffsetText
from ._ISOTime import ISOTime
from ._Max35Text import Max35Text

class CutOff1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CutOffTm", "_CutOffUpdId", "_ValDtOffset"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CutOffTm(self):
		return self._CutOffTm

	@CutOffTm.setter
	def CutOffTm(self, value):
		self._CutOffTm = value if type(value) != base_types.auto else self.make_default("CutOffTm")

	@CutOffTm.deleter
	def CutOffTm(self):
		del self._CutOffTm
		self._CutOffTm = None

	@property
	def CutOffUpdId(self):
		return self._CutOffUpdId

	@CutOffUpdId.setter
	def CutOffUpdId(self, value):
		self._CutOffUpdId = value if type(value) != base_types.auto else self.make_default("CutOffUpdId")

	@CutOffUpdId.deleter
	def CutOffUpdId(self):
		del self._CutOffUpdId
		self._CutOffUpdId = None

	@property
	def ValDtOffset(self):
		return self._ValDtOffset

	@ValDtOffset.setter
	def ValDtOffset(self, value):
		self._ValDtOffset = value if type(value) != base_types.auto else self.make_default("ValDtOffset")

	@ValDtOffset.deleter
	def ValDtOffset(self):
		del self._ValDtOffset
		self._ValDtOffset = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CutOffTm', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CutOffUpdId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDtOffset', type=DateOffsetText, min=1, max=1, mutex_group=None, array=False),
	))