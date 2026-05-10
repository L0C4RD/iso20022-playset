from . import base_types
from .ATMStatus1Code import ATMStatus1Code
from .Max35Text import Max35Text

class ATMStatus2(base_types._BaseFieldType):

	__slots__ = ["_DmnddSts", "_CurStsRsn", "_CurSts"]
	@property
	def DmnddSts(self):
		return self._DmnddSts

	@DmnddSts.setter
	def DmnddSts(self, value):
		self._DmnddSts = value if type(value) != base_types.auto else self.make_default("DmnddSts")

	@DmnddSts.deleter
	def DmnddSts(self):
		del self._DmnddSts
		self._DmnddSts = None

	@property
	def CurStsRsn(self):
		return self._CurStsRsn

	@CurStsRsn.setter
	def CurStsRsn(self, value):
		self._CurStsRsn = value if type(value) != base_types.auto else self.make_default("CurStsRsn")

	@CurStsRsn.deleter
	def CurStsRsn(self):
		del self._CurStsRsn
		self._CurStsRsn = None

	@property
	def CurSts(self):
		return self._CurSts

	@CurSts.setter
	def CurSts(self, value):
		self._CurSts = value if type(value) != base_types.auto else self.make_default("CurSts")

	@CurSts.deleter
	def CurSts(self):
		del self._CurSts
		self._CurSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DmnddSts', type=ATMStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurStsRsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CurSts', type=ATMStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

