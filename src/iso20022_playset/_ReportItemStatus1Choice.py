from . import base_types
from ._NoReasonCode import NoReasonCode
from ._ReportItemStatus1 import ReportItemStatus1

class ReportItemStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_Accptd", "_Rjctd", "_AccptdWthXcptn"]
	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if type(value) != base_types.auto else self.make_default("Accptd")

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = None

	@property
	def AccptdWthXcptn(self):
		return self._AccptdWthXcptn

	@AccptdWthXcptn.setter
	def AccptdWthXcptn(self, value):
		self._AccptdWthXcptn = value if type(value) != base_types.auto else self.make_default("AccptdWthXcptn")

	@AccptdWthXcptn.deleter
	def AccptdWthXcptn(self):
		del self._AccptdWthXcptn
		self._AccptdWthXcptn = None

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != base_types.auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AccptdWthXcptn', type=ReportItemStatus1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Rjctd', type=ReportItemStatus1, min=0, max=1, mutex_group=1, array=False),
	))

