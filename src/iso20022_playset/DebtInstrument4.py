import base_types
import ISODate

class DebtInstrument4(base_types._BaseFieldType):

	__slots__ = ["_MtrtyDt"]
	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

