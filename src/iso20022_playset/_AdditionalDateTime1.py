# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import ISODateTime

class AdditionalDateTime1(base_types._BaseFieldType):

	__slots__ = ["_AccptncDtTm", "_PoolgAdjstmntDt", "_XpryDtTm"]
	@property
	def AccptncDtTm(self):
		return self._AccptncDtTm

	@AccptncDtTm.setter
	def AccptncDtTm(self, value):
		self._AccptncDtTm = value if value is not None else base_types.UninitialisedField(self, 'AccptncDtTm', ISODateTime, False)

	@AccptncDtTm.deleter
	def AccptncDtTm(self):
		del self._AccptncDtTm
		self._AccptncDtTm = base_types.UninitialisedField(self, 'AccptncDtTm', ISODateTime, False)

	@property
	def PoolgAdjstmntDt(self):
		return self._PoolgAdjstmntDt

	@PoolgAdjstmntDt.setter
	def PoolgAdjstmntDt(self, value):
		self._PoolgAdjstmntDt = value if value is not None else base_types.UninitialisedField(self, 'PoolgAdjstmntDt', ISODate, False)

	@PoolgAdjstmntDt.deleter
	def PoolgAdjstmntDt(self):
		del self._PoolgAdjstmntDt
		self._PoolgAdjstmntDt = base_types.UninitialisedField(self, 'PoolgAdjstmntDt', ISODate, False)

	@property
	def XpryDtTm(self):
		return self._XpryDtTm

	@XpryDtTm.setter
	def XpryDtTm(self, value):
		self._XpryDtTm = value if value is not None else base_types.UninitialisedField(self, 'XpryDtTm', ISODateTime, False)

	@XpryDtTm.deleter
	def XpryDtTm(self):
		del self._XpryDtTm
		self._XpryDtTm = base_types.UninitialisedField(self, 'XpryDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptncDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolgAdjstmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))