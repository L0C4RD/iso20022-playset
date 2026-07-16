# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationFormat1Choice
from . import CommunicationMethod2Choice
from . import Frequency7Code
from . import Max350Text

class StatementFrequencyAndForm1(base_types._BaseFieldType):

	__slots__ = ["_ComMtd", "_DlvryAdr", "_Frmt", "_Frqcy"]
	@property
	def ComMtd(self):
		return self._ComMtd

	@ComMtd.setter
	def ComMtd(self, value):
		self._ComMtd = value if value is not None else base_types.UninitialisedField(self, 'ComMtd', CommunicationMethod2Choice, False)

	@ComMtd.deleter
	def ComMtd(self):
		del self._ComMtd
		self._ComMtd = base_types.UninitialisedField(self, 'ComMtd', CommunicationMethod2Choice, False)

	@property
	def DlvryAdr(self):
		return self._DlvryAdr

	@DlvryAdr.setter
	def DlvryAdr(self, value):
		self._DlvryAdr = value if value is not None else base_types.UninitialisedField(self, 'DlvryAdr', Max350Text, False)

	@DlvryAdr.deleter
	def DlvryAdr(self):
		del self._DlvryAdr
		self._DlvryAdr = base_types.UninitialisedField(self, 'DlvryAdr', Max350Text, False)

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', CommunicationFormat1Choice, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', CommunicationFormat1Choice, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency7Code, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency7Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComMtd', type=CommunicationMethod2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAdr', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=CommunicationFormat1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency7Code, min=1, max=1, mutex_group=None, array=False),
	))