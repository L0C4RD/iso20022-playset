from . import base_types
from ._Max35Text import Max35Text
from ._ISODate import ISODate

class EndPoint1Choice(base_types._BaseFieldType):

	__slots__ = ["_NbOfPmts", "_LastPmtDt"]
	@property
	def NbOfPmts(self):
		return self._NbOfPmts

	@NbOfPmts.setter
	def NbOfPmts(self, value):
		self._NbOfPmts = value if type(value) != base_types.auto else self.make_default("NbOfPmts")

	@NbOfPmts.deleter
	def NbOfPmts(self):
		del self._NbOfPmts
		self._NbOfPmts = None

	@property
	def LastPmtDt(self):
		return self._LastPmtDt

	@LastPmtDt.setter
	def LastPmtDt(self, value):
		self._LastPmtDt = value if type(value) != base_types.auto else self.make_default("LastPmtDt")

	@LastPmtDt.deleter
	def LastPmtDt(self):
		del self._LastPmtDt
		self._LastPmtDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfPmts', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LastPmtDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
	))

