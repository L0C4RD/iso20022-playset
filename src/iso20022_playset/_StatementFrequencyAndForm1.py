from . import base_types
from .CommunicationMethod2Choice import CommunicationMethod2Choice
from .Frequency7Code import Frequency7Code
from .CommunicationFormat1Choice import CommunicationFormat1Choice
from .Max350Text import Max350Text

class StatementFrequencyAndForm1(base_types._BaseFieldType):

	__slots__ = ["_ComMtd", "_Frmt", "_Frqcy", "_DlvryAdr"]
	@property
	def ComMtd(self):
		return self._ComMtd

	@ComMtd.setter
	def ComMtd(self, value):
		self._ComMtd = value if type(value) != base_types.auto else self.make_default("ComMtd")

	@ComMtd.deleter
	def ComMtd(self):
		del self._ComMtd
		self._ComMtd = None

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def DlvryAdr(self):
		return self._DlvryAdr

	@DlvryAdr.setter
	def DlvryAdr(self, value):
		self._DlvryAdr = value if type(value) != base_types.auto else self.make_default("DlvryAdr")

	@DlvryAdr.deleter
	def DlvryAdr(self):
		del self._DlvryAdr
		self._DlvryAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComMtd', type=CommunicationMethod2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=CommunicationFormat1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAdr', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))

