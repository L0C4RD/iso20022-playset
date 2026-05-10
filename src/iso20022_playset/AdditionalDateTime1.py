from . import base_types
import ISODate
import ISODateTime

class AdditionalDateTime1(base_types._BaseFieldType):

	__slots__ = ["_PoolgAdjstmntDt", "_AccptncDtTm", "_XpryDtTm"]
	@property
	def PoolgAdjstmntDt(self):
		return self._PoolgAdjstmntDt

	@PoolgAdjstmntDt.setter
	def PoolgAdjstmntDt(self, value):
		self._PoolgAdjstmntDt = value if type(value) != auto else self.make_default("PoolgAdjstmntDt")

	@PoolgAdjstmntDt.deleter
	def PoolgAdjstmntDt(self):
		del self._PoolgAdjstmntDt
		self._PoolgAdjstmntDt = None

	@property
	def AccptncDtTm(self):
		return self._AccptncDtTm

	@AccptncDtTm.setter
	def AccptncDtTm(self, value):
		self._AccptncDtTm = value if type(value) != auto else self.make_default("AccptncDtTm")

	@AccptncDtTm.deleter
	def AccptncDtTm(self):
		del self._AccptncDtTm
		self._AccptncDtTm = None

	@property
	def XpryDtTm(self):
		return self._XpryDtTm

	@XpryDtTm.setter
	def XpryDtTm(self, value):
		self._XpryDtTm = value if type(value) != auto else self.make_default("XpryDtTm")

	@XpryDtTm.deleter
	def XpryDtTm(self):
		del self._XpryDtTm
		self._XpryDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PoolgAdjstmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

